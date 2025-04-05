import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

# PyQt5 Browser Class
class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("StylesOnRBLX's Browser")
        self.setGeometry(100, 100, 1280, 900)  # Set window size to larger dimensions (1280x900)
        self.setWindowIcon(QIcon("browser_icon.png"))  # You can add your own icon here

        # Create a QWidget as the central widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Set up the main layout
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # Create a top bar for navigation buttons and address bar
        self.top_bar = QWidget(self)
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.layout.addWidget(self.top_bar)

        # Adjust the height of the top bar to make it smaller
        self.top_bar.setFixedHeight(40)  # Set the height of the top bar (address bar area)

        # Create a QWebEngineView to display web pages
        self.browser_view = QWebEngineView(self)
        self.layout.addWidget(self.browser_view)

        # Set default URL to load
        self.browser_view.setUrl(QUrl("https://www.google.com"))

        # Back button
        self.back_button = QPushButton("<", self)
        self.back_button.setFixedSize(40, 40)
        self.back_button.clicked.connect(self.browser_view.back)
        self.top_bar_layout.addWidget(self.back_button)

        # Forward button
        self.forward_button = QPushButton(">", self)
        self.forward_button.setFixedSize(40, 40)
        self.forward_button.clicked.connect(self.browser_view.forward)
        self.top_bar_layout.addWidget(self.forward_button)

        # Address bar (smaller version)
        self.address_bar = QLineEdit(self)
        self.address_bar.setPlaceholderText("Enter URL here...")
        self.address_bar.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border-radius: 5px;
                font-size: 10px;
                padding: 2px 5px;
            }
        """)
        self.address_bar.setFixedHeight(20)  # Further reduced height for a compact address bar
        self.top_bar_layout.addWidget(self.address_bar)
        self.address_bar.returnPressed.connect(self.navigate_to_url)

        # Navigation for address bar
        self.browser_view.urlChanged.connect(self.update_address_bar)

    def navigate_to_url(self):
        # Get URL from the address bar and load it in the browser
        url = self.address_bar.text()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url  # Add "http://" if no scheme is present
        self.browser_view.setUrl(QUrl(url))

    def update_address_bar(self, qurl):
        # Update the address bar when the URL changes
        self.address_bar.setText(qurl.toString())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("StylesOnRBLX's Browser")

    # Styling the application globally
    app.setStyle("Fusion")
    window = Browser()
    window.show()

    sys.exit(app.exec_())
