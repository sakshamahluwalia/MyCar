import obd

obd.logger.setLevel(obd.logging.DEBUG)
ports = obd.scan_serial()

connection = obd.OBD() # auto-connects to USB or RF port

cmd = obd.commands.SPEED # select an OBD command (sensor)

response = connection.query(cmd) # send the command, and parse the response

print(response.value) # returns unit-bearing values thanks to Pint
print(response.value.to("mph")) # user-friendly unit conversions

obd.elm327.ELM327(portname='/dev/tty.OBDII-SPP', baudrate=9600, protocol=1234, timeout=None)
obd.elm327.ELM327(portname='/dev/tty.Bluetooth-Incoming-Port', baudrate=9600, protocol=1234, timeout=None)
obd.elm327.ELM327(portname='/dev/uart.BLTH', baudrate=9600, protocol=1234, timeout=None)


ser = serial.Serial('/dev/tty.OBDII-SPP', timeout=1, baudrate=9600)

obd.OBD(portstr='/dev/tty.OBDII-SPP', timeout=None)
