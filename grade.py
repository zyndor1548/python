def gradefunc(mark,total):
    if mark >= (90/100) *  total :
        grade = 'A'
    elif mark >= (75/100) * total:
        grade = 'B'
    elif mark >= (50/100) * total:
        grade = 'C'
    elif mark >= (40/100) * total:
        grade = 'D'
    else:
        grade = 'F'
    return grade
print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\ngrade")
while (True):
    subjectcount = input ( "\nHow many subject do you have : ")
    if subjectcount.isnumeric():
        num = int(subjectcount)
        break
    else:
        print ("\tEnter a number in the feild")
while (True):        
    subjecttotal = input ( "\nHow much is the total mark for one subject : ")
    if subjecttotal.isnumeric():
        total = int(subjecttotal)
        break
    else:
        print ("\tEnter a number in the feild")

name = []
gradelist = []
marklist =[]
totalmark = 0
for i in range(num):
    inname = input (f"\nEnter subject {i + 1} name : ")
    name.append(inname)
    while (True):
        mark = str ( input (f"\tEnter {name[i]} mark : "))
        if mark.isnumeric():
            intmark = int(mark)
            grade = gradefunc(intmark,total) 
            marklist.append(intmark)
            gradelist.append(grade)
            totalmark += intmark
            break
        else:
            print ("\tEnter a number in the field")

print("\n\n\n")
for i in range(num):
    print(f"Your grade for {name[i]} is {gradelist[i]}  ({marklist[i]}/{total})")
print (f"\n\tYour total mark is {totalmark} out of {total * len(gradelist)}\n\tYour total grade is {gradefunc(totalmark,total * len(gradelist))}")
