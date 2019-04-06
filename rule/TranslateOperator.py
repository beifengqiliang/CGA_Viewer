
class TranslateOperator:
    def __init__(self, mode, coordSystem, x, y, z):
        self.name = "translate"
        self.mode = mode
        self.coordSystem = coordSystem
        self.x = x
        self.y = y
        self.z = z
        
    def apply(self, shape, grammar, stack):
        # float actual_x;
        # float actual_y;
        # float actual_z;

	    if (x.type == Value.TYPE_RELATIVE):
            actual_x = shape._scope.x * grammar.evalFloat(x.value, shape)
        else:
            actual_x = grammar.evalFloat(x.value, shape)
            
	    if (y.type == Value.TYPE_RELATIVE):
            actual_y = shape._scope.y * grammar.evalFloat(y.value, shape)
        else:
            actual_y = grammar.evalFloat(y.value, shape)
        
        if (z.type == Value.TYPE_RELATIVE):
            actual_z = shape._scope.z * grammar.evalFloat(z.value, shape)
        else:
            actual_z = grammar.evalFloat(z.value, shape)
        
        shape.translate(mode, coordSystem, actual_x, actual_y, actual_z)
        return shape

    def toXml(self, doc):
        node = doc.createElement(name.c_str())
        
        if (mode == MODE_ABSOLUTE):
            node.setAttribute("mode", "abs")
        elif (mode == MODE_RELATIVE):
            node.setAttribute("mode", "rel")
        
        if (coordSystem == COORD_SYSTEM_WORLD):
            node.setAttribute("coordSystem", "world")
        elif (coordSystem == COORD_SYSTEM_OBJECT):
            node.setAttribute("coordSystem", "object")
        
        child1 = x.toXml(doc)
        child1.setAttribute("name", "x")
        node.appendChild(child1)
        
        child2 = y.toXml(doc)
        child2.setAttribute("name", "y")
        node.appendChild(child2)
        
        child3 = z.toXml(doc)
        child3.setAttribute("name", "z")
        node.appendChild(child3)
        
        return node