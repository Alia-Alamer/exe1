students = {}
exersises = []

def add_student(students, exercises):
    number = input("give student number: ")

    if number in students:
        print("student number already exists")
        return

    first = input("enter first name: ")
    last = input("enter last name: ")

    grades = {}
    for ex in exercises:
        points = float(input("enter the points for the exercise: "))
        grades[ex] = points

    students[number] = {"first_name": first, "last_name": last, "grades": grades}

    print("student added")