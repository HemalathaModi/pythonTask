#----------------------------------Decorators------------------------------------------------
def example(func):
    def wrapper(username):
        print('verifying username..')
        func(username)
        print(f'{username} ---> welcome to the page!!')
    return wrapper

@example
def register(username):
    print('registration processing...')

@example
def login(username):
    print('login processing...')

register('John Doe')
print()
login('Harry')


#-------------------------------------Inheritance-----------------------------------------------
'''Single Inheritance'''

class Parent:
    def properties(self, name):
        print(f'{name} is the owner of my land and gold!!')

class Child(Parent):
    pass

c1 = Child()
c1.properties('John')

'''Multi Level Inheritance'''

class GrandParent:
    def properties(self, name):
        print(f'{name} is the owner of my land and gold!!')

class Parent(GrandParent):
    pass

class Child(Parent):
    pass

c1 = Child()
c1.properties('Harry')

'''Multiple Inheritance'''

class Mother:
    def gold_property(self, name):
        print(f'I will give my gold to my child {name}')

class Father:
    def land_property(self, name):
        print(f'My child {name} is the owner of this land')

class Child(Mother, Father):
    pass

c1 = Child()
c1.gold_property('John')
c1.land_property('John')

'''Hierarchical Inheritance'''

class Parent:
    def properties(self, name):
        print(f'My child {name} is the owner of 1/3rd of my properties!!')

class Child1(Parent):
    pass

class Child2(Parent):
    pass

class Child3(Parent):
    pass

c1 = Child1()
c1.properties('John')

c2 = Child2()
c2.properties('Doe')

c3 = Child3()
c3.properties('Harry')

'''Hybrid Inheritance'''

class GrandParent:
    def property(self):
        print(f'I will give my properties to my children',end=' ')

class Mother:
    def gold_property(self, name):
        print(f'I will give my gold to my child {name}')

class Father(GrandParent):
    def land_property(self, name):
        print(f'My child {name} is the owner of this land')

class Child(Mother, Father):
    print('My Grand parent sent this..',end=' ')
    pass

c1 = Child()
name = 'Doe'
c1.property()
print('--->to my father')
c1.gold_property(name)
c1.land_property(name)

