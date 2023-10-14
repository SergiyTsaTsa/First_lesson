#######################
# Створити ієрархію класів для опису академії.
# Cписок класів: Person, Student group, Student, Subject, Academy, Teacher,
# Продумати архітектуру: реалізувати принципи ООП

class Person:
    __name = None
    __age = None
    __id_number = None

    def __init__(self, name, age, id_number):
        self.__name = name
        self.__age = age
        self.__id_number = id_number

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if 2 < len(name) < 20:
            self.__name = name
        else:
            print("Incorrect name length!")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 15 < age < 100:
            self.__age = age
        else:
            print("Incorrect age!")

    @property
    def id_number(self):
        return self.__id_number

    @id_number.setter
    def id_number(self, id_number):
        if 8 < id_number < 16:
            self.__id_number = id_number
        else:
            print("Incorrect id_number!")

    def get_name(self):
        print(f"Name: {self.__name} Age: {self.__age} Id_number: {self.__id_number}")


class Teacher(Person):
    __last_name = None
    __subject = None

    def __init__(self, name, last_name, age, id_number, subject):
        super().__init__(name, age, id_number)
        self.__subject = subject
        self.__last_name = last_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        if 2 < len(last_name) < 20:
            self.__last_name = last_name
        else:
            print("Incorrect last_name!")

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject):
        if 2 < len(subject) < 50:
            self.__subject = subject
        else:
            print("Incorrect subject!")

    def teach(self):
        print(f"{self.name} {self.__last_name} {self.__age} {self.__id_number} is teaching {self.__subject}.")


class Student(Person):
    __student_group = None

    def __init__(self, name, age, id_number, student_group):
        super().__init__(name, age, id_number)
        self.__student_group = student_group

    @property
    def student_group(self):
        return self.__student_group

    @student_group.setter
    def student_group(self, student_group):
        if 1 < student_group < 20:
            self.__student_group = student_group
        else:
            print("Incorrect student_group!")

    def study(self):
        print(f"{self.__name} {self.__age}  {self.__id_number} is student_group {self.__student_group}.")


class Subject:
    __name = None

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if 2 < len(name) < 20:
            self.__name = name
        else:
            print("Incorrect name length!")


class Academy:
    def __init__(self, name, accreditation):
        self.name = name
        self.accreditation = accreditation
        self.teachers = []
        self.students = []
        self.subjects = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)


teacher1 = Teacher("Yana", "Olegivna", "33", "2860049658", "Mathematic")
teacher2 = Teacher("Olga", "Samuilivna", "58", "4557852689", "IT")
teacher3 = Teacher("Marina", "Aronivna", "45", "2376940351", "language")

student1 = Student("Sacha", "19", "3194527896", "38")
student2 = Student("Nikolay", "20", "4258796845", "42")
student3 = Student("Natasha", "17", "2587459625", "16")

academy1 = Academy("Odessa National Economic University", "4")
academy2 = Academy("Odessa National Polytechnic University", "4")
academy3 = Academy("Odessa National Maritime Academy", "4")