from DataStructures.List import array_list as al

def new_heap(is_min_pq=True):
    if is_min_pq == True:
        cmp_function = default_compare_lower_value()
    else:
        cmp_function = default_compare_higher_value()
    lista = al.new_list()
    al.add_last(lista, None)
    my_heap = {"elelemts": lista,
               "size": 0,
               "cmp_function": cmp_function}
    return my_heap

def default_compare_higher_value(father_node, child_node):
    if father_node >= child_node:
        return True
    else:
        return False

def default_compare_lower_value(father_node, child_node):
    if father_node <= child_node:
        return True
    else:
        return False
