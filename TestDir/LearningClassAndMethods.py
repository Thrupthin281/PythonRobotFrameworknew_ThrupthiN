class TestClass:

    a = 5
    x = "Mobile"

    def myTestmethodName(self, frameworkName):

        print(frameworkName+ ""+"Framework")

    def AddTwoNumbers(self, a, b):
        print(a+b)

    def HowToUseReturnStatement(self, a, b):

        if a > b:
            x = "Computer"
        else:
            x = "Laptop"

        return x

obj = TestClass ()
obj.myTestmethodName("Testing Robot")
obj.AddTwoNumbers(5, 5)
print(obj.HowToUseReturnStatement(10, 4))
print(obj.HowToUseReturnStatement(4, 40))