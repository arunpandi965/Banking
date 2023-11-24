rgNo = ""
name = ""
sub1 = 0
sub2 = 0
sub3 = 0
total = 0
average = 0
result = ""
percentage = 0


def getStudentDetail():
    global rgNo 
    global name
    rgNo = input("Enter Student Register Number:")
    name = input("Enter Student Name:")

def getStudentMarkDetails():
    global sub1 
    global sub2 
    global sub3 

    sub1 = int(input("Enter Mark for Subject1:"))
    sub2 = int(input("Enter Mark for Subject2:"))
    sub3 = int(input("Enter Mark for Subject3:"))

def calcuateTotalResultAndPercentage():
    try:
        global total
        global percentage
        global average
        global result

        total = (sub1 + sub2 + sub3)
        percentage = ((sub1 + sub2 + sub3) / 300) * 100
        average = total / 3
        if sub1 >= 35 and sub2 >= 35 and sub3 >= 35:
            result = "Pass"
        else:
            result = "Fail" 
    except:
        print("An exception occurred")

def printStudentDetailsWithMarks():
    print("\n\n"+"Student Register Number: " + rgNo +"\n"+
            "Student Name: " + name +"\n"+
            "Subject 1: " + str(sub1) +"\n"+
            "Subject 2: " + str(sub2) +"\n"+
            "Subject 2: " + str(sub3) +"\n"+
            "Total: " + str(total) +"\n"+
            "Percentage: " + str(percentage) +"\n"+
            "Average: " + str(average) +"\n"+
            "Result: " + result +"\n")

getStudentDetail()
getStudentMarkDetails()
calcuateTotalResultAndPercentage()
printStudentDetailsWithMarks()




