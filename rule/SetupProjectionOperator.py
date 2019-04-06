
class SetupProjectionOperator:
    def __init__(self, axesSelector, texWidth, texHeight):
        self.name = "setupProjection"
        self.axesSelector = axesSelector
        self.texWidth = texWidth
        self.texHeight = texHeight
        
    def apply(self, shape, grammar, stack):
        # float actual_texWidth;
        # float actual_texHeight;

	    if (texWidth.type == Value.TYPE_RELATIVE):
            actual_texWidth = shape._scope.x * grammar.evalFloat(texWidth.value, shape)
        else:
            actual_texWidth = grammar.evalFloat(texWidth.value, shape)
        
	    if (texHeight.type == Value.TYPE_RELATIVE):
            actual_texHeight = shape._scope.y * grammar.evalFloat(texHeight.value, shape)
        else:
            actual_texHeight = grammar.evalFloat(texHeight.value, shape)
            
        shape.setupProjection(axesSelector, actual_texWidth, actual_texHeight)
        
        return shape
        
    def toXml(self, doc):
        node = doc.createElement(name.c_str())
        
        if (axesSelector == AXES_SCOPE_XY):
            node.setAttribute("axesSelector", "scope.xy")
        elif (axesSelector == AXES_SCOPE_XZ):
            node.setAttribute("axesSelector", "scope.xz")
        elif (axesSelector == AXES_SCOPE_YZ):
            node.setAttribute("axesSelector", "scope.yz")
        
        child1 = texWidth.toXml(doc)
        child1.setAttribute("name", "texWidth")
        node.appendChild(child1)
        
        child2 = texHeight.toXml(doc)
        child2.setAttribute("name", "texHeight")
        node.appendChild(child2)
        
        return node