# Цилиндр Джеферсона - это механический шифровальный аппарат, который состоит из нескольких дисков, на которых записаны алфавиты (состоящие из одинаковых символов, но в случайном порядке).
#
#Для шифрования с его помощью текст разбивают на блоки, длинная каждого блока равна числу дисков в механизме.
#
#Каждый символ блока шифруется с помощью алгоритма Цезаря с использованием соответствующего диска (т.е. 1й символ с помощью 1 диска, 2й символ с помощью 2 диска и т.д.) с общим сдвигом.
#
#Таким образом сдвиг (ключ для шифрования Цезаря) не является секретом для цилиндра Джеферсона - цилиндры легко повернуть вокруг оси и на них видны сразу все комбинации расшифровки, так что даже не требуется брутфорс. Однако, если сами цилиндры (а значит и порядок символов в алфавитах) хранятся в секрете, а так же в секрете порядок следования алфавитов, то такой метод шифрования очень надёжен.

import random
#n = int(input())
#clear_alphabet = input()
discs = []
random.seed(42)
for i in range(n):
    alph = list(map(str, clear_alphabet))
    random.shuffle(alph)
    discs.append(alph)
d = []
strok = ""
for i in discs:
    for o in i:
        strok += o
    d.append(strok)
    strok = ""
discs = d
#print("DISCS:")
#for i in discs:
#    print(i)
#print()
def jefferson_encryption(text, discs, step, reverse=False):
    text = text.upper()
    new_text = ""
    for i in text:
        if i in clear_alphabet:
            new_text+=i
    k = 0
    result = ""
    for t in new_text:
        i = discs[k].index(t)
        if reverse==False:
            i = (i + step)%len(clear_alphabet)
        elif reverse==True:
            i = (i - step)%len(clear_alphabet)
        result +=discs[k][i]
        k += 1
        if k>(n-1):
            k = 0
    return result
    #print("Encription (step="+str(step)+"):")
    #print(result)
    #print("Decryption back (step="+str(step)+"):")
    #return new_text
#print(jefferson_encryption(text = "Some encripted text",step = 13, discs = discs, reverse=False))
