
def add(a, b):
    q=int(a)
    p=int(b)
    sum = q+p
    return sum 
def output(a, b, sum):
    print('the sum of a and b is sum')  # ...


def main():
    a,b= input_the_two_numbers()
    sum = add(a, b)

    output(a, b, sum)


if __name__ == '__main__':
    main()
