name = input("Enter your name ")

print("__INSTRUCTIONS__")
print("Enter marks between 0-100")
print("Write -1 in subject marks when you are done with inputing marks")

count=0
Total=0
avg=0
while True:
    try:
        marks=float(input("Enter your marks of subject "))
        
        if marks>=0 and marks<101:
            Total+=marks
            count+=1

        elif marks== -1:
            break

        else:
            print("Enter a valid marks!!")

    except:
        print("Enter a valid marks!!")
        continue


if count==0:
    print("No Input.Successfully Executed")

else:
   
    avg=Total/count
    

    grade_dict = {

        "A+": (91,101),
        "A" : (80,91),
        "B" : (70,80),
        "C" : (50,70),
        "D" : (40,50),
        "F" : (0,40)
    }

    grade= None
    for g,(low,high) in grade_dict.items():

        if low<= avg <high:
            grade=g
            break
    
    print("__Grade Chart__")
    for g,(start,end) in grade_dict.items():
        print(f"Grade: {g} : {start} to {end}")

    if grade is None:
        print("Invalid Score")
        
    elif grade=='F':
        print("Fail! Better luck next time")

    else:
        print("Conratulation you are passed!!!<3")
        

    print(name," has scored ",Total," marks with Grade of ",grade)