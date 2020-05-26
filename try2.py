class x:
    def add(self,a,b):
        print(a + b)
        return a + b


class y:
    def sum(self,a,b):
        print(x().add(a,b))

y().sum(4,5)

