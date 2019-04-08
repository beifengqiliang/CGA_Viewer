import PySide2.QtXml
from PySide2.QtXml import QDomDocument
from PySide2.QtCore import QFile
from PySide2.QtCore import QIODevice

# 测试
def parserGrammar(filename):
	doc = QDomDocument(filename)
	file = QFile(filename)

	doc.setContent(file)
	root = doc.documentElement()
	child_node = root.firstChild()

	# 对xml文件的每个grammar节点进行分析
	while not(child_node.isNull()):
		if child_node.toElement().tagName() == "grammar" :
			grammar = Grammar()
			parseGrammar(child_node.toElement(), grammar)
			grammars.push_back(grammar)
        
		child_node = child_node.nextSibling()
    		
def parseGrammar(filename, grammar):
	file = QFile(filename)

	doc = QDomDocument()
	doc.setContent(file, true)
	root = doc.documentElement()

	parseGrammar(root, grammar)

def parseGrammar(filename, grammars):
	doc = QDomDocument(filename)
	file = QFile(filename)

	doc.setContent(file)
	root = doc.documentElement()
	child_node = root.firstChild()

	# 对xml文件的每个grammar节点进行分析
	while not(child_node.isNull()):
		if child_node.toElement().tagName() == "grammar" :
			grammar = Grammar()
			parseGrammar(child_node.toElement(), grammar)
			grammars.push_back(grammar)
			
		child_node = child_node.nextSibling()

# 对一个grammar里的attr和rule子节点进行解析
def parseGrammar(root, grammar):
	child_node = root.firstChild()
	while not(child_node.isNull()):
		if (child_node.toElement().tagName() == "attr"): 
			if not(child_node.toElement().hasAttribute("name")):
				throw("<attr> tag must contain name attribute.")
			name = child_node.toElement().attribute("name").toUtf8().constData()
			if not(child_node.toElement().hasAttribute("value")):
				throw("<attr> tag must contain value attribute.")
			value = child_node.toElement().attribute("value").toUtf8().constData()

			#std::vector<float> range;这句不懂怎么写
			if child_node.toElement().hasAttribute("range"):
				value = child_node.toElement().attribute("range").split(",")
				range.push_back(value[0].toFloat())
				range.push_back(value[1].toFloat())
			if range.size() > 0 :
				grammar.addAttr(name, Attribute(name, value, range[0], range[1]))
			else:
				grammar.addAttr(name, Attribute(name, value))
		elif (child_node.toElement().tagName() == "rule"):
			if not(child_node.toElement().hasAttribute("name")):
				throw("<rule> tag must contain name attribute.")
			name = child_node.toElement().attribute("name").toUtf8().constData()

			grammar.addRule(name)

			operator_node = child_node.firstChild()
			while not(operator_node.isNull()):
				operator_name = operator_node.toElement().tagName().toUtf8().constData()

				if operator_name == "center":
					grammar.addOperator(name, parseCenterOperator(operator_node))
				elif operator_name == "color":
					grammar.addOperator(name, parseColorOperator(operator_node))
				elif operator_name == "comp":
					grammar.addOperator(name, parseCompOperator(operator_node))
				elif operator_name == "copy":
					grammar.addOperator(name, parseCopyOperator(operator_node))
				elif operator_name == "cornerCut":
					grammar.addOperator(name, parseCornerCutOperator(operator_node))
				elif operator_name == "extrude":
					grammar.addOperator(name, parseExtrudeOperator(operator_node))
				elif operator_name == "hemisphere":
					grammar.addOperator(name, parseHemisphereOperator(operator_node))
				elif operator_name == "innerArch":
					grammar.addOperator(name, parseInnerArchOperator(operator_node))
				elif operator_name == "innerCircle":
					grammar.addOperator(name, parseInnerCircleOperator(operator_node))
				elif operator_name == "innerSemiCircle":
					grammar.addOperator(name, parseInnerSemiCircleOperator(operator_node))
				elif operator_name == "insert":
					grammar.addOperator(name, parseInsertOperator(operator_node))
				elif operator_name == "offset":
					grammar.addOperator(name, parseOffsetOperator(operator_node))
				elif operator_name == "pyramid":
					grammar.addOperator(name, parsePyramidOperator(operator_node))
				elif operator_name == "roofGable":
					grammar.addOperator(name, parseRoofGableOperator(operator_node))
				elif operator_name == "roofHip":
					grammar.addOperator(name, parseRoofHipOperator(operator_node))
				elif operator_name == "rotate":
					grammar.addOperator(name, parseRotateOperator(operator_node))
				elif operator_name == "setupProjection":
					grammar.addOperator(name, parseSetupProjectionOperator(operator_node))
				elif operator_name == "shapeL":
					grammar.addOperator(name, parseShapeLOperator(operator_node))
				elif operator_name == "shapeU":
					grammar.addOperator(name, parseShapeUOperator(operator_node))
				elif operator_name == "size":
					grammar.addOperator(name, parseSizeOperator(operator_node))
				elif operator_name == "split":
					grammar.addOperator(name, parseSplitOperator(operator_node))
				elif operator_name == "taper":
					grammar.addOperator(name, parseTaperOperator(operator_node))
				elif operator_name == "texture":
					grammar.addOperator(name, parseTextureOperator(operator_node))
				elif operator_name == "translate":
					grammar.addOperator(name, parseTranslateOperator(operator_node))

				operator_node = operator_node.nextSibling()

		child_node = child_node.nextSibling()

