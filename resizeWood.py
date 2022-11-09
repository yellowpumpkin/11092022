from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import heatWood
import inputWood
import withdrawWood
import saleWood
import cuttingWood
import main
import resize_card
import receiveWood

from mySQL import database

db = database()


class UI_Resizewood(QMainWindow):
    def __init__(self):
        super().__init__()
        self.addHeat = None
        self.tb = None
        self.addHome = None
        self.addInput = None
        self.addCut = None
        self.resizeTable2 = None

        self.setWindowTitle("รายการแปลงไม้")
        self.setWindowIcon(QIcon('icons/cutting.png'))
        self.setGeometry(450, 50, 1280, 1024)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.toolBar()
        self.display()
        self.displayTable1()
        self.funcFetchData()
        self.layouts()

    # Tool Bar
    def toolBar(self):
        self.tb = self.addToolBar("Tool Bar")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        # หน้าหลัก
        self.addHome = QAction(QIcon('icons/warehouse01.png'), "หน้าหลัก", self)
        self.tb.addAction(self.addHome)
        self.addHome.triggered.connect(self.funcHome)
        self.tb.addSeparator()
        # รับไม้เข้า
        self.addInput = QAction(QIcon('icons/forklift.png'), "รายการรับไม้เข้า", self)
        self.tb.addAction(self.addInput)
        self.addInput.triggered.connect(self.funcInput)
        self.tb.addSeparator()
        # Cutting
        self.addCut = QAction(QIcon('icons/cutting.png'), "รายการตัด/ผ่า", self)
        self.tb.addAction(self.addCut)
        self.addCut.triggered.connect(self.funcCut)
        self.tb.addSeparator()
        # Resize
        self.addResize = QAction(QIcon('icons/sawmill.png'), "รายการแปลงไม้", self)
        self.tb.addAction(self.addResize)
        self.tb.addSeparator()
        # Resize
        self.addReceive = QAction(QIcon('icons/wood01.png'), "รายการรับไม้", self)
        self.tb.addAction(self.addReceive)
        self.addReceive.triggered.connect(self.funcReceive)
        self.tb.addSeparator()
        # Heat
        self.addHeat = QAction(QIcon('icons/heat01.png'), "รายการอบไม้", self)
        self.tb.addAction(self.addHeat)
        self.addHeat.triggered.connect(self.funcHeat)
        self.tb.addSeparator()
        # Sale
        self.addSale = QAction(QIcon('icons/sale01.png'), "รายการขาย", self)
        self.tb.addAction(self.addSale)
        self.addSale.triggered.connect(self.funcSale)
        self.tb.addSeparator()
        # เบิกไม้
        self.addWithdraw = QAction(QIcon('icons/wood02.png'), "รายการเบิกไม้", self)
        self.tb.addAction(self.addWithdraw)
        self.addWithdraw.triggered.connect(self.funcWithdraw)
        self.tb.addSeparator()

    # display
    def display(self):
        self.wg = QWidget()
        self.setCentralWidget(self.wg)

        self.searchText = QLabel("Wood Code : ")
        self.searchEntry = QLineEdit()
        self.searchEntry.setPlaceholderText("Ex. ARG291221")

        self.searchButton = QPushButton("Search")
        self.searchButton.clicked.connect(self.funcSearch)
        self.searchButton.setShortcut('Return')

        self.btn_withdraw = QPushButton("เบิกไม้ประจำวัน")
        self.btn_withdraw.setShortcut('Return')

        self.btn_refresh = QPushButton("Refresh")
        self.btn_refresh.clicked.connect(self.funcRefresh)
        self.btn_refresh.setShortcut('F5')

        self.btn_excel = QPushButton(self)
        self.btn_excel.setIcon(QIcon('icons/excel (2).png'))

        withdraw_type = db.sqlWithdrawType()
        self.type_resize = withdraw_type[3]
        self.text_type_withdraw = QLabel("ประเภทการเบิก : " + str(self.type_resize))

        date = QDateTime.currentDateTime()
        self.dateDisplay = date.toString('yyyy-MM-dd')
        self.dateText = QLabel("วันทีเบิกไม้ : " + self.dateDisplay)

    # table
    def displayTable1(self):
        self.resizeTable1 = QTableWidget()
        self.resizeTable1.setColumnCount(8)
        header = ['โค้ดไม้', 'หนา', 'กว้าง', 'ยาว', 'ปริมาตร', 'ประเภท', 'จำนวน', 'manage']
        self.resizeTable1.setHorizontalHeaderLabels(header)
        column_size = self.resizeTable1.horizontalHeader()

        for i in range(0, 7):
            column_size.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        self.resizeTable1.setEditTriggers(QAbstractItemView.NoEditTriggers)



    def displayTable2(self):
        self.resizeTable2 = QTableWidget()
        self.resizeTable2.setColumnCount(8)
        header = ['โค้ดไม้', 'หนา', 'กว้าง', 'ยาว', 'ปริมาตร', 'ประเภท', 'จำนวน', 'Delete']
        self.resizeTable2.setHorizontalHeaderLabels(header)
        column_size = self.resizeTable2.horizontalHeader()
        for i in range(0, 7):
            column_size.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        self.resizeTable2.setEditTriggers(QAbstractItemView.NoEditTriggers)

    # Layouts
    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.mainTable1Layout = QHBoxLayout()
        self.mainTable2Layout = QHBoxLayout()
        self.mainTopLayout = QHBoxLayout()
        self.textLayout = QHBoxLayout()
        self.btn_withdraw_Layout = QHBoxLayout()
        self.centerMiddleLayout = QHBoxLayout()
        self.btn_refresh_Layout= QHBoxLayout()
        self.searchLayout = QHBoxLayout()
        self.btnGropBox = QGroupBox("")
        self.btnGropBox2 = QGroupBox("")
        self.textGropBox = QGroupBox("")
        self.searchGropBox = QGroupBox()

        # Search
        self.searchLayout.addWidget(self.searchText)
        self.searchLayout.addWidget(self.searchEntry)
        self.searchLayout.addWidget(self.searchButton)
        self.searchGropBox.setLayout(self.searchLayout)

        # Btn
        self.btn_withdraw_Layout.addWidget(self.btn_withdraw)
        self.btn_withdraw_Layout.addWidget(self.btn_excel)
        self.btnGropBox.setLayout(self.btn_withdraw_Layout)
        self.btn_refresh_Layout.addWidget(self.btn_refresh)
        self.btnGropBox2.setLayout(self.btn_refresh_Layout)

        # Left Top
        self.textLayout.addStretch()
        self.textLayout.addWidget(self.text_type_withdraw)
        self.textLayout.addWidget(self.dateText)
        # self.leftTopLayout.addWidget(self.dateDisplay)
        self.textLayout.addStretch()
        self.textGropBox.setLayout(self.textLayout)

        # Table
        self.mainTable1Layout.addWidget(self.resizeTable1)
        self.mainTable2Layout.addWidget(self.resizeTable2)

        # All Layout
        self.mainTopLayout.addWidget(self.searchGropBox)
        self.mainTopLayout.addWidget(self.textGropBox)
        self.mainTopLayout.addWidget(self.btnGropBox2)
        self.mainTopLayout.addWidget(self.btnGropBox)

        self.mainLayout.addLayout(self.mainTopLayout)
        self.mainLayout.addLayout(self.mainTable1Layout)
        # self.mainLayout.addLayout(self.mainTable2Layout)

        # Main Layout
        self.wg.setLayout(self.mainLayout)

    def funcFetchData(self):
        for i in reversed(range(self.resizeTable1.rowCount())):
            self.resizeTable1.removeRow(i)
        query = db.fetch_dataResize()
        for row_data in query:
            row_number = self.resizeTable1.rowCount()
            self.resizeTable1.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem()
                item.setData(QtCore.Qt.EditRole, data)
                self.resizeTable1.setItem(row_number, column_number, item)
            btn_select = QPushButton('เลือก')

            btn_select.setStyleSheet("""
                                               QPushButton {
                                                   color:  black;
                                                   border-style: solid;
                                                   border-width: 3px;
                                                   border-color:  #4CAF50;
                                                   border-radius: 12px }
                                               QPushButton:hover{
                                                   background-color: #4CAF50;
                                                   color: white; }
                                               """)
            btn_select.clicked.connect(self.func_handleButtonClicked)
            self.resizeTable1.setCellWidget(row_number, 7, btn_select)
        self.resizeTable1.setEditTriggers(QAbstractItemView.NoEditTriggers)

    # Search
    def funcSearch(self):
        value = self.searchEntry.text()
        if value == "":
            QMessageBox.warning(self, "Siam Kyohwa", "search cant be empty!")
        else:
            self.searchEntry.text()
            results = db.searchCutting(value)
            if results == []:
                QMessageBox.warning(self, "Siam Kyohwa", "wood id information not found!")
            else:
                for i in reversed(range(self.resizeTable1.rowCount())):
                    self.resizeTable1.removeRow(i)
                for row_data in results:
                    row_number = self.resizeTable1.rowCount()
                    self.resizeTable1.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        item = QTableWidgetItem()
                        item.setData(QtCore.Qt.EditRole, data)
                        self.resizeTable1.setItem(row_number, column_number, item)
                    btn_select = QPushButton('เลือก')
                    btn_select.setStyleSheet("""
                                                QPushButton {
                                                    color:  black;
                                                    border-style: solid;
                                                    border-width: 3px;
                                                    border-color:  #4CAF50;
                                                    border-radius: 12px }
                                                QPushButton:hover{
                                                    background-color: #4CAF50;
                                                    color: white; }
                                                        """)
                    # btn_select.clicked.connect(self.func_handleButtonClicked)
                    self.resizeTable1.setCellWidget(row_number, 7, btn_select)
                self.resizeTable1.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def func_handleButtonClicked(self):
        list_value = []
        for col in range(0, 7):
            list_value.append(self.resizeTable1.item(self.resizeTable1.currentRow(), col).text())
        self.w = Another_Window(list_value,self.dateDisplay,self.type_resize)
    # Refresh
    def funcRefresh(self):
        self.funcFetchData()

    # Function Home
    def funcHome(self):
        self.newHome = main.Ui_MainWindow()
        self.close()

    # Function AddProduct
    def funcInput(self):
        self.newInput = inputWood.UI_Inputwood()
        self.close()

    # Function Cut
    def funcCut(self):
        self.newCut = cuttingWood.UI_Cutwood()
        self.close()

    # Function Withdraw
    def funcWithdraw(self):
        self.newWithdraw = withdrawWood.UI_Withdraw()
        self.close()

    # Function Heat
    def funcHeat(self):
        self.newHeat = heatWood.UI_Heatwood()
        self.close()

    # Function Sale
    def funcSale(self):
        self.newSale = saleWood.UI_Salewood()
        self.close()

    def funcReceive(self):
        self.newReceive = receiveWood.UI_Receive()
        self.close()

