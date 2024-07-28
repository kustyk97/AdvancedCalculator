from AdvancedCalculator.utils import is_formula
from AdvancedCalculator.advancedOperations import calculate

def main():

    welcome_message = """Welcom in advanced calculator!!!
    
You can calculate here formula,
if you want to leave write \"esc\""""
    print(welcome_message)

    while True:
        print("Write your formula:", end=" ")

        input_text = input()
        if input_text == "esc":
            break
        if is_formula(input_text):
            result = calculate(input_text)
            print("Result:", result)
        else:
            print("I can't understund formula, try again!")


    print("Bye :D")

if __name__=="__main__":
    main()