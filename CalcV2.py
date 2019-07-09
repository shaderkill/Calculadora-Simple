import re

# -- Variable global
numeros = []
input_str: str
answer = ['si', 'no', 'n', 's', 'yes', 'y']
answer_yes = ['si', 's', 'yes', 'y']

def calcular():
    global input_str
    print('\n\Operación ingresada es %s' % input_str)
    exec("print('El resultado es', %s)" % input_str)
    salir()

def entrada():
    try:
        success = False
        global input_str
        input_str = ''.join(re.findall('\d\W+|\d+|\W+', input('Ingrese un calculo:\n')))
        calcular()
    except SyntaxError:
        print('SyntaxError: el calculo ingresado no es valido')
        entrada()
        pass

def salir():
    while True:
        str_exit = input('¿Quieres realizar otro calculo? ("si" o "no")\n')
        if str_exit not in answer:
            print('Error: solo puede responder "si" o "no"')
        else:
            if str_exit in answer_yes:
                entrada()
            else:
                False
                break
    pass

entrada()
