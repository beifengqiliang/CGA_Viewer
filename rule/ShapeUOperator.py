
class ShapeUOperator:
    def __init__(self, frontWidth, backDepth):
        self.name = "shapeU"
        self.frontWidth = frontWidth
        self.backDepth = backDepth
        
    def apply(self, shape, grammar, stack):
        # float actual_frontWidth;
        # float actual_backDepth;

	    if (frontWidth.type == Value.TYPE_RELATIVE):
            actual_frontWidth = shape._scope.x * grammar.evalFloat(frontWidth.value, shape)
        else:
            actual_frontWidth = grammar.evalFloat(frontWidth.value, shape)
        
        if (backDepth.type == Value.TYPE_RELATIVE):
            actual_backDepth = shape._scope.y * grammar.evalFloat(backDepth.value, shape)
        else:
            actual_backDepth = grammar.evalFloat(backDepth.value, shape)
        
        return shape.shapeU(shape._name, actual_frontWidth, actual_backDepth)
        
    def toXml(self, doc):
        node = doc.createElement(name.c_str())
        
        child1 = frontWidth.toXml(doc)
        child1.setAttribute("name", "frontWidth")
        node.appendChild(child1)
        
        child2 = backDepth.toXml(doc)
        child2.setAttribute("name", "backDepth")
        node.appendChild(child2)
        
        return node