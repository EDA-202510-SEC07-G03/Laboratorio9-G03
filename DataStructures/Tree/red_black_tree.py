from DataStructures.Tree import rbt_node as rbt
from DataStructures.List import single_linked_list as sl
def new_map():
    rbt_tree = {"root":None, "type":"RBT"}
    return rbt_tree

def is_red(node_rbt):
    if node_rbt == None:
        return False
    bol = rbt.is_red(node_rbt)
    if bol:
        return True
    else:
        return False

def insert_node(root, key, value):
    if root == None:
        root = rbt.new_node(key, value)
    elif root["key"] == key:
        root["value"] = value
    else:
        if key <= root["key"]:
            root["left"] = insert_node(root["left"], key, value)
        elif key > root["key"]:
            root["right"] =  insert_node(root["right"], key, value)
    if is_red(root["right"]) and not is_red(root["left"]):
        root = rotate_left(root)
    if is_red(root["left"]) and is_red(root["left"]["left"]):
        root = rotate_right(root)
    if is_red(root["left"]) and is_red(root["right"]):
        flip_color(root)
    
    return root

def put(my_bst, key, value):
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    my_bst["root"]["color"] == 1
    return my_bst 
    
def flip_color_node(node_rbt):
    if node_rbt is not None:
        if node_rbt["color"] == 1:
            rbt.change_color(node_rbt, 0)
        elif node_rbt["color"] == 0:
            rbt.change_color(node_rbt, 1)
    return node_rbt

def flip_color(node_rbt):
    if node_rbt is not None:
        flip_color_node(node_rbt)
        if node_rbt["left"] is not None:
            flip_color_node(node_rbt["left"])
        if node_rbt["right"] is not None:
            flip_color_node(node_rbt["right"])
    return node_rbt

def rotate_left(node_rbt):
    new_pops = node_rbt["right"]
    node_rbt["right"] = new_pops["left"]
    new_pops["left"] = node_rbt
    new_pops["color"] = node_rbt["color"]
    rbt.change_color(node_rbt, 0)
    return new_pops

def rotate_right(node_rbt):
    new_pops = node_rbt["left"]
    node_rbt["left"] = new_pops["right"]
    new_pops["right"] = node_rbt
    new_pops["color"] = node_rbt["color"]
    rbt.change_color(node_rbt, 0)
    return new_pops
