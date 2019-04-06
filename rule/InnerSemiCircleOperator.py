
class InnerSemiCircleOperator:
    def __init__(self):
        self.name = "semiCircle"

    def apply(self, shape, grammar, stack):
        return shape.innerSemiCircle(shape._name)

    def toXml(self, doc):
        node = doc.createElement(name.c_str())
        
        return node