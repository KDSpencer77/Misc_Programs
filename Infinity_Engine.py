# InfinityEngine
# Coded using Python 3.7.0

ProgramState = 77

x = 2

while ProgramState == 77:
    result = pow(pow(2, x), x)
    print(result)
    x += 2
    if x > 50:
        ProgramState = 69
