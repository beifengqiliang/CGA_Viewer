

class CenterOperator:
    def __init__(self, axesSelector):
        self.name = "center"
        self.axesSelector = axesSelector

    def apply(self, shape, grammar, stack):
        shape.center(axesSelector)
        return shape

    def toXml(self, doc):
        node = doc.createElement(name.c_str())
        if (axesSelector == AXES_SELECTOR_XYZ):
            node.setAttribute("axesSelector", "xyz")
        elif (axesSelector == AXES_SELECTOR_X):
            node.setAttribute("axesSelector", "x")
        elif (axesSelector == AXES_SELECTOR_X):
            node.setAttribute("axesSelector", "x")
        elif (axesSelector == AXES_SELECTOR_Y):
            node.setAttribute("axesSelector", "y")
        elif (axesSelector == AXES_SELECTOR_Z):
            node.setAttribute("axesSelector", "z")
        elif (axesSelector == AXES_SELECTOR_XY):
            node.setAttribute("axesSelector", "xy")
        elif (axesSelector == AXES_SELECTOR_XZ):
            node.setAttribute("axesSelector", "xz")
        elif (axesSelector == AXES_SELECTOR_YZ):
            node.setAttribute("axesSelector", "yz")
        
        return node