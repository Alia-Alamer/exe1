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
        while True:
            try:
                points = float(input(f"enter the points for exercise {ex}: "))
                break
            except ValueError:
                print("please enter a number")
        grades[ex] = points

    students[number] = {"first_name": first, "last_name": last, "grades": grades}

    print("student added")

def add_exercise(students, exercises):
    ex_name = input("enter the name of the exercise: ")

    if not ex_name:
        print("exercise name cannot be empty")
        return

    if ex_name in exercises:
        print("exercise already exists")
        return

    exercises.append(ex_name)

    for number, info in students.items():
        while True:
            try:
                points = float(input(f"enter points for {info['first_name']} {info['last_name']}: "))
                if points < 0:
                    print("points cannot be negative")
                    continue
                break
            except ValueError:
                print("please enter a number")
        info["grades"][ex_name] = points

    print("exercise and grades added")



while True:
    print("1) add student")
    print("2) add exercise grading")
    print("3) view exercise")
    print("4) view student")
    print("5) exit")

    choice = input("choose an option: ")

    if choice == "1":
        add_student(students, exercises)
    elif choice == "2":
        add_exercise(students, exercises)
        # if statement for the rest of the options will be written when the rest of the functions view student and exercise are ready
        # 3 view exercise
        # 4 view student
    elif choice == "5":
        print("Goodbye!")
        break