def parseCenterOperator(node):
	#int axesSelector;

	if not(node.toElement().hasAttribute("axesSelector")):
		throw("center node has to have axesSelector attribute.")
	
	if node.toElement().attribute("axesSelector") == "xyz":
		axesSelector = AXES_SELECTOR_XYZ
	elif node.toElement().attribute("axesSelector") == "x":
		axesSelector = AXES_SELECTOR_X
	elif node.toElement().attribute("axesSelector") == "y":
		axesSelector = AXES_SELECTOR_Y
	elif node.toElement().attribute("axesSelector") == "z":
		axesSelector = AXES_SELECTOR_Z
	elif node.toElement().attribute("axesSelector") == "xy":
		axesSelector = AXES_SELECTOR_XY
	elif node.toElement().attribute("axesSelector") == "xz":
		axesSelector = AXES_SELECTOR_XZ
	else:
		axesSelector = AXES_SELECTOR_YZ

	return (CenterOperator(axesSelector))

def parseColorOperator(node):
	#std::string r;
	#std::string g;
	#std::string b;
	#std::string s;

	if node.toElement().hasAttribute("r"):
		r = node.toElement().attribute("r").toUtf8().constData()
	if node.toElement().hasAttribute("g"):
		g = node.toElement().attribute("g").toUtf8().constData()
	if node.toElement().hasAttribute("b"):
		b = node.toElement().attribute("b").toUtf8().constData()
	if node.toElement().hasAttribute("s"):
		s = node.toElement().attribute("s").toUtf8().constData()

	if s.empty():
		return (ColorOperator(r, g, b))
	else:
		return (ColorOperator(s))

def parseCompOperator(node):
	#std::string front_name;
	#std::string side_name;
	#std::string top_name;
	#std::string bottom_name;
	#std::string inside_name;
	#std::string border_name;
	#std::string vertical_name;
	#std::map<std::string, std::string> name_map;

	child = node.firstChild()
	while not(child.isNull()):
		if child.toElement().tagName() == "param":
			name = child.toElement().attribute("name")
			value = child.toElement().attribute("value").toUtf8().constData()

			if name == "front":
				name_map["front"] = value
			elif name == "right":
				name_map["right"] = value
			elif name == "left":
				name_map["left"] = value
			elif name == "back":
				name_map["back"] = value
			elif name == "side":
				name_map["side"] = value
			elif name == "top":
				name_map["top"] = value
			elif name == "bottom":
				name_map["bottom"] = value
			elif name == "inside":
				name_map["inside"] = value
			elif name == "border":
				name_map["border"] = value
			elif name == "vertical":
				name_map["vertical"] = value

		child = child.nextSibling()
	
	return (CompOperator(name_map))

def parseCopyOperator(node):
	if not(node.toElement().hasAttribute("name")):
		throw("copy node has to have name attribute.")

	copy_name = node.toElement().attribute("name").toUtf8().constData()

	return (CopyOperator(copy_name))

def parseCornerCutOperator(node):
	if not(node.toElement().hasAttribute("type")):
		throw("curnerCut node has to have type attribute.")
	#int type;
	if (node.toElement().attribute("type") == "straight"):
		type = CORNER_CUT_STRAIGHT
	elif (node.toElement().attribute("type") == "curve"):
		type = CORNER_CUT_CURVE
	else:
		type = CORNER_CUT_NEGATIVE_CURVE

	if not(node.toElement().hasAttribute("length")):
		throw("curnerCut node has to have length attribute.")

	length = node.toElement().attribute("length").toUtf8().constData()

	return (CornerCutOperator(type, length))

