class Calculator:
    @staticmethod
    def calculation(first_operand, second_operand, operator):
        result = 0

        if operator == '+':
            result = first_operand + second_operand
        elif operator == '-':
            result = first_operand - second_operand
        elif operator == '*':
            result = first_operand * second_operand
        elif operator == '/':
            if second_operand != 0:
                result = first_operand / second_operand
            else:
                raise ArithmeticError("Деление на ноль невозможно")
        else:
            raise ValueError("Неожиданное значение: " + operator)

        return result

    @staticmethod
    def calculate_discount(purchase_amount, discount_percentage):
        if purchase_amount < 0 or discount_percentage < 0 or discount_percentage > 100:
            raise ArithmeticError("Недопустимые аргументы")

        discount_amount = purchase_amount * (discount_percentage / 100)
        discounted_price = purchase_amount - discount_amount
        return discounted_price
