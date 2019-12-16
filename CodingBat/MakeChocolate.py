''' website: https://codingbat.com/prob/p190859

Problem Statement: We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). 
Return the number of small bars to use, assuming we always use big bars before small bars. 
Return -1 if it can't be done.

'''

def make_chocolate(small, big, goal):
  
  while(big * 5 > goal):
    big = big - 1
  
  maxchoco = small + big * 5
  
  if maxchoco >= goal:
    extra = maxchoco - goal
    used = (small - extra)
    return used
  else:
    return -1



a = make_chocolate(4, 1, 9)
b = make_chocolate(4, 1, 10)
c = make_chocolate(4, 1, 7)

print(a)
print(b)
print(c)