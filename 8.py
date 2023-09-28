num = int(input("Число: "))
summa = 0
proiz = 1

while num > 0:
    G = num % 10
    summa += G
    proiz *= G
    num = num // 10

print("Сумма цифр:", summa)
print("Произведение цифр:", proiz)
