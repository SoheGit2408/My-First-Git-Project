print("Enter Number of rows to print in number pattern.")
number = int(input())

print("Enter 0 for number pattern and 1 for reverse number pattern")
choice = int(input())


def number_pattern(a):

    for i in range(0, a):

        for j in range(0, (i+1)):
            print(j, end="")
        print("")


def reverse_number_pattern(b):

    for i in range(0, b):

        for j in range(0, (b - i)):
            print(j, end="")
        print("")


if choice == 0:
    number_pattern(number)
elif choice == 1:
    reverse_number_pattern(number)
else:
    print("Invalid choice Entered")
