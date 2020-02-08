import serial
import pynmea2

port = "/dev/ttyUSB0"

def parseGPS(str):
    if str.find('GGA') > 0:
        msg = pynmea2.parse(str)
        print "Timestamp: %s -- Lat: %s %s -- Lon: %s %s -- Altitude: %s %s -- Satellites: %s" % (msg.timestamp,msg.lat,msg.lat_dir,msg.lon,msg.lon_dir,msg.altitude,msg.altitude_units,msg.num_sats)


serialPort = serial.Serial(port, baudrate = 9600, timeout = 0.5)
while True:
    str = serialPort.readline()
    parseGPS(str)


# from gps import *
# import time
#
# gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)
# print 'latitude\tlongitude\ttime utc\t\t\taltitude\tepv\tept\tspeed\tclimb' # '\t' = TAB to try and output the data in columns.
#
# try:
#
#
#     while True:
#         report = gpsd.next() #
#         if report['class'] == 'TPV':
#
#             print  getattr(report,'lat',0.0),"\t",
#             print  getattr(report,'lon',0.0),"\t",
#             print getattr(report,'time',''),"\t",
#             print  getattr(report,'alt','nan'),"\t\t",
#             print  getattr(report,'epv','nan'),"\t",
#             print  getattr(report,'ept','nan'),"\t",
#             print  getattr(report,'speed','nan'),"\t",
#             print getattr(report,'climb','nan'),"\t"
#
#         time.sleep(1)
#
# except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
#     print "Done.\nExiting."
