from xml.dom import minidom


class readXML:

    def readTestDataFromXML(self, nodeName):

        xmlobj = minidom.parse("C:/Users/00004999/PycharmProjects/robot scripts/pythonProject/Day1PythonProgramming/TestDir/ReadfromXML.xml")
        mydatavalue = xmlobj.getElementsByTagName(nodeName)[0]
        return mydatavalue.firstChild.data

obj = readXML()
print(obj.readTestDataFromXML("userEmail"))