def parseExtrudeOperator(node):
	if not(node.toElement().hasAttribute("height")):
		throw("extrude node has to have height attribute.")
	
	height = node.toElement().attribute("height").toUtf8().constData()

	return (ExtrudeOperator(height))

def parseHemisphereOperator(node):
	return (HemisphereOperator())

def parseInnerArchOperator(node):
	inside = node.toElement().attribute("inside").toUtf8().constData()
	border = node.toElement().attribute("border").toUtf8().constData()

	return (InnerArchOperator(inside, border))

def parseInnerCircleOperator(node):
	return (InnerCircleOperator())

def parseInnerSemiCircleOperator(node):
	return (InnerSemiCircleOperator())

def parseInsertOperator(node):
	if not(node.toElement().hasAttribute("geometryPath")):
		throw("insert node has to have geometryPath attribute.")

	geometryPath = node.toElement().attribute("geometryPath").toUtf8().constData()

	return (InsertOperator(geometryPath))

def parseOffsetOperator(node):
	if not(node.toElement().hasAttribute("offsetDistance")):
		throw("offset node has to have offsetDistance attribute.")

	offsetDistance = node.toElement().attribute("offsetDistance").toUtf8().constData()
	inside = node.toElement().attribute("inside").toUtf8().constData()
	border = node.toElement().attribute("border").toUtf8().constData()

	return (OffsetOperator(offsetDistance, inside, border))

def parsePyramidOperator(node):
	if not(node.toElement().hasAttribute("height")):
		throw("pyramid node has to have height attribute.")

	height = node.toElement().attribute("height").toUtf8().constData()

	return (PyramidOperator(height))

def parseRoofGableOperator(node):
	if not(node.toElement().hasAttribute("angle")):
		throw("roofGable node has to have angle attribute.")
		
	angle = node.toElement().attribute("angle").toUtf8().constData()

	return (RoofGableOperator(angle))

def parseRoofHipOperator(node):
	if not(node.toElement().hasAttribute("angle")):
		throw("roofHip node has to have angle attribute.")

	angle = node.toElement().attribute("angle").toUtf8().constData()

	return (RoofHipOperator(angle))

def parseRotateOperator(node):
	#float xAngle = 0.0f;
	#float yAngle = 0.0f;
	#float zAngle = 0.0f;

	child = node.firstChild()
	while not(child.isNull()):
		if (child.toElement().tagName() == "param"):
			name = child.toElement().attribute("name")

			if (name == "xAngle"):
				xAngle = child.toElement().attribute("value").toFloat()
			elif (name == "yAngle"):
				yAngle = child.toElement().attribute("value").toFloat()
			elif (name == "zAngle"):
				zAngle = child.toElement().attribute("value").toFloat()
				
		child = child.nextSibling()

	return (RotateOperator(xAngle, yAngle, zAngle))

def parseSetupProjectionOperator(node):
	if not(node.toElement().hasAttribute("axesSelector")):
		throw("setupProjection node has to have axesSelector attribute.")
		
	#int axesSelector;
	sAxesSelector = node.toElement().attribute("axesSelector").toUtf8().constData()
	if (sAxesSelector == "scope.xy"):
		axesSelector = AXES_SCOPE_XY
	elif (sAxesSelector == "scope.xz"):
		axesSelector = AXES_SCOPE_XZ
	else:
		axesSelector = AXES_SCOPE_XY

	#Value texWidth;
	#Value texHeight;

	child = node.firstChild()
	while not(child.isNull()):
		if (child.toElement().tagName() == "param"):
			name = child.toElement().attribute("name")

			if (name == "texWidth"):
				type =  child.toElement().attribute("type").toUtf8().constData()
				value =  child.toElement().attribute("value").toUtf8().constData()
				if (type == "absolute"):
					texWidth = Value(Value.TYPE_ABSOLUTE, value)
				elif (type == "relative"):
					texWidth = Value(Value.TYPE_RELATIVE, value)
				else:
					throw("type of texWidth for texture has to be either absolute or relative.")
			elif (name == "texHeight"):
				type =  child.toElement().attribute("type").toUtf8().constData()
				value =  child.toElement().attribute("value").toUtf8().constData()
				if (type == "absolute"):
					texHeight = Value(Value.TYPE_ABSOLUTE, value)
				elif (type == "relative"):
					texHeight = Value(Value.TYPE_RELATIVE, value)
				else:
					throw("type of texHeight for texture has to be either absolute or relative.")

		child = child.nextSibling()

	return (SetupProjectionOperator(axesSelector, texWidth, texHeight))

