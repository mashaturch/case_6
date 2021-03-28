"""Case-study #6 Парсинг web-страниц
Разработчики:
Турчинович М., Зубарева Т. , Костылев М.
"""

import turtle as t
import math

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
    color_1 = ''
    color_2 = ''
    input_color = 'Пожалуйста, введите цвет: '
    while color_1 == '' or color_2 == '':
        color = input(input_color)
        if color in list_color:
            if color_1 == '':
                color_1 = color
                print (color_1)
                input_color = 'Пожалуйста, введите цвет: '
            elif color_2 == '':
                color_2 = color


        else:
            print ("'" + color + "'" + ' не является верным значением. Пожалуйста, повторите попытку: ', end='')
    return color_1 + color_2
get_color_choice()


def draw_hexagon(x,y, side_len, color):
    '''Drawing the hexagon'''
    t.goto (x, y)
    t.color(color)
    t.down ()
    t.begin_fill()
    t.right (30)
    for i in range (6):
        t.forward (side_len)
        t.left (60)
    t.end_fill()
    t.left (30)
    t.up()

def draw_hexagons (color_1, color_2, count):
    """Drawing hexagons """
    side_len = (500 / count) / math.sqrt(3)
    x = -250
    y = 250
    for i in range (count):
        for j in range (count):
            draw_hexagon(x, y, side_len, color_1)
            x += 500 / count
            color_1, color_2 = color_2, color_1
            if count % 2 != 0:
                if i == 0 or i == 1 or i == 4 or i == 5 or i == 8 or i == 9 or i == 12 or i == 13 or i == 16 or i == 17:
                    color_1, color_2 = color_2, color_1
            else:
                if i == 2 or i == 3 or i == 6 or i == 7 or i == 10 or i == 11 or i == 14 or i == 15 or i == 18 or i == 19:
                    color_1, color_2 = color_2, color_1






get_num_hexagons(a)
get_color_choice()