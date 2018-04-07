class Food():

    def __init__(self, name, price, calories, fat, sodium, vitC, vitA, protein):
        self._name = name
        self._calories = calories  # in calories
        self._fat = fat  # in grams
        self._sodium = sodium  # in milligrams
        self._vitC = vitC  # in milligrams
        self._vitA = vitA  # in mcg
        self._protein =protein  # in grams
        self._price = price  # in dollars

    def name(self):
        return self._name

    def price(self):
        return self._price

    def fat(self):
        return self._fat

    def sodium(self):
        return self._sodium

    def vitC(self):
        return self._vitC

    def vitA(self):
        return self._vitA

    def calories(self):
        return self._calories

    def protein(self):
        return self._protein
