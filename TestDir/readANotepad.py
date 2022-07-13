# \Users\00004999\PycharmProjects\robot scripts\pythonProject\Day1PythonProgramming\TestDir\readANotepad.txt

class ReadNotepad:

    def readingANotepad(self):
        a = open("C:/Users/00004999/PycharmProjects/robot scripts/pythonProject/Day1PythonProgramming/TestDir/readANotepad.txt", "r")
        print(a.read())

    def appendingANotepad(self, myappendLine):
        a = open("C:/Users/00004999/PycharmProjects/robot scripts/pythonProject/Day1PythonProgramming/TestDir/readANotepad.txt", "a")
        a.write(myappendLine)
        a.close()


obj = ReadNotepad()
obj.readingANotepad()
obj.appendingANotepad("Tomorrow will be learning Selenium xpath and CSS")
# obj.appendToNoteToInteger(50)

"""

class ReadNotepad:

    def ReadFromNotePad1(self): a = open("C:/Users/00004999/PycharmProjects/robot 
    scripts/pythonProject/Day1PythonProgramming/TestDir/readANotepad.txt", "r") print(a.read()) 

    def appendToNote(self, mappedLine): a = open("C:/Users/00004999/PycharmProjects/robot 
    scripts/pythonProject/Day1PythonProgramming/TestDir/readANotepad.txt", "a") a.write(mappedLine) a.close() 

    def appendToNoteToInteger(self, FinalValue): for x in range(FinalValue): a = open(
    "C:/Users/00004999/PycharmProjects/robot scripts/pythonProject/Day1PythonProgramming/TestDir/readANotepad.txt", 
    "a") a.write(str(x)) a.close() 

obj = ReadNotepad()
#obj.ReadFromNotePad1()
#obj.appendToNote("Tomorrow will start selenium xpath")
obj.appendToNoteToInteger(50)

"""
