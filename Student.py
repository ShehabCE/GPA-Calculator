import GPAOPs
Letter_To_Grade = GPAOPs.Template.items()

class Student:
    def __init__(self, Name):
        self.Name = Name
        self.GPA = 0.0
        self.CreditCount = 0
        self.List_of_Courses = []
        self.List_of_Grades_CHR = {}
        self.List_of_Course_Grade = {}
        #Below Attribute Hinted as main private attribute.
        self.__Student_Data = {
            "Student Name": self.Name,
            "Overall GPA": self.GPA,
            "Credit Hours": self.CreditCount,
            "Courses": self.List_of_Course_Grade
        }

    def Show_GPA(self):
        print ("="*15)
        print("Overall GPA: ", self.GPA)
        print ("="*15)

    def Show_Total_Credits(self):
        print ("="*15)
        print ("Total Credit Hours: ", self.CreditCount)
        print ("="*15)

    def Add_Grade(self, CourseName, letter, CHR):
        self.List_of_Courses.append(CourseName)
        self.List_of_Grades_CHR[Letter_To_Grade[letter]] = CHR
        self.List_of_Course_Grade[CourseName] = letter
        self.GPA += GPAOPs.Update_GPA(letter, CHR)
        self.CreditCount += CHR

    def Remove_Grade(self, CourseName):
        try:
            self.List_of_Courses.remove(CourseName)
            deleted_letter = self.List_of_Course_Grade[CourseName]
            deleted_CHR = self.List_of_Grades_CHR[Letter_To_Grade[deleted_letter]]

            del self.List_of_Grades_CHR[Letter_To_Grade[deleted_letter]]
            #Code below checking if course name is in the dictionary. Redundant...
            #if CourseName in self.List_of_Course_Grade:
            del self.List_of_Course_Grade[CourseName]
            self.GPA -= GPAOPs.Update_GPA(deleted_letter, deleted_CHR)
            self.CreditCount -= deleted_CHR

        except:
            print ("Error: %s doesn't exist! Cannot remove it", CourseName)

    def retrieve_Student_Data(self):
        return self.__Student_Data

    def set_Student_Data(self, data):
        self.__Student_Data = data
