
class CopyOperator:
    def __init__(self, copy_name):
        self.name = "copy"
        self.copy_name = copy_name

    def apply(self, shape, grammar, stack):
        copy = shape.clone(copy_name)
        stack.push_back(copy)
        
        return shape

    def toXml(self, doc):
	    node = doc.createElement(name.c_str())
	    node.setAttribute("name", copy_name.c_str())

	    return node