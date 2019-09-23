from mock import patch

from src.daemon import watch
import logging

logger = logging.getLogger(__name__)


@patch('smtplib.SMTP_SSL')
@patch('subprocess.Popen')
@patch('sys.exit')
def run_tests(exit, Popen, smtp):
    # Given retry-count of 2, expect 2 startup tries before giving up
    watch({'smtp_user': '', 'smtp_password': '', 'smtp_server': '', 'alert_recipient': '', 'SMTP_SSL_port': ''},
          2, 'SomethingThatDoesNotExists', 'Cmd', 1, 1, logger)
    assert exit.call_count == 1
    assert Popen.call_count == 2
    Popen.assert_called_with(['Cmd'], shell=True, stderr=None, stdin=None, stdout=None)
    assert smtp.call_count == 2
    exit.call_count == 1

