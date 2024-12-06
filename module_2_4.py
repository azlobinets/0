numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for i in range(0, len(numbers)):  # перебираем индексы списка

    if numbers[i] == 1:
        continue  # пропускаем число, если оно является единицей

    if numbers[i] == 2:
        primes.append(numbers[i])  # помещает элемент в конец списка
        continue

    is_not_primes = False  # флаг
    for j in range(2, numbers[i]):  # перебираем делители

        if (numbers[i] % j) == 0:
            not_primes.append(numbers[i])  # помещает не простое в конец списка

            is_not_primes = True 
            break  # меняем флаг и выходим из цикла

    if is_not_primes == True:
        continue  # если число не простое, то возвращаемся к началу цикла 

    primes.append(numbers[i])  # помещает простое число в конец списка

print("Primes: ", primes)
print("Not primes: ", not_primes)
