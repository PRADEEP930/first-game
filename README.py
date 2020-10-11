# first-game
name=input("enter your name:")
age=int(input("enter age:"))
print("welcome",name,"your age is",age,"years")
health=10
if ((age>=18) and (age<=50)):
    print("you are eligible and safe to go outside for this  game")
    x=str(input("which side you want to go left/right?"))
    if x=="left":
        print("you choose right path \U0001f600" )
        y=str(input("you have seen your friend will you give hand to him yes/no"))
        if y=="yes":
          print("you lost 5% health\U0001fA78")
          health-=5
        else :
           print("nic move\U0001f44C")

        z=str(input("did you put mask yes/no"))
        if z=="yes":
            print("nic")
        else:
           print("you died  \U0001f480")
           health=0
    else:
      print("sorry it is red zone and you died \U0001f480")
      health-=10
    if health>=5:
      print("u won\U0001F3C5")
    else:
      print("u lost\U0001F62D")
elif (age<=18):
    print("your not eligible and not safe to go outside ")
    
else :
    print("you are  eligible but not safe to go outside for this  game")
    


    

