import os
a = int(input("Input 1st edge: "))
b = int(input("Input 2nd edge: "))
c = int(input("Input 3rd edge: "))
if (a + b > c) and (c + a > b) and (b + c > a):
    p = (a + b + c) / 2
    cos_alpha = (b ** 2 + c ** 2 - a ** 2)/(2 * b * c)
    tg_alpha_2_2 = (1 - cos_alpha) / (1 + cos_alpha)
    S = 3.14 * (p - a) ** 2 *tg_alpha_2_2
    print(S)
else:
    print("Incorrect values of the edges")