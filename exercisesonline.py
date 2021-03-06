import numpy

# exercises from https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/

# function that takes two numbers and sees if their product is greater than 1000; if the result is greater than 1000, it sums them instead
def sumOrMult(numb, numb2):
    product = numb * numb2
    if (product >= 1000):
        print(product)
    else:
        print(numb + numb2)

# returns the first ten natural numbers
def firstTenNaturals(number):
    count = 1
    while (count <= 10):
        print (count)
        count += 1

# creates a pattern going from 1 to 5
for i in range(1, 6):
    for j in range(1, 6):
        if (i >= j):
            print(j, end=' ')

    print()

#  code that will print the sum of all numbers from 1 to the one inserted by the client (input 10, output 55)
n = int(input("Enter your number here: "))
sum = 0
for num_inserted in range (1, n + 1):
    sum += num_inserted
print(sum)

# this little piece of code will return the multiplication table of the number chosen by the client
num_input = int(input("Choose the Multiplication Table you wanna see: "))
for number_ins in range (1, 11):
    print(number_ins * num_input)
    
# function that constructs a new list over certain conditions imposed in the previous one (changed the exercise a bit to return a list)
def search(list):
    # creates an empty list that will serve as the output list
    end = []
    # starts the loop - one by one, it analyses the elements in the list
    for elem_list in list:
        # condition to stop the loop
        if (elem_list > 500):
            break
            # conditions given by the exercise to choose which element goes to the new list
        if (elem_list % 5 == 0 and elem_list <= 150):
            end.append(elem_list)
    return end

def countDigit(n):
    counter = 0
    while n != 0:
        n = n // 10
        counter += 1
    return counter

print(countDigit(10))

def reverseValues(list):
    for elem in reversed(list):
        print(elem)

def reverseValues_1(list):
    list.reverse()
    for elem in list:
        print(elem)

def reverseValues_2(list):
    rev_list = list[::-1]
    for elem in rev_list:
        print(elem)

# write a Python program to sum all the elements in a list.
def sumInList(lt):
    result = 0
    for element in lt:
        result += element
    print(result)


def sumInList2(lt):
    result = sum(lt)
    print(result)


# write a Python program to multiply all the items in a list.
def multInList(lt):
    result = 1
    for element in lt:
        result *= element
    print(result)


def multInList2(lt):
    result = numpy.prod(lt) # can only be used on Python 3 or less
    print(result)
