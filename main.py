"""Case-study #6 Парсинг web-страниц
Разработчики:
Турчинович М. (50%), Зубарева Т. (45%) , Костылев М. (30%)
"""

import turtle as t
import math

# Choice colors
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
def get_num_hexagons():
    '''Checking the nubmber of hexagones'''
    num_hexagones = int (input ('Пожалуйста, введите количество шестиугольников, располагаемых в ряд: '))
    while num_hexagones < 4 or num_hexagones > 20:
        num_hexagones = int (input ('Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: '))
    return num_hexagones

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
                input_color = 'Пожалуйста, введите цвет: '
            elif color_2 == '':
                color_2 = color
        else:
            input_color = "'" + color + "'" + ' не является верным значением. Пожалуйста, повторите попытку: '
    colors_2 = colors (color_1, color_2)
    return colors_2

def colors (col_1, col_2):
    """Color transfer"""
    if col_1 == 'красный':
        col_1 = 'red'
    elif col_1 == 'синий':
        col_1 = 'blue'
    elif col_1 == 'зеленый':
        col_1 = 'green'
    elif col_1 == 'желтый':
        col_1 = 'yellow'
    elif col_1 == 'оранжевый':
        col_1 = 'orange'
    elif col_1 == 'фиолетовый':
        col_1 = 'purple'
    elif col_1 == 'розовый':
        col_1 = 'pink'

    if col_2 == 'красный':
        col_2 = 'red'
    elif col_2 == 'синий':
        col_2 = 'blue'
    elif col_2 == 'зеленый':
        col_2 = 'green'
    elif col_2 == 'желтый':
        col_2 = 'yellow'
    elif col_2 == 'оранжевый':
        col_2 = 'orange'
    elif col_2 == 'фиолетовый':
        col_2 = 'purple'
    elif col_2 == 'розовый':
        col_2 = 'pink'

    return col_1 + ' ' + col_2

def draw_hexagon(x,y, side_len, color):
    '''Drawing the hexagon'''
    t.up()
    t.goto (x, y)
    t.color('black', color)
    t.down()
    t.begin_fill()
    t.right (30)
    for i in range (6):
        t.forward (side_len)
        t.left (60)
    t.end_fill()
    t.left (30)

def draw_hexagons (color_1, color_2, count):
    '''Drawing hexagones'''
    side_len = math.sqrt((500 / (count)) ** 2 / 3)
    x = -250
    y = 250
    line = 1
    for i in range (count):
        for i in range (count):
            draw_hexagon(x, y, side_len, color_1)
            x = t.xcor() + math.sqrt(side_len ** 2 - (side_len / 2) ** 2) * 2
            color_1, color_2 = color_2, color_1
        if line % 2 == 0:
            lines = 1
        else:
            color_1, color_2 = color_2, color_1
            lines = 3
        if count % 2 == 0:
            color_1, color_2 = color_2, color_1
        y = t.ycor() - 3 * side_len / 2
        x = t.xcor() - (count * 2 - lines) * math.sqrt(side_len ** 2 - (side_len / 2) ** 2)
        t.up()
        t.goto(x, y)
        line += 1


def main():
    """The main part of the program"""
    col = get_color_choice()
    col_1, col_2 = col.split()
    count = get_num_hexagons ()
    t.screensize(500, 500)
    t.speed(100)
    draw_hexagons(col_1, col_2, count)
    t.mainloop()
    t.hideturtle()

# start program
main()