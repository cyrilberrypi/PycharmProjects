class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("Hi, it's me" + ", " + f'{self.name}')


Cyril = Person("Cyril Amara")
print(Cyril.name)
Cyril.talk()
