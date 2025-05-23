from DataStructures.List import array_list as al
from DataStructures.Priority_queue import index_pq_entry as ie

def new_heap(is_min_pq=True):
    if is_min_pq == True:
        cmp_function = default_compare_lower_value
    else:
        cmp_function = default_compare_higher_value
    lista = al.new_list()
    al.add_last(lista, None)
    my_heap = {"elements": lista,
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
    
def priority(my_heap, parent, child):
    if parent is None or child is None: 
        return False
    cmp_function = my_heap["cmp_function"]
    return cmp_function(parent, child)

def insert(my_heap, element, key):
    new_entry = ie.new_pq_entry(key, element)
    al.add_last(my_heap["elements"], new_entry)
    my_heap["size"] += 1
    swim(my_heap, my_heap["size"]-1)

def swim(my_heap, pos):
    if pos == 0:
        return my_heap
    else:
        father_pos = pos // 2
        if father_pos < 1: 
            return my_heap
        father = al.get_element(my_heap["elements"], father_pos)
        child = al.get_element(my_heap["elements"], pos)
        if father is None or child is None:  
            return my_heap
        if priority(my_heap, father["key"], child["key"]):
            al.exchange(my_heap["elements"], father_pos, pos)
            return swim(my_heap, father_pos)
        else:
            return my_heap

def size(my_heap):
    return my_heap["size"]

def is_empty(my_heap):
    if size(my_heap) == 0:
        return True
    else: 
        return False
    
def get_first_priority(my_heap):
    if is_empty(my_heap):
        return None
    else:
        elemento = al.get_element(my_heap["elements"], 1)
        return elemento["key"]

def remove (my_heap):
    if is_empty(my_heap):
        return None
    else:
        first = al.get_element(my_heap["elements"], 1)
        if my_heap["size"] > 1:  
            al.exchange(my_heap["elements"], 1, my_heap["size"])
        al.remove_last(my_heap["elements"])
        my_heap["size"] -= 1
        if my_heap["size"] > 0:  
            sink(my_heap, 1)
        return first["key"]


def sink(my_heap, pos):
    if pos >= my_heap["size"]:
        return my_heap
    else:
        left_child_pos = pos * 2
        right_child_pos = pos * 2 + 1
        father = al.get_element(my_heap["elements"], pos)

        left_child = al.get_element(my_heap["elements"], left_child_pos) if left_child_pos <= my_heap["size"] else None
        right_child = al.get_element(my_heap["elements"], right_child_pos) if right_child_pos <= my_heap["size"] else None

        if father is None or (left_child is None and right_child is None):
            return my_heap

        if right_child is None or (left_child is not None and priority(my_heap, left_child["key"], right_child["key"])):
            if left_child is not None and priority(my_heap, left_child["key"], father["key"]):
                al.exchange(my_heap["elements"], pos, left_child_pos)
                return sink(my_heap, left_child_pos)
        elif right_child is not None and priority(my_heap, right_child["key"], father["key"]):
            al.exchange(my_heap["elements"], pos, right_child_pos)
            return sink(my_heap, right_child_pos)

        return my_heap