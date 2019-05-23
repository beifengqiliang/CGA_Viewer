from PySide2 import QtCore, QtGui, QtQml


class Helper(QtCore.QObject):
    @QtCore.Slot(result='QVariant')
    def foo(self):
        return {"a": 1, "b": 2}
        # return [3.4, 4.5, 6.7]


if __name__ == '__main__':
    import sys

    app = QtGui.QGuiApplication(sys.argv)

    engine = QtQml.QQmlApplicationEngine()
    helper = Helper()
    engine.rootContext().setContextProperty("helper", helper)
    engine.load(QtCore.QUrl.fromLocalFile('main_dict_demo1.qml'))
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())