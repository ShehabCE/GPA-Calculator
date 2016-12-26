import Functions
Letter_To_Grade = Functions.Template.items()

class Student:
    def __init__(self, Name):
        self.Name = Name
        self.GPA = 0.0
        self.CreditCount = 0
        self.List_of_Courses = []
        self.List_of_Grades = []
        self.List_of_Course_Grade = {}
        self.Student_Data = {
            "Overall GPA" : self.GPA,
            "Credit Hours" : self.CreditCount,
            "Courses" : self.List_of_Course_Grade
        }


    def Show_GPA(self):
        print("Overall GPA: ", self.GPA)

    def Show_Total_Credits(self):
        print ("Total Credit Hours: ", self.CreditCount)

    def Add_Grade(self, CourseName, letter):
        self.List_of_Courses.append(CourseName)
        self.List_of_Grades.append(Letter_To_Grade[letter])
        self.List_of_Course_Grade[CourseName] = letter

    def Remove_Grade(self, CourseName):
        try:
            self.List_of_Courses.remove(CourseName)
            deleted_letter = self.List_of_Course_Grade[CourseName]
            self.List_of_Grades.remove(Letter_To_Grade[deleted_letter])
            if CourseName in self.List_of_Course_Grade:
                del self.List_of_Course_Grade[CourseName]

        except:
            print ("Error: %s doesn't exist! Cannot remove it", CourseName)
