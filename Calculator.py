#coding=utf-8
from __future__ import division
import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import (
    QWidget, QApplication, QGridLayout, QTextBrowser, 
    QPushButton, QMenuBar, QMessageBox, QAction  # ← 加上 QAction
)

########################################################################
class Example(QWidget):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super(Example, self).__init__()

        self.initUI_basic()


    #----------------------------------------------------------------------
    def initUI_basic(self):
        """"""
        
        self.point = 0
        self.flag = 0
        self.flag_equ = 0
        self.flag_add = 0 #加
        self.flag_sub = 0 #减
        self.flag_mul = 0 #乘
        self.flag_div = 0 #除
        self.flag_flag = ''

        self.num_1 = '0'
        self.num_2 = ''
        self.num_3 = ''
        
        
        #-------------------------------------------------------------------------
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(QApplication.quit)
        
        aboutAction = QAction(QIcon(''), '&About', self)
        aboutAction.triggered.connect(self.OnAboutButton)
        
        menubar = QMenuBar()
        
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        
        aboutMenu = menubar.addMenu('&About')
        aboutMenu.addAction(aboutAction)
        
        #----------------------------------------------------------------------
        global lcd
        lcd = QTextBrowser()
        lcd.setFixedHeight(300)
        lcd.setFont(QFont("Microsoft YaHei", 64))
        
        lcd.setText('0')
        grid = QGridLayout()
        self.setLayout(grid)
        grid.setSpacing(0)
        grid.addWidget(menubar, self.point, 0, 1, 4)
        grid.addWidget(lcd, self.point+1, 0, 1, 4)
        
        
        #----------------------------------------------------------------------
        button_1 = QPushButton('1')
        button_2 = QPushButton('2')
        button_3 = QPushButton('3')
        button_4 = QPushButton('4')
        button_5 = QPushButton('5')
        button_6 = QPushButton('6')
        button_7 = QPushButton('7')
        button_8 = QPushButton('8')
        button_9 = QPushButton('9')
        button_0 = QPushButton('0')
        button_dot = QPushButton('.')
        button_equ = QPushButton('=')
        button_div = QPushButton('/')
        button_mul = QPushButton('*')
        button_add = QPushButton('+')
        button_sub = QPushButton('-')
        button_cls = QPushButton('cls')
        
        button_0.setFixedSize(200, 150)
        button_1.setFixedSize(200, 150)
        button_2.setFixedSize(200, 150)
        button_3.setFixedSize(200, 150)
        button_4.setFixedSize(200, 150)
        button_5.setFixedSize(200, 150)
        button_6.setFixedSize(200, 150)
        button_7.setFixedSize(200, 150)
        button_8.setFixedSize(200, 150)
        button_9.setFixedSize(200, 150)
        button_dot.setFixedSize(200, 150)
        button_equ.setFixedSize(800, 150)
        button_div.setFixedSize(200, 150)
        button_mul.setFixedSize(200, 150)
        button_add.setFixedSize(200, 150)
        button_sub.setFixedSize(200, 150)
        button_cls.setFixedSize(200, 150)
        
        button_0.setFont(QFont("Microsoft YaHei", 48))
        button_1.setFont(QFont("Microsoft YaHei", 48))
        button_2.setFont(QFont("Microsoft YaHei", 48))
        button_3.setFont(QFont("Microsoft YaHei", 48))
        button_4.setFont(QFont("Microsoft YaHei", 48))
        button_5.setFont(QFont("Microsoft YaHei", 48))
        button_6.setFont(QFont("Microsoft YaHei", 48))
        button_7.setFont(QFont("Microsoft YaHei", 48))
        button_8.setFont(QFont("Microsoft YaHei", 48))
        button_9.setFont(QFont("Microsoft YaHei", 48))
        button_dot.setFont(QFont("Microsoft YaHei", 48))
        button_equ.setFont(QFont("Microsoft YaHei", 48))
        button_div.setFont(QFont("Microsoft YaHei", 48))
        button_mul.setFont(QFont("Microsoft YaHei", 48))
        button_add.setFont(QFont("Microsoft YaHei", 48))
        button_sub.setFont(QFont("Microsoft YaHei", 48))
        button_cls.setFont(QFont("Microsoft YaHei", 48))
        

        grid.addWidget(button_7, self.point+2,0)
        grid.addWidget(button_8, self.point+2,1)
        grid.addWidget(button_9, self.point+2,2)
        grid.addWidget(button_div, self.point+2,3)
        grid.addWidget(button_4, self.point+3,0)
        grid.addWidget(button_5, self.point+3,1)
        grid.addWidget(button_6, self.point+3,2)
        grid.addWidget(button_mul, self.point+3,3)
        grid.addWidget(button_1, self.point+4,0)
        grid.addWidget(button_2, self.point+4,1)
        grid.addWidget(button_3, self.point+4,2)
        grid.addWidget(button_sub, self.point+4,3)
        grid.addWidget(button_0, self.point+5,0)
        grid.addWidget(button_dot, self.point+5,1)
        grid.addWidget(button_cls, self.point+5,2)
        grid.addWidget(button_add, self.point+5,3)
        grid.addWidget(button_equ, self.point+6, 0, 1, 4)

        self.resize(1000, 800)
        self.move(300, 400)
        self.setWindowTitle('Calculator')
        grid.setSizeConstraint(QGridLayout.SetFixedSize)
        self.show()

        # 使用 PyQt5 新语法连接信号
        button_0.clicked.connect(self.func_button_0)
        button_1.clicked.connect(self.func_button_1)
        button_2.clicked.connect(self.func_button_2)
        button_3.clicked.connect(self.func_button_3)
        button_4.clicked.connect(self.func_button_4)
        button_5.clicked.connect(self.func_button_5)
        button_6.clicked.connect(self.func_button_6)
        button_7.clicked.connect(self.func_button_7)
        button_8.clicked.connect(self.func_button_8)
        button_9.clicked.connect(self.func_button_9)

        button_cls.clicked.connect(self.func_button_cls)
        button_dot.clicked.connect(self.func_button_dot)

        button_add.clicked.connect(self.func_button_add)
        button_sub.clicked.connect(self.func_button_sub)
        button_mul.clicked.connect(self.func_button_mul)
        button_div.clicked.connect(self.func_button_div)

        button_equ.clicked.connect(self.func_button_equ)

        
    #----------------------------------------------------------------------
    def OnAboutButton(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('About')
        dialog.resize(300, 150)
        dialog.setMinimumSize(200, 100)
        dialog.setMaximumSize(600, 400)
        dialog.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMaximizeButtonHint)

        layout = QVBoxLayout(dialog)
        label = QLabel("A Calculator!")
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setFont(QFont("Microsoft YaHei", 16))
        layout.addWidget(label)

        btn = QPushButton("OK")
        btn.setFixedSize(80, 40)
        btn.setFont(QFont("Microsoft YaHei", 12))
        btn.clicked.connect(dialog.accept)
        layout.addWidget(btn, alignment=QtCore.Qt.AlignCenter)

        dialog.exec_()
    
         
    #----------------------------------------------------------------------
    def keyPressEvent(self, event):
        """"""
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
            
        if event.key() == QtCore.Qt.Key_0:
            self.func_button_0()
            
        if event.key() == QtCore.Qt.Key_1:
            self.func_button_1()
        
        if event.key() == QtCore.Qt.Key_2:
            self.func_button_2()
                    
        if event.key() == QtCore.Qt.Key_3:
            self.func_button_3()

        if event.key() == QtCore.Qt.Key_4:
            self.func_button_4()

        if event.key() == QtCore.Qt.Key_5:
            self.func_button_5()
        
        if event.key() == QtCore.Qt.Key_6:
            self.func_button_6()
                            
        if event.key() == QtCore.Qt.Key_7:
            self.func_button_7()

        if event.key() == QtCore.Qt.Key_8:
            self.func_button_8()

        if event.key() == QtCore.Qt.Key_9:
            self.func_button_9()

        if event.key() == QtCore.Qt.Key_Period:
            self.func_button_dot()        
    
        if event.key() == QtCore.Qt.Key_Enter:
            self.func_button_equ()

        if event.key() == QtCore.Qt.Key_Plus:
            self.func_button_add()
                    
        if event.key() == QtCore.Qt.Key_Minus:
            self.func_button_sub()
        
        if event.key() == QtCore.Qt.Key_Asterisk:
            self.func_button_mul()          
                    
        if event.key() == QtCore.Qt.Key_Slash:
            self.func_button_div()
            
        if event.key() == QtCore.Qt.Key_C:
            self.func_button_cls()

    #----------------------------------------------------------------------
    def func_button_0(self):
        """"""
        if self.flag_equ == 0:

            if self.flag == 0:
                if self.num_1 == '0':
                    self.num_1 = '0'
                    lcd.setText(self.num_1)
                else:
                    self.num_1 = self.num_1+'0'
                    lcd.setText(self.num_1)
            else:
                if self.num_2 == '0' or self.num_2 == '':
                    self.num_2 = '0'
                else:
                    self.num_2 = self.num_2+'0'
                    lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2)
        else:
            self.flag_equ = 1

    #----------------------------------------------------------------------
    def func_button_1(self):
        """"""
        if self.flag_equ == 0:

            if self.flag == 0:
                if self.num_1 == '0':
                    self.num_1 = '1'
                    lcd.setText(self.num_1)
                else:
                    self.num_1 = self.num_1 + '1'
                    lcd.setText(self.num_1)

            else:
                if self.num_2 == '0' or self.num_2 == '':
                    self.num_2 = '1'
                    lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2)
                else:
                    self.num_2 = self.num_2 + '1'
                    lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2)
        else:
            self.flag_equ = 1

    #----------------------------------------------------------------------
    def func_button_2(self):
        """"""
        if self.flag_equ == 0:

            if self.flag == 0:
                if self.num_1 == '0':
                    self.num_1 = '2'
                    lcd.setText(self.num_1)
                else:
                    self.num_1 = self.num_1 + '2'
                    lcd.setText(self.num_1)

            else:
                if self.num_2 == '0' or self.num_2 == '':
                    self.num_2 = '2'
                    lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2)
                else:
                    self.num_2 = self.num_2 + '2'
                    lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2)
        else:
            self.flag_equ = 1

    #----------------------------------------------------------------------
    def func_button_3(self):
        """"""
        if self.flag_equ == 0:

            if self.flag == 0:
                if self.num_1 == '0':
                    self.num_1 = '3'
                    lcd.setText(self.num_1)
                else:
                    self.num_1 = self.num_1 + '3'
                    lcd.setText(self.num_1)

            else:
                if self.num_2 == '0' or self.num_2 == '':
                    self.num_2 = '3'
                    lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2)
                else:
                    self.num_2 = self.num_2 + '3'
                    lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2)
        else:
            self.flag_equ = 1

    #----------------------------------------------------------------------
    def func_button_4(self):
        """"""
        if self.flag_equ == 0:

            if self.flag == 0:
                if self.num_1 == '0':
                    self.num_1 = '4'
                    lcd.setText(self.num_1)
                else:
                    self.num_1 = self.num_1 + '4'
                    lcd.setText(self.num_1)

            else:
                if self.num_2 == '0' or self.num_2 == '':
                    self.num_2 = '4'
                    lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2)
                else:
                    self.num_2 = self.num_2 + '4'
                    lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2)
        else:
            self.flag_equ = 1

    #----------------------------------------------------------------------
    def func_button_5(self):
        """"""
        if self.flag_equ == 0:

            if self.flag == 0:
                if self.num_1 == '0':
                    self.num_1 = '5'
                    lcd.setText(self.num_1)
                else:
                    self.num_1 = self.num_1 + '5'
                    lcd.setText(self.num_1)

            else:
                if self.num_2 == '0' or self.num_2 == '':
                    self.num_2 = '5'
                    lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2)
                else:
                    self.num_2 = self.num_2 + '5'
                    lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2)
        else:
            self.flag_equ = 1

    #----------------------------------------------------------------------
    def func_button_6(self):
        """"""
        if self.flag_equ == 0:

            if self.flag == 0:
                if self.num_1 == '0':
                    self.num_1 = '6'
                    lcd.setText(self.num_1)
                else:
                    self.num_1 = self.num_1 + '6'
                    lcd.setText(self.num_1)

            else:
                if self.num_2 == '0' or self.num_2 == '':
                    self.num_2 = '6'
                    lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2)
                else:
                    self.num_2 = self.num_2 + '6'
                    lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2)
        else:
            self.flag_equ = 1


    #----------------------------------------------------------------------
    def func_button_7(self):
        """"""
        if self.flag_equ == 0:

            if self.flag == 0:
                if self.num_1 == '0':
                    self.num_1 = '7'
                    lcd.setText(self.num_1)
                else:
                    self.num_1 = self.num_1 + '7'
                    lcd.setText(self.num_1)

            else:
                if self.num_2 == '0' or self.num_2 == '':
                    self.num_2 = '7'
                    lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2)
                else:
                    self.num_2 = self.num_2 + '7'
                    lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2)
        else:
            self.flag_equ = 1

    #----------------------------------------------------------------------
    def func_button_8(self):
        """"""
        if self.flag_equ == 0:

            if self.flag == 0:
                if self.num_1 == '0':
                    self.num_1 = '8'
                    lcd.setText(self.num_1)
                else:
                    self.num_1 = self.num_1 + '8'
                    lcd.setText(self.num_1)

            else:
                if self.num_2 == '0' or self.num_2 == '':
                    self.num_2 = '8'
                    lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2)
                else:
                    self.num_2 = self.num_2 + '8'
                    lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2)
        else:
            self.flag_equ = 1

    #----------------------------------------------------------------------
    def func_button_9(self):
        """"""
        if self.flag_equ == 0:

            if self.flag == 0:
                if self.num_1 == '0':
                    self.num_1 = '9'
                    lcd.setText(self.num_1)
                else:
                    self.num_1 = self.num_1 + '9'
                    lcd.setText(self.num_1)

            else:
                if self.num_2 == '0' or self.num_2 == '':
                    self.num_2 = '9'
                    lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2)
                else:
                    self.num_2 = self.num_2 + '9'
                    lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2)
        else:
            self.flag_equ = 1

    #----------------------------------------------------------------------
    def func_button_dot(self):
        """"""
        if self.flag_equ == 0:

            if self.flag == 0:

                if '.' not in self.num_1:

                    if self.num_1 == '0':
                        self.num_1 = '0.'
                        print(self.num_1)
                        lcd.setText(self.num_1)
                    else:
                        self.num_1 = self.num_1 + '.'
                        lcd.setText(self.num_1)

            else:
                if '.' not in self.num_2:

                    if self.num_2 == '':
                        self.num_2 = '0.'
                        lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2)
                    else:
                        self.num_2 = self.num_2 + '.'
                        lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2)
        else:
            self.flag_equ = 1

    #----------------------------------------------------------------------
    def func_button_cls(self):
        """"""
        self.num_1 = '0'
        self.num_2 = ''
        self.flag = 0
        self.flag_equ = 0
        self.flag_add = 0
        self.flag_sub = 0
        self.flag_mul = 0
        self.flag_div = 0
        lcd.setText(self.num_1)

    #----------------------------------------------------------------------
    def func_button_add(self):
        """"""
        if self.flag == 0:
            self.flag = 1
            self.flag_add = 1
            self.flag_sub = 0
            self.flag_mul = 0
            self.flag_div = 0
            self.flag_flag = '+'
            lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2)
        else:
            pass

    #----------------------------------------------------------------------
    def func_button_sub(self):
        """"""
        if self.flag == 0:
            if self.num_1 == '0':
                self.num_1 = '-'
                lcd.setText(self.num_1)

            else:
                self.flag = 1
                self.flag_add = 0
                self.flag_sub = 1
                self.flag_mul = 0
                self.flag_div = 0
                self.flag_flag = '-'

                lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2)
        else:
            if self.num_2 == '':
                self.num_2 = '-'
                lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2)

    #----------------------------------------------------------------------
    def func_button_mul(self):
        """"""
        if self.flag == 0:

            self.flag = 1
            self.flag_add = 0
            self.flag_sub = 0
            self.flag_mul = 1
            self.flag_div = 0
            self.flag_flag = '*'

            lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2)
        else:
            pass

    #----------------------------------------------------------------------
    def func_button_div(self):
        """"""
        if self.flag == 0:
            self.flag = 1
            self.flag_add = 0
            self.flag_sub = 0
            self.flag_mul = 0
            self.flag_div = 1
            self.flag_flag = '/'

            lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2)
        else:
            pass

    #----------------------------------------------------------------------
    def func_button_equ(self):
        """"""
        if self.flag == 1:
            if self.flag_flag == '+':

                if '.' in self.num_1:
                    self.num_3 = str(float(self.num_1) + float(self.num_2))

                if '.' not in self.num_1:
                    if '.' not in self.num_2:
                        self.num_3 = str(int(self.num_1) + int(self.num_2))

                    elif '.' in self.num_2:
                        self.num_3 = str(float(self.num_1) + float(self.num_2))

                    else:
                        self.num_3 = str(int(self.num_1) + int(self.num_2))

                lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2 + ' = ' + self.num_3)
                self.flag = 0
                self.num_1 = '0'
                self.num_2 = ''
                self.num_3 = ''

            elif self.flag_flag == '-':

                if '.' in self.num_1:
                    self.num_3 = str(float(self.num_1) - float(self.num_2))

                if '.' not in self.num_1:
                    if '.' not in self.num_2:
                        self.num_3 = str(int(self.num_1) - int(self.num_2))

                    elif '.' in self.num_2:
                        self.num_3 = str(float(self.num_1) - float(self.num_2))

                    else:
                        self.num_3 = str(int(self.num_1) - int(self.num_2))

                lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2 + ' = ' + self.num_3)
                self.flag = 0
                self.num_1 = '0'
                self.num_2 = ''
                self.num_3 = ''            


            elif self.flag_flag == '*':

                if '.' in self.num_1:
                    self.num_3 = str(float(self.num_1) * float(self.num_2))

                if '.' not in self.num_1:
                    if '.' not in self.num_2:
                        self.num_3 = str(int(self.num_1) * int(self.num_2))

                    elif '.' in self.num_2:
                        self.num_3 = str(float(self.num_1) * float(self.num_2))

                    else:
                        self.num_3 = str(int(self.num_1) * int(self.num_2))

                lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2 + ' = ' + self.num_3)
                self.flag = 0
                self.num_1 = '0'
                self.num_2 = ''
                self.num_3 = ''

            elif self.flag_flag == '/':

                if self.num_2 == '0':
                    lcd.setText("0不能作为除数！")
                    self.flag = 0
                    self.num_1 = '0'
                    self.num_2 = ''
                    self.num_3 = ''

                else:
                    self.num_3 = float(self.num_1) / float(self.num_2)

                    if (self.num_3 * 10) % 10 == 0:
                        lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2 + ' = ' + str(int(self.num_3)))

                        self.flag = 0
                        self.num_1 = '0'
                        self.num_2 = ''
                        self.num_3 = ''
                    else:
                        lcd.setText(self.num_1 + ' ' + self.flag_flag + ' ' + self.num_2 + ' = ' + str(float(self.num_3)))

                        self.flag = 0
                        self.num_1 = '0'
                        self.num_2 = ''
                        self.num_3 = ''                        

        else:
            pass


#----------------------------------------------------------------------
def main():
    """"""
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()