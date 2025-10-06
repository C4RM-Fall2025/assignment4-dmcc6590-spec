def FizzBuzz(start, finish):
    outlist = []
    for num in range(start, finish + 1):
        if num % 3 == 0 and num % 5 == 0:
            outlist.append("fizzbuzz")
        elif num % 3 == 0:
            outlist.append("fizz")
        elif num % 5 == 0:
            outlist.append("buzz")
        else:
            outlist.append(num)
    return outlist

result = FizzBuzz(1, 15)
for i, val in enumerate(result, 1):
    print(i, val)