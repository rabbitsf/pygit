## Functions can be passed as parameters of another function
# def add(n1, n2):
#     return n1 + n2
#
# def subtract(n1, n2):
#     return n1 - n2
#
# def multiple(n1, n2):
#     return n1 * n2
#
# def division(n1, n2):
#     return n1 / n2
#
# def calculate(cal_function, n1, n2):
#     return cal_function(n1, n2)
#
# result = calculate(add, 2, 3)
# print(result)

## Nested Functions
# def outer_fuction():
#     print("This is outer.")
#
#     def nested_function():
#         print("This is inner.")
#
#     nested_function()
#
# outer_fuction()
# nested_function()    # You can call the nested function from outside

## Functions can be returned from other functions
# def outer_fuction():
#     print("This is outer.")
#
#     def nested_function():
#         print("This is inner.")
#
#     return nested_function
#
# outer_fuction()

## Functions can be returned from other functions
def outer_fuction():
    print("This is outer.")

    def nested_function():
        print("This is inner.")

    return nested_function

inner_function = outer_fuction()
inner_function()