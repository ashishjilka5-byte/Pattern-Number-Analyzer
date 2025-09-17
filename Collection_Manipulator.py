
print("Welcome to the Student Data Organizer!")
print(" ")

stored = {}
while True:
 print("\nSelect an option:")
 print("1. Add Student")
 print("2. Display All Student")
 print("3. Update Student Information")
 print("4. Delete Student")
 print("5. Display Subjects Offered")
 print("6. Exit")


 choice = int(input("Enter your choice:"))

 print(" ")

 print("Enter Student details:")
 if choice == 1:

    std_id = input("Student id:")
    name = input("Name:")
    Age = input("Age:")
    Grade = input("Grade:")
    B_day = input("Date of Birth (YYYY-MM-DD):")
    sub = input("Subjects (come-separated):")
    print(" ")
    tuple_std = (std_id,B_day)

    stored[std_id]={
        "name": name,
        "Age": Age,
        "Grade": Grade,
        "B_day": B_day,
        "sub": sub,
    }

    print("Student addd successfully!")
    print(" ")
 elif choice ==2:
      if not stored:
        print("No Student available.")
      else:
         for sid in stored:
            info = stored[sid]
            print("\nid:",sid)
            print("Name:",info["name"])
            print("Age:",info["Age"])
            print("Grade:",info["Grade"])
            print("Birthday:",info["B_day"])
            print("sub:",info["sub"])

 elif choice == 3:
    sid = input("Enter the student ID to update:")
    if sid in stored:
        name = input("New name:")
        age = input("New age:")
        grade = input("Enter grade:")
        b_day = input("New data of birth(yyyy-mm-dd):")
        sub = input("New subject:")

        stored[sid] = {
            "name": name,
            "age": age,
            "grade": grade,
            "b_day": b_day,
            "subject": sub,
        }
        print("Student updated successfully")
    else:
        print("Student not found")
 elif choice ==4:
     sid = input("Enter Student ID to delete:")
     if sid in stored:
         del stored[sid]
         print("Student deleted successfully")
     else:
         print("Student not found")
         # option 5 helping ai google for  understanding
 elif choice == 5:
         if not stored:
             print("No subjects yet.")
         else:
             print("Subjects offered:")
             for sid in stored:
                 print("ID:", sid, "=>", stored[sid]["sub"])
 elif choice == 6:
     print("Exiting... Goodbye!")
     break

 else:
     print("Invalid choice, try again.")









