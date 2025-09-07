
print("Welcome to Pattern Generator and Number Analyzer\n")

while True:
    print("Select an option:")
    print("1. Generate a pattern")
    print("2. Analyze a range of numbers")
    print("3. Exit")

    enter = int(input("Enter the choice number: "))

    if enter == 1:
        row  = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        print("\nPattern:")

        i = 1
        while i <= row:
            j = 1
            while j <= i and j <= cols:
                print("*", end="")
                j += 1
            print()
            i += 1
        print("")

    elif enter == 2:
        a = int(input("Enter the start number: "))
        b = int(input("Enter the end number: "))

        odd_sum = 0
        even_sum = 0

        for number in range(a, b + 1):
            if number % 2 == 0:
                print(f"Number {number} is even")
                even_sum += number
            else:
                print(f"Number {number} is odd")
                odd_sum += number

        total_sum = odd_sum + even_sum


        print(f"Total sum of numbers from {a} to {b} is: {total_sum}\n")

    elif enter == 3:
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid option! Please select 1, 2, or 3.\n")
