# -*- coding: utf-8 -*-
import threadpool
from PyQt4 import QtGui

from UI import *
from qq_login_third_party import Login
import threading
from check_proxy import proxy_check
import Queue
import random
class MainWindow(QtGui.QDialog):

    def __init__(self,parent=None):

        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_Dialog()# Ui_Dialog为.ui产生.py文件中窗体类名，经测试类名以Ui_为前缀，加上UI窗体对象名（此处为Dialog，见上图）
        self.ui.setupUi(self)
        self.ui.threadnum.setText('5')
        self.connect(self.ui.login, QtCore.SIGNAL("clicked()"),
                     self, QtCore.SLOT("login()"))
        self.connect(self.ui.file1,QtCore.SIGNAL("clicked()"),
                     self,QtCore.SLOT("choose_path()"))

        self.connect(self.ui.proxy_file, QtCore.SIGNAL("clicked()"),
                     self, QtCore.SLOT("choose_path2()"))
        self.connect(self.ui.write2file, QtCore.SIGNAL("clicked()"),
                     self, QtCore.SLOT("write2file()"))

    @QtCore.pyqtSlot()
    def write2file(self):
        x = QtGui.QFileDialog().getSaveFileName()
        path=x.__str__()
        fd=open(path,'w')
        fd.write(self.ui.result.toPlainText())
        fd.close()

    @QtCore.pyqtSlot()
    def choose_path2(self):
        x = QtGui.QFileDialog().getOpenFileName()
        self.ui.proxy_file_2.setText(x)

    @QtCore.pyqtSlot()
    def choose_path(self):
        x = QtGui.QFileDialog().getOpenFileName()
        self.ui.file_path.setText(x)

    @QtCore.pyqtSlot()
    def login(self):
        # self.ui.status.setText(u'批量登录开始' )
        threading.Thread(target=self.logining).start()

            # self.ui.result.append('\n')
    def logining(self):
        file = self.ui.file_path.text().__str__()
        proxy_file=self.ui.proxy_file_2.text().__str__()

        self.proxy_list=Queue.Queue()
        if proxy_file is not u'':
            for line in open(proxy_file).readlines():
                item=line.strip().split('----')
                self.proxy_list.put(item)
        else:
            self.proxy_list=None
        pool=threadpool.ThreadPool(int(self.ui.threadnum.text().__str__()))
        args=[]
        rk_username = self.ui.rk_user.text().__str__()
        rk_password = self.ui.rk_password.text().__str__()
        for line in open(file).readlines():


            username, password = line.strip().split('----')[0:2]
            args.append(([username,password,rk_username,rk_password],None))

            # username=self.ui.username.text().__str__()
            # password=self.ui.password.text().__str__()
            # self.ui.status.setText(u'账号：%s正在登录'%username)


        reqs=threadpool.makeRequests(self.logining_2,args)
        [pool.putRequest(req) for req in reqs]
        pool.wait()
        # self.logining_2(username,password,rk_username,rk_password)
        self.ui.output.addItem(u'登录结束' )
        # self.ui.status.setText(u'批量登录完成')
    def logining_2(self,username,password,rk_username,rk_password):
        self.ui.output.addItem(u'账号：%s正在登录' % username)
        if self.proxy_list is not None:

            while True:
                proxy =self.proxy_list.get()
                if proxy_check(proxy) is True:
                    break
        else:

            proxy=None
        result = Login(username, password,proxy,rk_username,rk_password).login()
        if result ==-1:
            if proxy is None:
                ip=u'本地IP'
                self.ui.output.addItem(u'IP：%s登录过多' % ip)
                return False
            else:
                ip=proxy[0]
            self.ui.output.addItem(u'IP：%s登录过多' % ip)

            return self.logining_2(username, password, rk_username, rk_password)
        if result ==-2:
            self.ui.output.addItem(u'账号：%s密码错误' % username)
            return False
        if result ==-3:
            self.ui.output.addItem(u'账号：%s密码错误' % username)
            return False
        if result == -4:
            self.ui.output.addItem(u'账号：%s代理错误' % username)
            return self.logining_2(username, password, rk_username, rk_password)

        if result == -5:
            self.ui.output.addItem(u'账号：%s账号被回收' % username)
            return False
        self.ui.output.addItem(u'账号：%s登录成功' % username)
        self.proxy_list.put(proxy)
        self.ui.result.append('----'.join([username, password, result]))
        return True

if __name__ == "__main__":

    import sys

    app = QtGui.QApplication(sys.argv)
    myapp=MainWindow()
    myapp.show()
    app.exec_()