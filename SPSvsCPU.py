import random
play=True
while(play):
    x=0
    y=0
    i=1
    while((x!=5)&(y!=5)):
        print("\nround ",i,":")
        print("\npress 1 for stone")
        print("press 2 for scissors")
        print("press 3 for paper\n")
        print("enter choice of player 1")
        a=int(input())
        if(a==1):
            print("player 1 chose stone")
        elif(a==2):
            print("player 1 chose scissors")
        else:
            print("player 1 chose paper")
        
        b=random.randint(1,3)
        if(b==1):
            print("CPU chose stone")
        elif(b==2):
            print("CPU chose scissors")
        else:
            print("CPU chose paper")
        if((a==1)&(b==1)):
         print("its a draw")
        elif((a==1)&(b==2)):
         print("player 1 wins")
         x+=1
        elif((a==1)&(b==3)):
         print("CPU wins")
         y+=1
        elif((a==2)&(b==1)):
         print("CPU wins")
         y+=1
        elif((a==2)&(b==2)):
         print("its a draw")
        elif((a==2)&(b==3)):
         print("player 1 wins")
         x+=1
        elif((a==3)&(b==1)):
         print("player 1 wins")
         x+=1
        elif((a==3)&(b==2)):
         print("CPU wins")
         y+=1
        elif((a==3)&(b==3)):
         print("its a draw")
        else:
         print("enter a valid choice")
         continue
        print("\nScore:\nplayer 1: ",x,"\n     CPU: ",y)
        i+=1
    print("game over")
    if(x==5):
     print("player 1 is the winner")
    else:
     print("CPU is the winner")
    c=input("\nDo you want to play again?\n")
    if(c=="no"):
        play=False
    

