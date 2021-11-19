# FizzBuzz

def fizz_buzz(num:int):
    for cnt_i in range(1,num):
        if cnt_i % 15 == 0 :
            print('FizzBuzz')
        elif cnt_i % 3 == 0 :
            print('Fizz')
        elif cnt_i % 5 == 0 :
            print('Buzz')
        else:
            print(str(cnt_i))

if __name__ == '__main__':
    fizz_buzz(100)