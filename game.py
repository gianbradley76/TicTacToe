# Change current player
def change_player(current_player):
    current_player = 'O' if current_player == 'X' else 'X'


# Input coordinates
def enter_coordinates(final_array, current_player):
    while True:
        # table coordinates
        # (1, 3)(2, 3)(3, 3)
        # (1, 2)(2, 2)(3, 2)
        # (1, 1)(2, 1)(3, 1)
        coordinate_input = input('Enter the coordinates: ').split()
        # Check if input is integer values
        try:
            coordinate = [int(x) - 1 for x in coordinate_input[::-1]]
            # Check if input is from 1 to 3
            valid = [True if int(x) in range(1, 4)
                     else False for x in coordinate_input]
            if not all(valid):
                print('Coordinates should be from 1 to 3!')
            else:
                # True = coordinate is taken
                # False = coordinate is not yet taken
                if final_array[int(coordinate[0])][int(coordinate[1])][1] is False:
                    final_array[int(coordinate[0])][int(
                        coordinate[1])][1] = True
                    final_array[int(coordinate[0])][int(
                        coordinate[1])][0] = current_player
                    break
                else:
                    print("This cell is occupied! Choose another one!")
        except ValueError:
            print('You should enter numbers!')


# Check the state of the game
def game_state(final_array, current_player):
    # Wnning Coordinates
    # Horizontal
    H_1 = [final_array[2][0], final_array[2][1], final_array[2][2]]

    H_2 = [final_array[1][0], final_array[1][1], final_array[1][2]]

    H_3 = [final_array[0][0], final_array[0][1], final_array[0][2]]


# final_array[2][0], final_array[2][1], final_array[2][2]
# final_array[1][0], final_array[1][1], final_array[1][2]
# final_array[0][0], final_array[0][1], final_array[0][2]


# Vertical
    V_1 = [final_array[2][0],
           final_array[1][0],
           final_array[0][0]]

    V_2 = [final_array[2][1],
           final_array[1][1],
           final_array[0][1]]

    V_3 = [final_array[2][2],
           final_array[1][2],
           final_array[0][2]]

    # Diagonal
    D_1 = [final_array[2][0],
           final_array[1][1],
           final_array[0][2]]

    D_2 = [final_array[0][0],
           final_array[1][1],
           final_array[2][2]]

    winning_conditions = [H_1, H_2, H_3,
                          V_1, V_2, V_3,
                          D_1, D_2]

    print_table(final_array)

    game_won = False
    for condition in winning_conditions:
        # for index, value in enumerate(condition):
        if condition[0][0] == condition[1][0] == condition[2][0]:
            print(f'{current_player} wins')
            game_won = True
            break

    # Print the initial table -> end of the games

    is_draw = True
    all_occupied = True
    for condition in winning_conditions:
        if condition[0][1] is True and condition[1][1] is True and condition[2][1] is True:
            if condition[0][0] == 'X' and condition[1][0] == 'X' and condition[2][0] == 'X':
                is_draw = False
            elif condition[0][0] == 'O' and condition[1][0] == 'O' and condition[2][0] == 'O':
                is_draw = False
        else:
            all_occupied = False

        #print(is_draw, '  :  ', all_occupied, '  :  ', condition)

    if is_draw and all_occupied:
        print('Draw')
    elif is_draw and not all_occupied:
        print('Game not finished')

    # if any(winning_conditions):
    #
    # elif all(winning_conditions) and not any(winning_conditions):
    #     print('Draw')


# Print the table
def print_table(final_array):
    print(f'---------\n'
          f'| {final_array[2][0][0]} {final_array[2][1][0]} {final_array[2][2][0]} |\n'
          f'| {final_array[1][0][0]} {final_array[1][1][0]} {final_array[1][2][0]} |\n'
          f'| {final_array[0][0][0]} {final_array[0][1][0]} {final_array[0][2][0]} |\n'
          f'---------')


if __name__ == "__main__":
    # First input of the player
    #
    initial_input = input("Enter cells: ")

    # Make the input into an array
    initial_array = [char for char in initial_input]

    # Declare final array for the start of the game
    final_array = []

    num_X = 0  # Number of X at the start of the game
    num_O = 0  # Number of O at the start of the game
    outer = 0
    inner_container = []
    outer_container = []

    # Makes the input into 2D list and assign it to final_array
    for char in initial_array:

        if char == '_':
            char = ' '

        if char == 'X':
            num_X += 1
        if char == 'O':
            num_O += 1

        inner_container.append(char)
        # True = coordinate is taken
        # False = coordinate is not yet taken
        inner_container.append(False if char == ' ' else True)

        outer_container.append(inner_container)
        outer += 1
        inner_container = []

        if outer == 3:
            outer = 0
            final_array.append(outer_container)
            outer_container = []

    final_array = final_array[::-1]

    # print(final_array)
    current_player = 'X' if num_X == num_O else 'O'

    # Print the initial table -> start of the games
    print_table(final_array)

    # Input coordinates
    enter_coordinates(final_array, current_player)

    # Check the state of the game
    game_state(final_array, current_player)

    # Change current player
    change_player(current_player)
