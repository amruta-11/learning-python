''' link: https://codingbat.com/prob/p118406'''
''' Problem Statement: We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) 
and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. 
This is a little harder than it looks and can be done without any loops. 

make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
'''

def make_bricks(small, big, goal):
  if (small * 1) + (big * 5) < goal:
    return False
  
  qty = goal % 5
  if qty <= small:
    return True
  else:
    return False

a = make_bricks(3, 1, 8)
b = make_bricks(3, 1, 9)

print(a)
print(b)