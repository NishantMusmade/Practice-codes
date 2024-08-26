def fibonacci(num):
    num = num-2
    num1 = 0
    num2 = 1

    print(num1,end = ' ')
    print(num2,end = ' ')

    while num>0:
        result = num1+num2
        num1 = num2
        num2 = result
        print(result,end = ' ')
        num = num-1



num= int(input("Enter the number upto which you want to print Fibonacci series: "))

fibonacci(num)
