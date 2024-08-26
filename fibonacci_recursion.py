def fibonacci(x):
    if x<=1:
        return x
    else:
        return fibonacci(x-1) + fibonacci(x-2)

num_terms = int(input("Enter number of terms that you want in Fibonacci series: "))
fibonacci_series=[]
for x in range(num_terms):
    fibonacci_series.append(fibonacci(x))

print(fibonacci_series)
