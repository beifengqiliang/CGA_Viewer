import QtQuick 2.7
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3
import QtQml.Models 2.2


Panel {
    id: root

    title: "Images"
    width: 300
    height: 480
    readonly property alias currentItem: grid.currentItem
    readonly property string currentItemSource: grid.currentItem ? grid.currentItem.source : ""
    readonly property var currentItemMetadata: grid.currentItem ? grid.currentItem.metadata : undefined


    ListModel {
        id: planets
        
        ListElement { name: "Mercury"; imageSource: "images/03.jpg" }
        ListElement { name: "Venus"; imageSource: "images/06.jpg" }
        ListElement { name: "Earth"; imageSource: "images/25.jpg" }
    }
    
    GridView {
        id: grid
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
