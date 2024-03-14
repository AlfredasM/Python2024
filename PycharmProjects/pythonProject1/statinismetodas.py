class MatematiniaiVeiksmai:
    @staticmethod
    def sudetis(a,b):
        return a + b

    @staticmethod
    def atimtis(x,y):
        return x - y

#statiniame metode nereikia
#sudetis = MatematiniaiVeiksmai()
# sudetis.sudetis(4, 5)


sudetis1 = MatematiniaiVeiksmai.sudetis(5,7)
atimtis = MatematiniaiVeiksmai.atimtis(10,2)
sudetis2 = MatematiniaiVeiksmai.sudetis('labas', 'rytas')

print(atimtis)
print(sudetis1)
print(sudetis2)