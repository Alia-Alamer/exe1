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

def view_exercise(students, exercises):
    ex_name = input("enter the exercise number: ")

    if ex_name not in exercises:
        print("exercise not found")
        return

    print(f"\nResults for exercise {ex_name}:")
    for number, info in students.items():
        points = info["grades"].get(ex_name, "no grade")
        print(f"{info['first_name']} {info['last_name']} ({number}): {points}")
    print()

def view_student(students, exercises):
    number = input("enter student number: ")

    if number not in students:
        print("student not found")
        return

    info = students[number]
    print(f"\nStudent: {info['first_name']} {info['last_name']} ({number})")
    if not info["grades"]:
        print("no grades yet")
    else:
        for ex, pts in info["grades"].items():
            print(f"  Exercise {ex}: {pts}")
    print()

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
    elif choice == "3":
        view_exercise(students, exercises)
    elif choice == "4":
        view_student(students, exercises)
    elif choice == "5":
        print("Goodbye!")
        break