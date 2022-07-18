l, r, m = 0, 100, 50
i = 0
k = input("Загадайте число: ")
file = open("result.txt", "w")
while True:
    print(f"Загаданное вами число равно {m}?")
    otvet = input()
    i += 1
    if otvet == '>':
        l = m
        m = (l + r) // 2
    elif otvet == '<':
        r = m
        m = (l + r) // 2
    elif otvet.lower() == 'да':
        print(f"\nКоличество попыток: {i}")
        file.writelines(f"\nКоличество попыток: {i}")
        file.writelines(f"\nУгаданное число: {m}")
        file.close()
        break

