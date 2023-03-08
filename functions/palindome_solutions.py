from memory_profiler import profile

"""Complicated O(n)"""

@profile
def checkPalindrome1(string):
    reversedWord = string[::-1]
    return string == reversedWord


"""Complicated O(n^2)"""

@profile
def checkPalindrome2(string):
    size = len(string)
    if size == 0 or size == 1:
        return True
    if string[0] == string[size - 1]:
        return checkPalindrome2(string[1:size - 1])
    return False


"""Complicated O(n)"""

@profile
def checkPalindrome3(string):
    size = len(string)
    for i in range(size // 2):
        if string[i] != string[size - 1 - i]:
            return False
    return True
