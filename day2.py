#AoC2023 day 2 part 2
#contains bits relevant only to part 1 (game_tag)
#as I went stream-of-consciousness and overwrote/reworked part 1 to become part 2


max_colors = {
    'red': 0,
    'green': 0,
    'blue': 0
    }
colors = ['red', 'green', 'blue']


power_sum = 0
game_number_sum = 0

with open('day2input.txt','r') as file:
    line = file.readline()
    while line != '':

        max_colors = {
            'red': 1,
            'green': 1,
            'blue': 1
        }

        game_tag = line.split(':')[0] # gets "Game #" string
        draws = line.split(':')[1].split(";")  # gets list of draws
        print(draws)

        good_draw = True
        for text in draws:
            each_draw = text.split(',')  #create list of each draw from set

            for pick in each_draw:
                num_of_color = ''.join(character for character in pick if character.isdigit())
                number_of_color = int(num_of_color)  # number of cubes drawn
                for color in colors:
                    if color in pick:
                        break
                print(f'{color}:{number_of_color}')
                if number_of_color > max_colors[color]:
                    max_colors[color] = number_of_color

        power = max_colors['red'] * max_colors['blue'] * max_colors['green']
        power_sum += power



        line = file.readline()

# print(game_number_sum)
print(power_sum)
