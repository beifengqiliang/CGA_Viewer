import QtQuick 2.7
import Qt3D.Core 2.1
import Qt3D.Render 2.1
import Qt3D.Extras 2.1
import Qt3D.Input 2.1
import Qt3D.Extras 2.12


Entity {
    id: rootEntity

    Camera {
        id: mainCamera
        projectionType: CameraLens.PerspectiveProjection
        fieldOfView: 45
        nearPlane: 0.01
        farPlane: 1000.0
        position: Qt.vector3d(24.0, 20.0, -20.0)
        upVector: Qt.vector3d(0.0, 1.0, 0.0)
        viewCenter: Qt.vector3d(0.0, 0.0, 0.0)
    }

    FirstPersonCameraController { camera: mainCamera }

    components: [
        RenderSettings {
            activeFrameGraph: ForwardRenderer {
                camera: mainCamera
                clearColor: "transparent"
            }
        },
        InputSettings {}
    ]


    PhongMaterial {
        id: phongMaterial
        ambient: "#FFF"
        diffuse: "#222"
        specular: diffuse
        shininess: 0
    }

    Entity {
        id: childentity

        Mesh {
            id: chestMesh
            //source: "assets/03.obj"

            ConeMesh {
                id: cone

                bottomRadius:20
                hasBottomEndcap: false
                hasTopEndcap: true
                rings : 20
                slices : 3
                topRadius : 3

            }
               
            
        }

        components: [ chestMesh, cone, phongMaterial ]
    }


    Grid3D { enabled: true }
}
