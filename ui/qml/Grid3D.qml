import QtQuick 2.7
import Qt3D.Core 2.0
import Qt3D.Render 2.0
import Qt3D.Extras 2.0


Entity {
    id: gridEntity

    components: [
        PhongMaterial {
            // 冯氏光照模型参数设置
            ambient: "#FFF" // 环境光
            diffuse: "#222" // 散射光
            specular: diffuse // 镜面反射
            shininess: 0 // 光泽常数
        },

        GeometryRenderer {
            // 利用GeometryRenderer提供的基本类型(line)来进行几何图形的绘制
            primitiveType: GeometryRenderer.Lines
            // 几何数据的坐标
            geometry: Geometry {
                Attribute {
                    id: gridPosition
                    attributeType: Attribute.VertexAttribute
                    vertexBaseType: Attribute.Float // 定义顶点的数据类型
                    vertexSize: 3 // 顶点大小
                    count: 0
                    name: defaultPositionAttributeName
                    buffer: Buffer {
                        type: Buffer.VertexBuffer
                        data: {
                            function buildGrid(first, last, offset, attribute) {
                                var vertexCount = (((last - first) / offset) + 1) * 7;
                                var f32a = new Float32Array(vertexCount * 2);
                                for(var id = 0, i = first; i <= last; i += offset, id++){
                                    f32a[12*id] = i;
                                    f32a[12*id+1] = 0.0;
                                    f32a[12*id+2] = first;

                                    f32a[12*id+3] = i;
                                    f32a[12*id+4] = 0.0;
                                    f32a[12*id+5] = last;

                                    f32a[12*id+6] = first;
                                    f32a[12*id+7] = 0.0;
                                    f32a[12*id+8] = i;

                                    f32a[12*id+9] = last;
                                    f32a[12*id+10] = 0.0;
                                    f32a[12*id+11] = i;

                                    f32a[12*id+12] = i;
                                    f32a[12*id+13] = 0.0;
                                }
                                attribute.count = vertexCount
                                return f32a;
                            }
                            return buildGrid(-14, 14, 1, gridPosition);
                        }
                    }
                }
            }
        }
    ]
}
