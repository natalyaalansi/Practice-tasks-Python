# 1) Наследование (Голубь(Dove) и Соловей(Philomel)ялвляются наследниками базового класса Птица(Bird)).
# В классе Соловей(Philomel) используется метод родительского класса __init__, Голубь(Dove) является
# наследником, но не реализует метод родительского класса.
# 2) Поле __tempo_jump и метод __speed_up инкапсулированы в классе Соловей(Philomel),
# использовать можно только на уровне текущего класса.
# 3) В классах Голубь(Dove) и Соловей(Philomel) есть метод get_tempo, который в каждом классе
# переопределяется по-своему

class Bird:
    def __init__(self, sing):
        self.sing = sing

    def get_sing(self):
        return self.sing

class Philomel(Bird):
    __tempo_jump = 2

    def __init__(self, sing, tempo):
        Bird.__init__(self, sing)
        self.tempo = tempo

    def get_tempo(self):
        return "Я пою очень нежно. Мой темп - %d ударов в минуту" % self.tempo

    def __speed_up(self):
        return self.__tempo_jump * self.tempo

    def get_speed_up(self):
        return "Кажется, я распелся, можно и ускориться! ДО %d ударов в минуту" % self.__speed_up()

class Dove(Bird):

    def __init__(self, tempo):
        self.tempo = tempo

    def get_tempo(self):
        return "Я просто воркую - %d ударов в минуту" % self.tempo


philomel = Philomel("Трильлильлиль", 100)
youngPhilomel = Philomel("Трультруль", 70)
dove = Dove(20)

print("СОЛОВЕЙ: " + str(philomel.get_sing()))
print(str(philomel.get_tempo()))
print(philomel.get_speed_up())
print("---------------------------------------------------------------")
print("ДЕТЕНЫШ СОЛОВЬЯ: " + str(youngPhilomel.get_sing()))
print(str(youngPhilomel.get_tempo()))
print(youngPhilomel.get_speed_up())
print(youngPhilomel._Philomel__speed_up())
print("---------------------------------------------------------------")
print("ГОЛУБЬ: " + dove.get_tempo())
