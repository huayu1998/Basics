def FizzBuzz():
    temp = 1
    while temp <= 20:
        if temp % 3 == 0 and temp % 5 == 0:
            print('FizzBuzz')
        elif temp % 3 == 0:
            print('Fizz')
        elif temp % 5 == 0:
            print('Buzz')
        # Update the temp
        temp += 1

FizzBuzz()
