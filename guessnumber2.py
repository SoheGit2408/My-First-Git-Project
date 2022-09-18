
win_num=55
count=1
print("guess the number")
guess=int(input())
while guess!=win_num and count<10:
    if guess>win_num:
        print("you have entered some larger number try again")
        count=count+1
    elif guess<win_num:
        print("you have enterd some smaller number try again")
        count=count+1
    
    print("you have",10-count,"guesses remain")
    if (10-count)==0:
        break
    guess=int(input())
if guess==win_num:
    print("you won you have guess the right number and you guess it in",count, "guesses")
    print("Game Over")
else:
    print("you loss the game")
    print("Game Over")
