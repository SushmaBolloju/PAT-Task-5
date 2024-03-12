from functools import reduce

#defining a lambda function to generate fibonacci sequence

fibonacci = lambda n:reduce(lambda x,_:x+[x[-1]+x[-2]],range(n-2),[0,1])

fibonacci_series=fibonacci(50) #generating a fibonacci series with 50 elements

print(fibonacci_series) #printing fibonacci series

print(len(fibonacci_series))
