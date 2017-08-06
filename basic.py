def do_something_else(value):
    return "Foobar " + value


def do_something():
    print do_something_else(value="with vigor! Quite vigorously!")


if __name__ == '__main__':
    do_something()
