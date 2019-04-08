import QtQuick 2.7
import QtQuick.Controls 2.3
import QtQuick.Controls 1.4 as Controls1
import QtQuick.Layouts 1.1
import QtQml.Models 2.2
import QtQml 2.2
import QtQuick.Dialogs 1.3


ApplicationWindow {
    id: _window
    title: "pictureviewer"
    width: 1000
    height: 800
    visible: true

    FileDialog {
        id: openFileDialog
        title: "Open Files"
        nameFilters: ["XML Files(*.xml)"]
        folder: shortcuts.desktop
        onAccepted: {
            console.log("You chose: " + openFileDialog.fileUrls)
            //loadCGA(openFileDialog.fileUrls)  
        }
    }

    // 菜单栏
    menuBar: MenuBar {
        //palette.window: Qt.darker(activePalette.window, 1.15)
        width: parent.width
        height: 0

        Menu {
            title: "File"
            Action {
                text: "New"
                shortcut: "Ctrl+N"
            }
            Action {
                text: "Open CGA"
                shortcut: "Ctrl+O"
                onTriggered: openFileDialog.open()
            }
            Action {
                id: saveAction
                text: "Save"
                shortcut: "Ctrl+S"
            }
            Action {
                id: saveAsAction
                text: "Save As..."
                shortcut: "Ctrl+Shift+S"
            }
            MenuSeparator {}
            Action {
                text: "Quit"
                onTriggered: Qt.quit()
            }
        }
        Menu {
            title: "Edit"
            MenuItem {
                text:"undoAction"
                
            }
            MenuItem {
                text:"redoAction"
                
            }
        }
        Menu {
            title: "View"
            MenuItem {
                id: graphEditorVisibilityCB
                text: "Graph Editor"
                checkable: true
                checked: true
            }
            MenuItem {
                id: liveSfMVisibilityCB
                text: "Live Reconstruction"
                checkable: true
                checked: false
            }
            MenuSeparator {}
            Action {
                text: "Fullscreen"
                checkable:true
                checked: _window.visibility == ApplicationWindow.FullScreen
                shortcut: "Ctrl+F"
                onTriggered: _window.visibility == ApplicationWindow.FullScreen ? _window.showNormal() : showFullScreen()
            }
        }
        Menu {
            title: "Help"
            Action {
                text: "About ..."
                shortcut: "F1"
            }
        }
    }

    header: ToolBar {
        id: toolbar
        padding: 0
        leftPadding: 4
        rightPadding: 4
        ToolTip.toolTip.background: Rectangle {
            color: "lightslategray"
            border.color: "black"
        }
    }

    Controls1.SplitView {
        anchors.fill: parent
        orientation: Qt.Vertical
        
        ToolTip.toolTip.background: Rectangle {
            color: "lightslategray"
            border.color: "black"
        }

        ColumnLayout {
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.topMargin: 2
            implicitHeight: Math.round(parent.height * 0.7)
            spacing: 4

            RowLayout {
                Layout.rightMargin: 4
                Layout.leftMargin: 4
                Layout.fillWidth: false
                Layout.alignment: Qt.AlignHCenter

            }
            
        }

        WorkspaceView {
            id: workspaceView
            Layout.fillWidth: true
            Layout.fillHeight: true

        }

        Controls1.SplitView {
            orientation: Qt.Horizontal
            width: parent.width
            height: Math.round(parent.height * 0.3)
            visible: true

            Rectangle {
                id: graphEditorPanel
                Layout.fillWidth: true
                border { width: 0.5 }
                RowLayout {
                    Button {
                        text: "button1"
                        font.pointSize: 11
                    }
                }

                Rectangle{
                    id: graphEditor
                    border { width: 0.5 }
                    anchors.fill: parent
                }
            }

            Rectangle{
                width: Math.round(parent.width * 0.3)
                border { width: 0.5 }
            }
        }
    }

}