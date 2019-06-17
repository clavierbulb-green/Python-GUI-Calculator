#!/usr/bin/env python3

import operator
import PySimpleGUI as sg
#import calculator

layout=[[sg.Text('', size=(15, 1), font=('Helvetica', 18), key='out')],
        [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('*')],
        [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('/')],
        [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('-')],
        [sg.Button('C'), sg.Button('0'), sg.Button('='), sg.Button('+')]]
        
window = sg.Window('Calculator', layout, return_keyboard_events=True, 
        use_default_focus=False, default_button_element_size=(5, 2), 
        auto_size_buttons=False, grab_anywhere=False)

display = ''
keys_entered = ''
first_operand = None
second_operand = None
current_operator = None
answered = False

operators = { "+": operator.add, "-": operator.sub, "*": operator.mul, 
        "/": operator.truediv }

def convertShortcut(event):
    if event == 'e':
        event = '='
    elif event == 'a':
        event = '+'
    elif event == 's':
        event = '-'
    elif event == 'm':
        event = '*'
    elif event == 'd':
        event = '/'
    elif event == 'q':
        event = None

    return event

while True:
    event, values = window.Read()

    event = convertShortcut(event)
    
    if event is None:
        break
    if event.lower() == 'c':
        display = ''
        keys_entered = ''
        first_operand = None
        second_operand = None
        current_operator = None
    elif event in '1234567890.':
        if answered:
            answered = False
            if not current_operator:
                display = ''
                keys_entered = ''
        display += event
        keys_entered += event
    elif event in operators:
        if not keys_entered:
            continue
        if not first_operand:
            first_operand = float(keys_entered)
        keys_entered = ''
        display += event
        current_operator = event
    elif event == '=': 
        if not first_operand or not current_operator:
            continue

        second_operand = float(keys_entered)

        answer = operators[current_operator](first_operand,second_operand)
        answer = round(answer, 10)

        if answer.is_integer():
            answer = int(answer)
        display = str(answer)

        keys_entered = display
        first_operand = float(display)
        second_operand = None
        current_operator = None
        answered = True

    window.Element('out').Update(display)
    #sg.Popup(button, values)

window.Close()

