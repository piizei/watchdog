## Watchdog

Python script that watches over a operating system process. If process is not found, it tries to restart it.
Script also sends alert emails.

### Requirements
- Python 3.6+

## Installing

Tested with MacOs & Ubuntu:latest only.

- `git clone https://github.com/piizei/watchdog`
- `cd watchdog`
- `pip install -e .`



## Usage

## Todo
- Stopping the watchdog
- Nice email formatting
- Improve testing (and testing setup)
- For any other ideas, Pull Request accepted


## Development
package requirements for unit testing are not in the requirements.txt.
You might need to add something. Using virtualenv is highly recommended.


### Misc

Using gmail with 2nd factor (as you should!): 
Create an app password from https://security.google.com/settings/security/apppasswords
