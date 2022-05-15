import numpy as np
from sympy import li
from tabulate import tabulate
from math import *

def eulere(der,stratx,h,starty,endx):
    calc = EulerCalculator()
    points = calc.evaluate(
    derivative=der, startX=stratx, startY=starty, endX=stratx+endx*h, stepSize=h
    )
    v=dict()
    i=0
    for y in points:
        v[i]={"x":str(y[0]),"y":(str(y[1]))}
        i+=1

    return v

class EulerCalculator:
    __quirkDict = dict()

    def __preprocess(self, inputString):
        if len(self.__quirkDict) == 0:
            with open("quirks.txt", "r") as fin:
                quirks = fin.readlines()
            for quirk in quirks[:-1]:
                original, final = tuple(quirk.split(", "))
                final = final[:-1]
                self.__quirkDict[original] = final
        for quirk in self.__quirkDict.keys():
            inputString = inputString.replace(quirk, self.__quirkDict[quirk])
        return inputString

    def __getFunction(self, inputString):
        inputString = self.__preprocess(inputString)
        return lambda x, y: eval(inputString)

    def evaluate(self, **args):
        requiredArgs = ["derivative", "startX", "startY", "endX", "stepSize"]
        for arg in requiredArgs:
            if arg not in args:
                raise ValueError(arg + " is invalid")
        derivative = args["derivative"]
        startX = args["startX"]
        startY = args["startY"]
        endX = args["endX"]
        stepSize = args["stepSize"]
        if abs(stepSize) < pow(10, -4):
            raise ValueError("Step size is too small")
        derivativeFunction = self.__getFunction(derivative)
        currentValue = startY
        data = []
        while abs(startX - endX - stepSize) >= pow(10, -4):
            data.append(
                [startX, currentValue,]
            )
            currentValue += stepSize * derivativeFunction(startX, currentValue)
            startX += stepSize
        return data

    def print(self, data):
        return tabulate(data, headers=["x", "y"])




