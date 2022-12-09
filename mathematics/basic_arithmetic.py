class basic_arithmetic:
    def __init__(self):
        print("Indidididd")
    
    #Basic Calculator Function
    def basic_calculator(firstOperand, secondOperand, operator):
        output = ""
        match operator:
            case 'times':
                output = firstOperand * secondOperand
            case '*':
                output = firstOperand * secondOperand
            case 'divide':
                output = firstOperand / secondOperand
            case '/':
                output = firstOperand / secondOperand
            case 'plus':
                output = firstOperand + secondOperand
            case '+':
                output = firstOperand + secondOperand
            case 'minus':
                output = firstOperand - secondOperand
            case '-':
                output = firstOperand - secondOperand
            case '^':
                output = pow(firstOperand, secondOperand)
        
        return output

    #Advanced Calculator Function
    def advanced_calculator(firstOperand, secondOperand, operator):
        output = ""
        match operator:
            case 'times':
                output = firstOperand * secondOperand
            case '*':
                output = firstOperand * secondOperand
            case 'divide':
                output = firstOperand / secondOperand
            case '/':
                output = firstOperand / secondOperand
            case 'plus':
                output = firstOperand + secondOperand
            case '+':
                output = firstOperand + secondOperand
            case 'minus':
                output = firstOperand - secondOperand
            case '-':
                output = firstOperand - secondOperand
            case '^':
                output = pow(firstOperand, secondOperand)
        
        return output