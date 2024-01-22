def safe_print_list(my_list=[], x=0):
    try:
        num_of_elements = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            num_of_elements += 1
        print()
        return count
    except IndexError:
        print()
        return num_of_elements

