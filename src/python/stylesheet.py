def return_stylesheet(font_family, accent_color):
    return f"""
        QWidget {{
            font-size: 18px;
            font-family: {font_family};
            background-color: #fff;
        }}

        #sidebar QPushButton,
        #media_page_header QPushButton,
        #locked_folder_page_header QPushButton,
        #photo_page_header QPushButton,
        #video_page_header QPushButton,
        #settings_page_scroll_area_widget QPushButton {{
            border: none;
            border-radius: 25px;
            color: #444746;
            padding: 15px;
            text-align: left;
            font-weight: 600;
        }}

        #sidebar QPushButton:hover,
        #media_page_header QPushButton:hover,
        #locked_folder_page_header QPushButton:hover,
        #photo_page_header QPushButton:hover,
        #video_page_header QPushButton:hover,
        #settings_page_scroll_area_widget QPushButton:hover {{
            background-color: #ededed;
        }}

        #sidebar QPushButton:pressed,
        #media_page_header QPushButton:pressed,
        #locked_folder_page_header QPushButton:pressed,
        #photo_page_header QPushButton:pressed,
        #video_page_header QPushButton:pressed,
        #settings_page_scroll_area_widget QPushButton:pressed {{
            background-color: {accent_color};
        }}

        #media_page_header_label, #locked_folder_page_header_label,
        #photo_page_header_label, #video_page_header_label,
        #settings_page_header_label {{
            font-size: 22px;
        }}

        #label_8, #label, #label_4 {{
            font-size: 20px;
            font-weight: bold;
        }}

        QScrollBar:vertical {{
            background: #ededed;
            width: 10px;
            margin: 0px;
            border-radius: 5px;
        }}

        QScrollBar::handle:vertical {{
            background-color: {accent_color};
            border-radius: 5px;
        }}

        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
            background: none;
            height: 0px;
        }}

        QMessageBox QPushButton, QInputDialog QPushButton {{
            color: #444746;
            border-radius: 10px;
            min-width: 80px;
            padding: 5px;
        }}

        QMessageBox QPushButton:hover, QInputDialog QPushButton:hover {{
            background-color: #ededed;
        }}

        QMessageBox QPushButton:pressed, QInputDialog QPushButton:pressed {{
            background-color: {accent_color};
        }}
        
        QComboBox, QFontComboBox {{
            color: #000;
            background-color: {accent_color};
            padding: 10px;
            border-radius: 20px;
        }}
    """