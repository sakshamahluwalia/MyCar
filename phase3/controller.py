from model import Connection as conn

from View_ import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore


class Controller:

    # Workflow after initialisation for when we sue obd
    # watch cmds -> start -> show -> exit (later) -> stop_connection
    def __init__(self):

        # self.conn = conn.Connection()
        self.app = QApplication([])
        self.view = View_(self.app)


        # This block of code represents the watch commmands.
        # watch commands will call functions from this file
        # self.conn.get_connection().watch(obd.commands.RPM, callback=self.update_rpm) ??
        # self.conn.start_connection()

        self.view.show_view()

        # Add CSS
        self.app.setStyleSheet(open('./public/app.css').read())


        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(lambda: self.update(self.view))
        # self.timer.timeout.connect(lambda: self.update_rpm("updated")) --tested
        self.timer.start(500)


        self.app.exec_()
        # self.conn.stop_connection()


    def update(self, view):
        '''
        test function for seed data (rpm_label)
        '''
        self.view.set_test_label()

    # use with obd
    def update_rpm(self, rpm):
        self.view.set_rpm_label(rpm.value)


if __name__ == '__main__':
    controller = Controller()
