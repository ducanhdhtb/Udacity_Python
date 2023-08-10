class FoodInterface():
    def __init__(self, mustCook):
        self.mustCook = mustCook


class IceCream(FoodInterface):
    def __init__(self, flavor):
        self.flavor = flavor
        super().__init__(False)


class HotDog(FoodInterface):
    def __init__(self, meat):
        self.meat = meat
        super().__init__(True)
