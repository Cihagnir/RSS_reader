import sys
from PyQt5.QtWidgets import QApplication,QCheckBox,QTabWidget,QVBoxLayout,QWidget,QLabel,QPushButton,QLineEdit

import RSS
import Web_site

class Window(QWidget):
    def __init__(self):
        """Prepare the main board to play on it"""
        super().__init__()
        self.setWindowTitle("RSS feed reader")
        self.resize(500, 600)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        """Creating a menutab"""
        self.menu_tab = QTabWidget()
        self.Menutab_handler()
        self.main_layout.addWidget(self.menu_tab)


        self.Webpage_name_text = QLabel("Web Page Name :: ")
        self.Webpage_name = QLineEdit()
        self.Web_link_text = QLabel("RSS feed link :::")
        self.Web_link = QLineEdit()
        self.Add_button = QPushButton("Add the new RSS feed link")

        self.main_layout.addWidget(self.Webpage_name_text)
        self.main_layout.addWidget(self.Webpage_name)
        self.main_layout.addWidget(self.Web_link_text)
        self.main_layout.addWidget(self.Web_link)
        self.main_layout.addWidget(self.Add_button)

        self.Add_button.clicked.connect(self.RSS_link_adder)


    def Menutab_handler(self):

        for webpage_name,weblink in RSS.RSS_reader.list_RSS :
            list_news = RSS.RSS_reader.get_scracth(weblink)
            sub_tab = QWidget()
            main_layout = QVBoxLayout()
            for news_tuple in list_news:
                self.Tab_ui_creator(main_layout,news_tuple)
            sub_tab.setLayout(main_layout)
            self.menu_tab.addTab(sub_tab,webpage_name)

    def Tab_ui_creator(self,main_layout,news_tuple):
        news_layout = QVBoxLayout()
        news_layout.addWidget(QLabel(news_tuple[0]))
        news_layout.addWidget(QLabel(news_tuple[1]))
        news_layout.addWidget(QLabel(news_tuple[2]))
        main_layout.addLayout(news_layout)

    def RSS_link_adder(self):
        Webpage_name = self.Webpage_name.text()
        Webpage_link = self.Web_link.text()

        RSS.RSS_reader.add_RSS(Webpage_name,Webpage_link)



    def generalTabUI(self):
        """Create the General page UI."""
        generalTab = QWidget()
        layout_1= QVBoxLayout()
        layout_2 = QVBoxLayout()
        layout_2.addWidget(QCheckBox("General Option 1"))
        layout_2.addWidget(QCheckBox("General Option 2"))
        layout_3 = QVBoxLayout()
        layout_3.addWidget(QCheckBox("General Option 1"))
        layout_3.addWidget(QCheckBox("General Option 2"))
        layout_1.addLayout(layout_2)
        layout_1.addLayout(layout_3)
        generalTab.setLayout(layout_1)
        return generalTab


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
