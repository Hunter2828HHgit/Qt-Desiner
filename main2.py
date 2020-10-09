import sys
from test5 import *
import math

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

symbol = ""
view_numbers = ""
num_1 = ""
num_2 = ""
def button_0():
    global view_numbers
    global num_1
    view_numbers = view_numbers + '0'
    ui.lineEdit.setText(view_numbers)
    num_1 = num_1+'0'

ui.b0.clicked.connect(button_0)


def button_1():
    global view_numbers
    global num_1
    view_numbers = view_numbers + '1'
    ui.lineEdit.setText(view_numbers)
    num_1 = num_1+'1'

ui.b1.clicked.connect(button_1)


def button_2():
    global view_numbers
    global num_1
    view_numbers = view_numbers + '2'
    ui.lineEdit.setText(view_numbers)
    num_1 = num_1+'2'

ui.b2.clicked.connect(button_2)


def button_3():
    global view_numbers
    global num_1
    view_numbers = view_numbers + '3'
    ui.lineEdit.setText(view_numbers)
    num_1 = num_1+'3'

ui.b3.clicked.connect(button_3)


def button_4():
    global view_numbers
    global num_1
    view_numbers = view_numbers + '4'
    ui.lineEdit.setText(view_numbers)
    num_1 = num_1+'4'

ui.b4.clicked.connect(button_4)


def button_5():
    global view_numbers
    global num_1
    view_numbers = view_numbers + '5'
    ui.lineEdit.setText(view_numbers)
    num_1 = num_1+'5'

ui.b5.clicked.connect(button_5)


def button_6():
    global view_numbers
    global num_1
    view_numbers = view_numbers + '6'
    ui.lineEdit.setText(view_numbers)
    num_1 = num_1+'6'

ui.b6.clicked.connect(button_6)


def button_7():
    global view_numbers
    global num_1
    view_numbers = view_numbers + '7'
    ui.lineEdit.setText(view_numbers)
    num_1 = num_1+'7'

ui.b7.clicked.connect(button_7)


def button_8():
    global view_numbers
    global num_1
    view_numbers = view_numbers + '8'
    ui.lineEdit.setText(view_numbers)
    num_1 = num_1+'8'

ui.b8.clicked.connect(button_8)


def button_9():
    global view_numbers
    global num_1
    view_numbers = view_numbers + '9'
    ui.lineEdit.setText(view_numbers)
    num_1 = num_1+'9'

ui.b9.clicked.connect(button_9)


def Delete():
    global view_numbers
    global num_1
    view_numbers = view_numbers[0:-1]
    ui.lineEdit.setText(view_numbers)
    num_1 = num_1[0:-1]

ui.bdel.clicked.connect(Delete)


def Backspace():
    global view_numbers
    global num_1
    global symbol
    global num_2
    symbol = ""
    view_numbers = ""
    num_1 = ""
    num_2 = ""
    ui.lineEdit.setText(view_numbers)
ui.bc.clicked.connect(Backspace)


def procent():
    global view_numbers
    global num_1
    global symbol
    global num_2
    if '+'in view_numbers or '-'in view_numbers or '/'in view_numbers or 'x'in view_numbers or '%' in view_numbers:
        pass
    else:
        num_1 = float(num_1)
        num_1 = num_1 * 0.01
        num_1 = str(num_1)
        view_numbers = num_1
        ui.lineEdit.setText(view_numbers)
ui.bpr.clicked.connect(procent)


def factorial():
    global view_numbers
    global num_1
    global symbol
    global num_2
    if '+'in view_numbers or '-'in view_numbers or '/'in view_numbers or 'x'in view_numbers or '%' in view_numbers:
        ui.lineEdit.setText('Ошибка!')
    else:
        if float(view_numbers) <= 0:
            ui.lineEdit.setText('Ошибка!')
        else:
            try:
                fact = 1
                num_1 = int(num_1)
                for i in range(1, num_1 + 1):
                    fact = fact * i
                num_1 = fact
                num_1 = str(num_1)
                view_numbers = num_1
                ui.lineEdit.setText(view_numbers)
            except:
                ui.lineEdit.setText('Число нецелое')
ui.bv.clicked.connect(factorial)

def point():
    global view_numbers
    global num_1
    global symbol
    global num_2
    if '.' in num_1:
        pass
    else:
        num_1 = num_1 + '.'
        view_numbers = view_numbers + '.'
        ui.lineEdit.setText(view_numbers)
ui.bt.clicked.connect(point)


def devision():
    global view_numbers
    global num_1
    global symbol
    global num_2
    if '+' in view_numbers or '-' in view_numbers or '/' in view_numbers or '*' in view_numbers:
        pass
    else:
        view_numbers = view_numbers + '/'
        ui.lineEdit.setText(view_numbers)
        symbol = '/'
        num_2 = num_1
        num_1 = ''
ui.pushButton_20.clicked.connect(devision)


def plus():
    global view_numbers
    global num_1
    global symbol
    global num_2
    if '+' in view_numbers or '-' in view_numbers or '/' in view_numbers or '*' in view_numbers:
        pass
    else:
        view_numbers = view_numbers + '+'
        ui.lineEdit.setText(view_numbers)
        symbol = '+'
        num_2 = num_1
        num_1 = ''
ui.bp.clicked.connect(plus)


def mult():
    global view_numbers
    global num_1
    global symbol
    global num_2
    if '+' in view_numbers or '-' in view_numbers or '/' in view_numbers or '*' in view_numbers:
        pass
    else:
        view_numbers = view_numbers + 'x'
        ui.lineEdit.setText(view_numbers)
        symbol = 'x'
        num_2 = num_1
        num_1 = ''
ui.bu.clicked.connect(mult)



def minus():
    global view_numbers
    global num_1
    global symbol
    global num_2
    if '+' in view_numbers or '-' in view_numbers or '/' in view_numbers or '*' in view_numbers:
        pass
    else:
        view_numbers = view_numbers + '-'
        ui.lineEdit.setText(view_numbers)
        symbol = '-'
        num_2 = num_1
        num_1 = ''

ui.bm.clicked.connect(minus)


def ravno():
    global view_numbers
    global num_1
    global symbol
    global num_2
    if symbol == '+':
        num_1 = float(num_1)
        num_2 = float(num_2)
        answer = num_1+num_2
        num_1 = answer
        answer = str(answer)
        ui.lineEdit.setText(answer)
        num_1 = str(num_1)
        num_2 = str(num_2)
        view_numbers = num_1
        answer = ''
    elif symbol == '-':
        num_1 = float(num_1)
        num_2 = float(num_2)
        answer = num_1-num_2
        num_1 = answer
        answer = str(answer)
        ui.lineEdit.setText(answer)
        num_1 = str(num_1)
        num_2 = str(num_2)
        view_numbers = num_1
        answer = ''
    elif symbol == '/':
        num_1 = float(num_1)
        num_2 = float(num_2)
        answer = num_2/num_1
        num_1 = answer
        answer = str(answer)
        ui.lineEdit.setText(answer)
        num_1 = str(num_1)
        num_2 = str(num_2)
        view_numbers = num_1
        answer = ''
    elif symbol == 'x':
        num_1 = float(num_1)
        num_2 = float(num_2)
        answer = num_1*num_2
        num_1 = answer
        answer = str(answer)
        ui.lineEdit.setText(answer)
        num_1 = str(num_1)
        num_2 = str(num_2)
        view_numbers = num_1
        answer = ''
    else:
        ui.lineEdit.setText('Ошибка! Симбол не выбран!')

ui.br.clicked.connect(ravno)

sys.exit(app.exec_())
