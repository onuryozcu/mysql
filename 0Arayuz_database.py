#database class oluştur.
#database bağlanma init kısmında sabit olsun bu hatta program başında en başta bir defa bağlanması daha iyi olur.
#database tabloya sürekli olarak verileri tarih-tespit-edilen ürün-oranı-toplam sayısı toplamda 4 adet parametre alacak ve save edecek.
import mysql.connector

#database dışarıdan bağlanma ayarlarda bulunan yetkilerden % işareti ile yapılmaktadır.
#bunu bi thread çevirip yapmak gerek,

from PyQt5.QtCore import QThread, pyqtSignal

class database(QThread):

    signal_database = pyqtSignal(np.ndarray)

    def __init__(self,datestring,detect_object,detect_rate,detect_count):

        self.datestring = datestring
        self.detect_object = detect_object
        self.detect_rate = detect_rate
        self.detect_count = detect_count

        #bu geçici olarak burada, program açılırken alacağız ki sürekli olarak burada bağlanmaya çalışmasın
        #sistemi yormanın mantığı yok :)

        try:
            self.mydb = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="12345",
                database = "Detection"
            )

        except Exception as e:
            print("Database başarısız bağlanma", e)

        finally:
            print("DataBase Bağlanma Block tamamlandı..")

        self.update_database()
        self.show_database()


    def update_database(self):

        try:
            mycursor = self.mydb.cursor()
            sorgu = "INSERT INTO detect_information_table (detect_object_class, detect_date,detect_rate,detect_total_count) VALUES (%s, %s,%s,%s)"

            val = [(f'{self.detect_object}', f'{self.datestring}',f'{self.detect_rate }',f'{self.detect_count}')]

            mycursor.executemany(sorgu, val)
            self.mydb.commit()


        except mysql.connector.Error as e:
            raise e

        finally:
            print("database guncel veriler eklendi..")



    def show_database(self):

        try:

            mycursor = self.mydb.cursor()
            sorgu = "SELECT * FROM detect_information_table"

            mycursor.execute(sorgu)

            #fetchall (1,'bardak','10.10.2002','%98','4 Adet tespit edildi')
            myresult = mycursor.fetchall()

            for row in myresult:
                print(row)

            #tabloda ki değeri fetchone ile çekiyoruz dememin nedeniz burada tek tek değerlere ulabiliriz.
            #
            # myresult2 = mycursor.fetchone()
            # for row2 in myresult2:
            #     print(x)

        except mysql.connector.Error as e:
            raise e

        finally:
            if mycursor:
                mycursor.close()
                print("The database connection is closed")


if __name__ == '__main__':
    data = database(str('15.10.2022 SAAT 15:23'),str('bardak'),98,48)


    # self.datestring = datestring
    # self.detect_object = detect_object
    # self.detect_rate = detect_rate
    # self.detect_count = detect_count


