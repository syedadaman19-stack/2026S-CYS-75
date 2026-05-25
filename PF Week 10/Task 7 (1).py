a=int(input("Enter Total Students :"))
i=1
while (i<=a):
    name=str(input("\nEnter Name :"))
    roll=str(input("Enter Roll Number :"))
    obt = int(input("Enter Obtained Marks : "))
    tot = int(input("Enter Total Marks : "))
    per = float((obt / tot) * 100)
    print(f"\nStudent {i} Name :", name)
    print("Roll Number :", roll)
    print("Percentage : ", per)
    if per > 90:
        Grade = "A"
    elif per >= 85:
        Grade = "A-"
    elif per >= 80:
        Grade = "B+"
    elif per >= 75:
        Grade = "B"
    elif per >= 70:
        Grade = "B-"
    elif per >= 65:
        Grade = "C+"
    elif per >= 60:
        Grade = "C"
    elif per >= 55:
        Grade = "D+"
    elif per >= 50:
        Grade = "D"
    elif per < 50:
        Grade = "F"
    print("Grade : ",Grade)
    i=i+1