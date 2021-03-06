
class ExtrudeOperator:
    def __init__(self,  height):
        self.name = "extrude"
        self.height = height

    def apply(self, shape, grammar, stack):
        actual_height = grammar.evalFloat(self.height, shape)
        return shape.extrude(shape._name, actual_height)

    def toXml(self, doc):
        node = doc.createElement(self.name.c_str())
        node.setAttribute("height", self.height.c_str())
                
        return node