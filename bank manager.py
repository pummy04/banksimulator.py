name=str(input("Please enter your name:"))
# by default input is always in string-
print("Hello,How are You",name)
message="""
HOW CAN I HELP YOU?
please select the option,
TYPE 1>>TO SEE CURRENT AMOUNT:
TYPE 2>>TO DEPOSIT AMOUNT:
TYPE 3>>TO WITHDRAW AMOUNT:
"""
print(message)
# use pass instead of ...
task=int(input("PLEASE CHOOSE ANY OPERATION:"))
print(task)
print(type(task))
A_amt=1000
if task>=1 and task<=3:
 print("-------------WELCOME TO VIRTUAL BANK---------")
else:
    print("-----PLEASE ENTER THE VALID OPERATION -----")
if task==1:
    print("THANKS FOR VISTING US,YOUR CURRENT AMOUNT IS:",A_amt)
elif task==2:
    deposit=int(input("PLEASE WRITE AMOUNT YOU WANT TO DEPOSIT:"))
    print(deposit)
    print("YOUR FINAL AMOUNT:",deposit+A_amt)
    print("THANKS FOR VISTING US,YOUR CURRENT AMOUNT IS:",deposit+A_amt)
elif task==3:
    withdraw=int(input("ENTER THE AMOUNT YOU WANT TO WITHDRAW:"))
    print(withdraw)
    if withdraw<A_amt:
        print("YOUR TOTAL AMOUNT:",A_amt-withdraw)
    else:
        print("YOU DONT HAVE THAT MUCH AMOUNT")

    
# try catch and final------