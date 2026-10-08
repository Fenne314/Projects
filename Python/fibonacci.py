x = 0
y = 1
times = int(input("How many numbers of the fibonacci row?"))

for i in range(times):
    output = x + y
    print(output)
    x = y
    y = output
