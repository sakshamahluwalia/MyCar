import obd
import time
# from values import values

class connection:
    """
    This class will also follow singleton design pattern and should
    only be instantiated once.


    #TODO: write getter/setter docstrings
    """

    def __init__(self, values, portstr_='/dev/rfcomm0'):
        """
        self -> connection
        portstr_ -> string port to connect to.
        values -> values

        Initialize obd connection and add commands on watch-list
        to update fields in values
        """
        
        print("DEBUG: init connection")

        self.values = values
        self.connection = "change flag to true to use OBD"
        if False:
            self.connection = obd.Async(portstr=portstr_, fast=False)
        print(self.get_connection())

        # add block with watch statements
        # add call-backs to update variables in values

    def update_test(self):
        """
        Function to provide a steady stream of values.
        Mimics the watch function from obd
        """

        tmp_ = self.values.get_test()
        tmp_ += 1
        self.values.set_test(tmp_)

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

if __name__ == '__main__':
    conn = connection()
    conn.update_test()
