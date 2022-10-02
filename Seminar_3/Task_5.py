def fibonacci(n):
	if n<=1:
		return n
	else:
		return(fibonacci(n-1) + fibonacci(n-2))

def fibonacci_nega(n):
	if n<=1:
		return n
	else:
		return(fibonacci_nega(n-2) - fibonacci_nega(n-1))

numbers = int(input("Введите размер ряда фибоначчи: "))

fib_series = []

for i in range(0,numbers):
	fib_series.append(fibonacci_nega(i))

fibonacci_nega(numbers)	
fib_series.reverse()

for i in range(0,numbers):
	fib_series.append(fibonacci(i))

fibonacci(numbers)
print(fib_series)