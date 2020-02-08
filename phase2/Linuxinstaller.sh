# #!/usr/bin/env python2
# import os
#
# # connect bluetooth using rfcomm (sudo rfcomm connect <bltaddr> <rfcomm1>)
# os.system("sudo rfcomm connect {} {}".format(addr, port))
# os.system("pip install obd")
# # os.system("pip install pynmea2")

#!/bin/bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install bluez-tools
pip install obd
chmod 700 setup.sh

. setup.sh
