def fibonacci(n):
   if n == 0:
        return 0
   elif n == 1:
        return 1
   else:
        return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
   if n == 0:
        return 2
   elif n == 1:
        return 1
   else:
        return lucas(n-1) + lucas(n-2)

# example
n = 10
fibonacci_sequence = [fibonacci(i) for i in range(n)]
lucas_series = [lucas(i) for i in range(n)]
print(f"Fibonacci sequence up to {n} terms: {fibonacci_sequence}")
print(f"Lucas series up to {n} terms: {lucas_series}")
