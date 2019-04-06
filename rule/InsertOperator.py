
class InsertOperator:
    def __init__(self, geometryPath):
        self.name = "insert"
        self.geometryPath = geometryPath

    def apply(self, shape, grammar, stack):
        return shape.insert(shape._name, grammar.evalString(geometryPath, shape))

    def toXml(self, doc):
        node = doc.createElement(name.c_str())
        node.setAttribute("geometryPath", geometryPath.c_str())
        
        return node