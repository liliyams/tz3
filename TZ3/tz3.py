def convert(data):
    li = list(data.split())
    li = list(map(int, li))
    return li


def min_number(data):
    smallest = data[0]
    for line in data[1:]:
        if smallest > line:
            smallest = line
    return smallest


def max_number(data):
    biggest = data[0]
    for line in data[1:]:
        if biggest < line:
            biggest = line
    return biggest


def sum_of_numbers(data):
    summa = 0
    for n in data:
        summa += n
    return summa


def product_of_numbers(data):
    product = 1
    for n in data:
        product *= n
    return product


def main():
    file_name = input('Enter file name:')
    f1 = open(file_name, 'r')
    data_from_file = f1.read()
    my_list = convert(data_from_file)
    print('The smallest number is:', min_number(my_list))
    print('The biggest number is:', max_number(my_list))
    print('The sum of numbers is:', sum_of_numbers(my_list))
    print('The product of numbers is:', product_of_numbers(my_list))


if __name__ == "__main__":
    main()
