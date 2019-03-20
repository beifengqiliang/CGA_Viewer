import QtQuick 2.7
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3
import QtQml.Models 2.2


Panel {
    id: root

    title: "Images"

    width: 300
    height: 480


    ListModel {
        id: planets
        
        ListElement { name: "Mercury"; imageSource: "images/mercury.jpg" }
        ListElement { name: "Venus"; imageSource: "images/venus.jpg" }
        ListElement { name: "Earth"; imageSource: "images/earth.jpg" }
        ListElement { name: "Mars"; imageSource: "images/mars.jpg" }
    }
    
    GridView {
        anchors.fill: parent
        anchors.margins: 20

        clip: true
        model: planets
        delegate: planetsDelegate

        // 单元宽度（cellWidth）与单元高度（cellHeight）
        cellWidth: 85
        cellHeight: 85  
    }

    Component {
        id: planetsDelegate

        Rectangle {
            width: 80
            height: 80

            Image {
                anchors.fill: parent
                fillMode: Image.PreserveAspectFit
                source: imageSource 
            }
        }
    }
}
