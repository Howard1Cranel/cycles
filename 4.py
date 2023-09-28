num = int(input("Число: "))
result = 1
if num < 0:
	print("ERROR")
else:
	for i in range(1,num + 1):
		result = result * i
	print(result)
