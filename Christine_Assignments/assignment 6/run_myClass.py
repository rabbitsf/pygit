import myClass

student = myClass.Student("S101","Peter","ISYS","2019-08-20",2.5)

print('ID :', student.studentID)
print('Name :', student.studentName)
print('Major :', student.major)
print('GPA :', float(student.gpa))
print(student.academicStatus())
print(student.estimatedGraduationDate())
