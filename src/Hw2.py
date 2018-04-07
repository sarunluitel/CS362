from scipy.optimize import minimize
import numpy as np
from Food import Food

apple = Food('Apple', 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
apple1 = Food('Apple1', 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
chips = Food('chips', 1.0, 10.0, 10.0, 1.0, 1.0, 1.0, 1.0)
chips1 = Food('chips1', 1.0, 10.0, 10.0, 1.0, 1.0, 1.0, 1.0)
chips2 = Food('chips2', 1.0, 10.0, 10.0, 1.0, 1.0, 1.0, 1.0)

FoodList = [apple, apple1, chips, chips1, chips2]


def objective(foodNum):
    totalPrice, index = 0, 0
    for food in FoodList:
        totalPrice += foodNum[index] * food.price()
        index += 1
    return totalPrice


def fat(foodNum):
    fat, index = 0, 0
    for food in FoodList:
        fat += foodNum[index] * food.fat()
    return 20 - fat


def sodium(foodNum):
    sodium, index = 0, 0
    for food in FoodList:
        sodium += foodNum[index] * food.sodium()
        index += 1
    return 2400 - sodium


def vitC(foodNum):
    vitC, index = 0,0
    for food in FoodList:
        vitC += foodNum[index] * food.vitC()
        index += 1
    return vitC - 90


def vitA(foodNum):
    vitA, index = 0, 0
    for food in FoodList:
        vitA += foodNum[index] * food.vitA()
        index += 1
    return vitA - 700


def protien(foodNum):
    protein, index = 0, 0
    for food in FoodList:
        protein += foodNum[index] * food.protein()
        index += 1
    return protein - 56


def calories(foodNum):
    calories, index = 0,0
    for food in FoodList:
        calories += foodNum[index] * food.calories()
        index += 1
    return 2000 - calories


def main():
    #  Order of parameters (name, price, calories, fat, sodium, vitC, vitA, protein)

    con1 = {'type': 'eq', 'fun': calories}
    con2 = {'type': 'ineq', 'fun': fat}
    con3 = {'type': 'ineq', 'fun': sodium}
    con4 = {'type': 'ineq', 'fun': vitC}
    con5 = {'type': 'ineq', 'fun': vitA}
    con6 = {'type': 'ineq', 'fun': protien}

    allcons = [con1, con2, con3, con4, con5, con6]
    foodnum = np.array([1, 1, 1, 1, 1])

    solution = minimize(objective, foodnum, method='SLSQP', constraints=allcons)

    print(solution)


if __name__ == '__main__':
    main()
