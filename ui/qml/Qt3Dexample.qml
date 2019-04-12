import QtQuick 2.7
import Qt3D.Core 2.12
import Qt3D.Render 2.12
import Qt3D.Input 2.12
import Qt3D.Extras 2.12

Entity {
    id: sceneRoot
    Camera {
        id: camera
        projectionType: CameraLens.PerspectiveProjection
        fieldOfView: 45
        aspectRatio: 16/9
        nearPlane: 0.1
        farPlane: 1000.0
        position: Qt.vector3d(24.0, 20.0, -20.0)
        upVector: Qt.vector3d(0.0, 1.0, 0.0)
        viewCenter: Qt.vector3d(0.0, 0.0, 0.0)
    }

    components: RenderSettings {
         activeFrameGraph: ForwardRenderer {
            camera: camera
            clearColor: "blue"
        }
    }

    CylinderMesh {
        id: mesh
        radius: 1
        length: 3
        rings: 100
        slices: 20
    }
    Transform {
        id: transform
        scale3D: Qt.vector3d(1.5, 1, 0.5)
        rotation: fromAxisAndAngle(Qt.vector3d(1, 0, 0), 45)
    }
    PhongMaterial {
        id: phongMaterial
        ambient: "#FFF"
        diffuse: "#222"
        specular: diffuse
        shininess: 0
    }
    Entity {
        id: mainEntity
        objectName: "mainEntity"
        components: [ mesh, phongMaterial, transform ]
    }
}