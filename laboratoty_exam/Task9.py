# 12. Из заданного текста удалить все знаки препинания (2 балла)
import string

def remove():
    # Создаем таблицу перевода символов с помощью метода maketrans (без знаков пунктуации, метод punctuation )
    table = str.maketrans({key: "" for key in string.punctuation})
    print(table)
    # translate() возвращает копию строки, в которой все символы были переведены с помощью maketrans
    out = s.translate(table)
    print(out)

s=("Скреативлен креатив не по-креативному, нужно перекреативить!")
remove()