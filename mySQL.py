import mysql.connector

class database():

    def generate_conn_singleton(self):
        try:
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Root1516",
                database="warehouse"
            )
            # cur = con.cursor()
            return con

        except mysql.connector.Error as error:
            print("Failed to insert record into Laptop table {}".format(error))

    def size(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute('SELECT * From WoodSize')
        data = cur.fetchall()
        return data

    def sqlThick(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute('SELECT Thick From WoodSize')
        data = cur.fetchall()
        data_thick = []
        thick_set = set(data)
        for i in thick_set:
            data_thick.append(i[0])
        data_thick.sort()
        conn.close()
        return data_thick

    def sqlWide(self):
        # pass
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute('SELECT Wide From WoodSize')
        data = cur.fetchall()
        data_wide = []
        wide_set = set(data)
        for i in wide_set:
            data_wide.append(i[0])
        data_wide.sort()
        conn.close()
        return data_wide

    def sqlLong(self):
        # pass
        conn = self.generate_conn_singleton()
        cur = conn.cursor()

        cur.execute('SELECT Longs From WoodSize')
        data = cur.fetchall()
        data_long = []
        long_set = set(data)
        for i in long_set:
            data_long.append(i[0])
        data_long.sort()
        conn.close()
        return data_long

    def sqlType(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute("SELECT WoodType_name From WoodType")

        data = cur.fetchall()
        data_type= []
        type_set = set(data)
        for i in type_set:
            data_type.append(i[0])
        data_type.sort()

        conn.close()
        return   data_type

    def sqlWithdrawType(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute("SELECT WithdrawType_name , WithdrawType_nameEn From Withdrawtype")
        data = cur.fetchall()
        withdraw_type_set = set(data)
        data_withdraw_typeTH = []
        # data_withdraw_typeEN = []
        for i in withdraw_type_set:
            data_withdraw_typeTH.append(i[0])
            # data_withdraw_typeEN.append(i[1])
        data_withdraw_typeTH.sort()

        conn.close()
        return   data_withdraw_typeTH

    def sqlSupplier(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute("SELECT Supplier From Inputs")
        data = cur.fetchall()
        supplier_set = set(data)
        data_supplier = []
        for i in supplier_set:
            data_supplier.append(i[0])
            # data_withdraw_typeEN.append(i[1])
        data_supplier.sort()
        conn.close()
        return  data_supplier


    def fetch_dataHome(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute('SELECT wood.wood_code , WoodType.WoodType_name , WoodSize.Thick , '
                    'WoodSize.Wide , WoodSize.Longs , quantity , Wood.Volume , Wood.main_head , Wood.Activity '
                    'FROM stock '
                    'INNER JOIN Wood ON stock.wood_id = Wood.Wood_id '
                    'INNER JOIN WoodType ON Wood.WoodType = WoodType.WoodType_id  '
                    'INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.WoodSize_id')
        data = cur.fetchall()
        conn.close()
        return  data

    def fetch_dataInput(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute("SELECT Inputs.Date , Wood_code , WoodType.WoodType_name , WoodSize.Thick ,WoodSize.Wide , "
                    "WoodSize.Longs , Inputs.Quantity , Volume , Inputs.Supplier "
                    "FROM Wood "
                    "INNER JOIN WoodType ON Wood.WoodType = WoodType.WoodType_id "
                    "INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.WoodSize_id "
                    "INNER JOIN Inputs ON Wood.Inputs = Inputs.Input_id "
                    "Where Wood.Activity='Available' "
                   )
        data = cur.fetchall()
        conn.close()
        return  data

    def fetch_dataCut(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute(
            "SELECT wood.wood_code , WoodSize.Thick , WoodSize.Wide , WoodSize.Longs  ,"
            "Wood.Volume  , WoodType.WoodType_name , Quantity "
            "FROM stock "
            "INNER JOIN Wood ON stock.wood_id = Wood.Wood_id "
            "INNER JOIN WoodType ON Wood.WoodType = WoodType.WoodType_id "
            "INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.WoodSize_id "
            "Where Wood.Activity='Available'"
            )
        #
        data = cur.fetchall()
        conn.close()
        return data

    def fetch_dataResize(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute(
            "SELECT wood.wood_code , WoodSize.Thick ,WoodSize.Wide , WoodSize.Longs  ,"
            "Wood.Volume , WoodType.WoodType_name , Quantity "
            "FROM stock "
            "INNER JOIN Wood ON stock.wood_id = Wood.Wood_id  "
            "INNER JOIN WoodType ON Wood.WoodType = WoodType.WoodType_id "
            "INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.WoodSize_id "
            "Where Wood.Activity='Available'"
            )
        data = cur.fetchall()
        conn.close()
        return data

    def fetch_dataHeat(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute(
            "SELECT wood.wood_code , WoodSize.Thick ,WoodSize.Wide , WoodSize.Longs  ,"
            "Wood.Volume , WoodType.WoodType_name , Quantity "
            "FROM stock "
            "INNER JOIN Wood ON stock.wood_id = Wood.Wood_id  "
            "INNER JOIN WoodType ON Wood.WoodType = WoodType.WoodType_id "
            "INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.WoodSize_id "
            "Where Wood.Activity='Available'"
            )
        data = cur.fetchall()
        conn.close()
        return data

    def fetch_dataSale(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute(
            "SELECT wood.wood_code , WoodSize.Thick ,WoodSize.Wide , WoodSize.Longs  ,"
            "Wood.Volume , WoodType.WoodType_name , Quantity "
            "FROM stock "
            "INNER JOIN Wood ON stock.wood_id = Wood.Wood_id  "
            "INNER JOIN WoodType ON Wood.WoodType = WoodType.WoodType_id "
            "INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.WoodSize_id "
            "Where Wood.Activity='Available'"
            )

        data = cur.fetchall()
        conn.close()
        return  data

    def fetch_dataReceive(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute(
            "SELECT Receive.date_withdraw , wood.wood_code , WoodSize.Thick ,WoodSize.Wide , WoodSize.Longs , WoodType.WoodType_name"
            ", Quantity "
            "FROM Receive "
            "INNER JOIN Wood ON Receive.receive_wood = Wood.Wood_id  "
            "INNER JOIN WoodType ON Wood.WoodType = WoodType.WoodType_id "
            "INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.WoodSize_id "
            "Where Wood.Activity='Available'"
            )

        data = cur.fetchall()
        conn.close()
        print(data)
        return data

    def fetch_dataWithdraw(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute("SELECT withdraw_id , date , wood.wood_code , WoodSize.Thick ,"
                    "WoodSize.Wide , WoodSize.Longs , quantity , withdrawtype.WithdrawType_name  "
                    "FROM withdraw "
                    "INNER JOIN Wood ON withdraw.woodid = Wood.Wood_id "
                    "INNER JOIN withdrawtype ON withdraw.withdrawtype = withdrawtype.WithdrawType_id "
                    "INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.WoodSize_id "
                    "INNER JOIN WoodType ON Wood.WoodType = WoodType.WoodType_id " )

        data = cur.fetchall()
        conn.close()
        return data

    def searchHome(self, value):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        sql = "SELECT wood.wood_id , wood.wood_code , WoodType.WoodType_name , WoodSize.Thick , " \
        "WoodSize.Wide , WoodSize.Longs , quantity , Wood.Volume , Wood.Activity FROM stock " \
        "INNER JOIN Wood ON stock.wood_id = Wood.Wood_id " \
        "INNER JOIN WoodType ON Wood.WoodType = WoodType.WoodType_id  " \
        "INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.WoodSize_id " \
        "where Wood_code Like '%" + value + "%'"

        cur.execute(sql)
        data = cur.fetchall()
        return  data

    def searchInput(self, value):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        sql = "SELECT Inputs.Date , Wood_code , WoodType.WoodType_name , WoodSize.Thick ,WoodSize.Wide , WoodSize.Longs , Inputs.Quantity , Volume , Inputs.Supplier " \
              "FROM Wood " \
              "INNER JOIN WoodType ON Wood.WoodType = WoodType.WoodType_id " \
              "INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.WoodSize_id " \
              "INNER JOIN Inputs ON Wood.Inputs = Inputs.Input_id "\
              "where Wood_code Like '%"+value+"%'"
        cur.execute(sql)
        data = cur.fetchall()
        return  data

    def searchCutting(self, value):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        sql = "SELECT wood.Wood_code , WoodType.WoodType_name , WoodSize.Thick ,WoodSize.Wide , WoodSize.Longs , WoodType.WoodType_name , Quantity  " \
              "FROM stock " \
              "INNER JOIN Wood ON stock.wood_id = Wood.Wood_id "\
              "INNER JOIN WoodType ON Wood.WoodType = WoodType.WoodType_id " \
              "INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.WoodSize_id " \
              "where Wood_code Like '%"+value+"%'"
        cur.execute(sql)
        data = cur.fetchall()
        return  data

    # Update
    def update_dataInput(self,check,date,code,g_type,g_thick,g_wide,g_long,quantity,volume,supplier):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()

        # sql = 'UPDATE Inputs SET Quantity=%s Where Input_id=(SELECT wood_id FROM wood WHERE Wood_code =%s)'
        # value = (quantity,code)
        # cur.execute(sql, value)
        #
        sql2 = 'UPDATE Wood SET Wood_code=%s , ' \
              'WoodType=(select WoodType.WoodType_id  FROM WoodType Where WoodType.WoodType_name=%s) ,' \
              'WoodSize=(Select WoodSize.Woodsize_id FROM WoodSize Where WoodSize.Thick=%s AND WoodSize.Wide=%s AND WoodSize.Longs=%s) ,' \
              'Inputs=(select Inputs.Input_id FROM Inputs WHERE Inputs.Supplier=%s AND Inputs.Date=%s AND Inputs.Quantity=%s) ,' \
              'Volume=%s' \
              'Where Wood_code=%s'

        value2 = (code,g_type,g_thick,g_wide,g_long,supplier,date,quantity,volume,check)
        cur.execute(sql2,value2)

        sql3 = "UPDATE stock SET Quantity =%s " \
              "Where wood_id = (SELECT wood_id FROM wood WHERE Wood_code =%s ) "
        value3 = (quantity,code)
        cur.execute(sql3, value3)

        conn.commit()

    def funcListAvailable(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute("SELECT wood.wood_id , wood.wood_code , WoodType.WoodType_name , WoodSize.Thick ,"
                    "WoodSize.Wide , WoodSize.Longs , quantity , Wood.Volume , Wood.Activity FROM stock "
                    "INNER JOIN Wood ON stock.wood_id = Wood.Wood_id "
                    "INNER JOIN WoodType ON Wood.WoodType = WoodType.WoodType_id  "
                    "INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.WoodSize_id "
                    "Where Wood.Activity='Available'")
        data = cur.fetchall()
        conn.close()
        return data

    def funcListUnavailable(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute("SELECT wood.wood_id , wood.wood_code , WoodType.WoodType_name , WoodSize.Thick ,"
                    "WoodSize.Wide , WoodSize.Longs , quantity , Wood.Volume , Wood.Activity FROM stock "
                    "INNER JOIN Wood ON stock.wood_id = Wood.Wood_id "
                    "INNER JOIN WoodType ON Wood.WoodType = WoodType.WoodType_id  "
                    "INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.WoodSize_id "
                    "Where Wood.Activity='Unavailable'")
        data = cur.fetchall()
        conn.close()
        return data

    def func_check_quantity_wood(self,wood_code):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()

        sql = "SELECT Quantity  " \
              "FROM stock " \
              "INNER JOIN Wood ON stock.wood_id = Wood.Wood_id " \
              "where Wood_code Like '%" + wood_code + "%'"
        cur.execute(sql)
        data = cur.fetchone()
        return data

    def func_update_quantity(self,wood_code,quantity):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        sql = "UPDATE stock SET Quantity = Quantity-%s " \
              "Where wood_id = (SELECT wood_id FROM wood WHERE Wood_code =%s ) "
        value = (quantity,wood_code)
        cur.execute(sql,value)
        conn.commit()

    def func_insert_withdrawcut_tosql(self,date,quantity,typewithdraw,woodcode):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        sql = """INSERT INTO withdraw (date,quantity,withdrawtype,woodid) VALUES (%s,%s,%s,(SELECT wood_id FROM wood WHERE wood_id = (SELECT wood_id FROM wood WHERE Wood_code=%s ))) """
        value = (date,quantity,typewithdraw,woodcode)
        cur.execute(sql,value)
        conn.commit()

    def func_insert_input(self,date,value_wood_pack,value_quantity_per_pack,value_quantity,value_supplier,wood_code,value_thick,value_wide,value_long,value_type,value_volume,quantitys):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        sql = """INSERT INTO Inputs (Date,Pack,Quan_per_Pack,Quantity,Supplier) VALUES (%s,%s,%s,%s,%s) """
        value = (date,value_wood_pack,value_quantity_per_pack,value_quantity,value_supplier)
        cur.execute(sql, value)

        sql2 = """INSERT INTO Wood (Wood_code,Woodsize,Woodtype,Inputs,Volume) VALUES (%s,(Select WoodSize.Woodsize_id FROM WoodSize Where WoodSize.Thick=%s AND WoodSize.Wide=%s AND WoodSize.Longs=%s),
        (SELECT WoodType.WoodType_id  FROM WoodType Where WoodType.WoodType_name=%s),(select Input_id FROM Inputs WHERE Date=%s AND Pack=%s AND Quan_per_Pack=%s AND Supplier=%s  ),%s) """
        value2 = (wood_code,value_thick,value_wide,value_long,value_type,date,value_wood_pack,value_quantity_per_pack,value_supplier,value_volume)
        cur.execute(sql2, value2)

        sql3 = """ INSERT INTO stock (quantity, wood_id) VALUES (%s,(SELECT wood_id FROM wood WHERE Wood_code=%s )) """
        value3 =(value_quantity, wood_code)
        cur.execute(sql3, value3)
        conn.commit()

    def func_insert_receive_into_stock(self,value_quantity,value_thick,value_wide,value_long,wood_code):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()


        sql3 = """  INSERT INTO stock (quantity, wood_id)  VALUES (%s,(SELECT wood_id FROM wood
                    WHERE WoodSize=(Select WoodSize.Woodsize_id FROM WoodSize Where WoodSize.Thick=%s AND WoodSize.Wide=%s AND WoodSize.Longs=%s)
                     AND Wood_code=%s)) """
        value3 =(value_quantity,value_thick,value_wide,value_long,wood_code)
        cur.execute(sql3,value3)

        conn.commit()

    def func_insert_resize_into_db(self, wood_code, value_thick, value_wide, value_long, value_type, value_quantity,
                                     value_volume,value_date):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()

        sql2 = """ INSERT INTO Wood (Wood_code,Woodsize,Woodtype,Volume) VALUES (%s,(Select WoodSize.Woodsize_id FROM WoodSize Where WoodSize.Thick=%s AND WoodSize.Wide=%s AND WoodSize.Longs=%s),
        (SELECT WoodType.WoodType_id  FROM WoodType Where WoodType.WoodType_name=%s),%s) """
        value2 = (wood_code,value_thick,value_wide,value_long,value_type,value_volume)
        cur.execute(sql2, value2)

        sql = """ INSERT INTO receive (date_withdraw,receive_wood,quantity) VALUES (%s,(SELECT wood_id FROM wood
                    WHERE WoodSize=(Select WoodSize.Woodsize_id FROM WoodSize Where WoodSize.Thick=%s AND WoodSize.Wide=%s AND WoodSize.Longs=%s)
                     AND Wood_code=%s),%s) """
        value = (value_date,value_thick,value_wide,value_long,wood_code,value_quantity)
        cur.execute(sql, value)

        conn.commit()


# mycursor.execute("CREATE TABLE WoodType(woodtype_name varchar(50) ,Woodtype_id	int PRIMARY KEY)")
# mycursor.execute("CREATE TABLE User(user_id	int PRIMARY KEY,password varchar(16) , activity int )")
# mycursor.execute("CREATE TABLE Customer(customer_id	int PRIMARY KEY, customer_name varchar(50) )")
# mycursor.execute("CREATE TABLE WithdrawType(WithdrawType_id	int PRIMARY KEY,WithdrawType_name varchar(50) )")
# mycursor.execute("CREATE TABLE WoodQuality(WoodQuality_id	int PRIMARY KEY,WoodQuality_name varchar(50) )"