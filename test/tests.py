import unittest
from functions import palindome_solutions as ps

lis = ["oso", "aibofobia", "girafarig", "sometemos", "reconocer", "arenera"]
notPalindrome = ["seco", "palabra", "papa", "acordeon", "juicio", "tarot"]


class testPalindromeAlgorithms(unittest.TestCase):
    def test_check_palindrome_1(self):
        for i in range(len(lis)):
            if not ps.checkPalindrome1(lis[i]):
                self.fail()

    def test_check_palindrome_2(self):
        for i in range(len(lis)):
            if not ps.checkPalindrome2(lis[i]):
                self.fail()

    def test_check_palindrome_3(self):
        for i in range(len(lis)):
            if not ps.checkPalindrome3(lis[i]):
                self.fail()

    def test_check_not_palindrome_1(self):
        for i in range(len(notPalindrome)):
            if ps.checkPalindrome1(notPalindrome[i]):
                self.fail()

    def test_check_not_palindrome_2(self):
        for i in range(len(notPalindrome)):
            if ps.checkPalindrome2(notPalindrome[i]):
                self.fail()

    def test_check_not_palindrome_3(self):
        for i in range(len(notPalindrome)):
            if ps.checkPalindrome3(notPalindrome[i]):
                self.fail()


if __name__ == '__main__':
    unittest.main
