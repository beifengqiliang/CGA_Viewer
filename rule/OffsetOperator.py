
class OffsetOperator:
    def __init__(self, offsetDistance, inside, border):
        self.name = "offset"
        self.offsetDistance = offsetDistance
        self.inside = inside
        self.border = border

    def apply(self, shape, grammar, stack):
        actual_offsetDistancet = grammar.evalFloat(offsetDistance, shape)
	    # std::vector<boost::shared_ptr<Shape> > shapes;
        shape.offset(shape._name, actual_offsetDistancet, inside, border, shapes)
        stack.insert(stack.end(), shapes.begin(), shapes.end())
        
        # return boost::shared_ptr<Shape>()

    def toXml(self, doc):
        node = doc.createElement(name.c_str())
        node.setAttribute("offsetDistance", offsetDistance.c_str())
        if not(inside.empty()):
            node.setAttribute("inside", inside.c_str())
        if not(border.empty()):
            node.setAttribute("border", border.c_str())
            
        return node