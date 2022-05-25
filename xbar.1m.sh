#!/bin/bash
#!/usr/bin/env /usr/local/bin/node
# <bitbar.title>Busylight</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Niraj Tolia</bitbar.author>
# <bitbar.author.github>ntolia</bitbar.author.github>
# <bitbar.desc>Tweak busylight settings depending on meeting status</bitbar.desc>

pythonenv="/usr/local/bin/python3"
script="/Users/ntolia/src/busylight/controller.py"

# Source credentials for Govee, O365
source /Users/ntolia/.bash_profile
$pythonenv $script
