
class InnerCircleOperator:
    def __init__(self):
        self.name = "innerCircle"

    def apply(self, shape, grammar, stack):
        return shape.innerCircle(shape._name)

    def toXml(self, doc):
        node = doc.createElement(name.c_str())
        
        return node