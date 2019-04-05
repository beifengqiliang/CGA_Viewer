
class Attribute:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.hasRange = false

    def __init__(self, name, value, range_start, range_end):
        self.name = name
        self.value = value
        self.hasRange = true
        self.range_start = range_start
        self.range_end = range_end
    
class Value:
    def getEstimateValue(self, size, grammar, shape):
        if (type == Value.TYPE_ABSOLUTE):
            return grammar.evalFloat(value, shape)
        elif (type == Value.TYPE_RELATIVE):
            return grammar.evalFloat(value, shape) * size
        else:
            return grammar.evalFloat(value, shape)

    def toXml(self, doc):
		# QDomElement对象代表整个XML文档
        node = doc.createElement("param")
		
		if (type == TYPE_ABSOLUTE):
			node.setAttribute("type", "absolute")
		elif (type == TYPE_RELATIVE):
			node.setAttribute("type", "relative")
		elif (type == TYPE_FLOATING):
			node.setAttribute("type", "floating")
		
		node.setAttribute("value", value.c_str())
		
		if (repeat):
			node.setAttribute("repeat", "true")
		
		return node

class Rule:
    def apply(self, shape, grammar, stack, shapes):
        # 将此规则应用于指定的形状。
        # 某些操作（例如comp和split）将应用的形状存储在堆栈中
        for i in range(0, operators.size(), 1):
            shape = operators[i].apply(shape, grammar, stack)
		    if (shape == NULL) break
	
	    if (shape != NULL):
		    if (operators.size() == 0 or operators.back().name == "copy"):
			    # 如果它以copy结束，则不再需要此shape
			    shape._active = false
			    shapes.push_back(shape)
		    else:
			    # 如果它不以copy结束，则需要绘制此shape
			    # 存储在shapes栈中
			    shape._active = true
			    shapes.push_back(shape)

    def decodeSplitSizes(self, size, sizes, output_names, grammar, shape, decoded_sizes, decoded_output_names):
        # 在指定split大小后计算每个片段的大小

        # float regular_sum = 0.0f;
	    # float floating_sum = 0.0f;
	    # int repeat_count = 0;
	    # float repeat_unit = 0.0f;
	    # int repeat_num = 0;
	    # float repeat_scale = 1.0f;

	    for i in range(0, sizes.size(), 1):
		    if (sizes[i].repeat):
			    repeat_count += 1
		
		    else:
			    if (sizes[i].type == Value.TYPE_ABSOLUTE):
				    regular_sum += grammar.evalFloat(sizes[i].value, shape)
			    elif (sizes[i].type == Value.TYPE_RELATIVE):
				    regular_sum += size * grammar.evalFloat(sizes[i].value, shape)
			    elif (sizes[i].type == Value.TYPE_FLOATING):
				    floating_sum += grammar.evalFloat(sizes[i].value, shape)
		floating_scale = 1.0
        if (floating_sum > 0 and repeat_count == 0):
            floating_scale = std::max(0.0, size - regular_sum) / floating_sum

	    if (repeat_count > 0):
            for i in range(0, sizes.size(), 1):
			    if (sizes[i].repeat):
				    repeat_unit += sizes[i].getEstimateValue(size - regular_sum - floating_sum * floating_scale, grammar, shape)
		    repeat_num = std.max(0.0, (size - regular_sum - floating_sum * floating_scale) / repeat_unit + 0.5)
		    if (repeat_num == 0):
			    if (size - regular_sum - floating_sum * floating_scale > 0):
				    repeat_num = 1
		    if (repeat_num > 0):
			repeat_scale = std.max(0.0, (size - regular_sum - floating_sum * floating_scale) / (float)repeat_num / repeat_unit)
		    if (floating_sum > 0):
			    floating_scale = std.max(0.0, size - regular_sum - repeat_unit * repeat_scale * repeat_num) / floating_sum)
	    for i in range(0, sizes.size(), 1):
		    if (sizes[i].repeat):
			    s = sizes[i].getEstimateValue(size - regular_sum - floating_sum * floating_scale, grammar, shape)
			    s *= repeat_scale
			    for k in range(0, repeat_num, 1):
				    decoded_sizes.push_back(s)
				    decoded_output_names.push_back(output_names[i])
		    else:
			    if (sizes[i].type == Value.TYPE_ABSOLUTE):
				    decoded_sizes.push_back(grammar.evalFloat(sizes[i].value, shape))
				    decoded_output_names.push_back(output_names[i])
			    elif (sizes[i].type == Value.TYPE_RELATIVE):
				    decoded_sizes.push_back(grammar.evalFloat(sizes[i].value, shape) * size)
				    decoded_output_names.push_back(output_names[i])
			    elif (sizes[i].type == Value.TYPE_FLOATING):
				    decoded_sizes.push_back(grammar.evalFloat(sizes[i].value, shape) * floating_scale)
				    decoded_output_names.push_back(output_names[i])

class Grammar:

	def contain(self, name):
		if (rules.find(name) == rules.end()):
			return false
		else:
			return true

    def addAttr(self, name, value):
		attrs[name] = value

    def addRule(self, name):
		rules[name].operators.clear()

	def addOperator(self, name, op):
		rules[name].operators.push_back(op)

	def evalFloat(self, attr_name, shape):
	    # myeval::calculator<std::string::const_iterator> calc;

	    # myeval::variables.clear();
	    # myeval::variables.add("scope.sx", shape->_scope.x);
	    # myeval::variables.add("scope.sy", shape->_scope.y);
	    # myeval::variables.add("scope.sz", shape->_scope.z);

	    it = attrs.begin()
		while (it != attrs.end()):
		    # float val;
		    if (sscanf(it.second.value.c_str(), "%f", val) != EOF):
			    myeval.variables.add(it.first, val)
			it += 1

	    # float result;
	    iter = attr_name.begin()
	    end = attr_name.end()
	    r = phrase_parse(iter, end, calc, result)
	    if (r and iter == end):
			return result
		else:
			rest(iter, end)
		    print("Parsing failed\n")
		    print("stopped at: \": " + rest + "\"\n")
		    throw("Parsing failed\nstpped at: \": " + rest + "\"\n")

	def evalString(self, attr_name, shape):
	    if (attrs.find(attr_name) == attrs.end()):
		    return attr_name
	    else:
			return attrs.at(attr_name).value
