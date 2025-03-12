# print('Gosto de ser um módulo!')
# print(__name__)

# if __name__ == '__main__':
#     print('Prefiro de ser um módulo')
# else:
#     print('Gosto de ser um módulo')

__count = 0

def suml(the_list):
    global __count
    __count += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum

def prodl(the_list):
    global __count
    __count += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod

if __name__ == '__main__':
    print('Prefiro ser um módulo')
    my_list = [i+1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)