def parseShapeLOperator(node):
	#Value frontWidth;
	#Value rightWidth;
	#bool frontWidthFound = false;
	#bool rightWidthFound = false;

	child = node.firstChild()
	while not(child.isNull()):
		if (child.toElement().tagName() == "param"):
			name = child.toElement().attribute("name")
			#QString type;

			if not(child.toElement().hasAttribute("type")):
				throw("param node under size node has to have type attribute.")

			type = child.toElement().attribute("type")
			value = child.toElement().attribute("value").toUtf8().constData()

			if (name == "frontWidth"):
				frontWidthFound = true
				if (type == "relative"):
					frontWidth = Value(Value.TYPE_RELATIVE, value)
				elif (type == "absolute"):
					frontWidth = Value(Value.TYPE_ABSOLUTE, value)
				else:
					throw("type attribute under shapeL node has to be either relative or absolute.")
			elif (name == "rightWidth"):
				rightWidthFound = true
				if (type == "relative"):
					rightWidth = Value(Value.TYPE_RELATIVE, value)
				elif (type == "absolute"):
					rightWidth = Value(Value.TYPE_ABSOLUTE, value)
				else:
					throw("type attribute under shapeL node has to be either relative or absolute.")

		child = child.nextSibling()

	if not(frontWidthFound):
		throw("shapeL node has to have frontWidth parametter.")
	if not(rightWidthFound):
		throw("shapeL node has to have rightWidth parametter.")

	return (ShapeLOperator(frontWidth, rightWidth))

def parseShapeUOperator(node):
	#Value frontWidth;
	#Value backDepth;
	#bool frontWidthFound = false;
	#bool backDepthFound = false;

	child = node.firstChild()
	while not(child.isNull()):
		if (child.toElement().tagName() == "param"):
			name = child.toElement().attribute("name")
			#QString type;

			if not(child.toElement().hasAttribute("type")):
				throw("param node under size node has to have type attribute.")

			type = child.toElement().attribute("type")
			value = child.toElement().attribute("value").toUtf8().constData()

			if (name == "frontWidth"):
				frontWidthFound = true
				if (type == "relative"):
					frontWidth = Value(Value.TYPE_RELATIVE, value)
				elif (type == "absolute"):
					frontWidth = Value(Value.TYPE_ABSOLUTE, value)
				else:
					throw("type attribute under shapeU node has to be either relative or absolute.")
			elif (name == "backDepth"):
				backDepthFound = true
				if (type == "relative"):
					backDepth = Value(Value.TYPE_RELATIVE, value)
				elif (type == "absolute"):
					backDepth = Value(Value.TYPE_ABSOLUTE, value)
				else:
					throw("type attribute under shapeU node has to be either relative or absolute.")

		child = child.nextSibling()

	if not(frontWidthFound):
		throw("shapeU node has to have frontWidth parametter.")
	if not(backDepthFound):
		throw("shapeU node has to have backDepth parametter.")

	return (ShapeUOperator(frontWidth, backDepth))

def parseSizeOperator(node):
	#Value xSize;
	#Value ySize;
	#Value zSize;
	#bool centered = false;

	if (node.toElement().hasAttribute("centered")):
		if (node.toElement().attribute("centered") == "true"):
			centered = true

	child = node.firstChild()
	while not(child.isNull()):
		if (child.toElement().tagName() == "param"):
			name = child.toElement().attribute("name")
			#QString type;

			if not(child.toElement().hasAttribute("type")):
				throw("param node under size node has to have type attribute.")

			type = child.toElement().attribute("type")
			value = child.toElement().attribute("value").toUtf8().constData()

			if (name == "xSize"):
				if (type == "relative"):
					xSize = Value(Value.TYPE_RELATIVE, value)
				elif (type == "absolute"):
					xSize = Value(Value.TYPE_ABSOLUTE, value)
				else:
					throw("type attribute under size node has to be either relative or absolute.")
			elif (name == "ySize"):
				if (type == "relative"):
					ySize = Value(Value.TYPE_RELATIVE, value)
				elif (type == "absolute"):
					ySize = Value(Value.TYPE_ABSOLUTE, value)
				else:
					throw("type attribute under size node has to be either relative or absolute.")
			elif (name == "zSize"):
				if (type == "relative"):
					zSize = Value(Value.TYPE_RELATIVE, value)
				elif (type == "absolute"):
					zSize = Value(Value.TYPE_ABSOLUTE, value)
				else:
					throw("type attribute under size node has to be either relative or absolute.")

		child = child.nextSibling()

	return (SizeOperator(xSize, ySize, zSize, centered))

