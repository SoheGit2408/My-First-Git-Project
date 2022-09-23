# Health Management System
# 3 clients - Harry, Rohan and Hammad
# Total 6 files write a function that when executed takes as input client name One more
# function to retrieve exercise or food for any client
# Create a food log file for each client Create an exercise log file for each client.
# Ask the user whether they log or retrieve client data. Write a function that takes
# the user input of the client's name. After the client's name is entered, it will display a
# message as "What you want to log-Diet or Exercise".  Write a function to retrieve exercise or food
# file records for any client.

def getdate():
    import datetime
    return datetime.datetime.now()


def choice(x):
    if x == 0:
        print("Which clients's data do you want to log enter 1 for Harry, 2 for Rohan and 3 for Hammad:")
    elif x == 1:
        print("Which clients's data do you want to retrive enter 1 for Harry, 2 for Rohan and 3 for Hammad:")
    else:
        print("You hava entered invalid input please input 0 or 1")


def person_record_retrive(g:int,h:int):
    if g == 1 and h == 0:
        print("Which data of harry you want to log enter 0 for diet and 1 for exercise ")
    elif g == 2 and h == 0:
        print("Which data of Rohan you want to log enter 0 for diet and 1 for exercise ")
    elif g == 3 and h == 0:
        print("Which data of Hammad  you want to log enter 0 for diet and 1 for exercise ")
    elif g == 1 and h == 1:
        print("Which data of harry you want to retrive enter 0 for diet and 1 for exercise ")
    elif g == 2 and h == 1:
        print("Which data of Rohan you want to retrive enter 0 for diet and 1 for exercise ")
    elif g == 3 and h == 1:
        print("Which data of Hammad you want to retrive enter 0 for diet and 1 for exercise ")
    else:
        print("Invalid input entered")


def write_record(w, k, j):
    with open(w, "a") as f:
            if k == 0:
                print("enter what diet " + j + " has been taken")
            elif k == 1:
                print("enter which exercise " + j + " has doing")

            a = input()
            b = str(getdate())

            f.write(b+"\t"+a+"\n")
            print("you have successfully write the record of the given client  as followes\n")
            print(b + "\t" + a)


def retrive_record(s):
    with open(s, "r+") as f:
        d=f.read()
        print("The record of the given client is as follows:\n")
        print(d)


a = int(input("What do you want either log the data or retrive \nthe data enter 0"
              " for logging and 1 for retriving the data\n"))

choice(a)
b = int(input())
if (a == 0 or a == 1) and (b == 1 or b == 2 or b == 3):
    person_record_retrive(b,a)
else:
    print("Invalid input entered")
c = int(input())

m="Harry_Diet.txt"
l = "Harry"

if a == 0:
    if b == 1 and c == 0:
        m = "Harry_Diet.txt"
        l = "Harry"
    elif b == 1 and c == 1:
        m = "Harry_Exercise.txt"
        l = "Harry"
    elif b == 2 and c == 0:
        m = "Rohan_Diet.txt"
        l = "Rohan"
    elif b == 2 and c == 1:
        m = "Rohan_Exercise.txt"
        l = "Rohan"
    elif b == 3 and c == 0:
        m = "Hammad_Diet.txt"
        l = "Hammad"
    elif b == 3 and c == 1:
        m = "Hammad_Exercise.txt"
        l = "Hammad"
    else:
        print("Enter the file name you want to log  with .txt extention")
        n=input()
        m = n

    write_record(m,c,l)

if a == 1:
    if b == 1 and c == 0:
        m = "Harry_Diet.txt"
    elif b == 1 and c == 1:
        m = "Harry_Exercise.txt"
    elif b == 2 and c == 0:
        m = "Rohan_Diet.txt"
    elif b == 2 and c == 1:
        m = "Rohan_Exercise.txt"
    elif b == 3 and c == 0:
        m = "Hammad_Diet.txt"
    elif b == 3 and c == 1:
        m = "Hammad_Exercise.txt"
    else :
        print("Error invalid input entered.")

    retrive_record(m)
