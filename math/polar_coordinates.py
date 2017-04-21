# Importing phase and polar from cmath
# Complex form a+bj, Polar coordinates (r,phi)
from cmath import phase, polar
# Reading input String
given_input = input()
# Converting given string into complex number i.e. a+bj format
in_complex_format = complex(given_input)
#calc_r = abs(in_complex_format) # abs gives the r of polar coordinates 
#calc_teta = phase(in_complex_format) # phase gives the phi of polar coordinates
# We can also use polar which will give the r and phi directly as a tuple.
(calc_r_using_polar, calc_teta_using_polar) = polar(in_complex_format)
#print(calc_r)
#print(calc_teta)
print(calc_r_using_polar)
print(calc_teta_using_polar)