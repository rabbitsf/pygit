import datetime

class Student:

    def __init__(self, studentID, studentName, major, admittedDate, gpa):
        self.studentID = studentID
        self.studentName = studentName
        self.major = major
        self.admittedDate = admittedDate
        self.gpa = gpa

    def academicStatus(self):
        if self.gpa < 2.0:
            return "Poor academic status"
        elif self.gpa < 3.0:
            return "Fair academic status"
        else:
            return "Excellent academic staus"

    def estimatedGraduationDate(self):
        date1 = datetime.datetime.strptime(self.admittedDate,"%Y-%m-%d")
        admittedDate = date1 + datetime.timedelta(days=1095)
        return date1.strftime("%m/%d/%y")
