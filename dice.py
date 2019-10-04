#Hank Warner
#P1, Dice Rolling Sim
import random

As = 0
bs = 0
cs = 0
ds = 0
es = 0
fs = 0

x = 1

RollNum = 1

rollAmount = int(input("How many times should it roll?"))

while x <= rollAmount:
	randomNum = random.randint(1, 6)
	x += 1
	print("Roll Number " + str(int(x)) + ":" + str(int(randomNum)))
	if randomNum == 1:
		As += 1
	elif randomNum == 2:
		bs += 1
	elif randomNum == 3:
		cs += 1
	elif randomNum == 4:
		ds += 1
	elif randomNum == 5:
		es += 1
	else:
		fs += 1
	
print("Total Rolls :" + str(rollAmount))
print("1s rolled : " + str(As))
print("2s rolled : " + str(bs))
print("3s rolled : " + str(cs))
print("4s rolled : " + str(ds))
print("5s rolled : " + str(es))
print("6s rolled : " + str(fs))
print("Percentages : ")

print("1s " + str(100 * As/rollAmount) + " %")
print("2s " + str(100 * bs/rollAmount) + " %")
print("3s " + str(100 * cs/rollAmount) + " %")
print("4s " + str(100 * ds/rollAmount) + " %")
print("5s " + str(100 * es/rollAmount) + " %")
print("6s " + str(100 * fs/rollAmount) + " %")