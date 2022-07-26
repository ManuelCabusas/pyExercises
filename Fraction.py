#!/usr/bin/python3
# Fraction.py implementation

def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n
        
        m = old_n
        n = old_m % old_n
    return n

class Fraction:
    def __init__(self, top, bottom):
        g = gcd(top, bottom)
        self.num = top/g
        self.den = bottom/g
        
    def __repr__(self):
        return str(self.num) + '/' + str(self.den)
    
    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
    
    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __eq__(self, other):
        num1 = self.num * other.den
        num2 = self.den * other.num
        return num1 == num2
    
    def __gt__(self, other):
        num1 = self.num * other.den
        num2 = self.den * other.num
        return num1 > num2
    
    def __ge__(self, other):
        num1 = self.num * other.den
        num2 = self.den * other.num
        return num1 >= num2
    
    def __lt__(self, other):
        num1 = self.num * other.den
        num2 = self.den * other.num
        return num1 < num2
    
    def __le__(self, other):
        num1 = self.num * other.den
        num2 = self.den * other.num
        return num1 <= num2
    
    def __ne__(self, other):
        num1 = self.num * other.den
        num2 = self.den * other.num
        return num1 != num2
    
    def get_num(self):
        return self.num
    
    def get_den(self):
        return self.den
        
