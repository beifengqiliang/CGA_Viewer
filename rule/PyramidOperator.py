
class PyramidOperator:
    def __init__(self, height):
        self.name = "pyramid"
        self.height = height

    def apply(self, shape, grammar, stack):
        actual_height = grammar.evalFloat(height, shape)
        
        return shape.pyramid(shape._name, actual_height)

    def toXml(self, doc):
        node = doc.createElement(name.c_str())
        node.setAttribute("height", height.c_str())
        
        return node