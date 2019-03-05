# -*- coding:utf-8 -*-
import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine


if __name__ == "__main__":

    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine("ui/qml/main.qml")
    app.exec_()