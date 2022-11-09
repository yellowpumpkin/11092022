from PyQt5 import  QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from mySQL import database
db = database()

class UI_editsInputwood(QWidget):
    def __init__(self, inputdata , input_id):
        super().__init__()
        self.setWindowTitle("แก้ไขข้อมูล")
        self.setWindowIcon(QIcon('icons/edit.png'))
        self.setGeometry(909, 250, 650, 550)

        str_date = inputdata[0]
        self.dt = tuple([int(x) for x in str_date[:10].split('-')])
        self.input_Wood_date = self.dt
        # self.input_Wood_id = inputdata[1]
        self.input_Wood_code = inputdata[1]
        self.input_Wood_type = inputdata[2]
        self.input_Wood_thick = inputdata[3]
        self.input_Wood_wide = inputdata[4]
        self.input_Wood_long = inputdata[5]
        self.input_Wood_quantity = inputdata[6]
        self.input_Wood_volume = inputdata[7]
        self.input_Wood_supplier = inputdata[8]
        self.check = input_id

        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.display()
        self.layout()

# Display
    def display(self):

        # TOP
        self.imgEditInputWood = QLabel()
        self.img = QPixmap('icons/forklift02.png')
        self.imgEditInputWood.setPixmap(self.img)
        self.imgEditInputWood.setAlignment(Qt.AlignCenter)
        self.title_txt = QLabel("แก้ไขข้อมูลรับไม้เข้า")
        self.title_txt.setFont(QFont('Arial', 12))
        self.title_txt.setAlignment(Qt.AlignCenter)

        # Info
        self.dateEditInputWood_txt = QLabel("วันที่รับไม้เข้า: ")
        self.dateEditInputWood = QDateEdit(self)
        self.dateEditInputWood.setDateTime(QtCore.QDateTime(QtCore.QDate(self.input_Wood_date[0], self.input_Wood_date[1], self.input_Wood_date[2])))
        self.dateEditInputWood.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dateEditInputWood.setDisplayFormat('yyyy-MM-dd')
        self.dateEditInputWood.setMinimumDate(QtCore.QDate(2019, 1, 1))
        self.dateEditInputWood.setCalendarPopup(True)
        self.dateEditInputWood.setReadOnly(True) # แก้ไข ไม่ได้
        self.woodcodeEntry = QLineEdit(self)
        self.woodcodeEntry.setText(self.input_Wood_code)

        # Type
        self.woodtypeCombobox = QComboBox() # combobox
        self.woodtypeCombobox.addItems([str(self.input_Wood_type)]) # add item
        Type = db.sqlType() # input database
        for data_type in Type:
            self.woodtypeCombobox.addItems([str(data_type)]) # add  item from db
        self.woodtypeCombobox.setEditable(True)  # แก้ไข  combobox ได้

        # Thick
        self.thickCombobox = QComboBox() # combobox
        self.thickCombobox.addItems([str(self.input_Wood_thick)]) # add item
        Thick = db.sqlThick() # input database
        for data_thick in Thick:
            self.thickCombobox.addItems([str(data_thick)]) # add  item from db
        self.thickCombobox.setEditable(True) # แก้ไข  combobox ได้
        self.thickCombobox.setValidator(QIntValidator()) # รับข้อมูล int
        # Wide
        self.wideCombobox = QComboBox() # combobox
        self.wideCombobox.addItem(self.input_Wood_wide) # add item
        Wide = db.sqlWide() # input database
        for data_wide in Wide:
            self.wideCombobox.addItems([str(data_wide)]) # add  item from db
        self.wideCombobox.setEditable(True) # แก้ไข  combobox ได้
        self.wideCombobox.setValidator(QIntValidator())  # รับข้อมูล int
        # Longs
        self.longCombobox = QComboBox()  # combobox
        self.longCombobox.addItem(self.input_Wood_long) # add item
        Long = db.sqlLong() # input database
        for data_long in Long:
            self.longCombobox.addItems([str(data_long)]) # add  item from db
        self.longCombobox.setEditable(True) # แก้ไข  combobox ได้
        self.longCombobox.setValidator(QIntValidator())  # รับข้อมูล int

        self.woodquantityEntry = QLineEdit(self) # จำนวน
        self.woodquantityEntry.setText(self.input_Wood_quantity)
        self.woodquantityEntry.setValidator(QIntValidator())  # รับข้อมูล int
        self.woodquantityEntry.setReadOnly(True) # แก้ไข ไม่ได้

        self.volomeEntry = QLineEdit()
        self.volomeEntry.setText(self.input_Wood_volume)
        self.volomeEntry.setValidator(QDoubleValidator(0.99,99.99,5))

        self.supplierEntry = QLineEdit()
        self.supplierEntry.setText(self.input_Wood_supplier)
        self.supplierEntry.setReadOnly(True)

        # Btn
        self.btnOK = QPushButton('&OK',self)
        self.btnOK.setText("แก้ไขข้อมูล") # text
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
              }
          """)

        self.btnOK.clicked.connect(self.funcbtnhandleUpdateInfo)

        self.btnCancel = QPushButton(self)
        self.btnCancel.setText("ลบ") #text
        self.btnCancel.setIcon(QIcon("icons\close.png")) #icon
        self.btnCancel.setShortcut('Ctrl+Q') #shortcut key
        self.btnCancel.setToolTip("Close the widget")
        self.btnCancel.move(100,100)
        self.btnCancel.setStyleSheet("""
              QPushButton {
                  background-color: red;
                  color: white;
                  font-size: 14px;
                  text-align: center;
                  padding: 10px 24px;
                  border-radius: 4px
               }
              QPushButton:hover {
                  background-color: white; 
                  border: 0.5px solid red;
                  color: black;
              }
          """)

        self.btnCancel.clicked.connect(self.close)

# Layout
    def layout(self):
        self.mainLayout = QVBoxLayout() # layout หลัก
        self.topLayout = QHBoxLayout() # text
        self.midLayout = QHBoxLayout() # pic
        self.bottomLayout = QFormLayout() # line edit
        self.btnbox = QHBoxLayout() # button

        self.text = QWidget()
        self.middleFrame = QGroupBox()
        self.bottomFrame = QFrame()

        # Top
        self.topLayout.addWidget(self.title_txt)
        self.text.setLayout(self.topLayout)

        # Middle
        self.midLayout.addWidget(self.imgEditInputWood)
        self.middleFrame.setLayout(self.midLayout)

        # Bottom
        self.bottomLayout.addRow(QLabel("วันที่รับไม้เข้า: "), self.dateEditInputWood)
        self.bottomLayout.addRow(QLabel("โค้ดไม้: "), self.woodcodeEntry)
        self.bottomLayout.addRow(QLabel("ประเภท: "), self.woodtypeCombobox)
        self.bottomLayout.addRow(QLabel("หนา: "), self.thickCombobox)
        self.bottomLayout.addRow(QLabel("กว้าง: "), self.wideCombobox)
        self.bottomLayout.addRow(QLabel("ยาว: "), self.longCombobox)
        self.bottomLayout.addRow(QLabel("จำนวน: "), self.woodquantityEntry)
        self.bottomLayout.addRow(QLabel("ปริมาตร: "), self.volomeEntry)
        self.bottomLayout.addRow(QLabel("Supplier: "), self.supplierEntry)
        self.bottomFrame.setLayout(self.bottomLayout)

        # Btn
        self.btnbox.addStretch(1)
        self.btnbox.addWidget(self.btnOK)
        self.btnbox.addWidget(self.btnCancel)

        # All Layout
        self.mainLayout.addWidget(self.text)
        # self.mainLayout.addWidget(self.middleFrame)
        self.mainLayout.addWidget(self.bottomFrame)
        self.mainLayout.addLayout(self.btnbox)
        self.setLayout(self.mainLayout)

    # Update
    def funcbtnhandleUpdateInfo(self):
        try:
            check = self.check
            date = self.dateEditInputWood.text()
            code = self.woodcodeEntry.text()
            g_type = self.get_type() # get type
            g_thick = self.get_thick() # get thick
            g_wide = self.get_wide() # get wide
            g_long = self.get_long() # get long
            quantity = int(self.woodquantityEntry.text())
            volume = float(self.volomeEntry.text())
            supplier = self.supplierEntry.text()

            check_size = db.size() # check size
            totem = False

            if (g_type == False or g_thick == False or g_wide == False  or g_long == False  ): # เช็ค ข้อมูล ไซซ์ ใน db
                if (g_type == False):
                    QMessageBox.information(self, "Siam Kyohwa", "ไม่พบข้อมูล ประเภท ในฐานข้อมูล")
                elif (g_thick == False):
                    QMessageBox.information(self, "Siam Kyohwa", "ไม่พบข้อมูล ความหนา ในฐานข้อมูล")
                elif (g_wide == False):
                    QMessageBox.information(self, "Siam Kyohwa", "ไม่พบข้อมูล ความกว้าง ในฐานข้อมูล")
                elif (g_long == False):
                    QMessageBox.information(self, "Siam Kyohwa", "ไม่พบข้อมูล ความยาว ในฐานข้อมูล")

            elif (date and code and g_type and g_thick and g_wide and g_long  and quantity and volume and supplier !=""):
                for i in check_size:
                    if (g_thick == i[1] and g_wide == i[2] and g_long == i[3]):
                        db.update_dataInput(check,date,code,g_type,g_thick,g_wide,g_long,quantity,volume,supplier) # update database
                        msg = QMessageBox()
                        msg.setWindowTitle("แก้ไขข้อมูล")
                        msg.setWindowIcon(QIcon('icons/edit.png'))
                        msg.setText("ยืนยันการแก้ไขข้อมูล")
                        msg.setIcon(QMessageBox.Information)
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.buttonClicked.connect(self.close)
                        msg.exec_()
                        totem = True
                        break
                if totem == False:
                    QMessageBox.information(self, "Siam Kyohwa", "ข้อมูล ไซซ์ ไม่ถูกต้อง กรุณาตรวจสอบใหม่อีกครั้งค่ะ")
            else:
                QMessageBox.information(self, "Siam Kyohwa", "มีข้อมูลว่าง")

        except ValueError:
            QMessageBox.information(self, "Siam Kyohwa", "มีข้อมูลว่าง")


    # delete
    def funcbtnhandleDeleteInfo(self):
        pass


# get_value
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