from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import resizeWood

from mySQL import database
db = database()

class resize_wood (QWidget):
    def __init__(self,listwood,date,type_resize,quantity):
        super().__init__()
        self.setWindowTitle("ใบเบิกไม้")
        self.setWindowIcon(QIcon('icons/cutting.png'))
        self.setGeometry(450,150,960,600)
        self.setFixedSize(self.size())
        self.list_wood_resize = listwood
        self.wood_code = listwood[0][0]
        self.wood_thick = listwood[0][1]
        self.wood_wide = listwood[0][2]
        self.wood_long = listwood[0][3]
        self.wood_volume = listwood[0][4]
        self.wood_type = listwood[0][5]

        self.wood_quantity = quantity
        self.str_date = date
        self.type_cut = type_resize
        self.UI()
        self.show()

    def UI(self):
        self.display()
        self.displayTable()
        self.funcShowdata()
        self.layout()

    def display(self):
        self.text_date = QLabel(self)
        self.text_date.setText("วันที่เบิกไม้: " + str(self.str_date))
        self.text_type = QLabel(self)
        self.text_type.setText("ประเภทการเบิกไม้ : "+self.type_cut+" (Resize)")

        icon = QPixmap('icons/s.png')
        self.text_company = QLabel("<font color='Black' size='5'>Siam Kyohwa Seisakusho Co., Ltd.</font> ", self)
        self.label = QLabel(self)
        self.label.setPixmap(icon)
        self.label.setAlignment(Qt.AlignCenter)
        self.text_company.setMinimumHeight(icon.height())

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
        self.btn_confirm.clicked.connect(self.func_handleButtonClicked)

        # RESIZE1
        self.thickText1 = QLabel("หนา")
        self.wideText1 = QLabel("x กว้าง")
        self.longText1 = QLabel("x ยาว")
        self.equal1 = QLabel(" =  ")

        # Thick
        self.thickCombobox1 = QComboBox()
        self.thickCombobox1.addItem("0")
        Thick = db.sqlThick()
        for data_thick in Thick:
            if data_thick <= int(self.wood_thick) :
                self.thickCombobox1.addItems([str(data_thick)])
        self.thickCombobox1.setValidator(QIntValidator())

        # Wide
        self.wideCombobox1 = QComboBox()
        self.wideCombobox1.addItem("0")
        Wide = db.sqlWide()
        for data_wide in Wide:
            if data_wide <= int(self.wood_wide):
                self.wideCombobox1.addItems([str(data_wide)])
        self.wideCombobox1.setValidator(QIntValidator())
        # Longs
        self.longCombobox1 = QComboBox()
        self.longCombobox1.addItem(self.wood_long)
        self.woodquantityEntry1 = QLineEdit(self)
        self.woodquantityEntry1.setValidator(QIntValidator())
        self.woodquantityEntry1.setText("0")

        # RESIZE2
        self.thickText2 = QLabel("หนา")
        self.wideText2 = QLabel("x กว้าง")
        self.longText2 = QLabel("x ยาว")
        self.equal2 = QLabel(" =  ")

        # Thick
        self.thickCombobox2 = QComboBox()
        self.thickCombobox2.addItem("0")
        for data_thick in Thick:
            if data_thick <= int(self.wood_thick):
                self.thickCombobox2.addItems([str(data_thick)])
        self.thickCombobox2.setValidator(QIntValidator())

        # Wide
        self.wideCombobox2 = QComboBox()
        self.wideCombobox2.addItem("0")
        for data_wide in Wide:
            if data_wide <= int(self.wood_wide):
                self.wideCombobox2.addItems([str(data_wide)])
        self.wideCombobox2.setValidator(QIntValidator())

        # Longs
        self.longCombobox2 = QComboBox()
        self.longCombobox2.addItem(self.wood_long)
        self.woodquantityEntry2 = QLineEdit(self)
        self.woodquantityEntry2.setValidator(QIntValidator())
        self.woodquantityEntry2.setText("0")

        # RESIZE3
        self.thickText3 = QLabel("หนา")
        self.wideText3 = QLabel("x กว้าง")
        self.longText3 = QLabel("x ยาว")
        self.equal3 = QLabel(" =  ")

        # Thick
        self.thickCombobox3 = QComboBox()
        self.thickCombobox3.addItem("0")
        for data_thick in Thick:
            if data_thick <= int(self.wood_thick):
                self.thickCombobox3.addItems([str(data_thick)])
        self.thickCombobox3.setValidator(QIntValidator())

        # Wide
        self.wideCombobox3 = QComboBox()
        self.wideCombobox3.addItem("0")
        for data_wide in Wide:
            if data_wide <= int(self.wood_wide):
                self.wideCombobox3.addItems([str(data_wide)])
        self.wideCombobox3.setValidator(QIntValidator())

        # Longs
        self.longCombobox3 = QComboBox()
        self.longCombobox3.addItem(self.wood_long)
        self.woodquantityEntry3 = QLineEdit(self)
        self.woodquantityEntry3.setValidator(QIntValidator())
        self.woodquantityEntry3.setText("0")

    def displayTable(self):
        self.table_resize = QTableWidget()
        self.table_resize .setColumnCount(8)
        header = ['โค้ดไม้', 'หนา', 'กว้าง', 'ยาว', 'ปริมาตร', 'ประเภท', 'จำนวน','จำนวนเบิก']
        self.table_resize .setHorizontalHeaderLabels(header)
        self.table_resize .horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        column_size = self.table_resize .horizontalHeader()
        for i in range(0, 7):
            column_size.setSectionResizeMode(i,QHeaderView.Stretch)

    def funcShowdata(self):
        query = self.list_wood_resize
        for row_data in query:
            row_number = self.table_resize .rowCount()
            self.table_resize .insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem()
                item.setData(QtCore.Qt.EditRole, data)
                self.table_resize.setItem(row_number, column_number, item)
                self.table_resize.setItem(row_number, 7, QTableWidgetItem(str(self.wood_quantity)))

    def layout(self):
        self.mainLayout = QVBoxLayout()
        self.headLayout = QHBoxLayout()
        self.mainTopLayout = QVBoxLayout()
        self.CenterLayout1 = QVBoxLayout()
        self.CenterLayout2 = QVBoxLayout()
        self.tableLayout = QHBoxLayout()

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

        self.tableLayout.addWidget(self.table_resize)

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
        self.mainTopLayout.addLayout(self.tableLayout)
        self.mainTopLayout.addWidget(self.resize1)
        self.mainTopLayout.addWidget(self.resize2)
        self.mainTopLayout.addWidget(self.resize3)

        # self.mainLayout.addLayout(self.headLayout)
        self.mainLayout.addLayout(self.mainTopLayout)
        self.mainLayout.addLayout(self.btn_box)

        self.setLayout(self.mainLayout)

    def func_handleButtonClicked(self):
        quantityEntry1 = int(self.woodquantityEntry1.text())
        quantityEntry2 = int(self.woodquantityEntry2.text())
        quantityEntry3 = int(self.woodquantityEntry3.text())

        thick = self.get_thick()
        wide = self.get_wide()
        long = self.get_long()
        check_size = db.size()  # check size

        sum_quantity = quantityEntry1+quantityEntry2+quantityEntry3
        sum2 = quantityEntry1+quantityEntry2
        totem = False
        totem2 = False
        totem3 = False
        self.func_insert_to_sql()




        if sum_quantity > self.wood_quantity or sum_quantity < self.wood_quantity:
            QMessageBox.critical(self, "Siam Kyohwa", "จำนวนการเบิกไม่ถูกต้อง!")

        elif  thick == False or wide == False or thick[0] == 0 or wide[0] == 0 :
            QMessageBox.critical(self, "Siam Kyohwa", "จำนวน ไซซ์ ไม่ถูกต้อง!")

        elif (thick[0] and wide[0] != 0) and (quantityEntry1 == self.wood_quantity) :
            for i in check_size:
                if (thick[0] == i[1] and wide[0] == i[2] and long[0] == i[3]):
                    db.func_update_quantity(self.wood_code, self.wood_quantity)
                    db.func_insert_resize_into_db(self.wood_code, thick[0], wide[0], long[0], self.wood_type,
                                                     quantityEntry1, self.wood_volume, self.str_date)
                    msg = QMessageBox()
                    msg.setWindowTitle("Siam Kyohwa")
                    msg.setText("เบิกสำเร็จ!")
                    msg.setWindowIcon(QIcon('icons/cutting.png'))
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()
                    self.close()
                    totem = True
                    break

            if totem == False:
                QMessageBox.critical(self, "Siam Kyohwa", "ข้อมูล ไซซ์ ไม่ถูกต้อง")

        # elif (thick[1] and wide[1] != 0 ) and (sum2 == self.wood_quantity) :
        #     check = False
        #     for i in check_size:
        #         if (thick[0] == i[1] and wide[0] == i[2] and long[0] == i[3]) :
        #             totem = True
        #             check = True
        #             break
        #     if totem == False:
        #         QMessageBox.critical(self, "Siam Kyohwa", "ข้อมูล ไซซ์ ไม่ถูกต้อง")
        #     if check == True :
        #         for i in check_size:
        #             if (thick[1] == i[1] and wide[1] == i[2] and long[1] == i[3]):
        #
        #                 print("Thick1 : " + str(thick[0]) + " Thick2 : " + str(thick[1]))
        #                 msg = QMessageBox()
        #                 msg.setWindowTitle("Siam Kyohwa")
        #                 msg.setText("เบิกสำเร็จ!")
        #                 msg.setWindowIcon(QIcon('icons/cutting.png'))
        #                 msg.setIcon(QMessageBox.Information)
        #                 msg.setStandardButtons(QMessageBox.Ok)
        #                 # msg.buttonClicked.connect(self.func_insert_to_sql)
        #                 msg.exec_()
        #                 self.close()
        #                 totem2 = True
        #                 break
        #         if totem2 == False:
        #             QMessageBox.critical(self, "Siam Kyohwa", "ข้อมูล ไซซ์ ไม่ถูกต้อง")
        # elif (thick[2] and wide[2] != 0 ) and (sum_quantity == self.wood_quantity) :
        #     check2 = False
        #     check3 = False
        #     for i in check_size:
        #         if (thick[0] == i[1] and wide[0] == i[2] and long[0] == i[3]):
        #             totem = True
        #             check2 = True
        #             break
        #     if totem == False:
        #         QMessageBox.critical(self, "Siam Kyohwa", "ข้อมูล ไซซ์ ไม่ถูกต้อง")
        #     if check2 == True:
        #         for i in check_size:
        #             if (thick[1] == i[1] and wide[1] == i[2] and long[1] == i[3]):
        #                 totem2 = True
        #                 check3 = True
        #                 break
        #         if totem2 == False:
        #             QMessageBox.critical(self, "Siam Kyohwa", "ข้อมูล ไซซ์ ไม่ถูกต้อง")
        #     if check3 == True :
        #         for i in check_size:
        #             if (thick[2] == i[1] and wide[2] == i[2] and long[2] == i[3]):
        #                 print("Thick1 : " + str(thick[0]) + " Thick2 : " + str(thick[1])+ " Thick3 : " + str(thick[2]))
        #                 msg = QMessageBox()
        #                 msg.setWindowTitle("Siam Kyohwa")
        #                 msg.setText("เบิกสำเร็จ!")
        #                 msg.setWindowIcon(QIcon('icons/cutting.png'))
        #                 msg.setIcon(QMessageBox.Information)
        #                 msg.setStandardButtons(QMessageBox.Ok)
        #                 # msg.buttonClicked.connect(self.func_insert_to_sql)
        #                 msg.exec_()
        #                 self.close()
        #                 totem3 = True
        #                 break
        #         if totem3 == False:
        #             QMessageBox.critical(self, "Siam Kyohwa", "ข้อมูล ไซซ์ ไม่ถูกต้อง")

    def func_insert_to_sql(self):
        date_withdraw = self.str_date
        type_withdraw = 4
        wood_code = self.wood_code
        quantity = self.wood_quantity
        db.func_insert_withdrawcut_tosql(date_withdraw,quantity,type_withdraw,wood_code)

    def get_thick(self):
        sql_thick = db.sqlThick()
        mylist = len(sql_thick) - 1
        thick1 = int(self.thickCombobox1.currentText())
        thick2 = int(self.thickCombobox2.currentText())
        thick3 = int(self.thickCombobox3.currentText())
        totem = False
        i = 0
        while True:
            if(thick1 == sql_thick[i] or thick2 == sql_thick[i] or thick3 == sql_thick[i]):
                return thick1,thick2,thick3
            else:
                i += 1
                if i > mylist:
                    break
        if totem == False:
            return False

    def get_wide(self):
        sql_wide = db.sqlWide()
        mylist = len(sql_wide) - 1
        wide1 = int(self.wideCombobox1.currentText())
        wide2 = int(self.wideCombobox2.currentText())
        wide3 = int(self.wideCombobox3.currentText())

        totem = False
        i = 0
        while True:
            if (wide1 == sql_wide[i] or wide2 == sql_wide[i] or wide3 == sql_wide[i]):
                return wide1,wide2,wide3
            else:
                i += 1
                if i > mylist:
                    break
        if totem == False:
            return False

    def get_long(self):
        sql_long = db.sqlLong()
        mylist = len(sql_long) - 1
        long1 = int(self.longCombobox1.currentText())
        long2 = int(self.longCombobox2.currentText())
        long3 = int(self.longCombobox3.currentText())
        totem = False
        i = 0
        while True:
            if (long1 == sql_long[i] or long2 == sql_long[i] or long3 == sql_long[i]):
                return long1,long2,long3
            else:
                i += 1
                if i > mylist:
                    break
        if totem == False:
            return False

