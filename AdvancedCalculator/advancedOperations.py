# from basicOperations import add, sub, mul, div
import re

from sympy import sympify

def calculate_formula(text: str) -> float:
    return sympify(text)