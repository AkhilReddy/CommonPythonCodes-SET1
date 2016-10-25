import math

X = 2.4
print math.ceil(X)
#Return the ceiling of x as a float, the smallest integer value greater than or equal to x.

Y= -1
print math.copysign(X,Y)
#Return x with the sign of y. On a platform that supports signed zeros, copysign(1.0, -0.0) returns -1.0.
x = -2.5999999999999
print math.fabs(x)
#Return the absolute value of x.
x =10
print math.factorial(x)
#Return x factorial. Raises ValueError if x is not integral or is negative.
x=2.5
print math.floor(x)
#Return the floor of x as a float, the largest integer value less than or equal to x.
x = 3.6
y = -2.2
print math.fmod(x, y)
#Return fmod(x, y), as defined by the platform C library. Note that the Python expression x % y may not return the same result.
#The intent of the C standard is that fmod(x, y) be exactly (mathematically; to infinite precision) equal to x - n*y for some integer n
#such that the result has the same sign as x and magnitude less than abs(y).
#Python’s x % y returns a result with the sign of y instead, and may not be exactly computable for float arguments.
#For example, fmod(-1e-100, 1e100) is -1e-100, but the result of Python’s -1e-100 % 1e100 is 1e100-1e-100, which cannot be represented exactly as a float, and
#rounds to the surprising 1e100.
#For this reason, function fmod() is generally preferred when working with floats, while Python’s x % y is preferred when working with integers.
x = 2.5
print math.frexp(x)
#Return the mantissa and exponent of x as the pair (m, e). m is a float and e is an integer such that x == m * 2**e exactly.
#If x is zero, returns (0.0, 0), otherwise 0.5 <= abs(m) < 1. This is used to “pick apart” the internal representation of a float in a portable way.
iterable = [1,2.4,5.333,4,5.6]
print math.fsum(iterable)
#Return an accurate floating point sum of values in the iterable. Avoids loss of precision by tracking multiple intermediate partial sums:
'''
>>> sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
0.9999999999999999
>>> fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
1.0
The algorithm’s accuracy depends on IEEE-754 arithmetic guarantees and the typical case where the rounding mode is half-even.
On some non-Windows builds, the underlying C library uses extended precision addition and may occasionally double-round an intermediate sum
causing it to be off in its least significant bit.
'''
print "ok"
#x = pow(10,pow(10,100))
x = 111111111111111111111111111111111111
print math.isinf(x)
#Check if the float x is positive or negative infinity.
x = -0.2
print math.isnan(x)
#Check if the float x is a NaN (not a number). For more information on NaNs, see the IEEE 754 standards.
print "ok"
x = 3
i = 2
print 'x:',3,'i:',i
print math.ldexp(x, i)
#Return x * (2**i). This is essentially the inverse of function frexp().
print "ok"
x = 4.5
a = math.modf(x)

print a
#Return the fractional and integer parts of x. Both results carry the sign of x and are floats.

x = 10
print math.trunc(x)
#Return the Real value x truncated to an Integral (usually a long integer). Uses the __trunc__ method.

#Note that frexp() and modf() have a different call/return pattern than their C equivalents: they take a single argument and return a pair of values,
#rather than returning their second return value through an ‘output parameter’ (there is no such thing in Python).

#For the ceil(), floor(), and modf() functions, note that all floating-point numbers of sufficiently large magnitude are exact integers.
#Python floats typically carry no more than 53 bits of precision (the same as the platform C double type),
#in which case any float x with abs(x) >= 2**52 necessarily has no fractional bits.

'''
 Power and logarithmic functions
'''

math.exp(x)
#Return e**x.

math.expm1(x)
#Return e**x - 1. For small floats x, the subtraction in exp(x) - 1 can result in a significant loss of precision; the expm1() function provides a way to compute this quantity to full precision:

'''
>>>
>>> from math import exp, expm1
>>> exp(1e-5) - 1  # gives result accurate to 11 places
1.0000050000069649e-05
>>> expm1(1e-5)    # result accurate to full precision
1.0000050000166668e-05
'''
x = 10
#math.log(x[, base])
math.log(x,2)
#With one argument, return the natural logarithm of x (to base e).
#With two arguments, return the logarithm of x to the given base, calculated as log(x)/log(base).

math.log1p(x)
#Return the natural logarithm of 1+x (base e). The result is calculated in a way which is accurate for x near zero.

math.log10(x)
#Return the base-10 logarithm of x. This is usually more accurate than log(x, 10).

math.pow(x, y)
#Return x raised to the power y. Exceptional cases follow Annex ‘F’ of the C99 standard as far as possible. In particular, pow(1.0, x) and pow(x, 0.0) always return 1.0,
#even when x is a zero or a NaN. If both x and y are finite, x is negative, and y is not an integer then pow(x, y) is undefined, and raises ValueError.
#Unlike the built-in ** operator, math.pow() converts both its arguments to type float. Use ** or the built-in pow() function for computing exact integer powers.

math.sqrt(x)
#Return the square root of x.

'''
Trigonometric functions
'''
x = math.degrees(60)
print math.cos(x)
#Return the arc cosine of x, in radians.
x = 2*math.pi
math.asin(math.pi)
#Return the arc sine of x, in radians.

math.atan(x)
#Return the arc tangent of x, in radians.

math.atan2(y, x)
#Return atan(y / x), in radians. The result is between -pi and pi. The vector in the plane from the origin to point (x, y) makes this angle with the positive X axis. The point of atan2() is that the signs of both inputs are known to it, so it can compute the correct quadrant for the angle. For example, atan(1) and atan2(1, 1) are both pi/4, but atan2(-1, -1) is -3*pi/4.

math.cos(x)
#Return the cosine of x radians.

math.hypot(x, y)
#Return the Euclidean norm, sqrt(x*x + y*y). This is the length of the vector from the origin to point (x, y).

math.sin(x)
#Return the sine of x radians.

math.tan(x)
#Return the tangent of x radians.

'''
Angular conversion
'''

math.degrees(x)
#Convert angle x from radians to degrees.

math.radians(x)
#Convert angle x from degrees to radians.

'''
Constants
'''
math.pi
#The mathematical constant π = 3.141592..., to available precision.

math.e
#The mathematical constant e = 2.718281..., to available precision.
