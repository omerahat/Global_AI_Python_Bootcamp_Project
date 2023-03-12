from PyQt5.QtWidgets import  QStyleFactory,QApplication, QMainWindow, QWidget, QVBoxLayout,QGridLayout,QLabel,QLineEdit,QComboBox,QHBoxLayout, QFrame, QButtonGroup, QRadioButton
from PyQt5.QtCore import QObject, QTimer,QSize
from PyQt5 import QtWidgets,QtCore
from PyQt5.uic import loadUi
import sys
from main import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import csv
from datetime import datetime



class MainPizza(QMainWindow):
    
    def __init__(self): 
        super(MainPizza, self).__init__()
        loadUi("..\\about_pizza.ui", self)

        self.setGeometry(600,100,1000,800)

        oImage = QImage("..\\Just.jpg")
        sImage = oImage.scaled(QSize(1041,681))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(oImage))                        
        self.setPalette(palette)

        self.Pay_Button = QPushButton('Pay', self)
        self.Pay_Button.move(80,580)
        self.Pay_Button.resize(151,51)
#souce
        self.cost = 0
        self.OliveButton.clicked.connect(self.Olive)
        self.MushroomButton.clicked.connect(self.Mushroom)
        self.OnionButton.clicked.connect(self.Onion)
        self.CheeseButton.clicked.connect(self.Cheese)
        self.CornButton.clicked.connect(self.Corn)
        self.MeatButton.clicked.connect(self.Meat)
        self.Pay_Button.clicked.connect(self.Pay)



        self.pizza_widget = MainPizza
        self.payment_widget = Payment()

        
    def Olive(self):
       self.olivetotal = 0
       if self.ClassicButton.isChecked():
           self.cost =  Decorator.get_cost(Olive) + Pizza.get_cost(Classic)
           self.description =  Pizza.get_description(Classic) + " with " + Decorator.get_description(Olive)
       if self.MargheritaButton.isChecked():
            self.cost =  Decorator.get_cost(Olive) + Pizza.get_cost(Margherita)
            self.description =  Pizza.get_description(Margherita) + " with " + Decorator.get_description(Olive)
       if self.TurkishButton.isChecked():
            self.cost =  Decorator.get_cost(Olive) + Pizza.get_cost(Turkish_Pizza)
            self.description =  Pizza.get_description(Turkish_Pizza) + " with " + Decorator.get_description(Olive)
       if self.DominosButton.isChecked():
            self.cost =  Decorator.get_cost(Olive) + Pizza.get_cost(Dominos_Pizza)
            self.description =  Pizza.get_description(Dominos_Pizza) + " with " + Decorator.get_description(Olive)
       self.Pay_Button.setText("PAY "+ str(self.cost) + " ₺")
      

    def Mushroom(self):
        self.mushroomtotal = 0 
        if self.ClassicButton.isChecked():
           self.cost =  Decorator.get_cost(Mushroom) + Pizza.get_cost(Classic)
           self.description =  Pizza.get_description(Classic) + " with "+  Decorator.get_description(Mushroom) 
        if self.MargheritaButton.isChecked():
            self.cost =  Decorator.get_cost(Mushroom) + Pizza.get_cost(Margherita)
            self.description =  Pizza.get_description(Margherita) + " with " + Decorator.get_description(Mushroom)
        if self.TurkishButton.isChecked():
            self.cost =  Decorator.get_cost(Mushroom) + Pizza.get_cost(Turkish_Pizza)
            self.description =  Pizza.get_description(Turkish_Pizza) + " with " + Decorator.get_description(Mushroom)
        if self.DominosButton.isChecked():
            self.cost =  Decorator.get_cost(Mushroom) + Pizza.get_cost(Dominos_Pizza)
            self.description =  Pizza.get_description(Dominos_Pizza) + " with " + Decorator.get_description(Mushroom)
        self.Pay_Button.setText("PAY "+ str(self.cost) + " ₺")
        self.mushroomtotal = self.cost
        return self.mushroomtotal

    def Onion(self):

       if self.ClassicButton.isChecked():
           self.cost =  Decorator.get_cost(Onion) + Pizza.get_cost(Classic)
           self.description =  Pizza.get_description(Classic) + " with " + Decorator.get_description(Onion) 
       if self.MargheritaButton.isChecked():
            self.cost =  Decorator.get_cost(Onion) + Pizza.get_cost(Margherita)
            self.description =  Pizza.get_description(Margherita) + " with " + Decorator.get_description(Onion) 
       if self.TurkishButton.isChecked():
            self.cost =  Decorator.get_cost(Onion) + Pizza.get_cost(Turkish_Pizza)
            self.description =  Pizza.get_description(Turkish_Pizza) + " with " + Decorator.get_description(Onion) 
       if self.DominosButton.isChecked():
            self.cost =  Decorator.get_cost(Onion) + Pizza.get_cost(Dominos_Pizza)
            self.description =  Pizza.get_description(Dominos_Pizza) + " with " + Decorator.get_description(Onion) 
       self.Pay_Button.setText("PAY "+str(self.cost) + " ₺")


    def Cheese(self):
   
       if self.ClassicButton.isChecked():
           self.cost =  Decorator.get_cost(GoatCheese) + Pizza.get_cost(Classic)
           self.description =  Pizza.get_description(Classic) + " with " + Decorator.get_description(GoatCheese)
       if self.MargheritaButton.isChecked():
           self.cost =  Decorator.get_cost(GoatCheese) + Pizza.get_cost(Margherita)
           self.description =   Pizza.get_description(Margherita) + " with " + Decorator.get_description(GoatCheese)
       if self.TurkishButton.isChecked():
            self.cost =  Decorator.get_cost(GoatCheese) + Pizza.get_cost(Turkish_Pizza)
            self.description =  Pizza.get_description(Turkish_Pizza) + " with " + Decorator.get_description(GoatCheese)
       if self.DominosButton.isChecked():
            self.cost =  Decorator.get_cost(GoatCheese) + Pizza.get_cost(Dominos_Pizza)
            self.description =  Pizza.get_description(Dominos_Pizza) +  " with " + Decorator.get_description(GoatCheese)
       self.Pay_Button.setText("PAY "+ str(self.cost) + " ₺")

    def Meat(self):

       if self.ClassicButton.isChecked():
           self.cost =  Decorator.get_cost(Meat) + Pizza.get_cost(Classic)
           self.description =  Pizza.get_description(Classic) + " with " + Decorator.get_description(Meat)
       if self.MargheritaButton.isChecked():
            self.cost = Decorator.get_cost(Meat) + Pizza.get_cost(Margherita)
            self.description = Pizza.get_description(Margherita) + " with " +  Decorator.get_description(Meat)
       if self.TurkishButton.isChecked():
            self.cost =  Decorator.get_cost(Meat) + Pizza.get_cost(Turkish_Pizza)
            self.description =  Pizza.get_description(Turkish_Pizza) + " with " + Decorator.get_description(Meat)
       if self.DominosButton.isChecked():
            self.cost =  Decorator.get_cost(Meat) + Pizza.get_cost(Dominos_Pizza)
            self.description =  Pizza.get_description(Dominos_Pizza) + " with " + Decorator.get_description(Meat)
       self.Pay_Button.setText("PAY "+str(self.cost) + " ₺")


    def Corn(self):
       if self.ClassicButton.isChecked():
           self.cost =  Decorator.get_cost(Corn) + Pizza.get_cost(Classic)
           self.description = Pizza.get_description(Classic) + " with " + Decorator.get_description(Corn)
       if self.MargheritaButton.isChecked():
            self.cost =  Decorator.get_cost(Corn) + Pizza.get_cost(Margherita)
            self.description = Pizza.get_description(Margherita) + " with " + Decorator.get_description(Corn)
       if self.TurkishButton.isChecked():
            self.cost =  Decorator.get_cost(Corn) + Pizza.get_cost(Turkish_Pizza)
            self.description =  Pizza.get_description(Turkish_Pizza) + " with " + Decorator.get_description(Corn) 
       if self.DominosButton.isChecked():
            self.cost =  Decorator.get_cost(Corn) + Pizza.get_cost(Dominos_Pizza)
            self.description =  Pizza.get_description(Dominos_Pizza) + " with " + Decorator.get_description(Corn)
       self.Pay_Button.setText("PAY "+ str(self.cost) + " ₺")

    
    def Pay(self):
        # self.pizza_widget.setVisible(0)
        self.payment_widget.setVisible(1)
        win2 = Payment()
        win2.show
        win2.showcost(str(self.cost),self.description)


