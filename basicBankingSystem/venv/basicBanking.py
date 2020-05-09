import random
import string

line1 = 's/n \tFull-Name \tUsername \t\tEmail \t\t\t\tPassword \n'
line2 = '1 \tJimoh Nafeesat \tmilereh \tjimohn97@gmail.com \t\tfeenah \n'
line3 = '2 \tBamise Eniola \tolaoluwa \tiyibamise20@gmail.com \tiyiola \n'
file1 = open('staff.txt', 'w')
file1.writelines([line1, line2, line3])
file1.close()


customerfile = open('customer.txt', 'w')
line1 = 'Full-Name \t\tAccount Balance \t\t\tAccount Type \t\t\t\tEmail \t\t\tAccount Number \n'
customerfile.write(line1)
customerfile.close()


def staff_login():
    username = input("USERNAME:")
    userPass = input("PASSWORD: ")

    # open the staff file and read from it
    file1 = open('staff.txt', 'r')
    registered = False
    # check each line for the username and password, if the two are present in a particular line, break the loop
    for line in file1:
        if username in line:
            if userPass in line:
                registered = True
                break
            else:
                print("incorrect password")

    if registered:
        staffActionsAfterLogin()
    else:
        print("Wrong user name and password, please try again!!!")
        staff_login()


def customerCreation():

    acctname = input("ACCOUNT NAME: ")
    acctbalance = int(input("OPENING BALANCE: "))
    accttype = input("ACCOUNT TYPE: ")
    acctemail = input("ACCOUNT EMAIL: ")
    acctnumber = ''.join(random.choice(string.digits) for n in range(10))

    line = f'{acctname} \t\t\t{acctbalance} \t\t\t{accttype} \t\t\t\t{acctemail} \t\t{acctnumber} \n'

    addaccounts = open('customer.txt', 'a')
    addaccounts.write(line)
    addaccounts.close()

    print(f"The newly generated account number is : {acctnumber} ")
    staffActionsAfterLogin()


def checkDetails():
    customer_file = open('customer.txt', 'r')
    requestforacct = input("Please provide your account number: ")

    for line in customer_file:
        if requestforacct in line:
            print(line)

    staffActionsAfterLogin()


def staffActionsAfterLogin():
    whattodo = input("What would you like to do? \n 1. Create new bank account \n 2. Check account details \n "
                     "3. Logout \n >>> ")
    while whattodo == '1':
        customerCreation()
    while whattodo == '2':
        checkDetails()
    else:
        landing()


def landing():
    options = int(input("1. Staff Login \n2. Close App \n>>>"))
    if options == 1:
        staff_login()
    elif options == 2:
        exit()
    else:
        print("Enter 1 or 2 for your choice of action!!!")


landing()
