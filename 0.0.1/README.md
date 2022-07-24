# powerplan
## Get windows power plan information

powerplan is a new Python package to get information about your current windows power plan using subprocess module.
## Features

- Get GUID of your current windows power plan
- Get name of your current windows power plan

## Installation

winpower requires [Python](https://www.python.org/) v3+ to run.

## Usage

```py
import powerplan
name = powerplan.get_current_scheme_name()
guid = powerplan.get_current_scheme_guid()
print(name, guid)
```
## License

MIT

**Made by Temal#5222**