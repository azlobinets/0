#1
example="any string"

#2
print(example[0])

#3
print(example[-1])

#4
print(example[4:])

#Решение для любой строки:
a=(len(example)-(len(example)//2+1)) # находим индекс, с которого начинается вторая пловина строки, содержащая нечётное число симвлов.
print(example[a:])

#5
print(example[::-1])

#6
print(example[1::2])

#7
example = 'Топинамбур'
print(example[0])
print(example[-1])
print(example[5:])
print(example[::-1])
print(example[1::2])