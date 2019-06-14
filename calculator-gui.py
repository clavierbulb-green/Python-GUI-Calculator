import PySimpleGUI as sg
import calculator

layout=[[sg.Text('', size=(10, 1), font=('Helvetica', 18), key='out')],
        [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('*')],
        [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('/')],
        [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('-')],
        [sg.Button('C'), sg.Button('0'), sg.Button('='), sg.Button('+')]]
        
window = sg.Window('Calculator', layout, default_button_element_size=(5, 2), 
        auto_size_buttons=False, grab_anywhere=False)

display = ''
keys_entered = ''
first_operand = None
second_operand = None
operator = None
answered = False

while True:
    event, values = window.Read()
    if event is None:
        break
    if event is 'C':
        display = ''
        keys_entered = ''
        first_operand = None
        second_operand = None
        operator = None
    elif event in '1234567890':
        if answered:
            answered = False
            if not operator:
                display = ''
                keys_entered = ''
        display += event
        keys_entered += event
    elif event in '*/+-':
        if not keys_entered:
            continue
        if not first_operand:
            first_operand = float(keys_entered)
        keys_entered = ''
        display += event
        operator = event
    elif event is '=':
        if not first_operand or not operator:
            continue

        second_operand = float(keys_entered)
        if operator == '+':
            display = str(calculator.add(first_operand, second_operand))
        elif operator == '-':
            display = str(calculator.subtract(first_operand, second_operand))
        elif operator == '*':
            display = str(calculator.multiply(first_operand, second_operand))
        elif operator == '/':
            display = str(calculator.divide(first_operand, second_operand))
        keys_entered = display
        first_operand = float(display)
        second_operand = None
        operator = None
        answered = True

    window.Element('out').Update(display)
    #sg.Popup(button, values)

window.Close()

