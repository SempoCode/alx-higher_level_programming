#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_set = set()
    for i  in my_list:
        uniq_set.add(i)
    return sum(uniq_set)
