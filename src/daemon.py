import logging
import subprocess
import sys
import time

import daemon
import psutil
from daemon import pidfile


from src.email_alert import send_alert


def start_daemon(config, pid_file, log_file):
    print("-------------------")
    print(f'Switching to daemon mode. Log will be outputed to {log_file}')
    with daemon.DaemonContext(
            working_directory='./',
            umask=0o002,
            pidfile=pidfile.TimeoutPIDLockFile(pid_file),
    ) as context:
        setup_and_watch(config, log_file)


def check_process(name):
    for proc in psutil.process_iter():
        try:
            if name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def setup_logger(logf):
    logger = logging.getLogger('watchdog')
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(logf)
    fh.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
    logger.addHandler(fh)
    return logger


def restart_process(ps):
    p = subprocess.Popen([ps], shell=True, stdin=None, stdout=None, stderr=None)
    time.sleep(0.5)


def setup_and_watch(config, logf):
    logger = setup_logger(logf)
    ps = config['process_name']
    cmd = config['restart_command']
    attempts = int(config['restart_attempts'])
    restart_interval_seconds = int(config['restart_interval_seconds'])
    watch_interval_seconds = int(config['watch_interval_seconds'])
    while True:
        watch(config=config,
              attempts=attempts,
              ps=ps,
              cmd=cmd,
              restart_interval_seconds=restart_interval_seconds,
              watch_interval_seconds = watch_interval_seconds,
              logger=logger)


def watch(config, attempts, ps, cmd, restart_interval_seconds, watch_interval_seconds, logger):
    time.sleep(watch_interval_seconds)
    success = check_process(ps)
    if not success:
        logger.info(f'Process {ps} failed. Starting restart attempts')
        send_alert(config, f'Process {ps} failed. Starting restart attempts')
        for i in range(attempts):
            restart_process(cmd)
            success = check_process(ps)
            logger.info(f'Restart attempt {i + 1} of {attempts}. Did it work: {success}')
            if success:
                logger.info(f'Process {ps} was succesfully restarted after {i + 1}  attempts')
                send_alert(config, f'Process {ps} was succesfully restarted after {i + 1}  attempts')
                break
            time.sleep(restart_interval_seconds)
        if not success:
            logger.info('Restarting of process failed. Giving up. Stopping....')
            send_alert(config,
                       f'Process {ps} could not be restarted after  {attempts} attempts. Watchdog is stopping.')
            sys.exit()
