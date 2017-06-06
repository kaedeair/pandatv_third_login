# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Tue Jun 06 14:29:25 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1052, 463)
        self.file_path = QtGui.QLineEdit(Dialog)
        self.file_path.setGeometry(QtCore.QRect(60, 80, 251, 20))
        self.file_path.setObjectName(_fromUtf8("file_path"))
        self.result = QtGui.QTextEdit(Dialog)
        self.result.setGeometry(QtCore.QRect(500, 50, 311, 301))
        self.result.setObjectName(_fromUtf8("result"))
        self.login = QtGui.QPushButton(Dialog)
        self.login.setGeometry(QtCore.QRect(360, 300, 75, 23))
        self.login.setObjectName(_fromUtf8("login"))
        self.file1 = QtGui.QPushButton(Dialog)
        self.file1.setGeometry(QtCore.QRect(340, 80, 75, 23))
        self.file1.setObjectName(_fromUtf8("file1"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 50, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 170, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.output = QtGui.QListWidget(Dialog)
        self.output.setGeometry(QtCore.QRect(60, 200, 256, 192))
        self.output.setObjectName(_fromUtf8("output"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(520, 30, 54, 12))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.proxy_file_2 = QtGui.QLineEdit(Dialog)
        self.proxy_file_2.setGeometry(QtCore.QRect(60, 130, 251, 21))
        self.proxy_file_2.setObjectName(_fromUtf8("proxy_file_2"))
        self.proxy_file = QtGui.QPushButton(Dialog)
        self.proxy_file.setGeometry(QtCore.QRect(340, 130, 75, 23))
        self.proxy_file.setObjectName(_fromUtf8("proxy_file"))
        self.proxy_ip = QtGui.QLabel(Dialog)
        self.proxy_ip.setGeometry(QtCore.QRect(70, 110, 131, 16))
        self.proxy_ip.setObjectName(_fromUtf8("proxy_ip"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(830, 60, 161, 141))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.rk_password = QtGui.QLineEdit(self.groupBox)
        self.rk_password.setGeometry(QtCore.QRect(20, 90, 113, 20))
        self.rk_password.setObjectName(_fromUtf8("rk_password"))
        self.rk_user = QtGui.QLineEdit(self.groupBox)
        self.rk_user.setGeometry(QtCore.QRect(20, 40, 113, 20))
        self.rk_user.setObjectName(_fromUtf8("rk_user"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 20, 111, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 70, 111, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(870, 280, 54, 12))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.threadnum = QtGui.QLineEdit(Dialog)
        self.threadnum.setGeometry(QtCore.QRect(870, 310, 113, 20))
        self.threadnum.setObjectName(_fromUtf8("threadnum"))
        self.write2file = QtGui.QPushButton(Dialog)
        self.write2file.setGeometry(QtCore.QRect(630, 370, 75, 23))
        self.write2file.setObjectName(_fromUtf8("write2file"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.login.setText(_translate("Dialog", "批量登陆", None))
        self.file1.setText(_translate("Dialog", "浏览", None))
        self.label.setText(_translate("Dialog", "账号文件", None))
        self.label_2.setText(_translate("Dialog", "登录状态", None))
        self.label_3.setText(_translate("Dialog", "cookie", None))
        self.proxy_file.setText(_translate("Dialog", "浏览", None))
        self.proxy_ip.setText(_translate("Dialog", "代理文件(不填就直连）", None))
        self.groupBox.setTitle(_translate("Dialog", "若快打码", None))
        self.label_7.setText(_translate("Dialog", "用户名", None))
        self.label_8.setText(_translate("Dialog", "密码", None))
        self.label_4.setText(_translate("Dialog", "线程数", None))
        self.write2file.setText(_translate("Dialog", "导出", None))

