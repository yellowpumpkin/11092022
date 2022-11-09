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

from mySQL import database

db = database()


class UI_Resizewood(QMainWindow):
    def __init__(self):
        super().__init__()
        self.addResize = None
        self.addHeat = None
        self.tb = None
        self.addHome = None
        self.addInput = None
        self.addCut = None
        self.resizeTable2 = None
        self.w = None  # No external window yet.
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
        self.displayTable2()
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
        self.addResize = QAction(QIcon('icons/cutting.png'), "รายการแปลงไม้", self)
        self.tb.addAction(self.addResize)
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
        self.wg = QWidget(self)
        self.setCentralWidget(self.wg)

        self.searchText = QLabel("Wood Code : ")
        self.searchEntry = QLineEdit()
        self.searchEntry.setPlaceholderText("Ex. ARG291221")

        self.searchButton = QPushButton("Search")
        self.searchButton.clicked.connect(self.funcSearch)

        self.btn_withdraw = QPushButton("เบิกไม้ประจำวัน")
        self.btn_withdraw.setShortcut('Return')

        self.btn_refresh = QPushButton("Refresh")
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
        self.mainLayout.addLayout(self.mainTable2Layout)

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


class Another_Window(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self,list_value,date,type_resize):
        super().__init__()
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

        if totem == True:
            self.neweditInput = resize_wood(self.list_wood, self.str_date, self.type_resize, wood_quantity)
            self.close()


