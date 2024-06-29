def is_prime(n):
    if n<=1 :
        return False
    return True
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
def prime_numbers_in_range(start,end):
    primes=[]
    for num in range(start,end+1):
         if is_prime(num):
             primes.append(num)
    return primes
print(prime_numbers_in_range(1,100))  