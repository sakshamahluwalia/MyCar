from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt


class View_:

    def __init__(self, app):
        '''
        Incoming param: QApplication app
        Return value  : None

        Responsible for creating labels to display. Add them to a display
        and show that display on screen
        '''

        # Create label
        self.test_label = QLabel("1000")
        self.test_label.setAlignment(Qt.AlignCenter)

        # obd labels (not added to layout)
        self.rpm_label = QLabel("100")
        self.rpm_label.setAlignment(Qt.AlignCenter)

        # Create layout and add widgets
        self.layout = QHBoxLayout()
        self.get_layout().addWidget(self.get_test_label())

        self.get_layout().addWidget(self.get_rpm_label())


        # Apply layout to widget
        self.widget = QWidget()
        self.get_widget().setLayout(self.get_layout())

    def show_view(self):
        '''
        Incoming param: View_ self
        Return value  : None
        show the widget (view)
        '''
        self.get_widget().showMaximized()

    def get_widget(self):
        '''
        Incoming param: View_ self
        Return value  : QWidget
        return the widget
        '''
        return self.widget

    def get_layout(self):
        '''
        Incoming param: View_ self
        Return value  : QHBoxLayout
        return the layout
        '''
        return self.layout

    def get_rpm_label(self):
        '''
        Incoming param: View_ self
        Return value  : Qlable
        return the rpm_label
        '''
        return self.rpm_label

    def set_rpm_label(self, value):
        '''
        Incoming param: View_ self
                        Str   value
        Return value  : None
        Update the rpm_label
        '''
        self.get_rpm_label().setText(str(value))

    # for test purposes. Should be deleted in final build
    def get_test_label(self):
        '''
        Incoming param: View_ self
        Return value  : QLable
        return the test label
        '''
        return self.test_label

    def set_test_label(self):
        '''
        Incoming param: View_ self
        Return value  : None
        Update the label
        '''
        x = int(self.get_test_label().text())+10
        self.get_test_label().setText(str(x))
