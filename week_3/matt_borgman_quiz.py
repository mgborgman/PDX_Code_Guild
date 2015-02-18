print "Hello World"

fruit = ['Apples', 'Oranges', 'Bananas']

print fruit

fruit[1] = 'Grapes'

for item in fruit:
    print item

people = {'Bob': {'Bob': 22},
          'Carol': {'Carol': 47},
          'Justin': {'Justin': 14},
}


def sum(a, b):
    print a + b


sum(5, 5)
sum(10, 15)
sum(3, 6)


def count_to_1000():
    num = input("Enter a number: ")

    while num < 996:
        num += 5
        print num


count_to_1000()


def fizzbuzz():
    nums = range(1, 101)

    for num in nums:
        if num % 3 == 0 and num % 5 == 0:
            print "FizzBuzz"
        elif num % 3 == 0:
            print "Fizz"
        elif num % 5 == 0:
            print "Buzz"
        else:
            print num


fizzbuzz()


class Customer():
    def __init__(self, name, age=27, location='Washington', credit_score=718):
        self.name = name
        self.age = age
        self.location = location
        self.credit_score = credit_score


Jessie = Customer("Jessie")
print Jessie.name
print Jessie.location
print Jessie.credit_score

Jessie.credit_score = 800
print Jessie.credit_score


