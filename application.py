def dec_printer(func):
    def inner(input_from_func):
        print("from inner")
        func(input_from_func)

    return inner


@dec_printer
def use_printer(input):
    print(input)


if __name__ == "__main__":
    use_printer("my input")
