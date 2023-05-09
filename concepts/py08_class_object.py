class Student:
    # class variable
    branch = "cse"

    # private class variable
    __college_name = "iit"

    def __init__(self, roll_no=1112, name="anand", age=25):
        # instance variable
        self.roll_no = roll_no
        self.name = name
        # private instance variable
        self.__age = age
        print("in constructor of Student class")

    def get_student_id(self):
        return self.roll_no

    @staticmethod
    def print_college_name():
        print(Student.__college_name)


def main_method():
    std = Student()
    print(std.get_student_id())
    print(std.__dict__)
    print(Student.branch)
    Student.print_college_name()


if __name__ == "__main__":
    main_method()
