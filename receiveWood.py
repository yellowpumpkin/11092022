from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import heatWood
import inputWood
import resizeWood
import saleWood
import main
import cuttingWood
import withdrawWood
from mySQL import database
db = database()

class  UI_Receive (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("รายการรับไม้")
        self.setWindowIcon(QIcon('icons/wood01.png'))
        self.setGeometry(450, 50, 1280, 1024)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.toolBar()
        self.displayTable()
        self.display()
        self.func_FetchData()
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
        self.addInput.triggered.connect(self.funcAddInput)
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
        # รับไม้
        self.addReceive = QAction(QIcon('icons/wood01.png'), "รายการรับไม้", self)
        self.tb.addAction(self.addReceive)
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


    # Display
    def display(self):
        self.wg=QWidget()
        self.setCentralWidget(self.wg)
        self.searchText = QLabel("Wood Code : ")
        self.searchEntry = QLineEdit()
        self.searchEntry.setPlaceholderText("Ex. ARG291221")
        self.searchButton = QPushButton("Search")
        self.searchButton.clicked.connect(self.funcSearch)

        # calender
        self.dateText = QLabel("ดูรายการวันที่เบิก : ")
        self.date = QDateEdit(self)
        self.date.setDate(QDate.currentDate())
        self.date.setDateTime(QtCore.QDateTime(QtCore.QDate()))
        self.date.setAcceptDrops(False)
        self.date.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.date.setAlignment(QtCore.Qt.AlignCenter)
        self.date.setDisplayFormat('yyyy-MM-dd')
        self.date.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.date.setCalendarPopup(True)

        # combobox type
        self.withdrawtypeText = QLabel("ประเภทการเบิก : ")
        self.combobox_withdrawType = QComboBox()
        Type = db.sqlWithdrawType()
        for data_type in Type:
            self.combobox_withdrawType.addItems([str(data_type)])
        self.btn_ok = QPushButton("ok")
        # self.btn_ok .clicked.connect(self.func_Find)

        # Btn
        self.btn_refresh = QPushButton("Refresh")
        # self.btn_refresh.clicked.connect(self.funcRefresh)
        self.btn_refresh.setShortcut('F5')
        self.btn_excel = QPushButton(self)
        self.btn_excel.setIcon(QIcon('icons/excel (2).png'))

    # Table
    def displayTable(self):
        self.receiveTable = QTableWidget()
        self.receiveTable.setColumnCount(8)
        header = ['วันที่เบิกไม้' ,'โค้ดไม้', 'หนา', 'กว้าง', 'ยาว', 'ประเภทไม้' ,'จำนวน'  , 'Receive']
        self.receiveTable.setHorizontalHeaderLabels(header)
        column_size = self.receiveTable.horizontalHeader()
        for i in range(0, 7):
            column_size.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        self.receiveTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

    # Display
    def func_FetchData(self):
        for i in reversed(range(self.receiveTable.rowCount())):
            self.receiveTable.removeRow(i)
        query = db.fetch_dataReceive()

        for row_data in query:
            row_number = self.receiveTable.rowCount()
            self.receiveTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.receiveTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            btn_select = QPushButton('รับไม้')
            btn_select.setStyleSheet("""
                                           QPushButton {
                                               color:  black;
                                               border-style: solid;
                                               border-width: 3px;
                                               border-color:  #4CAF50;
                                               border-radius: 12px
                                           }
                                           QPushButton:hover{
                                               background-color: #4CAF50;
                                               color: white;
                                           }
                                       """)
            btn_select.clicked.connect(self.func_handleButtonClicked)
            self.receiveTable.setCellWidget(row_number, 7, btn_select)
        self.receiveTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

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
                for i in reversed(range(self.receiveTable.rowCount())):
                    self.receiveTable.removeRow(i)
                for row_data in results:
                    row_number = self.receiveTable.rowCount()
                    self.receiveTable.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        item = QTableWidgetItem()
                        item.setData(QtCore.Qt.EditRole, data)
                        self.receiveTable.setItem(row_number, column_number, item)
                self.receiveTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

    # Function Home
    def funcHome(self):
        self.newHome=main.Ui_MainWindow()
        self.close()

    # Function Cut
    def funcCut(self):
        self.newCut = cuttingWood.UI_Cutwood()
        self.close()

    # Function AddProduct
    def funcAddInput (self):
        self.newInput=inputWood.UI_Inputwood()
        self.close()

    # Function Resize
    def funcResize(self):
        self.newResize=resizeWood.UI_Resizewood()
        self.close()

    # Function Heat
    def funcHeat(self):
        self.newHeat=heatWood.UI_Heatwood()
        self.close()

    # Function Sale
    def funcSale(self):
        self.newSale=saleWood.UI_Salewood()
        self.close()
    # Function Withdraw
    def funcWithdraw(self):
        self.newWithdraw = withdrawWood.UI_Withdraw()
        self.close()

    def func_handleButtonClicked(self):
        for row in range(self.receiveTable.rowCount()):
            list_table_receive = []
            for col in range(0, 7):
                list_table_receive.append(self.receiveTable.item(row, col).text())
            db.func_insert_receive_into_stock(list_table_receive[6],list_table_receive[2],
                                              list_table_receive[3],list_table_receive[4],
                                              list_table_receive[1])

        QMessageBox.information(self, "Siam Kyohwa", "รับไม้สำเร็จ")
        self.receiveTable.removeRow(self.receiveTable.currentRow())




   # Layout
    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.mainTableLayout = QHBoxLayout()
        self.mainTable2Layout = QHBoxLayout()
        self.mainTopLayout = QHBoxLayout()

        self.textLayout = QHBoxLayout()
        self.searchLayout = QHBoxLayout()
        self.dateLayout = QHBoxLayout()
        self.btn_withdraw_Layout = QHBoxLayout()
        self.btn_Layout = QHBoxLayout()

        self.btnGropBox = QGroupBox()
        self.textGropBox = QGroupBox()
        self.searchGroupBox = QGroupBox()
        self.dateGroupBox=QGroupBox()
        self.tableWidget = QWidget()

        # Search
        self.searchLayout.addWidget(self.searchText)
        self.searchLayout.addWidget(self.searchEntry)
        self.searchLayout.addWidget(self.searchButton)
        self.searchLayout.addWidget(self.withdrawtypeText)
        self.searchLayout.addWidget(self.combobox_withdrawType)
        self.searchLayout.addWidget(self.btn_ok)
        self.searchLayout.addWidget(self.dateText)
        self.searchLayout.addWidget(self.date)
        self.searchGroupBox.setLayout(self.searchLayout)

        # Btn GroupBox
        self.btn_Layout.addWidget(self.btn_refresh)
        self.btn_Layout.addWidget(self.btn_excel)
        self.btnGropBox.setLayout(self.btn_Layout)

        # Table
        self.mainTableLayout.addWidget(self.receiveTable)

        # All Layout
        self.mainTopLayout.addWidget(self.searchGroupBox)
        self.mainTopLayout.addWidget( self.btnGropBox)
        self.mainLayout.addLayout(self.mainTopLayout)
        self.mainLayout.addLayout(self.mainTableLayout)

        #  Main Layout
        self.wg.setLayout(self.mainLayout)

#Main
def recevie():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window=UI_Receive()
    sys.exit(app.exec_())


if __name__ == "__main__":
   recevie()
