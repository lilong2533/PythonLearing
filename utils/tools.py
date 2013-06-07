#-*- coding: UTF-8 -*-

def arithmetic(x = 1 ,y = 1 ,operator = "+"):
    result = {
        "+" : x + y,
        "-" : x - y,
        "*" : x * y,
        "/" : x / y      
        }
    return result.get(operator);

def search(* el ,**map):
    print el
    print map
    keys = map.keys()
    for el_item in el:
        for key in keys:
            if(el_item == key):
                print map.get(key)
    
