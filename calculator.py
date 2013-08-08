
class Calculator(object):
    def __init__(self):
        self.operators = {  '+' : lambda x,y : x+y, 
                            '-' : lambda x,y : x-y,
                            '*' : lambda x,y : x*y,
                            '/' : lambda x,y : x/y, }

    def calculate(self, expression):
        first_number    = ''
        second_number   = ''
        operator_found  = False

        for char in expression:
            if char in self.operators:
                self.next_operation = char
                operator_found = True
            elif char.isdigit():
                if not operator_found:
                    first_number += char
                else:
                    second_number += char
            else:
                return "Invalid input"
                
        first_number            = int(first_number)
        second_number           = int(second_number)
        operation_function      = self.operators[self.next_operation]
        
        answer  = operation_function(first_number, second_number)
        return answer

