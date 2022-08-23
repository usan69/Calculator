from art import logo


# add
def add(n1, n2):
    return n1 + n2


# subtract
def subtract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# division
def division(n1, n2):
    return n1 / n2


# exponent
def exponent(n1, n2):
    return n1 ** n2


# dictonary
all_sign = {"+": add,
            "-": subtract,
            "x": multiply,
            "/": division,
            "^": exponent, }


def new_calculation():
    print(logo)

    num1 = float(input("Type a number:"))

    for symbol in all_sign:
        print(symbol)

    continue_calculating = True

    while continue_calculating:

        # 1s_answer
        sign_selected = input("Which kind of calculation do you want : ")
        num2 = float(input("Type another number:"))
        calculation = all_sign[sign_selected]
        answer = calculation(num1, num2)
        print(f"{num1}  {sign_selected} {num2} ={answer}")

        # 2nd_answer
        # use_of-doc_str
        """sign_selected= input("entry next calculation type: ")
        calculation=all_sign[sign_selected]
        num3=int(input("Type next number : "))
        next_answer=calculation(answer ,num3)
        print(f"{answer} {sign_selected} {num3} = {next_answer}")"""

        re_calculating = input(f"Type 'y' to continue with {answer}, otherwise type 'n' to exit :")

        if re_calculating == "y":
            num1 = answer
        else:
            continue_calculating = False
            print("Thank You for joining with us ")
            new_calculation()


new_calculation()