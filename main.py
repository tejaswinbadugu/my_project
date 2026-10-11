def to_upper(name):
    return name.upper()


def say_hello(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    name = 'CircleCI'
    say_hello(name)
    print(to_upper(name))