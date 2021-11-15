import csv, myClass

studentList = []
with open('student.csv', mode='r') as stfile:
  streader = csv.reader(stfile)
  for row in streader:
    stObject = myClass.Student(row[0],row[1],row[2],row[3],float(row[4]))
    studentList.append(stObject)

stfile.close()
sumGPA = 0
for st in studentList:
    print('StudentID: '+st.studentID+', studentName: '+st.studentName+', major: '+st.major+', academicStatus: '+st.academicStatus()+', estimatedGraduationDate:'+ st.estimatedGraduationDate())
    sumGPA += st.gpa
print('\nAverage GPA of all students : %.2f\n' % (sumGPA/len(studentList)))
