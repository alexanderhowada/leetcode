import re
import math


def get_num_den(exp):
    num_denon = exp.split('/')
    num = [int(num_denon[0])]
    num += [int(re.findall("[-\+]\d+", nd, 0)[0]) for nd in num_denon[1:-1]]

    denon = []
    denon += [int(re.findall("(\d+)[-\+]?", nd, 0)[0]) for nd in num_denon[1:]]
    return num, denon

def get_num_den_n(num, denon):
    denominator = math.prod(denon)
    total = 0
    for n, d in zip(num, denon):
        total += denominator*n//d
    d = math.gcd(total, denominator)
    return total//d, denominator//d

class Solution:
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        num, denon = get_num_den(expression)
        n, d = get_num_den_n(num, denon)
        return f"{n}/{d}"
