import math

print("Welcome to the Data Analyzer and Transformer Program")

data = []
def filter_data():
    if data:
        threshold = int(input("Enter a threshold value to filter out data below this value:\n"))
        filtered = list(filter(lambda x: x >= threshold, data))
        print("\nFiltered Data (values >= 50):", filtered)


def Sort_data(data):
 print("Choose sorting option:")
 print("1. Ascending")
 print("2. Descending")

 sort_choice = input("Enter your choice: ")

 if sort_choice == "1":
  data.sort()
  print("Data sorted in Ascending order:", data)
 elif sort_choice == "2":
  data.sort(reverse=True)
  print("Data sorted in Descending order:", data)
 else:
  print("Invalid choice")


def Display_dataset(data):
 print("Dataset Statistics:")
 print("- Minimum value:", min(data))
 print("- Maximum value:", max(data))
 print("- Sum of all values:", sum(data))
 print(f"- Average value: {sum(data)/len(data):.2f}")



while True:
 print("\nMain Menu:")
 print("1. Input Data")
 print("2. Display Data summary (Built-in Functions)")
 print("3. Calculate Factorial ")
 print("4. Filter Data by Threshold")
 print("5. Sort Data")
 print("6. Display Dataset Statistics")
 print("7. Exit Program\n")


 Choice = int(input("Please enter your choice:"))


 if Choice == 1:
  data = list(map(int, input("Enter data for a 1D array (separated by spaces):\n").split()))
  print("\nData has been stored successfully")

 elif Choice == 2:
  print("\nData Summary:")
  print("- Total elements:",len(data))
  print("- Minimum value:",min(data))
  print("- Maximum value:",max(data))
  print("- Sum of all value:",sum(data))
  print(f"- Average value: {sum(data) / len(data):.2f}")





 elif Choice == 3:
  num = int(input("Enter a number to calculate its factorial: "))
  print(f"\nFactorial of {num} is {math.factorial(num)}")


 elif Choice == 4:
  filter_data()


 elif Choice == 5:
  Sort_data(data)

 elif Choice == 6:
  Display_dataset(data)

 elif Choice == 7:
  print("Thank you for using Data Analyzer and Transformer Program. Goodbye!\n")
  break

 else:
  print("Invalid choice! Please select a valid option.")


























