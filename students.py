class Student():
    def __init__(self, firstname, surname):
        self.__firstname = firstname
        self.__surname = surname
    def name(self):
        return self.__firstname + ' ' + self.__surname


class WorkingStudent(Student):
    def __init__(self, firstname, surname, company):
        super().__init__(firstname, surname)
        self.__company = company
    def name(self):
        return super().name() + ' (' + self.__company + ')'

student1 = Student('Michael', 'Migsch')
print(student1.name())

student2 = WorkingStudent('Alexandra', 'Maier', 'Händel GmbH')
print(student2.name())

students = [Student('Max', 'Mustermann'),
            WorkingStudent('Julia', 'Jam', 'AKH Wien'),
            WorkingStudent('Florian', 'Jam', 'ÖBB'),
            Student('Christian', 'Baum')]

for student in students:
    print(student.name())
