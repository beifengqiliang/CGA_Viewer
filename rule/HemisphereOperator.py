
class HemisphereOperator:
    def __init__(self):
        self.name = "hemisphere"

    def apply(self, shape, grammar, stack):
        return shape.hemisphere(shape._name)

    def toXml(self, doc):
        node = doc.createElement(name.c_str())
        return node