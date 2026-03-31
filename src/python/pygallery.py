import sys
import os
import json
import uuid
import time

from PySide6.QtWidgets import (QApplication, QMainWindow,
QFileDialog, QInputDialog, QMessageBox, QLineEdit)

from design import Ui_MainWindow

from generate_preview import generate_preview
from file_card import create_file_card
from stylesheet import return_stylesheet
import extensions
import message_boxes
from start_file import start_file

import resources


class PyGallery(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # главный page
        self.ui.all_pages_stacked_widget.setCurrentIndex(0)

        # убираем кнопки "Назад"
        self.ui.media_page_header_back_to_files_area_btn.hide()
        self.ui.locked_folder_page_header_back_to_files_area_btn.hide()

        self.current_parent = self.ui.media_page_files_area_stacked_widget
        self.current_scroll_area = self.ui.media_page_page_scroll_area.verticalScrollBar()
        self.current_create_album_btn = self.ui.media_page_header_create_album_btn
        self.current_back_to_files_area_btn = self.ui.media_page_header_back_to_files_area_btn

        # состояние скрытой папки
        self.is_open_locked_folder = False

        # переменная для хранения id ткущего альбома
        self.current_album_id = None

        # чтение файла данных
        self.data_file = os.path.join(self.get_base_path(), "data.json")
        self.data = None
        self.read_data()

        # инициализируем settings_page
        self.init_settings_page()

        # изменяем style
        self.change_main_style()

        # листы файлов
        self.media_files = {}
        self.photo_files = {}
        self.video_files = {}
        self.locked_files = {}

        self.create_files_list()

        # рендер файлов из файла данных
        self.render_files(self.media_files, self.ui.media_page_files_area)
        self.render_files(self.photo_files, self.ui.photo_page_files_area)
        self.render_files(self.video_files, self.ui.video_page_files_area)
        self.render_files(self.locked_files, self.ui.locked_folder_page_files_area)

        # привязка кнопок sidebar
        self.ui.media_page_btn.clicked.connect(self.open_media_page)
        self.ui.photo_page_btn.clicked.connect(self.open_photo_page)
        self.ui.video_page_btn.clicked.connect(self.open_video_page)
        self.ui.locked_folder_page_btn.clicked.connect(self.open_locked_folder_page)
        self.ui.settings_page_btn.clicked.connect(self.open_settings_page)

        # привязка кнопок media_page
        self.ui.media_page_header_add_files_btn.clicked.connect(self.add_files)
        self.ui.media_page_header_create_album_btn.clicked.connect(self.create_album)
        self.ui.media_page_header_back_to_files_area_btn.clicked.connect(self.back_to_files_area)
        self.ui.media_page_header_sort_files_btn.clicked.connect(self.choose_type_of_sorting_files)

        # привязка кнопок locked_folder_page
        self.ui.locked_folder_page_header_add_files_btn.clicked.connect(self.add_files)
        self.ui.locked_folder_page_header_create_album_btn.clicked.connect(self.create_album)
        self.ui.locked_folder_page_header_back_to_files_area_btn.clicked.connect(self.back_to_files_area)
        self.ui.locked_folder_page_header_sort_files_btn.clicked.connect(self.choose_type_of_sorting_files)

        # привязка кнопок photo_page
        self.ui.photo_page_header_sort_files_btn.clicked.connect(self.choose_type_of_sorting_files)

        # привязка кнопок video_page
        self.ui.video_page_header_sort_files_btn.clicked.connect(self.choose_type_of_sorting_files)

        # привязка кнопок settings_page
        self.ui.settings_page_def_folder_btn.clicked.connect(self.select_standard_folder)
        self.ui.settings_page_open_data_file_btn.clicked.connect(lambda: start_file(self.data_file))
        self.ui.settings_page_remove_data_btn.clicked.connect(self.remove_data)
        self.ui.settings_page_accent_color_combo_box.currentIndexChanged.connect(self.update_accent_color)
        self.ui.settings_page_font_combo_box.currentFontChanged.connect(self.update_font_family)
        self.ui.settings_page_auto_preview.toggled.connect(self.toggle_auto_preview)
        self.ui.settings_page_album_del_ask_check_box.toggled.connect(self.toggle_ask_before_album_del)
        self.ui.settings_page_file_del_ask_check_box.toggled.connect(self.toggle_ask_before_file_del)

    def choose_type_of_sorting_files(self):
        message_boxes.info_box(
            app=self,
            title="Сортировка файлов",
            info="Уже в разработке!"
        )

    def change_main_style(self):
        font_family = self.data["settings"].get("font_family", False) or self.ui.settings_page_font_combo_box.currentFont().family()
        accent_color = self.data["settings"].get("accent_color", "#c2ffc2")

        style_sheet = return_stylesheet(font_family, accent_color)

        self.setStyleSheet(style_sheet)

    def read_data(self):
        try:
            with open(self.data_file, "r", encoding="utf-8") as data_file:
                self.data = json.load(data_file)
        except FileNotFoundError:
            self.data = {}
        except json.JSONDecodeError:
            if os.path.getsize(self.data_file) == 0:
                self.data = {}
            else:
                message_boxes.error_box(self, "Файл дынных повреждён!")
                sys.exit()

        self.data.setdefault("files", {})
        self.data.setdefault("settings", {})

        self.save_data()

    def update_files_data(self, file_id, file_path, file_name, file_time, preview, is_album, save_now):
        file_info = {
            "file_path": file_path,
            "file_name": file_name,
            "file_time": file_time,
            "file_preview": preview,
            "is_album": is_album,
            "is_locked": self.is_open_locked_folder,
            "files": {} if is_album else None
        }

        if self.current_album_id:
            self.data["files"][self.current_album_id]["files"][file_id] = file_info
        else:
            self.data["files"][file_id] = file_info

        if save_now:
            self.save_data()

    def save_data(self):
        with open(self.data_file, "w", encoding="utf-8") as data_file:
            json.dump(self.data, data_file, ensure_ascii=False, indent=2)

    def add_files(self):
        default_dir = self.data["settings"].get("default_dir", False) or "."
        file_paths, _ = QFileDialog.getOpenFileNames(
            self,
            "Выберите файлы",
            default_dir,
            "Все медиафайлы (*.jpg *.jpeg *.png *.gif *.webp *.svg *.mp4 *.mov *.avi *.mkv *.wmv)"
        )

        if file_paths:
            for file_path in file_paths:
                preview = str(generate_preview(
                    source_path=file_path,
                    previews_dir=self.get_base_path(),
                    size=100
                ) if self.data["settings"].get("auto_preview", True) else "standard")
                file_id = str(uuid.uuid4())
                file_time = os.path.getctime(file_path)
                create_file_card(
                    file_id=file_id,
                    file_path=file_path,
                    file_name=file_path,
                    file_time=file_time,
                    preview=preview,
                    parent=self.current_parent.widget(1) if self.current_album_id else self.current_parent.widget(0),
                    app=self,
                    is_album=False
                )
                if not self.is_open_locked_folder:
                    if file_path.lower().endswith(extensions.img_ext):
                        create_file_card(
                            file_id=file_id,
                            file_path=file_path,
                            file_name=file_path,
                            file_time=file_time,
                            preview=preview,
                            parent=self.ui.photo_page_files_area,
                            app=self,
                            is_album=False
                        )
                    elif file_path.lower().endswith(extensions.vid_ext):
                        create_file_card(
                            file_id=file_id,
                            file_path=file_path,
                            file_name=file_path,
                            file_time=file_time,
                            preview=preview,
                            parent=self.ui.video_page_files_area,
                            app=self,
                            is_album=False
                        )
                self.update_files_data(
                    file_id=file_id,
                    file_path=file_path,
                    file_name=file_path,
                    file_time=file_time,
                    preview=preview,
                    is_album=False,
                    save_now=False
                )
            self.save_data()

    def create_album(self):
        text, ok = QInputDialog.getText(
            self,
            "Новый альбом",
            "Введите название альбома"
        )

        album_name = text.strip()

        if ok:
            if not album_name:
                message_boxes.warning_box(self, "Введите название альбома!")
                return

            for files_info in self.data["files"].values():
                if files_info.get("is_album") and files_info.get("file_name") == album_name:
                    message_boxes.warning_box(self, "Такой альбом уже есть!")
                    return

            album_id = str(uuid.uuid4())
            album_time = time.time()

            create_file_card(
                file_id=album_id,
                file_path=None,
                file_name=album_name,
                file_time=album_time,
                preview=None,
                parent=self.current_parent.widget(0),
                app=self,
                is_album=True
            )

            self.update_files_data(
                file_id=album_id,
                file_path=None,
                file_name=album_name,
                file_time=album_time,
                preview=None,
                is_album=True,
                save_now=True
            )

    def render_files(self, files_list, parent):
        for file_id, file_info in files_list.items():
            create_file_card(
                file_id=file_id,
                file_path=file_info["file_path"],
                file_name=file_info["file_name"],
                file_time=file_info["file_time"],
                preview=file_info["file_preview"],
                parent=parent,
                app=self,
                is_album=file_info.get("is_album", False)
            )

    def create_files_list(self):
        for file_id, file_info in self.data["files"].items():
            if file_info.get("is_locked", False):
                self.locked_files[file_id] = file_info
                continue
            if file_info.get("is_album", False):
                self.media_files[file_id] = file_info
                for _file_id, _file_info in file_info["files"].items():
                    if _file_info["file_path"].lower().endswith(extensions.img_ext):
                        self.photo_files[_file_id] = _file_info
                    elif _file_info["file_path"].lower().endswith(extensions.vid_ext):
                        self.video_files[_file_id] = _file_info
                continue
            if not file_info.get("is_album", False):
                if file_info["file_path"].lower().endswith(extensions.img_ext):
                    self.photo_files[file_id] = file_info
                elif file_info["file_path"].lower().endswith(extensions.vid_ext):
                    self.video_files[file_id] = file_info
                self.media_files[file_id] = file_info

    def can_proceed(self, text):
        response = QMessageBox.question(
            self,
            "Подтверждение",
            text,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        return response == QMessageBox.StandardButton.Yes

    def open_media_page(self):
        self.ui.all_pages_stacked_widget.setCurrentIndex(0)
        self.is_open_locked_folder = False
        self.current_parent.setCurrentIndex(0)
        self.current_album_id = None

        self.current_parent = self.ui.media_page_files_area_stacked_widget
        self.current_scroll_area = self.ui.media_page_page_scroll_area.verticalScrollBar()
        self.current_create_album_btn = self.ui.media_page_header_create_album_btn
        self.current_back_to_files_area_btn = self.ui.media_page_header_back_to_files_area_btn

    def open_photo_page(self):
        self.ui.all_pages_stacked_widget.setCurrentIndex(1)
        self.is_open_locked_folder = False

    def open_video_page(self):
        self.ui.all_pages_stacked_widget.setCurrentIndex(2)
        self.is_open_locked_folder = False

    def open_locked_folder_page(self):
        if self.is_open_locked_folder: return
        if self.data["settings"].get("password") is None:
            while True:
                text, ok = QInputDialog.getText(self, "Пароль", "Придумайте пароль")
                if not ok: return

                password = text.strip()
                if not password:
                    message_boxes.warning_box(self, "Введите пароль!")
                    continue

                self.data["settings"]["password"] = password
                self.save_data()
                break
        else:
            while True:
                text, ok = QInputDialog.getText(self, "Пароль", "Введите пароль", QLineEdit.EchoMode.Password)
                if not ok: return

                password = text.strip()
                if not password:
                    message_boxes.warning_box(self, "Введите пароль!")
                    continue

                if password == self.data["settings"]["password"]:
                    break
                else:
                    message_boxes.warning_box(self, "Неправильный пароль!")
                    continue

        self.ui.all_pages_stacked_widget.setCurrentIndex(3)
        self.is_open_locked_folder = True
        self.current_parent.setCurrentIndex(0)
        self.current_album_id = None

        self.current_parent = self.ui.locked_folder_page_files_area_stacked_widget
        self.current_scroll_area = self.ui.locked_folder_page_scroll_area.verticalScrollBar()
        self.current_create_album_btn = self.ui.locked_folder_page_header_create_album_btn
        self.current_back_to_files_area_btn = self.ui.locked_folder_page_header_back_to_files_area_btn

    def open_settings_page(self):
        self.ui.all_pages_stacked_widget.setCurrentIndex(4)
        self.is_open_locked_folder = False

    def back_to_files_area(self):
        album_page = self.current_parent.widget(1).layout()

        self.clear_layout(album_page)

        self.current_parent.setCurrentIndex(0)
        self.current_scroll_area.setValue(0)
        self.current_album_id = None
        self.current_create_album_btn.setEnabled(True)
        self.current_back_to_files_area_btn.hide()

    @staticmethod
    def clear_layout(layout):
        if layout is not None:
            while layout.count() > 0:
                item = layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()

        layout.addStretch()

    def init_settings_page(self):
        self.ui.settings_page_accent_color_combo_box.addItem("Мята", "#c2ffc2")
        self.ui.settings_page_accent_color_combo_box.addItem("Малиновый зефир", "#ffc2f0")
        self.ui.settings_page_accent_color_combo_box.addItem("Небесно-голубой", "#c2e0ff")
        self.ui.settings_page_accent_color_combo_box.addItem("Нежный персик", "#ffdec2")
        self.ui.settings_page_accent_color_combo_box.addItem("Кораллово-розовый", "#ffc2c2")
        self.ui.settings_page_accent_color_combo_box.addItem("Бледная лаванда", "#dec2ff")

        state = self.data["settings"].get("auto_preview", True)
        self.ui.settings_page_auto_preview.setChecked(state)

        state = self.data["settings"].get("ask_before_file_del", False)
        self.ui.settings_page_file_del_ask_check_box.setChecked(state)

        state = self.data["settings"].get("ask_before_album_del", True)
        self.ui.settings_page_album_del_ask_check_box.setChecked(state)

        accent_color = self.data["settings"].get("accent_color", "#c2ffc2")
        index = self.ui.settings_page_accent_color_combo_box.findData(accent_color)
        if index >= 0:
            self.ui.settings_page_accent_color_combo_box.setCurrentIndex(index)

    def select_standard_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Выберите папку", "")
        if folder_path:
            self.data["settings"]["default_dir"] = folder_path
            self.save_data()

    def remove_data(self):
        if self.can_proceed("Точно хотите стереть данные? Это удалит все ваши файлы и настройки"):
            self.data = {}
            self.save_data()
            self.restart_app()

    def update_accent_color(self):
        accent_color = self.ui.settings_page_accent_color_combo_box.currentData()
        self.data["settings"]["accent_color"] = accent_color
        self.save_data()
        # self.change_main_style()
        self.restart_app()

    def update_font_family(self):
        font_family = self.ui.settings_page_font_combo_box.currentFont().family()
        self.data["settings"]["font_family"] = font_family
        self.save_data()
        self.change_main_style()

    def toggle_auto_preview(self, is_checked):
        self.data["settings"]["auto_preview"] = is_checked
        self.save_data()

    def toggle_ask_before_file_del(self, is_checked):
        self.data["settings"]["ask_before_file_del"] = is_checked
        self.save_data()

    def toggle_ask_before_album_del(self, is_checked):
        self.data["settings"]["ask_before_album_del"] = is_checked
        self.save_data()

    @staticmethod
    def restart_app():
        executable = sys.executable
        args = sys.argv
        os.execl(executable, executable, *args)

    @staticmethod
    def get_base_path():
        if getattr(sys, 'frozen', False):
            return os.path.dirname(sys.executable)
        else:
            return os.path.dirname(os.path.abspath(__file__))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = PyGallery()
    window.show()

    sys.exit(app.exec())
