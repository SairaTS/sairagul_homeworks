data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

for i in data_tuple:
    if isinstance(i, str):
        letters.append(i)
    else:
        numbers.append(i)

print('Список letters: ', letters)
print('Список numbers: ', numbers)
numbers.remove(6.13)
print('Удалила 6.13 из списка numbers: ', numbers)
old_index = numbers.index(True)
letters.insert(len(letters), numbers.pop(old_index))
print('Переместила True в список letters под конец: ', letters)
numbers.insert(numbers.index(3) + 1, 2)
print('Вставила 2 между 3 и 1 в списке numbers: ', numbers)
numbers.sort()
print('Отсортировала numbers: ', numbers)
letters.reverse()
print('Риверсировала letters: ', letters)
index_C = letters.index('C')
letters.remove('C')
letters.insert(index_C, "c")
letters[1] = letters[letters.index('g')].upper()
print('Изменила пару букв в letters: ', letters)
numbers_copy = numbers.copy()
numbers.clear()

for j in numbers_copy:
    j = j ** 2
    numbers.append(j)
print('Изменила список numbers в список квадратов своих же чисел: ', numbers)

tuple1 = (*numbers,)
print('Кортеж numbers: ', tuple1)
tuple2 = (*letters, )
print('Кортеж letters:', tuple2)
