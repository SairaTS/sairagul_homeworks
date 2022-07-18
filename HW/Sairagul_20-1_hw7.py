ten = [i for i in range(1, 11)]
print(ten)
evens = list(filter(lambda x: x % 2 == 0, ten))
print(evens)
kvadrat = list(map(lambda x: x ** 2, evens))
print(kvadrat)

def func(ten):
    while True:
        try:
            index = int(input('Введите индекс>>  '))
            print(ten[index])
        except IndexError:
            print('Такого индекса нет!')
            ind_list = []
            for i in ten:
                ind_list.append(ten.index(i))
            print('Актуальные индексы:', ind_list)
        except ValueError:
            print('Вводите только числа!')

        question = input('Хотите продолжить(нет/да)>> ').lower()
        if question == 'нет':
            break

func(ten)

