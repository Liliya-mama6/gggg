class House:
    def __init__(self, name, nmb):
        self.name=name
        self.nmb=nmb
    def go_to(self, nf):
        if nf>self.nmb or nf<1:
            print("Такого этажа не существует")
        else:
            for i in range(1, nf+1):
                print(i)
    def __len__(self):
        return self.nmb
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей {self.nmb}.'
fff=House('tont', 88)
print(len(fff))
print(str(fff))