class resize_wood (QWidget):
    def __init__(self,listwood,date,type_resize,quantity):
        super().__init__()
        self.setWindowTitle("ใบเบิกไม้")
        self.setWindowIcon(QIcon('icons/cutting.png'))
        self.setGeometry(450,150,960,600)
        self.setFixedSize(self.size())
        self.list_wood_resize = listwood
        self.wood_code = listwood[0]
        self.wood_thick = listwood[1]
        self.wood_wide = listwood[2]
        self.wood_long = listwood[3]
        self.wood_type = listwood[5]
        self.wood_quantity = quantity
        self.str_date = date
        self.type_cut = type_resize
        self.UI()
        self.show()

    def UI(self):
        self.display()
        self.layout()

    def display(self):

        icon = QPixmap('icons/s.png')
        self.text_company = QLabel("<font color='Black' size='5'>Siam Kyohwa Seisakusho Co., Ltd.</font> ", self)
        self.label = QLabel(self)
        self.label.setPixmap(icon)
        self.label.setAlignment(Qt.AlignCenter)
        self.text_company.setMinimumHeight(icon.height())

        self.text_date = QLabel(self)
        self.text_date.setText("วันที่เบิกไม้: " + str(self.str_date))
        self.text_type = QLabel(self)
        self.text_type.setText("ประเภทการเบิกไม้ : "+self.type_cut+" (Resize)")
        self.wood_text = QLabel(self)
        self.wood_text.setText("WOOD CODE : "+self.wood_code+" Thick: "+self.wood_thick+
                               " Wide: "+self.wood_wide+" Long: "+self.wood_long+" Wood type: "+self.wood_type+" Quantity: "+str(self.wood_quantity))

        self.btn_confirm = QPushButton(self)
        self.btn_confirm.setText("ยืนยัน")
        self.btn_confirm.setShortcut('Return')
        self.btn_confirm.setStyleSheet("""
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
                 }
             """)
        # RESIZE1
        self.thickText1 = QLabel("หนา")
        self.wideText1 = QLabel("x กว้าง")
        self.longText1 = QLabel("x ยาว")
        self.equal1 = QLabel(" =  ")

        # Thick
        self.thickCombobox1 = QComboBox()
        Thick = db.sqlThick()
        for data_thick in Thick:
            self.thickCombobox1.addItems([str(data_thick)])
        self.thickCombobox1.setEditable(True)
        self.thickCombobox1.setValidator(QIntValidator())

        # Wide
        self.wideCombobox1 = QComboBox()
        Wide = db.sqlWide()
        for data_wide in Wide:
            self.wideCombobox1.addItems([str(data_wide)])
        self.wideCombobox1.setEditable(True)
        self.wideCombobox1.setValidator(QIntValidator())
        # Longs
        self.longCombobox1 = QComboBox()
        self.longCombobox1.addItem(self.wood_long)
        self.woodquantityEntry1 = QLineEdit(self)
        self.woodquantityEntry1.setValidator(QIntValidator())

        # RESIZE2
        self.thickText2 = QLabel("หนา")
        self.wideText2 = QLabel("x กว้าง")
        self.longText2 = QLabel("x ยาว")
        self.equal2 = QLabel(" =  ")

        # Thick
        self.thickCombobox2 = QComboBox()
        for data_thick in Thick:
            self.thickCombobox2.addItems([str(data_thick)])
        self.thickCombobox2.setEditable(True)
        self.thickCombobox2.setValidator(QIntValidator())

        # Wide
        self.wideCombobox2 = QComboBox()
        for data_wide in Wide:
            self.wideCombobox2.addItems([str(data_wide)])
        self.wideCombobox2.setEditable(True)
        self.wideCombobox2.setValidator(QIntValidator())
        # Longs
        self.longCombobox2 = QComboBox()
        self.longCombobox2.addItem(self.wood_long)
        self.woodquantityEntry2 = QLineEdit(self)
        self.woodquantityEntry2.setValidator(QIntValidator())

        # RESIZE3
        self.thickText3 = QLabel("หนา")
        self.wideText3 = QLabel("x กว้าง")
        self.longText3 = QLabel("x ยาว")
        self.equal3 = QLabel(" =  ")

        # Thick
        self.thickCombobox3 = QComboBox()
        for data_thick in Thick:
            self.thickCombobox3.addItems([str(data_thick)])
        self.thickCombobox3.setEditable(True)
        self.thickCombobox3.setValidator(QIntValidator())

        # Wide
        self.wideCombobox3 = QComboBox()
        for data_wide in Wide:
            self.wideCombobox3.addItems([str(data_wide)])
        self.wideCombobox3.setEditable(True)
        self.wideCombobox3.setValidator(QIntValidator())
        # Longs
        self.longCombobox3 = QComboBox()
        self.longCombobox3.addItem(self.wood_long)
        self.woodquantityEntry3 = QLineEdit(self)
        self.woodquantityEntry3.setValidator(QIntValidator())

    def layout(self):
        self.mainLayout = QVBoxLayout()
        self.headLayout = QHBoxLayout()
        self.mainTopLayout = QVBoxLayout()
        self.CenterLayout1 = QVBoxLayout()
        self.CenterLayout2 = QVBoxLayout()

        self.resize1Layout = QHBoxLayout()
        self.resize2Layout = QHBoxLayout()
        self.resize3Layout = QHBoxLayout()

        self.groupBox1 = QWidget()
        self.groupBox2 = QWidget()
        self.resize1 = QGroupBox("RESIZE 1")
        self.resize2 = QGroupBox("RESIZE 2")
        self.resize3 = QGroupBox("RESIZE 3")
        self.btn_box = QHBoxLayout()
        #
        self.headLayout.addStretch()
        self.headLayout.addWidget(self.label)
        self.headLayout.addWidget(self.text_company)
        self.headLayout.addStretch()
        self.groupBox2.setLayout(self.headLayout)


        self.CenterLayout1.addWidget(self.text_date)
        self.CenterLayout1.addWidget(self.text_type)
        # self.CenterLayout1.addWidget(self.wood_text)
        self.groupBox1.setLayout(self.CenterLayout1)

        self.resize1Layout.addWidget(self.thickText1)
        self.resize1Layout.addWidget(self.thickCombobox1)
        self.resize1Layout.addWidget(self.wideText1)
        self.resize1Layout.addWidget(self.wideCombobox1)
        self.resize1Layout.addWidget(self.longText1)
        self.resize1Layout.addWidget(self.longCombobox1)
        self.resize1Layout.addWidget(self.equal1)
        self.resize1Layout.addWidget(self.woodquantityEntry1)
        self.resize1.setLayout(self.resize1Layout)

        self.resize2Layout.addWidget(self.thickText2)
        self.resize2Layout.addWidget(self.thickCombobox2)
        self.resize2Layout.addWidget(self.wideText2)
        self.resize2Layout.addWidget(self.wideCombobox2)
        self.resize2Layout.addWidget(self.longText2)
        self.resize2Layout.addWidget(self.longCombobox2)
        self.resize2Layout.addWidget(self.equal2)
        self.resize2Layout.addWidget(self.woodquantityEntry2)
        self.resize2.setLayout(self.resize2Layout)

        self.resize3Layout.addWidget(self.thickText3)
        self.resize3Layout.addWidget(self.thickCombobox3)
        self.resize3Layout.addWidget(self.wideText3)
        self.resize3Layout.addWidget(self.wideCombobox3)
        self.resize3Layout.addWidget(self.longText3)
        self.resize3Layout.addWidget(self.longCombobox3)
        self.resize3Layout.addWidget(self.equal3)
        self.resize3Layout.addWidget(self.woodquantityEntry3)
        self.resize3.setLayout(self.resize3Layout)

        self.btn_box.addStretch()
        self.btn_box.addWidget(self.btn_confirm)

        self.mainTopLayout.addWidget(self.groupBox2)
        self.mainTopLayout.addWidget(self.groupBox1)
        self.mainTopLayout.addWidget(self.resize1)
        self.mainTopLayout.addWidget(self.resize2)
        self.mainTopLayout.addWidget(self.resize3)

        # self.mainLayout.addLayout(self.headLayout)
        self.mainLayout.addLayout(self.mainTopLayout)
        self.mainLayout.addLayout(self.btn_box)
        self.setLayout(self.mainLayout)


# Main
import sys
def Resize():
    app = QtWidgets.QApplication(sys.argv)
    window=UI_Resizewood()
    sys.exit(app.exec_())


if __name__ == "__main__":
   Resize()
