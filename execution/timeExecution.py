import time
from execution import dataGenerator
from functions import palindome_solutions as ps
from execution import constants


def takeTimes(size):
    res = []
    for _ in range(size):
        res.append(dataGenerator.getRandomStrings())
    return [
        takeExecutionTime(res, ps.checkPalindrome1),
        takeExecutionTime(res, ps.checkPalindrome2),
        takeExecutionTime(res, ps.checkPalindrome3)
    ]


def takeExecutionTime(array, palindrome_method):
    times = []
    for i in range(len(array)):
        start = time.time()
        palindrome_method(array[i])
        times.append(int(constants.TIME_MULTIPLIER * (time.time() - start)))
    times.sort()
    return times[len(times)//2]
