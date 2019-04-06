
class InnerArchOperator:
    def __init__(self, inside, border):
		self.name = "innerArch"
        self.inside = inside
        self.border = border

	def apply(self, shape, grammar, stack):
		#std::vector<boost::shared_ptr<Shape> > shapes
		shape.innerArch(shape._name, inside, border, shapes)
		stack.insert(stack.end(), shapes.begin(), shapes.end())

		#return boost::shared_ptr<Shape>()

	def toXml(self, doc):
		ode = doc.createElement(name.c_str())
		if not(inside.empty()):
            node.setAttribute("inside", inside.c_str())
		if not(border.empty()):
			node.setAttribute("border", border.c_str())

		return node