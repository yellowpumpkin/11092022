from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import heatWood
import main
import resizeWood
import saleWood
import withdrawWood
import cuttingWood
import editsInputwood
# import pandas as pd

from mySQL import database
db = database()

class UI_Inputwood(QMainWindow):
    def __init__(self):
        super().__init__()
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.setWindowTitle("ข้อมูลรับไม้เข้า")
        self.setWindowIcon(QIcon('icons/wood01.png'))
        self.setGeometry(450, 50, 1280, 1024)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):

        self.toolBar()
        self.displayTable()
        self.display()
        self.layouts()
        self.funcFetchData()

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
        self.tb.addSeparator()
        # Cutting
        self.addCut = QAction(QIcon('icons/cutting.png'), "รายการตัด/ผ่า", self)
        self.tb.addAction(self.addCut)
        self.addCut.triggered.connect(self.funcCut)
        self.tb.addSeparator()
        # Resize
        self.addResize = QAction(QIcon('icons/sawmill.png'), "รายการแปลงไม้", self)
        self.tb.addAction(self.addResize)
        self.addResize.triggered.connect(self.funcResize)
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

# Widget
    def display(self):
        self.wg = QWidget()
        self.setCentralWidget((self.wg))

        self.searchText = QLabel("Wood Code : ")
        self.searchEntry = QLineEdit()
        self.searchEntry.setPlaceholderText("Ex. ARG291221")
        self.searchButton = QPushButton("Search")
        self.searchButton.clicked.connect(self.funcSearch)

        # combobox
        self.sizeText = QLabel(self)
        self.sizeText.setText("size")
        self.thickText = QLabel("thick")
        self.wideText = QLabel("x wide")
        self.longText = QLabel("x long")

        # combobox thick
        self.combboxThick = QComboBox()
        Thick = db.sqlThick()
        for data_thick in Thick:
            self.combboxThick.addItems([str(data_thick)])

        # combobox wide
        self.comboboxWide = QComboBox()
        Wide = db.sqlWide()
        for data_wide in Wide:
            self.comboboxWide.addItems([str(data_wide)])

        # combobox long
        self.comboboxLong = QComboBox()
        Long = db.sqlLong()
        for data_long in Long:
            self.comboboxLong.addItems([str(data_long)])

        # combobox type
        self.typeText = QLabel("Type : ")
        self.comboboxType = QComboBox()
        Type = db.sqlType()
        for data_type in Type:
            self.comboboxType.addItems([str(data_type)])
        # calender
        self.dateText = QLabel("วันที่รับไม้เข้า : ")
        self.date = QDateEdit(self)
        self.date.setDate(QDate.currentDate())
        self.date.setDateTime(QtCore.QDateTime(QtCore.QDate()))
        self.date.setAcceptDrops(False)
        self.date.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.date.setAlignment(QtCore.Qt.AlignCenter)
        self.date.setDisplayFormat('yyyy-MM-dd')
        self.date.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.date.setCalendarPopup(True)

        # btn
        self.btn_insert_input = QPushButton("เพิ่มข้อมูล")
        self.btn_insert_input.clicked.connect(self.btn_insertClicked)
        self.btn_refresh = QPushButton("Refresh")
        self.btn_refresh.clicked.connect(self.funcRefresh)
        self.btn_refresh.setShortcut('F5')

        self.btn_excel = QPushButton(self)
        self.btn_excel.setIcon(QIcon('icons/excel (2).png'))
        # self.btn_excel.clicked.connect(self.exportExcel)

# Table
    def displayTable(self):
        self.inputTable = QTableWidget()
        self.inputTable.setColumnCount(10)
        header = ['วันที่รับไม้เข้า', 'โค้ดไม้', 'ประเภท', 'หนา' ,'กว้าง', 'ยาว', 'จำนวน', 'ปริมาตร (m^3)', 'ลูกค้า', 'Manage']
        self.inputTable.setHorizontalHeaderLabels(header)
        self.inputTable.doubleClicked.connect(self.func_handleButtonClicked)
        column_size = self.inputTable.horizontalHeader()
        for i in range(0, 10):
            column_size.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        # header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)

