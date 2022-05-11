player1=(input("enter what the first  player choose"))
player2=(input("enter what the the second player choose"))
r="rock"
s="scisccor"
p="paper"

if(player1=='r' and player2=='s'):
 print("player1 wins")

elif(player1=='r' and player2=='p'):
 print("player2 wins")

elif(player1=='s' and player2=='r'):
 print("player2 wins")

elif(player1=='p' and player2=='s'):
 print("player2 wins")

elif(player1=='p' and player2=='r'):
 print("player1 wins")

else:
 print("player1 wins")
