# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
number = int(input("Ведите число N: "))
i = 2 # первое простое число
list_simpleNumbers = []
old = number
while i <= number:
    if number % i == 0:
        list_simpleNumbers.append(i)
        number //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old} приведены в списке: {list_simpleNumbers}")