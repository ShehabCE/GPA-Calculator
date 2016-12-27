import GPAOPs
Letter_To_Grade = GPAOPs.Template

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
        print ("="*25)
        try:
            print("Overall GPA: ", self.GPA/self.CreditCount)
        except:
            print("Overall GPA: ", self.GPA)
        print ("="*25)

    def Show_Total_Credits(self):
        print ("="*25)
        print ("Total Credit Hours: ", self.CreditCount)
        print ("="*25)

    def Add_Grade(self, CourseName, letter, CHR):
        self.List_of_Courses.append(CourseName)
        x = Letter_To_Grade[letter]
        self.List_of_Grades_CHR[str(x)] = CHR
        self.List_of_Course_Grade[CourseName] = [letter, CHR]

        self.GPA += GPAOPs.Update_GPA(letter, CHR)
        self.CreditCount += CHR

        self.__Student_Data["Overall GPA"] = self.GPA/self.CreditCount
        self.__Student_Data["Credit Hours"] = self.CreditCount
        self.__Student_Data["Courses"] = self.List_of_Course_Grade

    def Remove_Grade(self, CourseName):
        try:
            self.List_of_Courses.remove(CourseName)
            ## Retrieving letter and CHR
            deleted_letter = self.List_of_Course_Grade[CourseName][0]
            deleted_x = Letter_To_Grade[deleted_letter]
            deleted_CHR = self.List_of_Course_Grade[CourseName][1]
            deleted_course = self.__Student_Data["Courses"]

            del deleted_course[CourseName]
            del self.List_of_Grades_CHR[str(deleted_x)]

            ## Deleting from GPA and Credits
            self.GPA -= GPAOPs.Update_GPA(deleted_letter, deleted_CHR)
            self.CreditCount -= deleted_CHR
            self.__Student_Data["Overall GPA"] = self.GPA
            self.__Student_Data["Credit Hours"] = self.CreditCount
            self.__Student_Data["Courses"] = self.List_of_Course_Grade

        except:
            print("Error: ", CourseName, " doesn't exist! Cannot remove non-existing course.")

    def retrieve_Student_Data(self):
        return self.__Student_Data

    def set_Student_Data(self, data):
        self.__Student_Data = data

    def Show_Student_Courses(self):
        print(self.List_of_Courses)
