# from PySide2.QtCore import Property, Signal, QByteArray
# from PySide2.Qt3DCore import Qt3DCore
from PySide2.Qt3DRender import Qt3DRender


class RoadLineGeometry(Qt3DRender.QGeometry):
    def __init__(self, parent=None):
        Qt3DRender.QGeometry.__init__(self, parent)
        self.m_position_buffer = Qt3DRender.QBuffer(self)
        self.m_position_buffer.setUsage(Qt3DRender.QBuffer.StaticDraw)
        self.m_position_attribute = Qt3DRender.QAttribute(self)
        self.m_position_attribute.setAttributeType(Qt3DRender.QAttribute.VertexAttribute)
        self.m_position_attribute.setDataType(Qt3DRender.QAttribute.Float)
        self.m_position_attribute.setDataSize(3)
        self.m_position_attribute.setName(Qt3DRender.QAttribute.defaultPositionAttributeName())
        self.m_position_attribute.setBuffer(self.m_position_buffer)
        self.addAttribute(self.m_position_attribute)