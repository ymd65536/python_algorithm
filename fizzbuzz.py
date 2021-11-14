# FizzBuzz

nums= [cnt for cnt in range(1,101)]

for i in nums:
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 5 == 0 :
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)