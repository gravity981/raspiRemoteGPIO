# raspiRemoteGPIO

Enables hardware attached to the Raspberry Pi's GPIO to be controlled from remote via HTTP requests

# Deploy, configure and run

* copy all files in subdirectory `server` on your Raspberry Pi
* Make sure Python3 is installed on the Raspberry Pi
* edit the config.json according to your hardware setup
* execute `python3 main.py` to run the application

# API

The devices attached to the Raspberry Pi can be controlled by http GET requests. 
The following request URLs are currently supported:
* `<ip>:<port>/servo/<servo_index>/<angle>` where `servo_index` goes from 0 to x, depending on your config.json and `angle` is
a value between **0 and 180** degrees or **off** to power off the servo and make it rotate freely only with the friction
from the gears
