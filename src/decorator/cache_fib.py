from functools import cache, lru_cache
import time

# @cache
@lru_cache(maxsize=3)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def main():
    for i in range(400):
        print (i, fib(i))
    print ("done!")

  
@lru_cache(maxsize=5) 
def fibonacci(n): 
    if n < 2: 
        return n 
    else: 
        return fibonacci(n-1) + fibonacci(n-2) 

if __name__ == "__main__":
    # main()
  
    # First call to the function will execute the computation and cache the result 
    start_time = time.time() 
    
    result = fibonacci(100) 
    print(result) 
    print("--- %s seconds ---" % (time.time() - start_time)) 
    start_time = time.time() 
    
    # Subsequent calls to the function with the same input will return the cached result 
    result = fibonacci(100) 
    print(result) 
    print("--- %s seconds ---" % (time.time() - start_time))