class Another_Window(QWidget):
    def __init__(self,list_value,date,type_resize):
        super().__init__()
        self.MainWindow = None
        self.setWindowTitle("เบิกไม้")
        self.setWindowIcon(QIcon('icons/cutting.png'))
        self.setGeometry(950, 350, 260, 260)
        self.setFixedSize(self.size())
        self.list_wood = list_value
        self.wood_code = list_value[0]
        self.quantity_stock = list_value[6]
        self.str_date = date
        self.type_resize = type_resize
        self.show()
        self.UI()

    def UI(self):
        self.display()
        self.layout()

    def display(self):
        self.title_txt = QLabel("เบิกไม้")
        self.title_txt.setFont(QFont('Arial', 12))
        self.title_txt.setAlignment(Qt.AlignCenter)

        self.woodcodeEntry = QLineEdit(self)
        self.woodcodeEntry.setText(self.wood_code)
        self.woodcodeEntry.setReadOnly(True)

        self.quantitystockEntry = QLineEdit(self)
        self.quantitystockEntry.setText(self.quantity_stock)
        self.quantitystockEntry.setReadOnly(True)

        self.quantityEntry = QLineEdit(self)
        self.quantityEntry.setValidator(QIntValidator())

        self.btnOK = QPushButton('&OK',self)
        self.btnOK.setText("ยืนยัน") # text
        self.btnOK.setShortcut('Return') # shortcut key
        self.btnOK.setStyleSheet("""
              QPushButton {
                  background-color: #008CBA;
                  color: white;
                  font-size: 14px;
                  text-align: center;
                  padding: 10px 24px;
                  border-radius: 4px
               }
              QPushButton:hover {
                  background-color: white; 
                  border: 0.5px solid #008CBA;
                  color: black;
              }   """)
        self.btnOK.clicked.connect(self.func_handleButtonClicked)

    def layout(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.midLayout = QHBoxLayout()
        self.bottomLayout = QFormLayout()
        self.btnbox = QHBoxLayout()
        self.text = QWidget()
        self.middleFrame = QGroupBox()
        self.bottomFrame = QFrame()
        # Top
        self.topLayout.addWidget(self.title_txt)
        self.text.setLayout(self.topLayout)

        self.bottomLayout.addRow(QLabel("woodcode : "), self.woodcodeEntry)
        self.bottomLayout.addRow(QLabel("จำนวนใน stock: "), self.quantitystockEntry)
        self.bottomLayout.addRow(QLabel("จำนวนเบิก: "), self.quantityEntry)
        self.bottomFrame.setLayout(self.bottomLayout)

        # Btn
        self.btnbox.addStretch()
        self.btnbox.addWidget(self.btnOK)

        # All Layout
        self.mainLayout.addWidget(self.bottomFrame)
        self.mainLayout.addLayout(self.btnbox)
        self.setLayout(self.mainLayout)

    def func_handleButtonClicked(self):
        wood_quantity = 0
        list_withdraw_resize=[]
        try:
            wood_code = self.woodcodeEntry.text()
            quantity = int(self.quantityEntry.text())
            check = db.func_check_quantity_wood(wood_code)
            my_quantity = int(check[0])
            totem = True
            if quantity <= 0:
                QMessageBox.critical(self, "Siam Kyohwa", " จำนวนการเบิกไม่ถูกต้อง ")
                totem = False
            if quantity > my_quantity:
                QMessageBox.critical(self, "Siam Kyohwa", " เบิกเกินจำนวนค่ะ ")
                totem = False
            else:
                wood_quantity = quantity
        except ValueError:
            QMessageBox.information(self, "Siam Kyohwa", "กรุณากรอกข้อมูลให้ครบถ้วนค่ะ")
            totem = False
        list_withdraw_resize.append(tuple(self.list_wood))
        if totem == True:
            self.close()
            # self.w = UI_Resizewood.close()
            self.neweditInput = resize_card.resize_wood(list_withdraw_resize, self.str_date, self.type_resize, wood_quantity)


import sys
def Resize():
    app = QtWidgets.QApplication(sys.argv)
    window=UI_Resizewood()
    sys.exit(app.exec_())

if __name__ == "__main__":
   Resize()
