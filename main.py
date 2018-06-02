import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
from PyQt5.QtCore import *

class Button():

    def __init__(self,text, results):
        self.b = QPushButton(str(text))
        self.text = text
        self.results = results
        self.b.clicked.connect(lambda : self.compute(self.text))

    def compute(self, v):

        if self.results.text() == "" and type(v) == str:
            self.results.setText("")

        elif v == "=":

            expr = self.results.text()

            if expr.find("√")!= -1:
                index = expr.find("√")
                expr = expr[:index] + str(math.sqrt(float(expr[index+1]))) + expr[index+2:]

            if expr.find("^")!=-1:
                index = expr.find("^")
                expr = expr[:index-1] + str(math.pow(int(expr[index-1]),int(expr[index+1]))) + expr[index+2:]

            res = eval(expr)
            self.results.setText(str(res))

        elif v == "AC":
            self.results.setText("")

        elif v == "DEL":
            curr_value = self.results.text()
            new_value = curr_value[:-1]
            self.results.setText(new_value)

        else:
            curr_value = self.results.text()
            new_value = curr_value + str(v)
            self.results.setText(new_value)




class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.createApp()

    def createApp(self):

        #create our grid
        grid = QGridLayout()
        results = QLineEdit()

        buttons = ["AC","√","DEL","/",
                   7,8,9,"*",
                   4,5,6,"-",
                   1,2,3,"+",
                   "^",0,".","="]

        row = 1
        col = 0

        grid.addWidget(results,0,0,1,4)

        for button in buttons:

            if col > 3:
                col = 0
                row += 1

            buttonObj = Button(button,results)

            grid.addWidget(buttonObj.b,row,col,1,1)

            col += 1

        self.setLayout(grid)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec_())