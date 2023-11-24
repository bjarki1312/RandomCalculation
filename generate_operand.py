from random import randint

def generate_operator():
    operands = ['+','-','/','*']
    return operands[randint(0,3)]

if __name__ == "__main__":
    pass