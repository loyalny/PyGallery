import os
from datetime import datetime

from PySide6.QtWidgets import (QWidget, QSizePolicy, QHBoxLayout,
QVBoxLayout, QPushButton, QLabel, QMessageBox, QInputDialog)
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QCursor

from start_file import start_file
import trim_file_name
import extensions
import message_boxes
import start_file

import resources

def create_file_card(file_id, file_path, file_name, file_time, preview, parent, app, is_album):
    file_card = QWidget()
    file_card.setObjectName(file_id)
    file_card.setProperty("class", "file_card")
    sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
    file_card.setSizePolicy(sizePolicy)
    file_card.setStyleSheet(f"""
        QWidget {{
            background-color: transparent;
        }}
    
        QWidget[class="file_card"] {{
            border-radius: 20px;
            border: none;
        }}
        QWidget[class="file_card"]:hover {{
            background: #ededed;
        }}
        #file_card_info_time {{
            color: #444746;
            font-size: 14px;
        }}
        QWidget#file_card_delete_btn, QWidget#file_card_rename_btn {{
            border-radius: 15px;
            border: none;
            padding: 20px;
        }}
        QWidget#file_card_delete_btn:hover {{
            background: #ffc2c2;
        }}
        QWidget#file_card_rename_btn:hover {{
            background: {app.data["settings"].get("accent_color", "#c2ffc2")};
        }}
    """)

    horizontalLayout = QHBoxLayout(file_card)
    horizontalLayout.setObjectName(u"horizontalLayout")
    horizontalLayout.setContentsMargins(10, 10, 10, 10)

    file_card_icon = QPushButton(file_card)
    file_card_icon.setObjectName(u"file_card_icon")
    sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
    file_card_icon.setSizePolicy(sizePolicy1)
    file_card_icon.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    file_card_icon.setToolTip(file_path or file_name)
    file_card_icon.setStyleSheet(u"border: none; padding: 0;")
    card_preview = QIcon()

    if is_album:
        card_preview.addFile(":/icons/icons/folder.png")

    elif preview != "standard" and os.path.exists(preview):
        card_preview.addFile(preview)
    else:
        card_preview.addFile(":/icons/icons/error_24dp_444746_FILL0_wght400_GRAD0_opsz24.png")

    if preview == "standard":
        if file_path.lower().endswith(extensions.img_ext):
            card_preview.addFile(":/icons/icons/photo_24dp_444746.png")
        elif file_path.lower().endswith(extensions.vid_ext):
            card_preview.addFile(":/icons/icons/video_camera_back_24dp_444746.png")
        else:
            card_preview.addFile(":/icons/icons/error_24dp_444746_FILL0_wght400_GRAD0_opsz24.png")

    if not is_album:
        file_card_icon.clicked.connect(lambda _, f=file_path: open_file(f, app))
    else:
        file_card_icon.clicked.connect(lambda _, f=file_id: open_album(f, app))

    file_card_icon.setIcon(card_preview)
    file_card_icon.setIconSize(QSize(100, 100))
    horizontalLayout.addWidget(file_card_icon)
    horizontalLayout.addStretch()

    file_card_info = QWidget()
    file_card_info.setObjectName(file_id)
    sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
    file_card_info.setSizePolicy(sizePolicy2)
    horizontalLayout.addWidget(file_card_info)
    horizontalLayout.addStretch()

    verticalLayout = QVBoxLayout(file_card_info)
    verticalLayout.setObjectName(u"verticalLayout")
    horizontalLayout.setContentsMargins(10, 10, 10, 10)

    file_card_info_label = QLabel(file_card)
    file_card_info_label.setObjectName(u"file_card_info_label")
    file_card_info_label.setText(trim_file_name.trim_file_name(file_name, 20))
    sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
    file_card_info_label.setSizePolicy(sizePolicy3)
    file_card_info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    verticalLayout.addWidget(file_card_info_label)

    file_card_info_time = QLabel(file_card)
    file_card_info_time.setObjectName(u"file_card_info_time")
    datatime_object = datetime.fromtimestamp(file_time)
    file_card_info_time.setText(datatime_object.strftime("%Y-%m-%d %H:%M:%S"))
    sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
    file_card_info_time.setSizePolicy(sizePolicy4)
    file_card_info_time.setAlignment(Qt.AlignmentFlag.AlignCenter)
    verticalLayout.addWidget(file_card_info_time)

    file_card_delete_btn = QPushButton(file_card)
    file_card_delete_btn.setObjectName(u"file_card_delete_btn")
    sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
    file_card_delete_btn.setSizePolicy(sizePolicy5)
    file_card_delete_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    icon = QIcon()
    icon.addFile(u":/icons/icons/delete_24dp_444746.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
    file_card_delete_btn.setIcon(icon)
    file_card_delete_btn.setIconSize(QSize(30, 30))
    horizontalLayout.addWidget(file_card_delete_btn)
    file_card_delete_btn.clicked.connect(
        lambda:
        remove_file_card(
            file_id=file_id,
            preview=None if is_album else preview,
            app=app,
            is_album=is_album
        )
    )

    file_card_rename_btn = QPushButton(file_card)
    file_card_rename_btn.setObjectName(u"file_card_rename_btn")
    sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
    file_card_rename_btn.setSizePolicy(sizePolicy6)
    file_card_rename_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    icon = QIcon()
    icon.addFile(u":/icons/icons/edit_24dp_444746_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
    file_card_rename_btn.setIcon(icon)
    file_card_rename_btn.setIconSize(QSize(30, 30))
    horizontalLayout.addWidget(file_card_rename_btn)
    file_card_rename_btn.clicked.connect(
        lambda:
        rename_file(
            app=app,
            file_name_widget=file_card_info_label,
            file_icon_widget=file_card_icon,
            file_id=file_id,
            is_album=is_album
        )
    )

    parent.layout().insertWidget(0, file_card)

def remove_file_card(file_id, preview, app, is_album):
    if is_album:
        if app.data["settings"].get("ask_before_album_del", True):
            if not app.can_proceed("При удалении папки удалятся все файлы в ней. Точно хотите продолжить?"):
                return

        for file_info in app.data["files"][file_id]["files"].values():
            if os.path.exists(file_info["file_preview"]):
                os.remove(file_info["file_preview"])
        del app.data["files"][file_id]

    else:
        if app.data["settings"].get("ask_before_file_del", False):
            if not app.can_proceed("Точно хотите удалить файл?"):
                return

        if file_id in app.data["files"]:
            del app.data["files"][file_id]

        elif file_id not in app.data["files"]:
            album_id = None
            for _file_id, _file_info in app.data["files"].items():
                if _file_info.get("files", False) is not None:
                    if file_id in _file_info["files"]:
                        album_id = _file_id
                        break

            del app.data["files"][album_id]["files"][file_id]

        if os.path.exists(preview):
            os.remove(preview)

    duplicates = app.findChildren(QWidget, file_id)
    for _ in duplicates:
        _.deleteLater()

    app.save_data()

def open_album(album_id, app):
    app.current_album_id = album_id
    app.current_parent.setCurrentIndex(1)
    app.current_scroll_area.setValue(0)
    app.current_create_album_btn.setEnabled(False)
    app.current_back_to_files_area_btn.show()

    if app.data["files"][album_id].get("files"):
        for file_id, file_info in app.data["files"][album_id]["files"].items():
            create_file_card(
                file_id=file_id,
                file_path=file_info["file_path"],
                file_name=file_info["file_name"],
                file_time=file_info["file_time"],
                preview=file_info["file_preview"],
                parent=app.current_parent.widget(1),
                app=app,
                is_album=False
            )

def open_file(file_path, app):
    try:
        start_file.start_file(file_path)
    except OSError:
        QMessageBox.critical(
            app,
            "Возникла ошибка!",
            "Не удалось открыть файл, возможно он был удалён или перемещён"
        )

def rename_file(app, file_name_widget, file_icon_widget, file_id, is_album):
    text, ok = QInputDialog.getText(
        app,
        "Переименование файла",
        "Введите новое название"
    )

    file_name = text.strip()

    if ok:
        if not file_name:
            message_boxes.warning_box(app, "Название не может быть пустым!")
            return

        for files_info in app.data["files"].values():
            if files_info.get("file_name") == file_name:
                message_boxes.warning_box(app, "Такой файл уже есть!")
                return

        if app.current_album_id:
            app.data["files"][app.current_album_id]["files"][file_id]["file_name"] = file_name
        else:
            app.data["files"][file_id]["file_name"] = file_name
        if is_album:
            file_icon_widget.setToolTip(file_name)
        app.save_data()

        # также обновляем имя в фото и видео
        app.create_files_list()
        # для фото
        app.clear_layout(app.ui.photo_page_files_area.layout())
        app.render_files(app.photo_files, app.ui.photo_page_files_area)
        # для видео
        app.clear_layout(app.ui.video_page_files_area.layout())
        app.render_files(app.video_files, app.ui.video_page_files_area)

        file_name_widget.setText(trim_file_name.trim_file_name(file_name, 20))
