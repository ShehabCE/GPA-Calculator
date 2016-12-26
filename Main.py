

#Display Message
print ("Playing around with Python 3.5.2 ... So here is a GPA Calculator!")
while(True):
    print ("What do you want to do?")
    print ("1) Calculate GPA")
    print ("2) Help")
    print ("3) Exit")
    reply = int(input())
    if(reply == 1):
        import Calculation
        break
    elif(reply == 2):
        import Help
        break
    elif(reply == 3):
        exit(0)