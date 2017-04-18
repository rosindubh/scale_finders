# code to print a list of lists
# taken from head first python
# phil welsby - 18 april 2017

def print_lol(the_list):
    """take one argument a list, and prints a list of lists"""
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)