class Payment(QWidget):  
     def __init__(self): 
        super().__init__()
        loadUi("..\\pay_pizza.ui", self)

        self.setGeometry(600,100,1000,800)

        self.payment_widget = Payment
        self.pizza_widget = MainPizza

        oImage = QImage("C:\\Users\\Admin\\Desktop\\global_ai_python_project\\about.png")                  
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(oImage))                        
        self.setPalette(palette)


        self.textbox = QLineEdit(self)
        self.textbox.move(30, 200)
        self.textbox.resize(451,30)

        self.name = QLineEdit(self)
        self.name.move(180, 300)
        self.name.resize(280,30)

        self.note = QLineEdit(self)
        self.note.move(45, 360)
        self.note.resize(130,90)

        self.id = QLineEdit(self)
        self.id.move(180, 365)
        self.id.resize(280,30)

        self.button = QPushButton('Pay', self)
        self.button.move(230,420)
        self.button.clicked.connect(self.on_click)

        self.show

     def on_click(self):

            textboxValue = self.textbox.text()
            textboxName = self.name.text()
            textboxNote = self.note.text()
            textboxid = self.id.text()
            order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("Orders_Database.csv", mode="a") as file:

                excel = csv.writer(file)
                excel.writerow([textboxName, textboxid , textboxValue, textboxNote,
                     order_time])

            QMessageBox.question(self, 'Confirmed',textboxName +"," + " Your order confirmed!  " , QMessageBox.Ok, QMessageBox.Ok)
            self.textbox.setText("")

     def showcost(self,cost,description):
         QWidget().__init__()
         self.price= str(cost)
         self.description = description
         with open("Orders_Database.csv", mode="a") as file:
                excel = csv.writer(file)
                excel.writerow([self.price, self.description])

def main():
    app = QApplication(sys.argv)
    win = MainPizza()
    win.show()
    app.exec_()

if __name__ == '__main__':
    sys.exit(main()) 
