#!/usr/bin/python3

def element_at(my_list, idx):
    for item in my_list:
        if (idx < 0) and (idx >= len(my_list)):
            return none
        return my_list[idx]
