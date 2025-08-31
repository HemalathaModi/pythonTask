def prime_check(num):
    for i in range(2,int(num ** 0.5) + 1):
        if num % i == 0 :
            return False
    return True

def print_primes(maxi):
    for i in range(2 , maxi + 1):
        if prime_check(i):
            print(i , end = ',')

maxi = int(input('Enter a max range you want to print prime numbers upto : '))
print_primes(maxi)