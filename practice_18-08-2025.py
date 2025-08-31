def check_number_positive_zero_negative(num):
  if num > 0 :
    print(f'{num} is positive.')
  elif num < 0 :
    print(f'{num} is negative.')
  else :
    print('zero')

num = int(input('Enter a number to check positive or not : '))
check_number_positive_zero_negative(num)

def odd_even_check(num):
  if num % 2 == 0 :
    print(f'{num} is even')
  else :
    print(f'{num} is odd.')

num = int(input('Enter a number to check even or not : '))
odd_even_check(num)

def check_vote_eligibility(age) :
  if age >= 18 :
    print('Eligible to vote')
  else :
    print('Not eligible to vote')
    
age = int(input('Enter your age to check eligibility for vote : '))
check_vote_eligibility(age)

def greatest_of_two(num1 , num2) :
  if num1 > num2 :
    print(f'{num1} is greatest of two')
  elif num2 > num1 :
    print(f'{num2} is greatest of two')
  else :
    print('Both are equal')

num1 = int(input('Enter a number : '))
num2 = int(input('Enter a number : '))
greatest_of_two(num1 , num2)
    
