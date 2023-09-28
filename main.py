import random
import string
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader

class PasswordGeneratorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('design.ui')
        self.ui.show()
        self.ui.setWindowTitle('password generator')
        self.ui.generator_btn.clicked.connect(self.generate_password)

    def generate_password(self):
        password_length = 8
        password_characters = string.ascii_letters + string.digits + string.punctuation
        self.ui.tb.setText(''.join(random.choice(password_characters) for _ in range(password_length)))

app = QApplication([])
window = PasswordGeneratorWindow()
app.exec()