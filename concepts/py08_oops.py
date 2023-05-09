"""
POINT-1 : you can't overload constructor in python,
for getting the same feature use default value.

NOTE-1 :
    We can create instance variable inside a method also , and
    it will be available for that instance , if that variable is not
    instantiated it will throw exception.
    Advised to declare all instance variable in init only

NOTE-2 :


"""


class ParentClass:
    # Class Variable
    data_id = 1000

    # Hidden member of MyClass
    __hiddenVariable = 0

    # init method or constructor
    def __init__(self, emp_id="1112", emp_name="Anand"):
        # Instance Variable
        self.emp_id = emp_id
        self.emp_name = emp_name
        # setting class variable value in constructor
        self.data_id = 1234
        print("base class constructor")

    # A member method that changes
    # __hiddenVariable
    def add(self, increment):
        self.__hiddenVariable += increment
        print (self.__hiddenVariable)

    # Sample Method
    def method1(self):
        print("base class : method1(), hello ", self.emp_name)

    def set_instance_var(self, argument):
        self.argument = argument
        print("base class : setInstanceVar(), hello " + str(self.emp_id) + " " + argument)


class ChildClass(ParentClass):
    def __init__(self):
        super(ChildClass, self).__init__()
        print("child class constructor")

    def method2(self):
        print("child class : method2(), hello " + self.emp_name + " " + str(self.emp_id))


class ChildClass1(ParentClass):
    pass


def main():
    # exercise the class methods
    print("=========== Base class ==================")
    parent = ParentClass(1122, "Patel")
    parent.method1()
    print("Class Variable :",ParentClass.data_id)
    print("Class Variable using instance :", parent.data_id)
    print("Instance Variable1 :", parent.emp_id)
    parent.set_instance_var("kumar")
    print("Instance Variable2 :", parent.argument)
    print("private variable change")
    parent.add(11);
    parent.add(11);
    print("=========== Child class 1==================")
    child = ChildClass()
    child.method2()
    print(child.__dict__)

    print("=========== Child class 2==================")
    child = ChildClass()
    child.method2()
    print(child.__dict__)

    # deleting object properties
    del parent.emp_id
    # print(parent.emp_id)
    # deleting object
    del parent
    # print(parent)

    child1 = ChildClass1()
    child1.method1()


if __name__ == "__main__":
    main()
