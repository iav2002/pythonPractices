# Al crear un metodo que calcule una secuencia lineal como fibonacci, lo que re-salta facilmente es la recursividad.
# secuencia recursiva, time complexity O(n2)
# def fibonacci_of(n):
#      if n in {0, 1}:  # Base case
#         return n
#      return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case

# print([fibonacci_of(n) for n in range(15)])


import time

start = time.time()



cache = {0: 0, 1: 1}

def fibonacci_of(n):
    if n in cache:  # Base case
     return cache[n]
# Compute and cache the Fibonacci number
    cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case
    return cache[n]

print([fibonacci_of(n) for n in range(30)])
end = time.time()
ftime = end - start
print(ftime)