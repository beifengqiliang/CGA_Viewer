
class TextureOperator:
    def __init__(self, texture):
        self.name = "texture"
        self.texture = texture
        
    def apply(self, shape, grammar, stack):
        shape.texture(grammar.evalString(texture, shape))
        return shape

    def toXml(self, doc):
        node = doc.createElement(name.c_str())
        node.setAttribute("texturePath", texture.c_str())
        
        return node