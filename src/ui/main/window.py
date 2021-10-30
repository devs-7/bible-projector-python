from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(709, 578)
        MainWindow.setStyleSheet("QPushButton {\n"
"    padding: 4px;\n"
"    background-color: transparent;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ccc;\n"
"    color: white;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #E9ECF1;")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(16, 8, 16, 16)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header_container = QtWidgets.QVBoxLayout()
        self.header_container.setObjectName("header_container")
        self.verticalLayout.addLayout(self.header_container)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(16)
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setObjectName("gridLayout")
        self.history_label = QtWidgets.QLabel(self.centralwidget)
        self.history_label.setStyleSheet("")
        self.history_label.setObjectName("history_label")
        self.gridLayout.addWidget(self.history_label, 0, 3, 1, 1)
        self.chapter_label = QtWidgets.QLabel(self.centralwidget)
        self.chapter_label.setObjectName("chapter_label")
        self.gridLayout.addWidget(self.chapter_label, 2, 0, 1, 1)
        self.preview_text_edit = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preview_text_edit.sizePolicy().hasHeightForWidth())
        self.preview_text_edit.setSizePolicy(sizePolicy)
        self.preview_text_edit.setMaximumSize(QtCore.QSize(16777215, 160))
        self.preview_text_edit.setStyleSheet("padding: 8px;\n"
"border: none;\n"
"border-radius: 8px;\n"
"background-color: white;\n"
"color: black;\n"
"font-size: 10pt;")
        self.preview_text_edit.setObjectName("preview_text_edit")
        self.gridLayout.addWidget(self.preview_text_edit, 1, 0, 1, 1)
        self.preview_label = QtWidgets.QLabel(self.centralwidget)
        self.preview_label.setObjectName("preview_label")
        self.gridLayout.addWidget(self.preview_label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(5, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.chapter_list_widget = QtWidgets.QListWidget(self.centralwidget)
        self.chapter_list_widget.setStyleSheet("QListWidget {\n"
"    padding: 8px;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    background-color: white;\n"
"    color: black;\n"
"    font-size: 10pt;\n"
"}")
        self.chapter_list_widget.setObjectName("chapter_list_widget")
        self.gridLayout.addWidget(self.chapter_list_widget, 3, 0, 1, 1)
        self.history_list_widget = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.history_list_widget.sizePolicy().hasHeightForWidth())
        self.history_list_widget.setSizePolicy(sizePolicy)
        self.history_list_widget.setMaximumSize(QtCore.QSize(240, 16777215))
        self.history_list_widget.setStyleSheet("padding: 8px;\n"
"border: none;\n"
"border-radius: 8px;\n"
"background-color: white;\n"
"color: black;\n"
"font-size: 10pt;")
        self.history_list_widget.setObjectName("history_list_widget")
        self.gridLayout.addWidget(self.history_list_widget, 1, 3, 3, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 709, 21))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        self.menuFerramentas = QtWidgets.QMenu(self.menubar)
        self.menuFerramentas.setObjectName("menuFerramentas")
        self.menuAjuda = QtWidgets.QMenu(self.menubar)
        self.menuAjuda.setObjectName("menuAjuda")
        MainWindow.setMenuBar(self.menubar)
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.actionVerificar_se_h_atualiza_es = QtWidgets.QAction(MainWindow)
        self.actionVerificar_se_h_atualiza_es.setObjectName("actionVerificar_se_h_atualiza_es")
        self.action_quit = QtWidgets.QAction(MainWindow)
        self.action_quit.setObjectName("action_quit")
        self.action_settings = QtWidgets.QAction(MainWindow)
        self.action_settings.setObjectName("action_settings")
        self.action_export_history = QtWidgets.QAction(MainWindow)
        self.action_export_history.setObjectName("action_export_history")
        self.action_advanced_search = QtWidgets.QAction(MainWindow)
        self.action_advanced_search.setObjectName("action_advanced_search")
        self.action_install_version = QtWidgets.QAction(MainWindow)
        self.action_install_version.setObjectName("action_install_version")
        self.menuArquivo.addAction(self.action_install_version)
        self.menuArquivo.addAction(self.action_export_history)
        self.menuArquivo.addSeparator()
        self.menuArquivo.addAction(self.action_settings)
        self.menuArquivo.addSeparator()
        self.menuArquivo.addAction(self.action_quit)
        self.menuFerramentas.addAction(self.action_advanced_search)
        self.menuAjuda.addAction(self.action_about)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuFerramentas.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Projetor bíblico"))
        self.history_label.setText(_translate("MainWindow", "Histórico"))
        self.chapter_label.setText(_translate("MainWindow", "Capítulo"))
        self.preview_label.setText(_translate("MainWindow", "Pré-visualização"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.menuFerramentas.setTitle(_translate("MainWindow", "Ferramentas"))
        self.menuAjuda.setTitle(_translate("MainWindow", "Ajuda"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))
        self.action_about.setText(_translate("MainWindow", "Sobre"))
        self.actionVerificar_se_h_atualiza_es.setText(_translate("MainWindow", "Verificar se há atualizações"))
        self.action_quit.setText(_translate("MainWindow", "Sair"))
        self.action_settings.setText(_translate("MainWindow", "Configurações"))
        self.action_export_history.setText(_translate("MainWindow", "Exportar histórico"))
        self.action_advanced_search.setText(_translate("MainWindow", "Pesquisa avançada"))
        self.action_install_version.setText(_translate("MainWindow", "Instalar versão"))
