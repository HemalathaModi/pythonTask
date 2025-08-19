def triangle(a,b,c):

    if a + b > c and b + c > a and a + c > b :
        print('By using these sides we can form a valid Traingle.')
        if  a == b and b == c and a == c :
            print('It is a equilateral triangle.')
            return
        elif a != b and b != c and a != c :
            print('It is a scalene triangle.')
        else:
            print('It is a isosceles triangle.')

        if a ** 2 == b ** 2 + c ** 2 or b ** 2 == c ** 2 + a ** 2 or c ** 2 == b ** 2 + a ** 2 :
            print('It is also a Right angled triangle.')
    else:
        print("We can't form a valid triangle by using these sides!!")

a = float(input('Enter length of a side : '))
b = float(input('Enter length of a side : '))
c = float(input('Enter length of a side : '))

triangle(a,b,c)

