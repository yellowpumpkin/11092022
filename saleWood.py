from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import inputWood
import resizeWood
import withdrawWood
import heatWood
import main
import cuttingWood
from mySQL import database
db = database()

class  UI_Salewood (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("รายการขาย")
        self.setWindowIcon(QIcon('icons/sale01.png'))
        self.setGeometry(450, 50, 1280, 1024)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.toolBar()
        self.displayTable()
        self.funcFetchDataSale()
        self.display()
        self.layouts()

# ToolBar
    def toolBar(self):
        self.tb = self.addToolBar("Tool Bar")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.addHome = QAction(QIcon('icons/warehouse01.png'), "หน้าหลัก", self)
        self.tb.addAction(self.addHome)
        self.addHome.triggered.connect(self.funcHome)
        self.tb.addSeparator()
        # รับไม้เข้า
        self.addInput = QAction(QIcon('icons/forklift.png'), "รายการับไม้เข้า", self)
        self.tb.addAction(self.addInput)
        self.addInput.triggered.connect(self.funcInput)
        self.tb.addSeparator()
        # Cutting
        self.addCut=QAction(QIcon('icons/cutting.png'),"รายการตัด/ผ่า",self)
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
        self.tb.addSeparator()
        # เบิกไม้
        self.addWithdraw = QAction(QIcon('icons/wood02.png'), "รายการเบิกไม้", self)
        self.tb.addAction(self.addWithdraw)
        self.addWithdraw.triggered.connect(self.funcWithdraw)
        self.tb.addSeparator()

# Display
    def display(self):
        self.wg = QWidget(self)
        self.setCentralWidget(self.wg)

        self.searchText = QLabel("Wood Code : ")
        self.searchEntry = QLineEdit()
        self.searchEntry.setPlaceholderText("Ex. 6328218")
        self.searchButton = QPushButton("Search")

        self.btn_withdraw = QPushButton("เบิกไม้ประจำวัน")
        self.btn_withdraw.setShortcut('Return')
        self.btn_refresh = QPushButton("Refresh")
        self.btn_refresh.setShortcut('F5')

        withdraw_type = db.sqlWithdrawType()
        self.type_cut = withdraw_type[0]
        self.text_type_withdraw = QLabel("ประเภทการเบิก : " + str(self.type_cut)+" (Sale)")

        date = QDateTime.currentDateTime()
        self.dateDisplay = date.toString('yyyy-MM-dd')
        self.dateText = QLabel("วันทีเบิกไม้ : " + self.dateDisplay)

    def displayTable(self):
        self.saleTable = QTableWidget()
        self.saleTable.setColumnCount(8)
        header = ['โค้ดไม้', 'หนา', 'กว้าง', 'ยาว', 'ปริมาตร', 'ประเภท', 'จำนวน', 'manage']
        self.saleTable.setHorizontalHeaderLabels(header)
        column_size = self.saleTable.horizontalHeader()
        for i in range(0, 7):
            column_size.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

    def funcFetchDataSale(self):
        for i in reversed(range(self.saleTable.rowCount())):
            self.saleTable.removeRow(i)
        query = db.fetch_dataSale()
        for row_data in query:
            row_number = self.saleTable.rowCount()
            self.saleTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem()
                item.setData(QtCore.Qt.EditRole, data)
                self.saleTable.setItem(row_number, column_number, item)
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
            self.saleTable.setCellWidget(row_number, 7, btn_select)
        self.saleTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.mainTable1Layout = QHBoxLayout()
        self.mainTable2Layout = QHBoxLayout()
        self.mainTopLayout = QHBoxLayout()
        self.textLayout = QHBoxLayout()
        self.searchLayout = QHBoxLayout()
        self.btn_withdraw_Layout = QHBoxLayout()
        self.btn_refresh_Layout = QHBoxLayout()

        self.btnGropBox = QGroupBox()
        self.btnGropBox2 = QGroupBox()
        self.textGropBox = QGroupBox()
        self.searchGropBox = QGroupBox()

        # Search
        self.searchLayout.addWidget(self.searchText)
        self.searchLayout.addWidget(self.searchEntry)
        self.searchLayout.addWidget(self.searchButton)
        self.searchGropBox.setLayout(self.searchLayout)
        # Text Type Date
        self.textLayout.addStretch()
        self.textLayout.addWidget(self.text_type_withdraw)
        self.textLayout.addWidget(self.dateText)
        self.textLayout.addStretch()
        self.textGropBox.setLayout(self.textLayout)
        # Btn GroupBox
        self.btn_withdraw_Layout.addWidget(self.btn_withdraw)
        self.btnGropBox.setLayout(self.btn_withdraw_Layout)
        self.btn_refresh_Layout.addWidget(self.btn_refresh)
        self.btnGropBox2.setLayout(self.btn_refresh_Layout)
        # Table
        self.mainTable1Layout.addWidget(self.saleTable)

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

# Function Home
    def funcHome(self):
        self.newHome=main.Ui_MainWindow()
        self.close()

# Function AddProduct
    def funcInput (self):
        self.newInput=inputWood.UI_Inputwood()
        self.close()

# Function Cut
    def funcCut(self):
        self.newCut = cuttingWood.UI_Cutwood()
        self.close()

# Function Withdraw
    def funcWithdraw(self):
        self.newWithdraw=withdrawWood.UI_Withdraw()
        self.close()

# Function Heat
    def funcHeat(self):
        self.newHeat=heatWood.UI_Heatwood()
        self.close()

# Function Sale
    def funcResize(self):
        self.newResize=resizeWood.UI_Resizewood()
        self.close()

# Main
# def main():
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     window=UI_Salewood()
#     sys.exit(app.exec_())
#
#
# if __name__ == "__main__":
#    main()