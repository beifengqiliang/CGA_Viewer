
class Circle:
    def __init__(self, name, grammar_type, pivot, modelMat, width, height, color):
        self._active = true
        self._axiom = false
        self._name = 
        self._grammar_type = grammar_type
        self._pivot = pivot
        self._modelMat = modelMat
        self._scope = glm::vec3(width, height, 0)
        self._color = color
        self._textureEnabled = false
        
    def clone(self, name):
        copy = Shape(new Circle(*this))
        copy._name = name
        return copy

    def extrude(self, name, height):
        return Shape(new Cylinder(name, _grammar_type, _pivot, _modelMat, _scope.x, _scope.y, height, _color))

    def hemisphere(self, name):
        return Shape(new Hemisphere(name, _grammar_type, _pivot, _modelMat, _scope.x, _scope.y, _color))
        
    def offset(self, name, offsetDistance, inside, border, shapes):
        # inner shape
        if not(inside.empty()):
            mat = translate(_modelMat, glm::vec3(-offsetDistance, -offsetDistance, 0))
        
        shapes.push_back(Shape(new Circle(inside, _grammar_type, _pivot, mat, _scope.x + offsetDistance * 2, _scope.y + offsetDistance * 2, _color)))

	    # border shape
	    if not(border.empty()):
            for i in range(i, CIRCLE_SLICES, 1):
                theta1 = (float)i / CIRCLE_SLICES * M_PI * 2.0
			    theta2 = (float)(i + 1) / CIRCLE_SLICES * M_PI * 2.0

			    # std::vector<glm::vec2> pts
			    # pts.push_back(glm::vec2(cosf(theta1) * _scope.x * 0.5 + _scope.x * 0.5, sinf(theta1) * _scope.y * 0.5 + _scope.y * 0.5));
			    # pts.push_back(glm::vec2(cosf(theta2) * _scope.x * 0.5 + _scope.x * 0.5, sinf(theta2) * _scope.y * 0.5 + _scope.y * 0.5));
			    # pts.push_back(glm::vec2(cosf(theta2) * (_scope.x * 0.5 + offsetDistance) + _scope.x * 0.5, sinf(theta2) * (_scope.y * 0.5 + offsetDistance) + _scope.y * 0.5));
			    # pts.push_back(glm::vec2(cosf(theta1) * (_scope.x * 0.5 + offsetDistance) + _scope.x * 0.5, sinf(theta1) * (_scope.y * 0.5 + offsetDistance) + _scope.y * 0.5));
			    # shapes.push_back(boost::shared_ptr<Shape>(new Polygon(border, _grammar_type, _pivot, _modelMat, pts, _color, _texture)));
		