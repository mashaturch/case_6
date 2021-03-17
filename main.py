import turtle as t
import math

red = 'красный'
blue = 'синий'
green = 'зеленый'
yellow = 'желтый'
orange = 'оранжевый'
purple = 'фиолетовый'
pink = 'розовый'
color_1 = ''
color_2 = ''
list_color = [red, blue, green, yellow, orange, purple, pink]

print ('Допустимые цвета заливки:\n {}\n {}\n {}\n {}\n {}\n {}'.format (red, blue, green, yellow, orange, purple, pink))

a = 'Пожалуйста, введите количество шестиугольников, располагаемых в ряд: '
a_again = 'Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: '
input_color = 'Пожалуйста, введите цвет:'
error_color =
def get_num_hexagons(a):
    '''Checking the nubmber of hexagones'''
    num_hexagones = int (input (a))
    if 4 <= num_hexagones <= 20:
        return num_hexagones
    else:
        return get_num_hexagons(a_again)

def get_color_choice():
    ''' Getting and checking the color ig hexagon'''
    color = input (input_color)
    if color in list_color:
        if color_1 == '':
           color_1 = color
           get_color_choice()
        elif color_2 == '':
            color_2 = color
    else:
        input_color = "'" + color + "'" + ' не является верным значением. Пожалуйста, повторите попытку: '

def draw_hexagon(x,y, side_len, color):
    '''Drawing the hexagon'''
    goto (x, y)
    fillcolor (color)
    down ()
    begin_fill()
    right (30)
    for i in range (6):
        forward (side_len)
        left (60)
    end_fill()
    left (30)
    up()






get_num_hexagons(a)
get_color_choice()