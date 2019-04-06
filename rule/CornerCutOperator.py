
class CornerCutOperator:
    def __init__(self, type, length):
        self.name = "cornerCut"
        self.type = type
        self.length = length

    def apply(self, shape, grammar, stack):
        actual_length = grammar.evalFloat(length, shape)
        return shape.cornerCut(shape._name, type, actual_length)

    def toXml(self, doc):
        node = doc.createElement(name.c_str())
        
        if (type == CORNER_CUT_STRAIGHT):
            node.setAttribute("type", "straight")
	    elif (type == CORNER_CUT_CURVE):
            node.setAttribute("type", "curve")
	    elif (type == CORNER_CUT_NEGATIVE_CURVE):
		    node.setAttribute("type", "negative_curve")

	    node.setAttribute("length", length.c_str())

	    return node