# user_input_num = int(input('Enter a number for calculating factorial \n'))
#
# # using for loop
#
# factorial_for = 1
# for val in range(1, int(user_input_num) + 1):
#     factorial_for = factorial_for * val
#
# print('Factorial of a number using for loop is : ', factorial_for)
#
# # using while loop
#
# factorial_while = 1
# while int(user_input_num) > 0:
#     factorial_while = factorial_while * user_input_num
#     user_input_num = user_input_num - 1
#
# print('Factorial using while loop : ', factorial_while)
#
#
# # lets try recursion
#
#
# def calculate_factorial(integer_val_only):
#     if integer_val_only == 1:
#         return 1
#     else:
#         return integer_val_only * calculate_factorial(integer_val_only - 1)
#
#
# recursion_int = int(input('Enter value to calculate factorial using recursion\n'))
#
# print('Factorial using recursion :', calculate_factorial(recursion_int))


# using class
class FactorialClass:

    def __init__(self, num):
        self.num = num

    def factorial_func(self):
        fact_val = 1
        for val in range(1, self.num + 1):
            fact_val = fact_val * val

        return fact_val


# creating object now
fact = FactorialClass(5)
result = fact.factorial_func()
print("Factorial using python class and recursion : ", result)
