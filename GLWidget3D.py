from PyQt5.QtCore import QObject
from rule.GrammarParser import parserGrammar

import PySide2.QtXml
from PySide2.QtXml import QDomDocument
from PySide2.QtCore import QFile
from PySide2.QtCore import QIODevice

class GLWidget3D(QObject):
  
    def loadCGA(self, filename):
        parserGrammar(filename)
        # start = boost::shared_ptr<cga::Shape>(new cga::Rectangle("Start", "", glm::translate(glm::rotate(glm::mat4(), -(float)CV_PI * 0.5f, glm::vec3(1, 0, 0)), glm::vec3(0, 0, 0)), glm::mat4(), 0, 0, glm::vec3(1, 1, 1)));
	    # system.stack.push_back(boost::shared_ptr<cga::Shape>(start));

        #grammars = Grammar()
        # 对xml文件进行解析
        #parseGrammar(filename, grammars)


if __name__ == "__main__":

    gl = GLWidget3D()
    filename = "test.xml"
    gl.loadCGA(filename)