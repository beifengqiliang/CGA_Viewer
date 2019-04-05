
class CompOperator:
    def __init__(self, string, sname_map):
        self.name = "comp"
        self.name_map = name_map

    def apply(self, shape, grammar, stack):
	    # std::vector<boost::shared_ptr<Shape> > shapes;
	
	    shape.comp(name_map, shapes)
	    stack.insert(stack.end(), shapes.begin(), shapes.end())

	    return Shape()

    def toXml(self, doc):
	    node = doc.createElement(name.c_str())
        it = name_map.begin()
        while (it != name_map.end()):
		    child = doc.createElement("param")
		    child.setAttribute("name", it.first.c_str())
		    child.setAttribute("value", it.second.c_str())
		    node.appendChild(child)
            it += 1
            
        return node
