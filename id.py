import datetime
import csv


account2 = {
    "576", "123",

}

FILENAME = "user_book_log.csv"


# Making a function that asks for user Id and reprompts the user if it is less than 6

def userid():
    try:
        user_id = input("Id: ")
        if len(user_id) == 6:
            return user_id
        else:
            print("Please enter a vaild Id.")
            userid()
    except ValueError:
        userid()
        
# Checks if the user input of account is vaild by using set

def account(account2):
    account_number = input("Account: ")
    if account_number in account2:
        print(account_number)
        return account_number
    else:
        print("Book not found try again")
        account(account2)

user_id = userid()


account_number = account(account2)

user_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


with open(FILENAME,mode= "a", newline="") as data:
    writer = csv.writer(data)
    writer.writerow([user_id,account_number , user_time])