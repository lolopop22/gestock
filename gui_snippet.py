import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Assuming the QTabWidget is called self.tab_widget and has been initialized
        self.tab_widget = QTabWidget(self)

        # Given that the tabs have already been added
        self.create_tabs()

        # Initially disabling tabs 2, 3, 4, and 5
        self.set_initial_tab_state()

        # Set the QTabWidget as the central widget
        self.setCentralWidget(self.tab_widget)

    def create_tabs(self):
        # Adding tabs as an example, assume these tabs are added somewhere in your application
        for i in range(1, 6):
            tab = QWidget()
            layout = QVBoxLayout()
            layout.addWidget(QLabel(f"Content of Tab {i}"))
            tab.setLayout(layout)
            self.tab_widget.addTab(tab, f"Tab {i}")

    def set_initial_tab_state(self):
        # Enable the first tab and disable others
        for index in range(1, 5):  # Tabs are zero-indexed, so indexes 1-4 correspond to tabs 2-5
            self.tab_widget.setTabVisible(index, False)

# Entry point of application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())