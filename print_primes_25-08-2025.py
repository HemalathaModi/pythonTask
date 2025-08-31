def prime_check(num):
    for i in range(2,int(num ** 0.5) + 1):
        if num % i == 0 :
            return False
    return True

def print_primes(mini , maxi):
    for i in range(mini , maxi + 1):
        if prime_check(i):
            print(i , end = ',')

mini = int(input('Enter a min number from where you want to start printing prime numbers : '))
maxi = int(input('Enter a max range you want to print prime numbers upto : '))
print_primes(mini , maxi)

