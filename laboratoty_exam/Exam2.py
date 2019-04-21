
def magic():
    cipher = [("h", "z"), ("e", "?"), ("l", "."), ("o", "x"), ("x", "o"), (".", "l"),
             ("?", "e"), ("z", "h"), ("!", "y"), ("y", "!")]

    s = input("Введите текст для шифровки/дешифровки: ")
    print(s.translate(str.maketrans(dict(cipher))))

magic()

# hello!