def parseSplitOperator(node):
	#int splitAxis;
	#std::vector<Value> sizes;
	#std::vector<std::string> names;

	if not(node.toElement().hasAttribute("splitAxis")):
		throw("split node has to have splitAxis attribute.")
	if (node.toElement().attribute("splitAxis") == "x"):
		splitAxis = DIRECTION_X
	elif (node.toElement().attribute("splitAxis") == "y"):
		splitAxis = DIRECTION_Y
	else:
		splitAxis = DIRECTION_Z

	child = node.firstChild()
	while not(child.isNull()):
		if (child.toElement().tagName() == "param"):
			type = child.toElement().attribute("type")
			value = child.toElement().attribute("value").toUtf8().constData()
			repeat = false
			if (child.toElement().hasAttribute("repeat")):
				repeat = true

			if (repeat):
				if (type == "absolute"):
					sizes.push_back(Value(Value.TYPE_ABSOLUTE, value, true))
				elif (type == "relative"):
					sizes.push_back(Value(Value.TYPE_RELATIVE, value, true))
				else:
					sizes.push_back(Value(Value.TYPE_FLOATING, value, true))
			else:
				if (type == "absolute"):
					sizes.push_back(Value(Value.TYPE_ABSOLUTE, value))
				elif (type == "relative"):
					sizes.push_back(Value(Value.TYPE_RELATIVE, value))
				else:
					sizes.push_back(Value(Value.TYPE_FLOATING, value))
			
			names.push_back(child.toElement().attribute("name").toUtf8().constData())

		child = child.nextSibling()

	return (SplitOperator(splitAxis, sizes, names))

def parseTaperOperator(node):
	if not(node.toElement().hasAttribute("height")):
		throw("taper node has to have height attribute.")
	if not(node.toElement().hasAttribute("slope")):
		throw("taper node has to have slope attribute.")

	height = node.toElement().attribute("height").toUtf8().constData()
	slope = node.toElement().attribute("slope").toUtf8().constData()

	return (TaperOperator(height, slope))

def parseTextureOperator(node):
	if not(node.toElement().hasAttribute("texturePath")):
		throw("texture node has to have texturePathtexturePath attribute.")

	texture = node.toElement().attribute("texturePath").toUtf8().constData()

	return (TextureOperator(texture))

def parseTranslateOperator(node):
	#int mode;
	#int coordSystem;
	#Value x;
	#Value y;
	#Value z;

	if not(node.toElement().hasAttribute("mode")):
		throw("translate node has to have mode attribute.")
	if (node.toElement().attribute("mode") == "abs"):
		mode = MODE_ABSOLUTE
	elif (node.toElement().attribute("mode") == "rel"):
		mode = MODE_RELATIVE
	else:
		throw("mode has to be either abs or rel.")

	if not(node.toElement().hasAttribute("coordSystem")):
		throw("translate node has to have coordSystem attribute.")
	if (node.toElement().attribute("coordSystem") == "world"):
		coordSystem = COORD_SYSTEM_WORLD
	elif (node.toElement().attribute("coordSystem") == "object"):
		coordSystem = COORD_SYSTEM_OBJECT
	else:
		throw("coordSystem has to be either world or object.")

	child = node.firstChild()
	while not(child.isNull()):
		if (child.toElement().tagName() == "param"):
			if not(child.toElement().hasAttribute("name")):
				throw("param has to have name attribute.")
			name = child.toElement().attribute("name").toUtf8().constData()
			if not(child.toElement().hasAttribute("value")):
				throw("param has to have value attribute.")
			value = child.toElement().attribute("value").toUtf8().constData()
			if not(child.toElement().hasAttribute("type")):
				throw("param has to have type attribute.")
			type = child.toElement().attribute("type").toUtf8().constData()

			if (name == "x"):
				if (type == "absolute"):
					x = Value(Value.TYPE_ABSOLUTE, value)
				elif (type == "relative"):
					x = Value(Value.TYPE_RELATIVE, value)
				else:
					throw("type of param for translate has to be either absolute or relative.")
			elif (name == "y"):
				if (type == "absolute"):
					y = Value(Value.TYPE_ABSOLUTE, value)
				elif (type == "relative"):
					y = Value(Value.TYPE_RELATIVE, value)
				else:
					throw("type of param for translate has to be either absolute or relative.")
			elif (name == "z"):
				if (type == "absolute"):
					z = Value(Value.TYPE_ABSOLUTE, value)
				elif (type == "relative"):
					z = Value(Value.TYPE_RELATIVE, value)
				else:
					throw("type of param for translate has to be either absolute or relative.")
			
		child = child.nextSibling()

	return TranslateOperator(mode, coordSystem, x, y, z)