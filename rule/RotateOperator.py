
class RotateOperator:
    def __init__(self, xAngle, yAngle, zAngle):
        self.name = "rotate"
        self.xAngle = xAngle
        self.yAngle = yAngle
        self.zAngle = zAngle

    def apply(self, shape, grammar, stack):
        shape.rotate(shape._name, xAngle, yAngle, zAngle)
        
        return shape

    def toXml(self, doc):
        node = doc.createElement(name.c_str())
        node.setAttribute("xAngle", xAngle)
        node.setAttribute("yAngle", xAngle)
        node.setAttribute("zAngle", xAngle)
        
        return node