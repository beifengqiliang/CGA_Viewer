import QtQuick 2.7
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3
import QtQml.Models 2.2


Panel {
    id: root

    title: "Images"

    width: 300
    height: 480

    ListView {
        id: listView
        anchors.fill: parent

        model: planets
        delegate: detailsDelegate
    }

    ListModel {
        id: planets
        
        ListElement { name: "Mercury"; imageSource: "images/mercury.jpg" }
        ListElement { name: "Venus"; imageSource: "images/venus.jpg" }
        ListElement { name: "Earth"; imageSource: "images/earth.jpg" }
        ListElement { name: "Mars"; imageSource: "images/mars.jpg" }
    }
    
    Component {
        id: detailsDelegate
        
        Item {
            id: wrapper
            width: listView.width
            height: 30
            
            Rectangle {
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                height: 30
                color: "#87CEFA"
                
                Text {
                    anchors.left: parent.left
                    anchors.verticalCenter: parent.verticalCenter
                    text: name
                }
            }
            
            Rectangle {
                id: image
                color: "black"
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.rightMargin: 2
                anchors.topMargin: 2
                width: 26
                height: 26
                
                Image {
                    anchors.fill: parent
                    fillMode: Image.PreserveAspectFit
                    source: imageSource
                }
            }
            
            MouseArea {
                anchors.fill: parent
                onClicked: parent.state = "expanded"
            }
            
            Rectangle {
                id: closeButton
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.rightMargin: 2
                anchors.topMargin: 2
                width: 26
                height: 26
                color: "gray"
                opacity: 0
                
                MouseArea {
                    anchors.fill: parent
                    onClicked: wrapper.state = ""
                }
            }
            
            states: [State {
                name: "expanded"
                
                PropertyChanges { target: wrapper; height: listView.height }
                PropertyChanges { target: image; width: listView.width; height: listView.width; anchors.rightMargin: 0; anchors.topMargin: 30 }
                PropertyChanges { target: closeButton; opacity: 1 }
                PropertyChanges { target: wrapper.ListView.view; contentY: wrapper.y; interactive: false }
            }]
            
            transitions: [Transition {
                NumberAnimation {
                    duration: 200;
                    properties: "height,width,anchors.rightMargin,anchors.topMargin,opacity,contentY"
                }
            }]
        }
    }
}
