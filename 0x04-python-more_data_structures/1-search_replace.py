#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return (new_list)

=================================
2-uniq_add.py

#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    num = 0

    for i in uniq_list:
        num += i

    return (num)
