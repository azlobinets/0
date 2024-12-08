a = int(input ("Введите число от 3 до 20: "))

b=[]
for i in range(1,a):

    for j in range(1,a):
        if a % (i+j) == 0:

            if [j,i] in b:  # проверка элемента на уникальность
                pass
            else:
                b.append([i,j])


result = ""  # Создаем пустую строку
for sublist in b: # Проходим по каждому подсписку и добавляем его элементы в строку
    result = result + ''.join(map(str, sublist))  # Преобразуем подсписки в строки и соединяем их

print(result)

