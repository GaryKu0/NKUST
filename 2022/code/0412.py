class teacher:
    def __init__(self,a,b):
        self.name = a
        self.weidght = b
    def eat(self):
        self.weidght += 1

i= teacher("Tom",76)
f= teacher("Jack",90)
f.eat()
print(f.weidght)
