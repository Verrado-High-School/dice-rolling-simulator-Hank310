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

randomNum = random.randint(1, 6)

while x <= rollAmount:
	x += 1
	print("Roll Number " + str(RollNum) + ":" + str(randomNum))
	if randomNum == 1:
		As += 1
	if randomNum == 2:
		bs += 1
	if randomNum == 3:
		cs += 1
	if randomNum == 4:
		ds += 1
	if randomNum == 5:
		es += 1
	if randomNum == 6:
		fs += 1
print("Total Rolls :" + str(rollAmount))
print("1s rolled : " + str(As))
print("2s rolled : " + str(bs))
print("3s rolled : " + str(cs))
print("4s rolled : " + str(ds))
print("5s rolled : " + str(es))
print("6s rolled : " + str(fs))
print("Percentages : ")
ap == As / rollAmount
bp == bs / rollAmount
cp == cs / rollAmount
dp == ds / rollAmount
ep == es / rollAmount
fp == fs / rollAmount
print(ap + "%")
print(bp + "%")
print(cp + "%")
print(dp + "%")
print(ep + "%")
print(fp + "%")