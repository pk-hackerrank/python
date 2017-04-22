# importing math
import math
# Reading AB
a = int(input())
# Reading BC
b = int(input())
# angle MBC is equal to angle BCA
# so tan(o) = opp side / adjacent side
t = a/b
# calculating inverse gives the value in radians.
t = math.atan(t)
# converting radians into degrees
t = math.degrees(t)
# Rounding to 0 decimals and adding degree symbol.
print(str(int(round(t,0))) + '°')