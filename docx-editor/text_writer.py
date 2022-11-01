from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtCore import *


class Ui_Doc_Writer(object):
    def setupUi(self, Doc_Writer):
        Doc_Writer.setObjectName("Doc_Writer")
        Doc_Writer.resize(852, 762)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        Doc_Writer.setFont(font)
        Doc_Writer.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Doc_Writer)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:  rgb(85, 85, 255);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.message = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.message.setFont(font)
        self.message.setStyleSheet("color:  rgb(85, 85, 255);")
        self.message.setText("")
        self.message.setObjectName("message")
        self.horizontalLayout_5.addWidget(self.message)
        self.verticalLayout.addWidget(self.frame_3)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_4.setStyleSheet("border: 0.5px solid rgb(180, 180, 180);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.fontComboBox = QtWidgets.QFontComboBox(self.frame_4)
        self.fontComboBox.setMinimumSize(QtCore.QSize(120, 20))
        self.fontComboBox.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.fontComboBox.setFont(font)
        self.fontComboBox.setStyleSheet(" border:none;\n"
"border-radius: 5px;\n"
"font: 12pt \"Segoe UI\";")
        self.fontComboBox.setObjectName("fontComboBox")
        self.horizontalLayout_8.addWidget(self.fontComboBox)
        self.spinBox = QtWidgets.QSpinBox(self.frame_4)
        self.spinBox.setMinimumSize(QtCore.QSize(70, 25))
        self.spinBox.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.spinBox.setFont(font)
        self.spinBox.setStyleSheet(" border:none;\n"
"border-radius: 5px;\n"
"font: 12pt \"Segoe UI\";")
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_8.addWidget(self.spinBox)
        self.horizontalLayout_7.addWidget(self.frame_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setMinimumSize(QtCore.QSize(160, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(220, 40))
        self.pushButton.setStyleSheet("#pushButton{\n"
"font: 12pt \"Segoe UI\";\n"
"font-weight: 500;\n"
"background-color: white;\n"
"color: black; \n"
"border-radius: 4px;\n"
" border: 2px solid #008CBA;\n"
"}\n"
"\n"
"#pushButton:hover {\n"
"  background-color: #008CBA;\n"
"  color: white;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_7.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.horizontalLayout_6.addWidget(self.frame_2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"font: 18pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 500))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setStyleSheet("\n"
".QScrollBar{ \n"
"\n"
"background-color: none;\n"
" } ")
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 443, 618))
        self.scrollAreaWidgetContents_2.setStyleSheet("border: none;")
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 600))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("border:none;")
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_4.addWidget(self.textEdit)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        spacerItem6 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        Doc_Writer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Doc_Writer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 852, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        Doc_Writer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Doc_Writer)
        self.statusbar.setObjectName("statusbar")
        Doc_Writer.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(Doc_Writer)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.toolBar.setFont(font)
        self.toolBar.setObjectName("toolBar")
        Doc_Writer.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actioncopy = QtWidgets.QAction(Doc_Writer)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("source/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actioncopy.setIcon(icon)
        self.actioncopy.setObjectName("actioncopy")
        self.actionLeft = QtWidgets.QAction(Doc_Writer)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("source/left-align.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLeft.setIcon(icon1)
        self.actionLeft.setObjectName("actionLeft")
        self.actionRight = QtWidgets.QAction(Doc_Writer)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("source/right-align.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRight.setIcon(icon2)
        self.actionRight.setObjectName("actionRight")
        self.actionCenter = QtWidgets.QAction(Doc_Writer)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("source/center-align.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCenter.setIcon(icon3)
        self.actionCenter.setObjectName("actionCenter")
        self.actionjustificar = QtWidgets.QAction(Doc_Writer)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("source/justification.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionjustificar.setIcon(icon4)
        self.actionjustificar.setObjectName("actionjustificar")
        self.actionrecortar = QtWidgets.QAction(Doc_Writer)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("source/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionrecortar.setIcon(icon5)
        self.actionrecortar.setObjectName("actionrecortar")
        self.actionitalic = QtWidgets.QAction(Doc_Writer)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("source/italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionitalic.setIcon(icon6)
        self.actionitalic.setObjectName("actionitalic")
        self.actionunderline = QtWidgets.QAction(Doc_Writer)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("source/underline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionunderline.setIcon(icon7)
        self.actionunderline.setObjectName("actionunderline")
        self.actionbold = QtWidgets.QAction(Doc_Writer)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("source/Negrito.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbold.setIcon(icon8)
        self.actionbold.setObjectName("actionbold")
        self.toolBar.addAction(self.actioncopy)
        self.toolBar.addAction(self.actionrecortar)
        self.toolBar.addAction(self.actionLeft)
        self.toolBar.addAction(self.actionRight)
        self.toolBar.addAction(self.actionCenter)
        self.toolBar.addAction(self.actionjustificar)
        self.toolBar.addAction(self.actionitalic)
        self.toolBar.addAction(self.actionunderline)
        self.toolBar.addAction(self.actionbold)

        self.actionLeft.triggered.connect(lambda : self.textEdit.setAlignment(Qt.AlignLeft))

        self.actionRight.triggered.connect(lambda : self.textEdit.setAlignment(Qt.AlignRight))

        self.actionCenter.triggered.connect(lambda : self.textEdit.setAlignment(Qt.AlignCenter))

        self.actionjustificar.triggered.connect(lambda : self.textEdit.setAlignment(Qt.AlignJustify))

        self.actioncopy.triggered.connect(self.textEdit.copy)
        self.actionrecortar.triggered.connect(self.textEdit.cut)
        self.spinBox.setValue(18)
        self.fontComboBox.activated.connect(self.setFont)
        self.spinBox.valueChanged.connect(self.setFontSize)
        self.actionitalic.triggered.connect(self.italicText)
        self.actionunderline.triggered.connect(self.underlineText)
        self.actionbold.triggered.connect(self.boldText)
        self.pushButton.clicked.connect(self.imprimir)
        self.retranslateUi(Doc_Writer)
        QtCore.QMetaObject.connectSlotsByName(Doc_Writer)
        
        #ok
    def setFontSize(self):
        value = self.spinBox.value()
        self.textEdit.setFontPointSize(value)  
        #ok
        
    def setFont(self):
        font = self.fontComboBox.currentText()
        print(font)

        self.textEdit.setCurrentFont(QFont('Arial'))    
        
        #ok
    def italicText(self):
        state = self.textEdit.fontItalic()
        self.textEdit.setFontItalic(not(state)) 
        #ok
    def underlineText(self):
        state = self.textEdit.fontUnderline()
        self.textEdit.setFontUnderline(not(state))   
        
    def boldText(self):
        if self.textEdit.fontWeight != QFont.Bold:
           self.textEdit.setFontWeight(QFont.Bold)
           return
        self.textEdit.setFontWeight(QFont.Normal)      

    def imprimir(self):

        from docxtpl import DocxTemplate, InlineImage
        import datetime as dt
        from docx2pdf import convert
        from docx.shared import Mm
        from datetime import datetime
        try:

                file = str(QFileDialog.getExistingDirectory(None, 'Select Path'))
                string = ''.join(file).replace("'", "")

                n_string = string.replace(', All Files (*))', '').strip("()")
                new_string = f'{n_string}/dados.docx'
                print(new_string)
                # create a document object
                doc = DocxTemplate("dat_do_ - lemb.docsti")


                
                dados = self.textEdit.toPlainText()
                print(dados)

                data_e_hora_atuais = datetime.now()
                data_atual = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")


                context = {
                        "datetime__": f"{data_atual}",
                        "note": f"{dados}",
                        "code": f"{'0'}",
                        "DATA_DE_HOJE": f"{data_atual}"
                }
                        # inject image into the context

        #  context['logo'] = InlineImage(doc, image_descriptor='icons8-login-64.png', width=Mm(20), height=Mm(24))



                        # render context into the document object
                doc.render(context)

                        # save the document object as a word file
                doc.save('lembrete.docx')

                # convert word file to a pdf file
                convert('lembrete.docx', 'lembrete.pdf')

        except:
                pass





    def retranslateUi(self, Doc_Writer):
        _translate = QtCore.QCoreApplication.translate
        Doc_Writer.setWindowTitle(_translate("Doc_Writer", "Writer"))
        self.label_2.setText(_translate("Doc_Writer", "PÁGINA INICIAL"))
        self.pushButton.setText(_translate("Doc_Writer", "Salvar documento"))
        self.label.setText(_translate("Doc_Writer", "       Docx Writer"))
        self.textEdit.setPlaceholderText(_translate("Doc_Writer", "Escreva aqui!"))
        self.toolBar.setWindowTitle(_translate("Doc_Writer", "toolBar"))
        self.actioncopy.setText(_translate("Doc_Writer", "copiar"))
        self.actionLeft.setText(_translate("Doc_Writer", "Left"))
        self.actionRight.setText(_translate("Doc_Writer", "Right"))
        self.actionCenter.setText(_translate("Doc_Writer", "Justificar"))
        self.actionjustificar.setText(_translate("Doc_Writer", "justificar"))
        self.actionrecortar.setText(_translate("Doc_Writer", "recortar"))
        self.actionitalic.setText(_translate("Doc_Writer", "italic"))
        self.actionunderline.setText(_translate("Doc_Writer", "underline"))
        self.actionbold.setText(_translate("Doc_Writer", "bold"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Doc_Writer = QtWidgets.QMainWindow()
    ui = Ui_Doc_Writer()
    ui.setupUi(Doc_Writer)
    Doc_Writer.show()
    sys.exit(app.exec_())
