num = int(input("Число: "))
summa= 0

while num > 0:
    G = num % 10
    if G % 2 == 0:
        summa += G
    num = num // 10

print("Сумма четных цифр:", summa)
