
class ColorOperator:
    def __init__(self, r, g, b):
        self.name = "color"
        self.r = r
        self.g = g
        self.b = b
        self.s = ""

    def __init__(self, s):
        self.name = "color"
        self.r = ""
        self.g = ""
        self.b = ""
        self.s = s

    def apply(self, shape, grammar, stack):
        if (s.empty()):
            shape._color.r = grammar.evalFloat(r, shape)
            shape._color.g = grammar.evalFloat(g, shape)
            shape._color.b = grammar.evalFloat(b, shape)
        else:
            decodeRGB(grammar.evalString(s, shape), shape._color.r, shape._color.g, shape._color.b)
        
        return shape
    
    def toXml(self, doc):
	    node = doc.createElement(name.c_str())
        if (s.empty()):
            node.setAttribute("r", r.c_str())
            node.setAttribute("g", g.c_str())
            node.setAttribute("b", b.c_str())
	    else:
            node.setAttribute("s", s.c_str())
	    
        return node

    def decodeRGB(self, str, r, g, b):
	    # int ir, ig, ib;
        # std::istringstream(str.substr(1, 2)) >> std::hex >> ir;
        # std::istringstream(str.substr(3, 2)) >> std::hex >> ig;
        # std::istringstream(str.substr(5, 2)) >> std::hex >> ib;

	    r = (float)ir / 255
	    g = (float)ig / 255
	    b = (float)ib / 255