import QtQuick 2.9
import QtQuick.Controls 2.4

ApplicationWindow {
    visible: true
    Component.onCompleted: { 
        var data = helper.foo()
        for(var key in data){
            var value = data[key]
            console.log(key, ": ", value)
        }
    }
}