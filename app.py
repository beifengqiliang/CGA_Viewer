# -*- coding: utf-8 -*-
from PySide2.QtCore import QUrl, QObject, Slot
from PySide2.QtGui import QGuiApplication
from PySide2.QtQuick import QQuickView

class MyClass(QObject):
    @Slot(str)    # 输入参数为str类型
    def outputString(self, string):
        """
        功能: 创建一个槽
        参数: 输出的数据string
        返回值: 无
        """
        print(string)
        
if __name__ == '__main__':
    path = 'test.qml'   # 加载的QML文件
    app = QGuiApplication([])
    view = QQuickView()
    con = MyClass()
    context = view.rootContext()
    context.setContextProperty("con", con)
    view.engine().quit.connect(app.quit)
    view.setSource(QUrl(path))
    view.show()
    app.exec_()