from AdvancedCalculator.basicOperations import add, sub, mul, div
from AdvancedCalculator.utils import try_get_float_value
import re

def get_id_of_open_bracket(list_of_math_sign :list) -> int:
    for index, element in enumerate(list_of_math_sign):
        if element == "(":
            return index
    return None
def get_id_of_close_bracket(list_of_math_sign: list) -> int:
    count = 0
    any_close_bracket_found = False 
    for index, element in enumerate(list_of_math_sign):
        if element == "(": 
            count += 1
        elif element == ")":
            any_close_bracket_found = True
            count -= 1
        if count == 0 and any_close_bracket_found  is True:
            return index 
    return None

def try_get_list_of_brackets(list_of_math_elements: list) -> list:
    list_of_brackets = []

    begin_id = get_id_of_open_bracket(list_of_math_elements)
    if begin_id is None:
        return list_of_brackets
    end_id = begin_id + 1 + get_id_of_close_bracket(list_of_math_elements[begin_id:])
    if end_id is None:
        return list_of_brackets
    
    result = (begin_id, end_id)
    list_of_brackets.append(result)
    results = try_get_list_of_brackets(list_of_math_elements[end_id:])
    for result in results:
        result = (result[0]+ end_id, result[1] + end_id)
        list_of_brackets.append(result)
    return list_of_brackets

def calculate_formula(list_of_math_elements: list) -> list:

    list_of_brackets = try_get_list_of_brackets(list_of_math_elements)


    results = []
    for brackets in list_of_brackets:
        result = calculate_formula(list_of_math_elements[brackets[0]+1:brackets[1]-1])
        results = results + result
        
    for result, brackets in zip(reversed(results), reversed(list_of_brackets)):
        del list_of_math_elements[brackets[0]:brackets[1]]
        list_of_math_elements.insert(brackets[0], result)
        
    index = 0
    while index < len(list_of_math_elements):
        if list_of_math_elements[index] == "*":
            value1 = float(list_of_math_elements[index-1])
            value2 = float(list_of_math_elements[index+1])
            result = mul(value1, value2)
            list_of_math_elements.pop(index -1)
            list_of_math_elements.pop(index -1)
            list_of_math_elements.pop(index -1)
            list_of_math_elements.insert(index - 1, str(result))
        elif list_of_math_elements[index] == "/":        
            value1 = float(list_of_math_elements[index-1])
            value2 = float(list_of_math_elements[index+1])
            result = div(value1, value2)
            list_of_math_elements.pop(index -1)
            list_of_math_elements.pop(index -1)
            list_of_math_elements.pop(index -1)
            list_of_math_elements.insert(index - 1, str(result))
        else:
            index +=1   

        
    index = 0
    while index < len(list_of_math_elements):
        if list_of_math_elements[index] == "+":
            value1 = float(list_of_math_elements[index-1])
            value2 = float(list_of_math_elements[index+1])
            result = add(value1, value2)
            list_of_math_elements.pop(index -1)
            list_of_math_elements.pop(index -1)
            list_of_math_elements.pop(index -1)
            list_of_math_elements.insert(index - 1, str(result))
        elif list_of_math_elements[index] == "-":        
            value1 = float(list_of_math_elements[index-1])
            value2 = float(list_of_math_elements[index+1])
            result = sub(value1, value2)
            list_of_math_elements.pop(index -1)
            list_of_math_elements.pop(index -1)
            list_of_math_elements.pop(index -1)
            list_of_math_elements.insert(index - 1, str(result))
        else:
            index +=1  

    return list_of_math_elements

def convert_to_list(text_formula: str) -> list:
    pattern = r'\d+|[\+\-\*/\(\)0-9]'
    list_of_math_elements = re.findall(pattern, text_formula)

    index = 0
    while index < len(list_of_math_elements):
        if list_of_math_elements[index] == "(" and index > 0:
                element = list_of_math_elements[index - 1]
                if element not in ["+", "-", "*", "/"]:
                    list_of_math_elements.insert(index, "*")

        index +=1

    return list_of_math_elements

def calculate(text_formula: str) -> float:

    list_of_math_elements = convert_to_list(text_formula)
    result = calculate_formula(list_of_math_elements)
    result = float(result[0])
    return result