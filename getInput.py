#A simple function for getting an input with a certain data type
def getInput(q, type):
    while True:  # Loop through until type is correct
        x = ''
        temp = input(q + ': ')
        if type == 'int':
            try:
                x = int(temp)
            except:
                print('Please input a number.')
        elif type == 'float':
            try:
                x = float(temp)
            except:
                print('Please input a number.')
        elif type == 'str':
            x = temp
        return x