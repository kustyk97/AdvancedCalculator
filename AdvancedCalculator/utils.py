import re
def is_int(value: str) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False
    
def is_float(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False

def try_get_float_value() -> float:
    value = input()
    if is_float(value) is True:
        value = float(value)
        return value
    else:
        print("This is not float value, try again")
        return None
    
def is_last_num_or_bracket(text: str) ->bool:
    result = re.search("[0-9\)]", text[-1])
    if result is None:
        return False
    else:
        return True 
    
def are_parentheses_matched(text: str) -> bool:
    result = 0
    for element in text:
        if element == "(":
            result += 1
        elif element == ")":
            result -= 1
        if(result < 0):
            return False
    if result != 0:
        return False
    return True

def is_only_floats(list_of_str: list) -> bool:
    for element in list_of_str:
        if not element or is_float(element):
            continue
        else:
            return False
    return True

def is_enable_chars(text: str) -> bool:
    pattern = r'[\+\-\*/\(\)]'
    results = re.split(pattern, text)
    return is_only_floats(results)

def is_formula(text: str) -> bool:
    return is_last_num_or_bracket(text) and are_parentheses_matched(text) and is_enable_chars(text)