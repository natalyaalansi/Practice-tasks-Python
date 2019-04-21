# Введенную с клавиатуры строку вывести на экран наоборот (использовать цикл)(0,5 балла)

def revers(s):
    string = ''
    # Вызываем функцию, ей в качестве аргумента точку
    s = s.split('.')
    for i in range(0, len(s)):
        string += s[i][::-1].strip() + '. '
    print(string)

strl = input()
revers(strl)