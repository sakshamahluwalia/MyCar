class values:
    """
    This class follows the singleton design pattern and will be used
    to store all the variables required in this app.


    #TODO: write getter/setter docstrings
    """

    def __init__(self):
        """
        self -> values

        Initialize all values.
        """
        print("DEBUG: init values")

        self.test = 500
        self.test1 = 0

        # use after starting obd connection
        self.rpm = 0

    def get_test(self):
        return self.test

    def set_test(self, value):
        self.test = value

    def get_test1(self):
        return self.test1

    def set_test1(self, value):
        self.test1 = value

    def get_rpm(self):
        return self.rpm

    def set_rpm(self, val):
        self.rpm = val

    def get_values_obj(self):
        return self
