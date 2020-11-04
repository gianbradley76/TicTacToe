import random
import sys


def comp_coordinate(final_list, current_player):
    """Generates a coordinate for computer

    Args:
        final_list (list): list of available coordinates
        current_player (string): the current player
    """

    print('Making move level "easy"')
    current_player = 'O'
    while True:
        comp_x = random.randint(0, 2)
        comp_y = random.randint(0, 2)
        if final_list[comp_x][comp_y][1] is False:
            final_list[comp_x][comp_y][1] = True
            final_list[comp_x][comp_y][0] = current_player
            break


# Input coordinates
def enter_coordinates(final_list):
    """Gets and checks user coordinate input
    Valid table coordinates
    (1, 3)(2, 3)(3, 3)
    (1, 2)(2, 2)(3, 2)
    (1, 1)(2, 1)(3, 1)

    Args:
        final_list (list ): list of availble coordinates
    """

    current_player = 'X'
    while True:
        
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
                if final_list[int(coordinate[0])][int(coordinate[1])][1] is False:
                    final_list[int(coordinate[0])][int(
                        coordinate[1])][1] = True
                    final_list[int(coordinate[0])][int(
                        coordinate[1])][0] = current_player
                    break
                else:
                    print("This cell is occupied! Choose another one!")
        except ValueError:
            print('You should enter numbers!')


# Check the state of the game
def game_state(final_list, current_player):
    """Checks if the game is still ongoing, won, or draw

    Args:
        final_list (list): list of available coordinates
        current_player (string): current player
    """

    # Wnning Coordinates
    # Horizontal
    H_1 = [final_list[2][0], final_list[2][1], final_list[2][2]]
    H_2 = [final_list[1][0], final_list[1][1], final_list[1][2]]
    H_3 = [final_list[0][0], final_list[0][1], final_list[0][2]]

    # Vertical
    V_1 = [final_list[2][0], final_list[1][0], final_list[0][0]]
    V_2 = [final_list[2][1], final_list[1][1], final_list[0][1]]
    V_3 = [final_list[2][2], final_list[1][2], final_list[0][2]]

    # Diagonal
    D_1 = [final_list[2][0], final_list[1][1], final_list[0][2]]
    D_2 = [final_list[0][0], final_list[1][1], final_list[2][2]]

    winning_conditions = [H_1, H_2, H_3,
                          V_1, V_2, V_3,
                          D_1, D_2]

    for condition in winning_conditions:
        if condition[0][0] == condition[1][0] == condition[2][0] and condition[0][0] != ' ' and condition[1][0] != ' ' and condition[2][0] != ' ':
            print(f'{current_player} wins')
            sys.exit(0)
            break

    # Print the initial table -> end of the games
    is_draw = True
    all_occupied = True
    for condition in winning_conditions:
        if condition[0][1] is True and condition[1][1] is True and condition[2][1] is True:
            if condition[0][0] == condition[1][0] == condition[2][0] == 'X':
                is_draw = False
            elif condition[0][0] == condition[1][0] == condition[2][0] == 'O':
                is_draw = False
        else:
            all_occupied = False

    if is_draw and all_occupied:
        print('Draw')
        sys.exit(0)
    elif is_draw and not all_occupied:
        print('Game not finished')


def print_table(final_list):
    """Prints out the table

    ---------
    | _ _ _ |
    | _ _ _ |
    | _ _ _ |
    ---------

    Args:
        final_list (list): list of available coordinates
    """
    print(f'---------\n'
          f'| {final_list[2][0][0]} {final_list[2][1][0]} {final_list[2][2][0]} |\n'
          f'| {final_list[1][0][0]} {final_list[1][1][0]} {final_list[1][2][0]} |\n'
          f'| {final_list[0][0][0]} {final_list[0][1][0]} {final_list[0][2][0]} |\n'
          f'---------')


if __name__ == "__main__":
    game_end = False
    current_player = 'X'
    final_list = []
    for _ in range(3):
        outer_array = []
        for _ in range(3):
            inner_array = []
            inner_array.append(' ')
            inner_array.append(False)
            outer_array.append(inner_array)
        final_list.append(outer_array)

    final_list = final_list[::-1]

    # Print the initial table -> start of the games
    print_table(final_list)

    while not game_end:
        # Input coordinates
        enter_coordinates(final_list)

        # Print player input
        print_table(final_list)

        # Check game status
        game_state(final_list, current_player)

        # Enter computer's coordinates
        comp_coordinate(final_list, current_player)

        # print computer input
        print_table(final_list)

        # Check game status
        game_state(final_list, current_player)
