import Functions
# When User selects "Calculate GPA" option
# This script is called from Main

#Array of Course names added.
List_Of_Courses = []

#Mapping Course to Grade.
Course_Grade = {}
#Mapping Course to Credit Hour.
Course_Crh = {}

#Overall GPA.
GPA = 0.0
Credit_Count = 0
#Data Structure for User. Example below
#Student_Data = {
#                   {'CS106': A,
#                   'RHET101': B},
#                   3.5
#                  }
Student_Data = {
    "Courses": Course_Grade,
    "Overall GPA": GPA
}

#Function Adder.
def Adder(GPA, Credit_Count):
    while(1):
        print "ADDING A GRADE"
        print '=' * 20
        single_course = raw_input("Course Name: ")
        single_grade = raw_input("Grade: ")
        single_crh = int(raw_input("Credit Hour: "))
        print '=' * 20
        List_Of_Courses.append(single_course)
        Course_Grade[single_course] = single_grade
        Course_Crh[single_course] = single_crh
        GPA = GPA + Functions.Update_GPA(single_grade, single_crh)
        Credit_Count = Credit_Count + single_crh

        response = raw_input("-> Add? (NO/YES)")
        response.upper()
        if(response == "NO"):
            break
Adder(GPA, Credit_Count)

while(1):
    print "Display which of the following: "
    print "1) Courses | Grades | Credit Hour"
    print "2) Overall GPA"
    print "3) BOTH (1) & (2)"
    print "4) Back to adding a grade"
    another_response = int(raw_input())
    if(another_response == 1):
        print "To do..."
        #To do...
    elif(another_response == 2):
        print "Achieved Credit Hours %d" %Credit_Count
        GPA = GPA / len(List_Of_Courses)
        print "Overall GPA : %f" %GPA
    elif(another_response == 3):
        print "To do..."
        #To do...
    elif(another_response == 4):
        print "Call function again. To do..."
        #To do...
        Adder(GPA, Credit_Count)
