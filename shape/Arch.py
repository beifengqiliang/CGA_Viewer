
class Arch:
    def __init__(self, name, grammar_type, pivot, modelMat, width, height, color):
        self._active = true
        self._axiom = false
        self._name = name
        self._grammar_type = grammar_type
        self._pivot = pivot
        self._modelMat = modelMat
        self._scope = vec3(width, height, 0)
        self._color = color
        self._textureEnabled = false

    def __init__(self, name, grammar_type, pivot, modelMat, width, height, color, texture, u1, v1, u2, v2):
        self._active = true
        self._axiom = false
        self._name = name
        self._grammar_type = grammar_type
        self._pivot = pivot
        self._modelMat = modelMat
        self._scope = vec3(width, height, 0)
        self._color = color
        self._texture = texture
        
        _texCoords.resize(4)
        _texCoords[0] = glm::vec2(u1, v1)
        _texCoords[1] = glm::vec2(u2, v1)
        _texCoords[2] = glm::vec2(u2, v2)
        _texCoords[3] = glm::vec2(u1, v2)
        self._textureEnabled = true