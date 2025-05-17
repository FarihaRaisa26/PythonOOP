class student:
    def __init__(self,student_id,name,dept,is_enrolled=False):
        self.__student_id=student_id
        self.__name=name
        self.__dept=dept
        self.__is_enrolled=is_enrolled

    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_department(self):
        return self.__dept

    def get_is_enrolled(self):
        return self.__is_enrolled

    def enroll_student(self):
        if not self.is_enrolled:
            self.is_enrolled=True
            print(f"student has been enrolled")
        else:
            raise Exception(f"{self.name} student is already enrolled")

    def drop_student(self):
        if self.is_enrolled:
            self.is_enrolled=False
            print(f"Student has dropped out")

        else:
            raise Exception(f"{self.name} Student can not be dropped out")
    
    def view_student_info(self):
        
        print(f"ID: {self.student_id}")
        print(f"NAME: {self.name}")
        print(f"DEPARTMENT: {self.dept}")
        print(f"IS_ENROLLED: {self.is_enrolled}")

class StudentDataBase :
    student_list=[]

    @classmethod
    def add_student(cls,student):

        if cls.find_student(student.student_id):
            raise Exception("A student with this ID already exists.")
        cls.student_list.append(student)

    @classmethod
    def view_all_students(cls):
        if not cls.student_list:
            print("No students found")
        else:
            for student in cls.student_list:
                student.view_student_info()

    @classmethod
    def find_student(cls,id):
        for s in cls.student_list:
            if s.student_id == id:
                return student
        return None

s1=student("Karim","01","CSE")
s2=student("Samia","02","CSE")
StudentDataBase.add_student(s1)
s1.enroll_student()
StudentDataBase.add_student(s2)
s2.enroll_student()

while True:
        
        print("1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")

        option = input("Enter your choice: ")

        if option == '1':
            StudentDataBase.view_all_students()

        elif option == '2':
            try:
              id = input("Enter Student ID: ")
              if StudentDataBase.find_student(id):
                  raise Exception("Student already exists...cant possible to enroll")                
              name = input("Enter Name: ")
              dept = input("Enter Department: ")
              student = student(id, name, dept)
              StudentDataBase.add_student(student)
              student.enroll_student()
            except Exception as e:
                print(e)

        elif option == '3':
            id = input("Student ID: ")
            student = StudentDataBase.find_student(id)
            if student:
                try:
                  student.drop_student()
                except Exception as e:
                  print(e)
            else:
                print("Student is not found")

        elif option == '4':
            print("Exit")
            break

        else:
            print("Invalid Option")

        