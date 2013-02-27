def factorial(num):
    iteration = 1
    for x in range(1, (num + 1)):
        iteration = x * iteration
    return iteration
    
numberString = str(factorial(100))
total = 0

for x in numberString:
    total += int(x)
    
print total