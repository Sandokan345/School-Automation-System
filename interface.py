# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets      #Arayüz için gerekli kütüphane
import sqlite3                      #Veri tabanı için gerekli kütüphane

con = sqlite3.connect("data.db")        #Veri tabanına bağlantı sağlanır
cursor = con.cursor()                   #Veri tabanında işlem yapılabilmesi için bir imleç oluşturulur


class Ui_Form(object):
    def veri_ekle_ogrenci(self):
        # Öğrenci bölümünde listeye ve veri tabanına eleman ekler
        no = self.lineEdit.text()
        self.lineEdit.clear()
        ad = self.lineEdit_2.text()
        self.lineEdit_2.clear()
        soyad = self.lineEdit_3.text()
        self.lineEdit_3.clear()
        cursor.execute("INSERT INTO Ogrenciler VALUES(?,?,?)", (no, ad, soyad))
        self.listWidget.addItem("{} {} {}".format(no, ad, soyad))
        con.commit()

    def veri_ekle_ders(self):
        # Ders bölümünde listeye ve veri tabanına elemean ekler.
        ders_kodu = self.lineEdit_5.text()
        self.lineEdit_5.clear()
        ders_adi = self.lineEdit_4.text()
        self.lineEdit_4.clear()
        cursor.execute("INSERT INTO Dersler VALUES(?,?)", (ders_kodu, ders_adi))
        self.listWidget_2.addItem("{} {}".format(ders_kodu, ders_adi))
        con.commit()

    def veri_ekle_not(self):
        # Seçilen öğrenci ve derse sınav notu ekler.
        ogr_no = self.item_ogrenci_no
        ders_kodu = self.item_ders_kodu
        vize_not = self.lineEdit_6.text()
        self.lineEdit_6.clear()
        final_not = self.lineEdit_7.text()
        self.lineEdit_7.clear()
        cursor.execute("INSERT INTO Notlar VALUES(?,?,?,?)", (ogr_no, ders_kodu, vize_not, final_not))
        self.listWidget_3.addItem("{} {} {} {}".format(ogr_no, ders_kodu, vize_not, final_not))
        con.commit()

    def ogrenci_liste(self):
        #Başlangıçta veri tabanında bulunan öğrenci bölümünü alıp lişteye ekler
        cursor.execute("Select * From Ogrenciler")
        result = cursor.fetchall()
        for i in result:
            self.listWidget.addItem("{} {} {}".format(i[0], i[1], i[2]))

    def dersler_liste(self):
        # Başlangıçta veri tabanında bulunan dersler bölümünü alıp lişteye ekler
        cursor.execute("Select * From Dersler")
        result = cursor.fetchall()
        for i in result:
            self.listWidget_2.addItem("{} {}".format(i[0], i[1]))

    def notlar_liste(self):
        # Başlangıçta veri tabanında bulunan notlar bölümünü alıp lişteye ekler
        cursor.execute("Select * From Notlar")
        result = cursor.fetchall()
        for i in result:
            self.listWidget_3.addItem("{} {} {} {}".format(i[0], i[1], i[2], i[3]))

    def item_ogr(self):
        #Öğrenciler bölümündeki listede seçilen öğenin öğrenci numarsını bir objeye kaydeder.
        self.item_ogrenci_no = ""
        temp = self.listWidget.currentItem()
        liste = temp.text().split()
        self.item_ogrenci_no = liste[0]

    def item_drs(self):
        #Dersler bölümündeki listede seçilen öğenin ders kodunu bir objeye kaydeder.
        self.item_ders_kodu = ""
        temp = self.listWidget_2.currentItem()
        liste = temp.text().split()
        self.item_ders_kodu = liste[0]

    def ogrenci_liste_sil(self):
        #Öğrenciler bölümünde seçilen öğenin listeden ve veri tabanından silinmesini sağlar.
        cursor.execute("DELETE FROM Ogrenciler WHERE OgrNo = ?", (self.item_ogrenci_no,))
        row = self.listWidget.currentRow()
        self.listWidget.takeItem(row)
        con.commit()

    def ders_liste_sil(self):
        #Dersler bölümünde seçilen öğenin listeden ve veri tabanından silinmesini sağlar.
        cursor.execute("DELETE FROM Dersler WHERE DersKodu = ?", (self.item_ders_kodu,))
        row = self.listWidget_2.currentRow()
        self.listWidget_2.takeItem(row)
        con.commit()

    def not_liste_sil(self):
        #Notlar bölümünde seçilen öğenin listeden ve veri tabanından silinmesini sağlar.
        temp = self.listWidget_3.currentItem()
        liste = temp.text().split()
        item_ogrenci_no = liste[0]
        cursor.execute("DELETE FROM Notlar WHERE OgrNo = ?", (item_ogrenci_no,))
        row = self.listWidget_3.currentRow()
        self.listWidget_3.takeItem(row)
        con.commit()

    def setupUi(self, Form):
        #Arayüzün ana kısmını oluşturan fonksiyondur.
        Form.setObjectName("Form")
        Form.resize(735, 479)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_5.addWidget(self.lineEdit_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_4.clicked.connect(self.veri_ekle_ogrenci)
        self.listWidget = QtWidgets.QListWidget(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.ogrenci_liste()
        self.listWidget.clicked.connect(self.item_ogr)
        self.pushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.ogrenci_liste_sil)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_6.addWidget(self.lineEdit_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_7.addWidget(self.lineEdit_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.veri_ekle_ders)
        self.listWidget_2 = QtWidgets.QListWidget(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_3.addWidget(self.listWidget_2)
        self.dersler_liste()
        self.listWidget_2.clicked.connect(self.item_drs)
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_5.clicked.connect(self.ders_liste_sil)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_10 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_8.addWidget(self.lineEdit_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_9.addWidget(self.lineEdit_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_4.addWidget(self.pushButton_6)
        self.pushButton_6.clicked.connect(self.veri_ekle_not)
        self.listWidget_3 = QtWidgets.QListWidget(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listWidget_3.setFont(font)
        self.listWidget_3.setObjectName("listWidget_3")
        self.verticalLayout_4.addWidget(self.listWidget_3)
        self.notlar_liste()
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_4.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(self.not_liste_sil)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Öğrenci Otomasyon Sistemi"))
        self.label.setText(_translate("Form", "ÖĞRENCİLER"))
        self.label_4.setText(_translate("Form", "ÖğrNo:"))
        self.label_3.setText(_translate("Form", "Adı:"))
        self.label_2.setText(_translate("Form", "Soyadı"))
        self.pushButton_4.setText(_translate("Form", "Ekle"))
        self.pushButton.setText(_translate("Form", "Seçili olanları sil"))
        self.label_7.setText(_translate("Form", "DERSLER"))
        self.label_5.setText(_translate("Form", "Ders Kodu:"))
        self.label_6.setText(_translate("Form", "Ders Adı:"))
        self.pushButton_2.setText(_translate("Form", "Ekle"))
        self.pushButton_5.setText(_translate("Form", "Seçili olanları sil"))
        self.label_10.setText(_translate("Form", "NOTLAR"))
        self.label_8.setText(_translate("Form", "Vize Notu:"))
        self.label_9.setText(_translate("Form", "Final Notu:"))
        self.pushButton_6.setText(_translate("Form", "Ekle"))
        self.pushButton_3.setText(_translate("Form", "Seçili olanları sil"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

