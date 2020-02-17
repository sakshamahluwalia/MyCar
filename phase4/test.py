import obd
import time

obd.logger.setLevel(obd.logging.DEBUG)

connection = obd.Async(portstr='/dev/rfcomm0', fast=False)

# a callback that prints every new value to the console
def new_rpm(r):
    print(r.value)

connection.watch(obd.commands.RPM, callback=new_rpm)
connection.start()

# the callback will now be fired upon receipt of new values

time.sleep(10)
connection.stop()



# print(response.value) # returns unit-bearing values thanks to Pint
# print(response.value.to("mph")) # user-friendly unit conversions

# if __name__ == '__main__':
# 	main() # this script will get a mac addr of a blt device
# 	then connect by issuing sudo rfcomm connect addr rfcomm1
