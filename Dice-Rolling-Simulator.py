#Hank Warner
#P1, Dice Rolling Sim
import random

1s = 0
2s = 0
3s = 0
4s = 0
5s = 0
6s = 0

x = 1

RollNum = 1

rollAmount = int(input("How many times should it roll?"))

randomNum = random.randint(1, 6)

while x <= rollAmount:
	x += 1
	print(randomNum)
	if randomNum == 1:
		1s += 1
	if randomNum == 2:
		2s += 1
	if randomNum == 3:
		3s += 1
	if randomNum == 4:
		4s += 1
	if randomNum == 5:
		5s += 1
	if randomNum == 6:
		6s += 1
print("Total Rolls :" + rollAmount)
print("1s rolled : " + 1s)
print("2s rolled : " + 2s)
print("3s rolled : " + 3s)
print("4s rolled : " + 4s)
print("5s rolled : " + 5s)
print("6s rolled : " + 6s)
print("Percentages : ")
print(1s / rollAmount + "%")
print(2s / rollAmount + "%")
print(3s / rollAmount + "%")
print(4s / rollAmount + "%")
print(5s / rollAmount + "%")
print(6s / rollAmount + "%")