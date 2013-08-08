import re

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

        m = re.match('(\d+)(\D)(\d+)', expression)
        if m is None:
            return "Invalid input"
        first_number, op, second_number = m.groups()
        first_number            = int(first_number)
        second_number           = int(second_number)
        operation_function      = self.operators[op]
        
        answer  = operation_function(first_number, second_number)
        return answer
