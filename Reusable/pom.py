from xml.dom import minidom
from pathlib import Path


def PopularCoursesSubLinksXpath(linkName):
    return "//h4[text()='Popular Courses']/following-sibling::p[1]/a[text()='" + linkName + "']"


def readXML(node_name):
    myxmlDoc = minidom.parse(str(Path(__file__).parent.parent) + "/Day7Xml.xml")
    test_Data = myxmlDoc.getElementsByTagName(node_name)[0]
    return test_Data.firstChild.data

def myImagePath(imageName):
    path = str(Path(__file__).parent.parent)+"/"+imageName
    return path

def FleekTopMenuBars(linkName):
    return "//nav[@class='main_menu drop_down right']/ul/li/a/span[text()='"+linkName+"']"


def ServicessubMenuOption(linkName):
    return "(//span[text()='"+linkName+"'])[1]"
