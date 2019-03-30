excel = {}

ops = {
    "+": (lambda a, b: a + b),
    "-": (lambda a, b: a - b),
    "*": (lambda a, b: a * b),
    "/": (lambda a, b: a / b)
}


def eval(expression):
    tokens = expression.split()
    stack = []

    for token in tokens:
        if token in ops:
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = ops[token](arg1, arg2)
            stack.append(result)
        else:
            if token in excel:
                token = excel[token]
            stack.append(int(token))

    return stack.pop()


def typing(no_cells):
    for i in range(no_cells):
        print('Cell number ', i + 1)
        cell_name = input('Cell name: ')
        cell_content = input('Cell content:')
        excel[cell_name] = cell_content
    return excel


def calculate():
    no_cells = input('Number of cells: ')
    excel = typing(int(no_cells))
    for key,value in excel.items():
        print(key,'\n',eval(value),'\n')

def detect_circular(excel):
    list = []
    for key, values in excel.items():
        vals = values.split()
        for val in vals:
            if val in excel:
                if any(set([key,val]) == x for x in list):
                    return True
                list.append(set([key,val]))
    return False


excel = typing(3)
lst = detect_circular(excel)



# calculate()
