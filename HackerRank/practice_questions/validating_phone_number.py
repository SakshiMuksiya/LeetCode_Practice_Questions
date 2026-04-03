#https://www.hackerrank.com/contests/assessment-23-2-1676278643/challenges/validating-the-phone-number

import re

n = int(input())
regex_patt = r"^[7-9][0-9]{9}$"
for i in range(n):
    numb = input()
    print("YES" if re.match(regex_patt,numb) else "NO")
