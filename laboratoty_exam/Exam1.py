# Написать программу переставляющую слова в предложении в обратном порядке
# Во входном тексте может быть несколько предложений.

def revers(s):
    s = s.split()
    s.reverse()
    for i in s:
        print(i, end=' ')
    print()


string = input()
revers(string)

# Написать программу переставляющую слова в предложении в обратном порядке