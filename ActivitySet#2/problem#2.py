
def add(a, b):
    q=int(a)
    p=int(b)
    sum = q+p

def output(a, b, sum):
    print('the sum of a and b is sum')  # ...


def main():
    a = input()
    b = input()
    sum = add(a, b)

    output(a, b, sum)


if __name__ == '__main__':
    main()
