## Watchdog

Python script that watches over a operating system process. If process is not found, it tries to restart it.
Script also sends alert emails.

### Requirements
- Python 3.6+

## Installing

Tested with MacOs & Ubuntu 18.04 only.

- `git clone https://github.com/piizei/watchdog`
- `cd watchdog`
- `pip install -e .`

Note: In some cases you might need to replace `pip` with `pip3` depending on your python setup.

Copy the template.ini into any directory you wish to run the watchdog from. Rename it to watchdog.ini.
for example `cp template.ini ~/watchdog.ini`. Edit your settings into the watchdog.ini. 
Then start watchdog in the same directory (with command `watchdog`).
Monitoring should now be enabled

## Usage

## Todo
- Stopping the watchdog (to stop now, look into watchdog.pid for a pid and use kill)
- Nice email formatting
- Improve testing (and testing setup)
- For any other ideas, Pull Request accepted


## Development
package requirements for unit testing are not in the requirements.txt.
You might need to add something. Using virtualenv is highly recommended.


### Misc

Using gmail with 2nd factor (as you should!): 
Create an app password from https://security.google.com/settings/security/apppasswords
