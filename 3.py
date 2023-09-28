A = int(input("Число: "))
B = int(input("Степень: "))
c = 1
result = A
if B < 0:
	print("ERROR")
else:
	while c < B:
		result = result * A
		c += 1

	print(result)