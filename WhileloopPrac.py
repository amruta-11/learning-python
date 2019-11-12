# while loop
given_list = [5, 4, 4, 3, 1, -2, -3, -5]
total = 0
i = 0
while given_list[i] > 0:
	total += given_list[i]
	i += 1
print(total)

# while loop with break
given_list1 = [5, 4, 4, 3, 1, -2, -3, -5]
total1 =  0
for element in given_list1:
	if element <= 0:
		break
	total1 += element
print(total1)

T = 0
for i in range(1, 100):
	if i % 3 == 0 or i % 5 == 0:
		T += i

print(T)

