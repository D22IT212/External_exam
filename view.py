# Import QApplication and the required widgets from PyQt5.QtWidgets

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout

class GUI(QMainWindow):
    """PyCalc's View (GUI)."""
    def __init__(self):
        """View initializer."""
        super().__init__()

        # Set some main window's properties
        self.setWindowTitle('Calculator')
        self.setFixedSize(235, 235)

        # Set the central widget and the general layout
        self.generalLayout = QVBoxLayout()

        # Set the central widget
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        # Create the display and the buttons
        self._createDisplayLED()
        self._createButtons()

    def _createDisplayLED(self):
        """Create the display."""
        
        # Create the display widget
        self.display = QLineEdit()
        # Set some display's properties
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        
        # Add the display to the general layout
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        """Create the buttons."""
        self.buttons = {}
        buttonsLayout = QGridLayout()
        # Button text | position on the QGridLayout
        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4),
                  }
        # Create the buttons and add them to the grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        # Add buttonsLayout to the general layout
        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        """Set display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def getDisplayText(self):
        """Get display's text."""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText('')
from view import GUI
from controller import Controller, NumeralConverter
from model import evaluateExpression

class ExtendedController(Controller):
    def __init__(self, model, view):
        super().__init__(model, view)
        self.converter = NumeralConverter()

        # Connect the numeral system conversion buttons to controller methods
        self.view.binary_to_decimal_clicked.connect(self.binary_to_decimal_conversion)
        self.view.decimal_to_binary_clicked.connect(self.decimal_to_binary_conversion)
        self.view.binary_to_octal_clicked.connect(self.binary_to_octal_conversion)
        self.view.octal_to_binary_clicked.connect(self.octal_to_binary_conversion)
        self.view.binary_to_hexadecimal_clicked.connect(self.binary_to_hexadecimal_conversion)
        self.view.hexadecimal_to_binary_clicked.connect(self.hexadecimal_to_binary_conversion)

    def binary_to_decimal_conversion(self):
        binary_str = self.view.get_input()
        decimal_value = self.converter.binary_to_decimal(binary_str)
        self.view.display_result(str(decimal_value))

    def decimal_to_binary_conversion(self):
        decimal_int = int(self.view.get_input())
        binary_str = self.converter.decimal_to_binary(decimal_int)
        self.view.display_result(binary_str)

    def binary_to_octal_conversion(self):
        binary_str = self.view.get_input()
        octal_str = self.converter.binary_to_octal(binary_str)
        self.view.display_result(octal_str)

    def octal_to_binary_conversion(self):
        octal_str = self.view.get_input()
        binary_str = self.converter.octal_to_binary(octal_str)
        self.view.display_result(binary_str)

    def binary_to_hexadecimal_conversion(self):
        binary_str = self.view.get_input()
        hexadecimal_str = self.converter.binary_to_hexadecimal(binary_str)
        self.view.display_result(hexadecimal_str)

    def hexadecimal_to_binary_conversion(self):
        hexadecimal_str = self.view.get_input()
        binary_str = self.converter.hexadecimal_to_binary(hexadecimal_str)
        self.view.display_result(binary_str)
