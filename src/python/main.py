import sys

from PySide6.QtWidgets import QApplication

from pygallery import PyGallery

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = PyGallery()
    window.show()

    sys.exit(app.exec())