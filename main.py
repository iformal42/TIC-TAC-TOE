# symbols
x = "X"
o = "O"

print("Welcome to TIC TAC TOE game")


def check_sym(sort, slot):
    """check any matches"""
    for k in sort:
        index = sort[k]
        all_sym = list(set(slot[i] for i in index))
        if (x and o in all_sym) and len(all_sym) == 2:
            # this block will use to make code more time efficient in future
            pass

        if len(all_sym) == 1:
            print(all_sym[0], "has won the game")
            return True, all_sym[0]

    return False, 0


def show(player, slot, x_wins, o_wins):
    """showing Tic Tac Toe interface"""
    ui = f'''
        X = {x_wins}
        O = {o_wins} 
        
        {player}                   
        
        
          
             {slot[0]} | {slot[1]} | {slot[2]}
             ----------
             {slot[3]} | {slot[4]} | {slot[5]}
             ----------  
             {slot[6]} | {slot[7]} | {slot[8]}
            
            '''
    return ui


def reset():
    """resetting all essential variables for
       new game
    """
    counter = 0
    slot = list(range(1, 10))
    sort = {"row1": (0, 1, 2),
            "row2": (3, 4, 5),
            "row3": (6, 7, 8),
            "col1": (0, 3, 6),
            "col2": (1, 4, 7),
            "col3": (2, 5, 8),
            "diag1": (0, 4, 8),
            "diag2": (2, 4, 6),
            }
    total_turns = list(range(1, 10))
    return counter, slot, sort, total_turns


def main():
    # number of wins of player
    x_count = 0
    o_count = 0

    counter, slot, sort, total_turns = reset()

    print(show(f"{x} :-", slot, x_count, o_count))
    while True:

        if counter >= 5:
            # the minimum turns to win is 5
            is_game_over, winner = check_sym(slot=slot, sort=sort)

            if is_game_over:
                if winner == x:
                    x_count += 1
                else:
                    o_count += 1

                counter, slot, sort, total_turns = reset()
                print(show(f"{x} :-", slot, x_count, o_count))

        if counter == 9:
            print("DRAW")
            counter, slot, sort, total_turns = reset()
            print(show(f"{x} :-", slot, x_count, o_count))

        user = input("Enter valid position: ")
        if user.isnumeric() and 1 <= int(user) <= 9:
            user = int(user)

            if user not in total_turns:
                print("entered position already acquired")
                continue

            if counter % 2 == 0:
                sym = x
                next_turn = o
            else:
                sym = o
                next_turn = x

            # replacing int to sym

            slot[user - 1] = sym

            # removing turns
            total_turns.remove(user)

            print(show(f"{next_turn}:-", slot, x_count, o_count))
            counter += 1
        else:
            print("provided input is not an integer or out range number")


if __name__ == "__main__":
    main()
