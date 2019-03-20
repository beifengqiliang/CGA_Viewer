import QtQuick 2.7
import QtQuick.Controls 2.3
import QtQuick.Controls 1.4 as Controls1 // For SplitView
import QtQuick.Layouts 1.3
import Qt.labs.platform 1.0 as Platform


/**
 * WorkspaceView is an aggregation of Meshroom's main modules.
 *
 * It contains an ImageGallery, a 2D and a 3D viewer to manipulate and visualize reconstruction data.
 */
Item {
    id: root

    implicitWidth: 300
    implicitHeight: 400

    SystemPalette { id: activePalette }

    Controls1.SplitView {
        anchors.fill: parent

        Controls1.SplitView {
            orientation: Qt.Vertical
            Layout.fillHeight: true
            Layout.minimumWidth: imageGallery.defaultCellSize
            
            ImageGallery {
                id: imageGallery
                Layout.fillHeight: true
                
            }
        }


        Panel {
            title: "Image Viewer"
            Layout.fillHeight: true
            Layout.fillWidth: true
            Layout.minimumWidth: 80
            
        }

        Panel {
            title: "3D Viewer"
            implicitWidth: Math.round(parent.width * 0.45)
            Layout.minimumWidth: 20
            Layout.minimumHeight: 80

        }
    }
}
