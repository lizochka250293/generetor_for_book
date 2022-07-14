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



