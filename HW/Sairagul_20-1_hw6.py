def first_word_find(word):
    if not type(word) == str:
        print(False)
    else:
        first_word = word.split()[0]
        print("First word in my string is", first_word)

word_input = input('Enter the string: ')
if word_input == '':
    word_def = 'Hello World'
    first_word_find(word_def)
else:
    first_word_find(word_input)

print('\n\nSecond Function: \n')

def avg(user_list):
    for i in range(len(user_list)):
        user_list[i] = int(user_list[i])
    avg = sum(user_list) / len(user_list)
    print("Average of numbers = ", int(round(avg, 2)))

input_string = input('Enter elements of a list separated by * :>> ')
user_list = input_string.split('*')
print('List of numbers: ', user_list)
avg(user_list)

print('\n\nThird Function: \n')

def check_passw(password):
    letters='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    numbers='0123456789'
    count_let = 0
    count_num = 0
    psw_list = list(password)
    if len(password)>=6:
        for i in psw_list:
            if i in letters:
                count_let+=1
            else:
                count_num+=1
        if count_let != 0 and count_num != 0:
            print(True)
        else:
            print(False)
    else:
        print(False)

password = input('Enter your password:>> ')
check_passw(password)

