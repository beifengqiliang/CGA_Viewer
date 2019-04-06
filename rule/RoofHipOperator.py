
class RoofHipOperator:
    def __init__(self, angle):
        self.name = "roofHip"
        self.angle = angle
        
    def apply(self, shape, grammar, stack):
        actual_angle = grammar.evalFloat(angle, shape)
        return shape.roofHip(shape._name, actual_angle)
        
    def toXml(self, doc):
        node = doc.createElement(name.c_str())
        node.setAttribute("angle", angle.c_str())
        return node