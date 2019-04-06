
class SizeOperator:
    def __init__(self, xSize, ySize, zSize, centered):
        self.name = "size"
        self.xSize = xSize
        self.ySize = ySize
        self.zSize = zSize
        self.centered = centered
        
    def apply(self, shape, grammar, stack):
        # float actual_xSize;
        # float actual_ySize;
        # float actual_zSize;
        if (xSize.type == Value.TYPE_RELATIVE):
            actual_xSize = shape._scope.x * grammar.evalFloat(xSize.value, shape)
        else:
            actual_xSize = grammar.evalFloat(xSize.value, shape)

	    if (ySize.type == Value.TYPE_RELATIVE):
            actual_ySize = shape._scope.y * grammar.evalFloat(ySize.value, shape)
        else:
            actual_ySize = grammar.evalFloat(ySize.value, shape)
        
        if (zSize.type == Value.TYPE_RELATIVE):
            actual_zSize = shape._scope.z * grammar.evalFloat(zSize.value, shape)
        else:
            actual_zSize = grammar.evalFloat(zSize.value, shape)
        
        shape.size(actual_xSize, actual_ySize, actual_zSize, centered)
        return shape

    def toXml(self, doc):
        node = doc.createElement(name.c_str())
        if (centered):
            node.setAttribute("centered", "true")
        
        child1 = xSize.toXml(doc)
        child1.setAttribute("name", "xSize")
        node.appendChild(child1)
        
        child2 = ySize.toXml(doc)
        child2.setAttribute("name", "ySize")
        node.appendChild(child2)
        
        child3 = zSize.toXml(doc)
        child3.setAttribute("name", "zSize")
        node.appendChild(child3)
        
        return node