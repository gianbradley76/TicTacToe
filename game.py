def change_player(current_player):
    current_player = 'O' if current_player == 'X' else 'X'

    def enter_coordinates(final_array, current_player):
    while True:

        coordinate_input = input('Enter the coordinates: ').split()
        # table coordinates
        # (1, 3)(2, 3)(3, 3)
        # (1, 2)(2, 2)(3, 2)
        # (1, 1)(2, 1)(3, 1)

        # Check if input is integer values
        try:
            coordinate = [int(x) - 1 for x in coordinate_input[::-1]]
            # Check if input is from 1 to 3
            valid = [True if int(x) in range(1, 4)
                     else False for x in coordinate_input]
            if not all(valid):
                print('Coordinates should be from 1 to 3!')
            else:
                # True = coordinate is not yet taken
                # False = coordinate is not yet taken
                if final_array[int(coordinate[0])][int(coordinate[1])][1] is True:
                    final_array[int(coordinate[0])][int(
                        coordinate[1])][1] = False
                    final_array[int(coordinate[0])][int(
                        coordinate[1])][0] = current_player
                    break
                else:
                    print("This cell is occupied! Choose another one!")
        except ValueError:
            print('You should enter numbers!')


def print_table(final_array):
    print(f'---------\n'
          f'| {final_array[2][0][0]} {final_array[0][1][0]} {final_array[2][2][0]} |\n'
          f'| {final_array[1][0][0]} {final_array[1][1][0]} {final_array[1][2][0]} |\n'
          f'| {final_array[0][0][0]} {final_array[2][1][0]} {final_array[0][2][0]} |\n'
          f'---------')


if __name__ == "__main__":
    # First input of the player
    #
    initial_input = input("Enter cells: ")

    # Make the input into an array
    initial_array = [char for char in initial_input]

    # Declare final array for the start of the game
    final_array = []

    num_X = 0
    num_O = 0
    # Makes the input into 2D list and assign it to final_array
    # True = coordinate is not yet taken
    # False = coordinate is not yet taken
    outer = 0
    inner_container = []
    outer_container = []
    for index, char in enumerate(initial_array):

        if char == '_':
            char = ' '

        if char == 'X':
            num_X += 1
        if char == 'O':
            num_O += 1

        inner_container.append(char)
        inner_container.append(True if char == ' ' else False)

        # print(index + 1)
        # print(f'inner -> {inner_container}')

        outer_container.append(inner_container)
        outer += 1
        inner_container = []

        # print(f'outer -> {outer_container}')

        if outer == 3:
            outer = 0
            final_array.append(outer_container)
            outer_container = []

    final_array = final_array[::-1]

    # print(final_array)
    current_player = 'X' if num_X == num_O else 'O'

    # Print the table in the start of the games
    print_table(final_array)

    # Input coordinates
    enter_coordinates(final_array, current_player)

    # Change current player
    change_player(current_player)

    # print(final_array)
    print_table(final_array)
    print(current_player)
