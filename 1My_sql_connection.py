#database bağlanma
import mysql.connector

try:
    mydb = mysql.connector.connect(

        host="127.0.0.1",
        user="root",
        password="12345"

    )
except Exception as e:
    print("Database başarısız bağlanma",e)

finally:
    print("DataBase Bağlanma Block tamamlandı..")


#database class oluştur.
#database bağlanma init kısmında sabit olsun bu hatta program başında en başta bir defa bağlanması daha iyi olur.
#database tabloya sürekli olarak verileri tarih-tespit-edilen ürün-oranı-toplam sayısı toplamda 4 adet parametre alacak ve save edecek.
