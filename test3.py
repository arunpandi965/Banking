print("(1)AVAILABLE")
print("(2)DEPOSIT")
print("(3)WITHDRAW")
print("(4)EXIT")
balance = 0
withdraw = 0
i = 0
while i < 5:
     selectnumber=input("please select your number:")
     if selectnumber=="1":
          print("available balance is:",balance)
     elif selectnumber=="2":
          deposit=int(input("enter the deposit amount:"))
          balance=deposit+balance
          print("available balance is:",balance)          
     elif selectnumber=="3":
          withdraw=int(input("enter the amount withdraw:"))
          if(balance < withdraw):
               print("you have insufficient balance")
          else:
               balance=balance-withdraw
               print("available balance is:",balance)
     elif selectnumber=="4":
          print("thank you")
     else:
          print("your transection completed")
     i +=1