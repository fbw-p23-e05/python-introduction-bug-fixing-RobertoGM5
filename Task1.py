three_mul = 'fizz'
five_mul = 'buzz'
both = 'fizzbuzz'

num1 = 3
num2 = 5
max_num = 100
for i in range(1,max_num):
    # % or modulo division gives you the remainder
    
    if i%num1 == 0 and i%num2 == 0:
        print(i, both)
    elif i%num1 == 0:
        print(i, three_mul)
    elif i%num2 == 0:
        print(i, five_mul)
    