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

            CuboidMesh {
                id: cuboid

                // 保持网格的x范围
                xExtent: 6
                // 保持网格的xy分辨率。此属性的宽度和高度值指定为网格的xy面生成的顶点数
                xyMeshResolution: Qt.size(150, 50)
                // 保持网格的xz分辨率。此属性的宽度和高度值指定为网格的xz面生成的顶点数
                xzMeshResolution: Qt.size(150, 50)
                // 保持网格的y范围
                yExtent: 6
                // 保持网格的yz分辨率。此属性的宽度和高度值指定为网格的yz面生成的顶点数
                yzMeshResolution: Qt.size(150, 50)
                // 保持网格的z范围
                zExtent: 5

            }         
            
        }

        components: [ chestMesh, cuboid, phongMaterial ]
    }


    Grid3D { enabled: true }
}
