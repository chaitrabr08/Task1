        # Define the Student class
class Student:
    def _init_(self, name, ssn, grade):
        self.name = name
        self.ssn = ssn
        self.grade = grade
    
    def _str_(self):
        return f"Name: {self.name}, ssn: {slef.ssn}, Grade: {self.grade}"

students = {}

def input_student_data():

    num_students = int(input("Enter the number of students: "))
    
    for i in range(num_students):
        print(f"\nEnter details for student {i+1}:")
        name = input("Enter student name{i+1}: ")
        ssn = int(input("Enter student ssn{i+1}: "))
        grade = input("Enter student grade: ")
        
        student = Student(name, ssn, grade)
        
        students[name] = student

input_student_data()

print("\nStudents :")
for name, student in students.items():
    print(name, ":", student)
