# THE ALGORITHM
# 1. Generate a Hundred data set for both the x_values and the function values
# 2. Collect the number that the user wants for the not interpolation
# 3.Find the number of figures in the data set. In our case 100
# 4.Set the summation of the function to zero
# 5.Create two for loops in which one is nested into the other and set both ranges to the number of figures in the data set, minus 1
# 6.Create a variable (prod) in the first for loop and set it to 1. This would be for the multiplications.
# 7.For every count(i) round of looping in the first for loop, run the second for loop and multiply prod by the new function values
# 8.In the second for loop, for every count(i) round of looping, if i is not equal to j, the previous value of prod is multiplied by the difference in values of the function values divide by difference in the x_values
# 9.Sum up all the previous values of prod
# 10.Display the summation


import random
n = int(input("Enter the number of figure:\n"))
x_values = []
y_values = []

print("Enter your x values:")
for f in range(n):
    x_values.append(float(input()))

print("Enter your y values:")
for f in range(n):
    y_values.append(float(input()))


x = float(input("Enter your Interpolating figure:\n"))

summation = 0
for i in range(0, n):
    prod = 1
    for j in range(0, n):
        if i != j:
            prod *= (x - x_values[j]) / (x_values[i] - x_values[j])

    prod *= y_values[i]
    summation += prod


print(summation)
