def fibonacci(n):

  if n <= 1:
    return 1
    
  else:
    a, b = 1,1
    for i in range(2, n + 1):
      c = a + b
      a = b
      b = c
    return c


num_terms = 50
fibonacci_sequence = []
for i in range(num_terms):
  fibonacci_sequence.append(fibonacci(i))

print(fibonacci_sequence)


