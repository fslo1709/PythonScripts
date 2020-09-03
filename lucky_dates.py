import random

day_list = [i+1 for i in range(366)]

months = [31,29,31,30,31,30,31,31,30,31,30,31]
monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
				"Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

random.shuffle(day_list)

for j in range(len(months)):
	if j == 0:
		continue
	months[j] = months[j] + months[j-1]

count = 0

for x in day_list:
	count += 1
	for y in range(len(months)):
		if x < months[y]:
			print("{}. {}/{}".format(count, monthNames[y], months[y] - x))
			break

print("This is the official list of the luckiest birthdates")
print("Look for yours up in the list!")
