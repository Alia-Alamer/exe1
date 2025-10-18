students = {}
exercises = []

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





while True:
    print("1) add student")
    print("2) add exercise grading")
    print("3) view exercise")
    print("4) view student")

    choice = input("choose an option: ")

    if choice == "1":
        add_student(students, exercises)
    elif choice == "2":
        add_exercise(students, exercises)
        # if statement for the rest of the options will be written when the rest of the functions view student and exercise are ready
        # 3 view exercise
        # 4 view student