# Layouts
    def layouts(self):
        # QV & QH
        self.mainLayout = QVBoxLayout()
        self.mainTableLayout = QHBoxLayout()
        self.mainTopLayout = QHBoxLayout()

        self.searchLayout = QHBoxLayout()
        self.comboboxLayout = QHBoxLayout()
        self.rightTopLayout = QHBoxLayout()

        self.searchGroupBox = QGroupBox()
        self.comboboxGroup = QGroupBox()
        self.btnGrop = QWidget()

        # Search
        self.searchLayout.addWidget(self.searchText)
        self.searchLayout.addWidget(self.searchEntry)
        self.searchLayout.addWidget(self.searchButton)
        self.searchLayout.addWidget(self.dateText)
        self.searchLayout.addWidget(self.date)
        self.searchGroupBox.setLayout(self.searchLayout)

        # Combobox
        self.comboboxLayout.addWidget(self.sizeText)
        self.comboboxLayout.addWidget(self.thickText)
        self.comboboxLayout.addWidget(self.combboxThick)
        self.comboboxLayout.addWidget(self.wideText)
        self.comboboxLayout.addWidget(self.comboboxWide)
        self.comboboxLayout.addWidget(self.longText)
        self.comboboxLayout.addWidget(self.comboboxLong)
        self.comboboxLayout.addWidget(self.typeText)
        self.comboboxLayout.addWidget(self.comboboxType)
        self.comboboxGroup.setLayout(self.comboboxLayout)

        # Right Top aka Btn
        self.rightTopLayout.addWidget(self.btn_insert_input)
        self.rightTopLayout.addWidget(self.btn_refresh)
        self.rightTopLayout.addWidget(self.btn_excel)
        self.btnGrop.setLayout(self.rightTopLayout)

        # Layout Table
        self.mainTableLayout.addWidget(self.inputTable)

        # All Layout
        self.mainTopLayout.addWidget(self.searchGroupBox)
        self.mainTopLayout.addWidget(self.comboboxGroup)
        self.mainTopLayout.addWidget(self.btnGrop)
        self.mainLayout.addLayout(self.mainTopLayout)
        self.mainLayout.addLayout(self.mainTableLayout)

        # Main Layout
        self.wg.setLayout(self.mainLayout)

# Function Home
    def funcHome(self):
        self.newHome = main.Ui_MainWindow()
        self.hide()

# Function Cut
    def funcCut(self):
        self.newCut = cuttingWood.UI_Cutwood()
        self.hide()

# Function Withdraw
    def funcWithdraw(self):
        self.newWithdraw = withdrawWood.UI_Withdraw()
        self.hide()

# Function Resize
    def funcResize(self):
        self.newResize = resizeWood.UI_Resizewood()
        self.hide()

# Function Heat
    def funcHeat(self):
        self.newHeat = heatWood.UI_Heatwood()
        self.hide()

# Function Sale
    def funcSale(self):
        self.newHeat = saleWood.UI_Salewood()
        self.hide()

# FetchData
    def funcFetchData(self):
        for i in reversed(range(self.inputTable.rowCount())):
            self.inputTable.removeRow(i)
        query = db.fetch_dataInput()
        for row_data in query:
            row_number = self.inputTable.rowCount()
            self.inputTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.inputTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            self.btn_edit = QPushButton('Edit')
            self.btn_edit.setStyleSheet("""
                        QPushButton {
                            color:  black;
                            border-style: solid;
                            border-width: 3px;
                            border-color:  #008CBA;
                            border-radius: 12px
                        }
                        QPushButton:hover{
                            background-color: #008CBA;
                            color: white;
                        }
                    """)
            self.btn_edit.clicked.connect(self.func_handleButtonClicked)
            self.inputTable.setCellWidget(row_number, 9, self.btn_edit)
        self.inputTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

# Button Clicked
    def func_handleButtonClicked(self):
        global Input_id
        listInput = []
        for i in range(0, 9):
            listInput.append(self.inputTable.item(self.inputTable.currentRow(), i).text())
        Input_id = listInput[1]
        self.neweditInput = editsInputwood.UI_editsInputwood(listInput,Input_id)

    # Search
    def funcSearch(self):
        value = self.searchEntry.text()
        if value == "":
            QMessageBox.information(self, "Siam Kyohwa", "Search cant be empty!")
        else:
            self.searchEntry.text()
            results = db.searchInput(value)
            if results == []:
                QMessageBox.information(self, "Siam Kyohwa", "wood id information not found!")
            else:
                for i in reversed(range(self.inputTable.rowCount())):
                    self.inputTable.removeRow(i)
                for row_data in results:
                    row_number = self.inputTable.rowCount()
                    self.inputTable.insertRow(row_number)
                    for column_number , data in enumerate(row_data):
                        self.inputTable.setItem(row_number,column_number,QTableWidgetItem(str(data)))
                    self.btn_edit = QPushButton('ยืนยัน')
                    self.btn_edit.setStyleSheet("""
                                QPushButton {
                                    color:  black;
                                    border-style: solid;
                                    border-width: 3px;
                                    border-color:  #008CBA;
                                    border-radius: 12px
                                }
                                QPushButton:hover{
                                    background-color: #008CBA;
                                    color: white;
                                }
                            """)
                    self.btn_edit.clicked.connect(self.func_handleButtonClicked)
                    self.inputTable.setCellWidget(row_number, 9, self.btn_edit)
                self.inputTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def funcRefresh(self):
       self.funcFetchData()

    def btn_insertClicked(self):
        self.neweditInput = insert_woodIn()

    def exportExcel(self):
        pass

