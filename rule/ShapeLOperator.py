
class ShapeLOperator:
    def __init__(self, frontWidth, rightWidth):
        self.name = "shapeL"
        self.frontWidth = frontWidth
        self.rightWidth = rightWidth
        
    def apply(self, shape, grammar, stack):
        # float actual_frontWidth;
        # float actual_rightWidth;

	    if (frontWidth.type == Value.TYPE_RELATIVE):
            actual_frontWidth = shape._scope.x * grammar.evalFloat(frontWidth.value, shape)
        else:
            actual_frontWidth = grammar.evalFloat(frontWidth.value, shape)
            
        if (rightWidth.type == Value.TYPE_RELATIVE):
            actual_rightWidth = shape._scope.y * grammar.evalFloat(rightWidth.value, shape)
        else:
            actual_rightWidth = grammar.evalFloat(rightWidth.value, shape)
        
        return shape.shapeL(shape._name, actual_frontWidth, actual_rightWidth)
        
    def toXml(self, doc):
        node = doc.createElement(name.c_str())
        
        child1 = frontWidth.toXml(doc)
        child1.setAttribute("name", "frontWidth")
        node.appendChild(child1)
        
        child2 = rightWidth.toXml(doc)
        child2.setAttribute("name", "rightWidth")
        node.appendChild(child2)
        
        return node