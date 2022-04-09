

#values for variables and lists that will be used later. The n=20 is used to create a line of # and the rest are lists. 
n = 20
Customer = []
Products = [
    {"name" : "tshirt", "price" : 15.0},
    {"name" : "pants", "price" : 20.0},
    {"name" : "hat", "price" : 10.0},
    {"name" : "shoes", "price" : 50.0},
    {"name" : "jacket", "price" : 40.0},
    {"name" : "socks", "price" : 5.0},
    {"name" : "shorts", "price" : 0.0},
]


#                           Functions
#Adding customer to dictionary
def addCust(name, cust_membership):
    Cust = {"customer_name" : name,
    "membership_status" : cust_membership}
    Customer.append()

#Checking if customer exists in system
def doesCustExist(name):
    for cust in Customer:
        if any(name):
            return True
        else:
            return False

#Checking if customer is a member
def checkCustMembership(name):
    for cust in Customer:
        if any(name):
            return cust["membership_status"]

#----------------------------FOR DISPLAYING CUSTOMER----------------------------
def displayExisting():
    print("Welcome to RMIT retail Management System!")
    print("#" * n)
    print("Here are all current customers in our system \n")
    for x in Customer:
        print(x["customer_name"])
    
#This will display all the existing names in the 'Customer' list without showing membership status, hence only printing
#'customer_name'.


#----------------------------FOR DISPLAYING CUSTOMERS WITH MEMBERSHIP----------------------------
def displayExistingMember():
    print("Welcome to RMIT retail Management System!")
    print("#" * n)
    print("Here are all customers who have membership with us \n")
    for x in Customer:
        if x["membership_status"] == True:
            print(x["customer_name"])

#This will identify anyone in the list who has a 'True' value for a membership and prints their names. Anyone who has a 'false'
#value for membership will not be displayed. 

#----------------------------ADD/UPDATE EXISTING PRODUCTS AND PRICES----------------------------

def addUpdate_product_price():
    print("Welcome to RMIt retail Management System!")

#----------------------------DISPLAY EXISTING PRODUCTS----------------------------

def displayProducts():
    print("Welcome to RMIT retail Management System!")
    print("#" * n)
    print("Here are all available products \n")
    for x in Products:
        print(x["name"], "unavailable" if x["price"] == 0 else x["price"], "(AUD)")

#----------------------------FOR PLACING AN ORDER----------------------------
def placeOrder():
    print("Welcome to RMIT retail Management System!")
    print("#" * n)
    print("You can place an order with us here \n")

    #Asking users for customer name
    customer_name = input("Please enter your name: \n")
    #Asking users for product name
    product_name = input("Please enter product name: \n")
    #Asking users for product quantity
    quantity = input("Please enter item quantity: \n")
    #Asking users about membership status
    membership_status = input("Are you a member with us? [Y or N]: \n")
    valid=False
    while not valid:
        membership_status = input("> ").strip("\n")
        match membership_status:
            case "Y":
                membership_status

    if membership_status == "Yes":
        print (customer_name + " purchases " + str(quantity) + " x " + product_name)
        print ("Unit price:             " + "COST" + " (AUD)")
        print (customer_name + " gets a discount of 5.0%!")
        print ("Total price             " + "COST" + " (AUD)")

        
            




    if membership_status == "No":
        print(customer_name + " purchases " + str(quantity) + " x " + product_name)
        print ("Total price:             " + "COST" + " (AUD)")

        if not doesCustExist(customer_name) or not checkCustMembership(customer_name):
            print("You do not have membership with us, would you like a membership? [y or n]: \n")

    




#Exiting the program, just closes the terminal application. 
def exitProgram():
    exit()




#Creating the menu for console application, i found an example of using 'match' and 'case' online as a new feature of python 3.0
#and decided it would be cleanest to implement. I chose this over using multiple defs and elifs as 'case' seemed a lot easier
#to implement. 

#Using defs and executing defs was the easiest way i found online to execute options from a menu and simplified the whole process
#of writing code and cleaning it up. As well as making sections easy to track and easy to fix problems. 
def menu():
    run = True
    while (True):
        print("Welcome to the RMIT retail management system!")
        print("#" * n)
        print("1: Place an order")
        print("2: Add/update products and prices")
        print("3: Display existing customers")
        print("4: Display existing customers with membership")
        print("5: Display existing products")
        print("0: Exit the program")
        print("#" * n)
        choice = input("> ")
        match choice:
            case "1":
                placeOrder()
            case "2":
                addUpdate_product_price()
            case "3":
                displayExisting()
            case "4":
                displayExistingMember()
            case "5":
                displayProducts()
            case "0":
                exitProgram()
            case _:
                print("Please enter a valid option")
                input()

#This executes the def for menu that is written earlier. 
menu()