class insert_woodIn (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ข้อมูลไม้เข้า")
        self.setWindowIcon(QIcon('icons/forklift.png'))
        self.setGeometry(909, 250, 650, 550)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.display()
        self.layout()

    def display(self):

        # head
        self.title_txt = QLabel("เพิ่มข้อมูลรับไม้เข้า")
        self.title_txt.setFont(QFont('Arial', 12))
        self.title_txt.setAlignment(Qt.AlignCenter)
        # date
        self.dateinsertWoodIn_txt = QLabel("วันที่รับไม้เข้า: ")
        self.dateinsertWoodIn= QDateEdit(self)
        self.dateinsertWoodIn.setDate(QDate.currentDate())
        self.dateinsertWoodIn.setDateTime(QtCore.QDateTime(QtCore.QDate()))
        self.dateinsertWoodIn.setAcceptDrops(False)
        self.dateinsertWoodIn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dateinsertWoodIn.setAlignment(QtCore.Qt.AlignCenter)
        self.dateinsertWoodIn.setDisplayFormat('yyyy-MM-dd')
        self.dateinsertWoodIn.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateinsertWoodIn.setCalendarPopup(True)

        self.woodcodeEntry = QLineEdit(self)

        # Type
        self.woodtypeCombobox = QComboBox()
        Type = db.sqlType()
        for data_type in Type:
            self.woodtypeCombobox.addItems([str(data_type)])
        self.woodtypeCombobox.setEditable(True)

        # Thick
        self.thickCombobox = QComboBox()
        Thick = db.sqlThick()
        for data_thick in Thick:
            self.thickCombobox.addItems([str(data_thick)])
        self.thickCombobox.setEditable(True)
        self.thickCombobox.setValidator(QIntValidator())

        # Wide
        self.wideCombobox = QComboBox()
        Wide = db.sqlWide()
        for data_wide in Wide:
            self.wideCombobox.addItems([str(data_wide)])
        self.wideCombobox.setEditable(True)
        self.wideCombobox.setValidator(QIntValidator())

        # Longs
        self.longCombobox = QComboBox()
        Long = db.sqlLong()
        for data_long in Long:
            self.longCombobox.addItems([str(data_long)])
        self.longCombobox.setEditable(True)
        self.longCombobox.setValidator(QIntValidator())

        self.wood_pack_Entry = QLineEdit(self)
        self.wood_pack_Entry.setValidator(QIntValidator())
        self.wood_quantity_per_pack_Entry = QLineEdit(self)
        self.wood_quantity_per_pack_Entry.setValidator(QIntValidator())
        self.woodquantityEntry = QLineEdit(self)
        self.woodquantityEntry.setValidator(QIntValidator())
        self.volomeEntry = QLineEdit()
        self.volomeEntry.setValidator(QDoubleValidator(0.99,99.99,5))

        # Supplier
        self.supplierCombobox = QComboBox()
        supplier = db.sqlSupplier()
        for data_supplier  in supplier :
            self.supplierCombobox .addItems([str(data_supplier)])
        self.supplierCombobox .setEditable(True)

        # Btn
        self.btnOK = QPushButton('&OK',self)
        self.btnOK.setText("ยืนยัน") #text
        self.btnOK.setShortcut('Return') #shortcut key
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
              }
          """)
        self.btnOK.clicked.connect(self.funcbtnhandleInsert)

    def layout(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.midLayout = QHBoxLayout()
        self.bottomLayout = QFormLayout()
        self.btnbox = QHBoxLayout()
        self.text = QWidget()
        self.middleFrame = QGroupBox()
        self.bottomFrame = QFrame()
        self.topLayout.addWidget(self.title_txt)
        self.topLayout.addStretch()
        self.text.setLayout(self.topLayout)

        # Middle
        # self.middleFrame.setLayout(self.midLayout)

        # Bottom
        self.bottomLayout.addRow(QLabel("วันที่รับไม้เข้า: "), self.dateinsertWoodIn)
        self.bottomLayout.addRow(QLabel("โค้ดไม้: "), self.woodcodeEntry)
        self.bottomLayout.addRow(QLabel("ประเภท: "), self.woodtypeCombobox)
        self.bottomLayout.addRow(QLabel("หนา: "), self.thickCombobox)
        self.bottomLayout.addRow(QLabel("กว้าง: "), self.wideCombobox)
        self.bottomLayout.addRow(QLabel("ยาว: "), self.longCombobox)
        self.bottomLayout.addRow(QLabel("จำนวนแพค: "), self.wood_pack_Entry)
        self.bottomLayout.addRow(QLabel("แพคละ: "), self.wood_quantity_per_pack_Entry)
        self.bottomLayout.addRow(QLabel("จำนวน: "), self.woodquantityEntry)
        self.bottomLayout.addRow(QLabel("ปริมาตร: "), self.volomeEntry)
        self.bottomLayout.addRow(QLabel("Supplier: "), self.supplierCombobox )
        self.bottomFrame.setLayout(self.bottomLayout)

        # Btn
        self.btnbox.addStretch(1)
        self.btnbox.addWidget(self.btnOK)

        # All Layout
        self.mainLayout.addWidget(self.text)
        self.mainLayout.addWidget(self.bottomFrame)
        self.mainLayout.addLayout(self.btnbox)
        self.setLayout(self.mainLayout)

    def funcbtnhandleInsert(self):
        try:
            date = self.dateinsertWoodIn.text()
            wood_code = self.woodcodeEntry.text()
            value_type  = self.get_type()
            value_thick = self.get_thick()
            value_wide = self.get_wide()
            value_long = self.get_long()
            value_wood_pack = int(self.wood_pack_Entry.text())
            value_quantity_per_pack = int(self.wood_quantity_per_pack_Entry.text())
            value_quantity =int(self.woodquantityEntry.text())
            value_volume = float(self.volomeEntry.text())
            value_supplier = self.supplierCombobox.currentText()
            quantity = value_wood_pack * value_quantity_per_pack

            check_size = db.size()
            totem = False

            if (value_type == False or value_thick == False or value_wide == False or value_long == False):
                if(value_type == False):
                    QMessageBox.information(self, "Siam Kyohwa", "ไม่พบข้อมูล ประเภทไม้ ในฐานข้อมูล")
                elif (value_thick == False):
                    QMessageBox.information(self, "Siam Kyohwa", "ไม่พบข้อมูล ความหนาไม้ ในฐานข้อมูล")
                elif (value_wide == False):
                    QMessageBox.information(self, "Siam Kyohwa", "ไม่พบข้อมูล ความกว้างไม้ ในฐานข้อมูล")
                elif (value_long == False):
                    QMessageBox.information(self, "Siam Kyohwa", "ไม่พบข้อมูล ความยาวไม้ใ นฐานข้อมูล")

            elif (date and wood_code and value_type and value_thick and value_wide and value_long
                    and value_wood_pack and value_quantity_per_pack and value_volume and value_supplier != ""):
                for i in check_size:
                    if (value_thick == i[1] and value_wide == i[2] and value_long == i[3]):
                        db.func_insert_input(date,value_wood_pack,value_quantity_per_pack,value_quantity,value_supplier,wood_code,value_thick,value_wide,value_long,value_type,value_volume,quantity)
                        QMessageBox.information(self, "Siam Kyohwa", "เพิ่มข้อมูลสำเร็จ")
                        totem = True
                        self.close()
                        break

                if totem == False:
                    QMessageBox.information(self, "Siam Kyohwa", "ข้อมูลไซซ์ไม้ไม่ถูกต้อง กรุณาตรวจสอบใหม่อีกครั้งค่ะ")
            else:
                QMessageBox.information(self, "Siam Kyohwa", "มีข้อมูลว่าง")

        except ValueError:
            QMessageBox.information(self, "Siam Kyohwa", "มีข้อมูลว่าง")

    def get_type(self):
        sql_type = db.sqlType()
        mylist = len(sql_type) - 1
        value_type = self.woodtypeCombobox.currentText()
        totem = False
        i = 0
        while True:
            if (value_type  == sql_type[i]):
                try:
                    str(value_type)
                    return value_type
                except:
                    print(False)
            else:
                i += 1
                if i > mylist:
                    break
        if totem == False:
            return False
    def get_thick(self):
        sql_thick  = db.sqlThick()
        mylist = len(sql_thick) - 1
        value_thick = int(self.thickCombobox.currentText())
        totem = False
        i = 0
        while True:
            if (value_thick  == sql_thick[i]):
                return  value_thick
            else:
                i += 1
                if i > mylist:
                    break
        if totem == False:
            return False

    def get_wide(self):
        sql_wide  = db.sqlWide()
        mylist = len(sql_wide) - 1
        value_wide = int(self.wideCombobox.currentText())
        totem = False
        i = 0
        while True:
            if (value_wide  == sql_wide[i]):
                return  value_wide
            else:
                i += 1
                if i > mylist:
                    break
        if totem == False:
            return False

    def get_long(self):
        sql_long  = db.sqlLong()
        mylist = len(sql_long) - 1
        value_long = int(self.longCombobox.currentText())
        totem = False
        i = 0
        while True:
            if (value_long  == sql_long[i]):
                return  value_long
            else:
                i += 1
                if i > mylist:
                    break
        if totem == False:
            return False

def input():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = UI_Inputwood()
    sys.exit(app.exec_())
if __name__ == "__main__":
    input()