
class SplitOperator:
    def __init__(self, splitAxis, sizes, output_names):
        self.name = "split"
        self.splitAxis = splitAxis
        self.sizes = sizes
        self.output_names = output_names

    def apply(self, shape, grammar, stack):
        # std::vector<boost::shared_ptr<Shape> > floors;
        # std::vector<Value> actual_sizes = sizes;
        for i in range(0, sizes.size(), 1) :
            actual_sizes[i].value = to_string(grammar.evalFloat(sizes[i].value, shape))
            
	    # std::vector<float> decoded_sizes;
	    # std::vector<std::string> decoded_output_names;
	    if (splitAxis == DIRECTION_X):
            Rule.decodeSplitSizes(shape._scope.x, actual_sizes, output_names, grammar, shape, decoded_sizes, decoded_output_names)
        elif (splitAxis == DIRECTION_Y):
            Rule.decodeSplitSizes(shape._scope.y, actual_sizes, output_names, grammar, shape, decoded_sizes, decoded_output_names)
        elif (splitAxis == DIRECTION_Z):
            Rule.decodeSplitSizes(shape._scope.z, actual_sizes, output_names, grammar, shape, decoded_sizes, decoded_output_names)

	    shape.split(splitAxis, decoded_sizes, decoded_output_names, floors)
	    stack.insert(stack.end(), floors.begin(), floors.end())

	    # return boost::shared_ptr<Shape>()

    def toXml(self, doc):
        node = doc.createElement(name.c_str())
        if (splitAxis == DIRECTION_X):
            node.setAttribute("splitAxis", "x")
        elif (splitAxis == DIRECTION_Y):
            node.setAttribute("splitAxis", "y")
        else if (splitAxis == DIRECTION_Z):
            node.setAttribute("splitAxis", "z")
        
        for i in range(0, sizes.size(),1):
            child = sizes[i].toXml(doc)
            child.setAttribute("name", output_names[i].c_str())
            node.appendChild(child)
            
        return node