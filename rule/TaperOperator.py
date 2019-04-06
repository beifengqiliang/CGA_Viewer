
class TaperOperator:
    def __init__(self, height, slope):
        self.name = "taper"
        self.height = height
        self.slope = slope
        
    def apply(self, shape, grammar, stack):
        actual_height = grammar.evalFloat(height, shape)
        actual_slope = grammar.evalFloat(slope, shape)
        
        return shape.taper(shape._name, actual_height, actual_slope)
    
    def toXml(self, doc):
        node = doc.createElement(name.c_str())
        node.setAttribute("height", height.c_str())
        node.setAttribute("slope", slope.c_str())
        
        return node