from PySide6.QtWidgets import QMessageBox

def error_box(app, err):
    QMessageBox.critical(app, "Ошибка", err)

def warning_box(app, warn):
    QMessageBox.warning(app, "Предупреждение", warn)

def info_box(app, title, info):
    QMessageBox.information(app, title, info, QMessageBox.StandardButton.Ok)
