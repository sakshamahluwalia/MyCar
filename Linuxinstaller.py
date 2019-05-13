#!/usr/bin/env python2
import os

# connect bluetooth using rfcomm (sudo rfcomm connect <bltaddr> <rfcomm1>)
os.system("sudo rfcomm connect {} {}".format(addr, port))
