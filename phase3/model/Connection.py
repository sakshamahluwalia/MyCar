import obd
import time

class Connection:

    def __init__(self, portstr_='/dev/rfcomm0'):

        self.connection = "change flag to true to use OBD"
        if True:
            self.connection = obd.Async(portstr=portstr_, fast=False)
        print(self.get_connection())


    def get_connection(self):
        '''
        Incoming param: Connection self
        Return value  : None
        return the connection
        '''
        return self.connection

    def start_connection(self):
        '''
        Incoming param: Connection self
        Function to start the connection
        '''
        self.get_connection().start()

    def stop_connection(self):
        '''
        Incoming param: Connection
        Function to end the connection
        '''
        self.get_connection().stop()
