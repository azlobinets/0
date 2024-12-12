def single_root_words(root_word,  *other_words): # пусть известно, что переменный параметр будет принимать последовательность строк и каждая строка будет являться словом.
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower(): # переводим в нижний регистр
            same_words.append(i)

        if i.lower() in root_word.lower():
            same_words.append(i)

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
