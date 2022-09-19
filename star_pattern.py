print("Enter Number of rows to print in star pattern.")
rows = int(input())

print("Enter 0 for star pattern and 1 for reverse star pattern")
choice = int(input())


def starpattern(a):

    for i in range(0, a):

        for j in range(0, (i+1)):
            print("*", end="")
        print("")


def reverse_starpattern(b):

    for i in range(0, b):

        for j in range(0, (b - i)):
            print("*", end="")
        print("")


if choice == 0:
    starpattern(rows)
elif choice == 1:
    reverse_starpattern(rows)
else:
    print("Invalid choice Entered")




