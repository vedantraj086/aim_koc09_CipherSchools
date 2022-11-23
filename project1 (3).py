import random
name=str(input("Enter your name: "))
print("Hey "+name+", Let's play a game \nyou have to enter a number between 1 and 6 . If computer's guess is same as your guess then you wil win")
print("")
x=0
while x==0:
    ch=input("Are you ready ? (Type 'y' for yes and 'n' for no): ")
    if ch=='y':
        a=0
        score=0
        user_in=int(input("Enter a number: "))
        print()
        while a==0:
            cpu_in=random.randint(1,6)
            print("Your choice is:",user_in)
            print("CPU's choice is:",cpu_in)
            print(" ")
            if user_in==cpu_in:
                score+=1
                print("You won \n+10")
                print(" ")
            else:
                print("Sorry try next time ")
                print("")
            i=0
            while i==0:
                s=input("Do you want to play again ?(Type 'y' for yes and 'n' for no): ")
                print(" ")
                if s=='y':
                    pass
                    i=1
                elif s=='n':
                    a=a+1
                    i=1
                else:
                    print("Please Enter a vaid input")
                    print("")
            i=0
        print("Thank you "+name+" !! your score is "+str(score*10))  
        x=1   
    elif ch=='n':
        print("Okay. See you later")
        x=1
    else:
        print("Please Enter a valid input")
        print("")
           
