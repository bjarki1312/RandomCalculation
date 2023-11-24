import generate_nums
import generate_operand

def calculate_result(num1, num2, operand):
    try:
        return eval(f"{num1} {operand} {num2}")
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception as e:
        return f"Error: An unexpected error occurred: {e}"

def main():
    num1 = generate_nums.generate_number()
    num2 = generate_nums.generate_number()
    operand = generate_operand.generate_operator()
    return f"{num1} {operand} {num2} = {calculate_result(num1, num2, operand)}"

if __name__ == "__main__":
    pass