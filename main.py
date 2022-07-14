def fun():
    with open('file.txt', 'r', encoding='utf-8') as f:
        total = []
        for line in f:
            s = line.strip()
            total.append(s)
        for i in total:
            yield i


d = fun()
while True:
    y = input('Читаем дальше? да/нет ')
    if y == 'да':
        try:
            print(next(d))
        except:
            print('закончилось')
            break
    else:
        print('чтение закончилось')



#Создайте функцию infinite(lst, tries), которая будет проходиться по элементам списка lst (целые числа) заданное количество раз (tries) циклически.
#Один раз - один элемент списка.
#После вывода последнего значения последовательности процедура начнется с самого начала.
def infinite(lst, tries):
    if len(lst) >= tries:
        y = lst[:tries]
        return y
    elif len(lst) <= tries:
        coun = tries//len(lst)
        c = tries-len(lst)*coun
        y = lst*coun + lst[:c]
        return y
print(infinite([1, 2, 9], 9))

