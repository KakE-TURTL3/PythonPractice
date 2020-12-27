import time

#Introduces user to program they are using
print("Welcome to *insert name here*")

#Asks the user to either register or log in
opt = int(input ("To continue you must login or register. Please pick an option.\n1)Log In\n2)Register\n"))

#Defines login function
def login():
    accountName = input("Please enter your account name: ")
    password = input("Please enter your password: ")
    f = open("accounts.txt", "r")
    real = f.read()
    accountDetails = accountName + ", " + password + "\n"
    if accountDetails == real:
        print("You have successfully logged in to the account: " + accountName + "\n")
        time.sleep(2)
    else:
        print("Login failed. You entered the wrong username or password. Please try again.\n")
        login()
    f.close()

#Define register function
def register():
    registerAccountName = input("Please input a suitable username: ")
    registerPassword = input("Please enter a suitable password: ")
    confirmPassword = input("Please confirm your password: ")
    if registerPassword == confirmPassword:
        f = open("accounts.txt", "w")
        f.write(registerAccountName + ", " + registerPassword + "\n")
        f.close()
        print("Now you must log in")
        login()
    else:
        print("The first password you entered didnt match the confirm password. Please try again.\n")
        register()

if opt == 1:
    login()
elif opt == 2:
    register()
else:
    quit
    
    
