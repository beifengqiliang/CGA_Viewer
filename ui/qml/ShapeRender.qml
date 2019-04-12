import QtQuick 2.7
import Qt3D.Core 2.12
import Qt3D.Render 2.12
import Qt3D.Input 2.12
import Qt3D.Extras 2.12


Entity{

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

    Entity{
        id: childentity

        GeometryRenderer{
            id: geometryRenderer
            instanceCount: 1
            primitiveType: GeometryRenderer.Triangles
            geometry: Geometry{
                
                Attribute{
                    attributeType: Attribute.VertexAttribute
                    vertexBaseType: Attribute.Float
                    vertexSize: 3
                    byteOffset: 0
                    byteStride: 3 * 4
                    count: drawData.count
                    buffer: drawData.buffer
                }
            }
        }
    
      components: [phongMaterial, geometryRenderer]
    }
    Grid3D {}
}