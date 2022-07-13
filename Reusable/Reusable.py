from xml.dom import minidom
from pathlib import Path


def readXmlTestData(nodeName):

    myxmlDoc = minidom.parse(str(Path(__file__).parent.parent)+"/testDataweb.xml")
    data = myxmlDoc.getElementsByTagName(nodeName)[0]
    return data.firstChild.data




