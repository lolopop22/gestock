import sys
from PySide6.QtWidgets import QApplication
from front_page import FrontPage


app = QApplication(sys.argv)

front_page_window = FrontPage()

front_page_window.show()
app.exec()
