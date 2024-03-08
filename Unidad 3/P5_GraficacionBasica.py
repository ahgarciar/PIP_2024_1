
from matplotlib import pyplot

x = [i for i in range(-10, 11)]
print(x)

#y = x^2

y = [xi**2 for xi in x]
print(y)

pyplot.plot(x, y)
pyplot.show()

