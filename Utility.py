class Utility:

    def is_mill(board,pos_type,v1,v2):
        return(board[v1] == pos_type and board[v2] == pos_type)

    def check_mill_list(board,i,pos_type):
        if i == 0:
            return (Utility.is_mill(board, pos_type, 2, 4))
        elif i == 1:
            return (Utility.is_mill(board, pos_type, 3, 5) or Utility.is_mill(board, pos_type, 8, 17))
        elif i == 2:
            return (Utility.is_mill(board, pos_type, 0, 4))
        elif i == 3:
            return (Utility.is_mill(board, pos_type, 5, 1) or Utility.is_mill(board, pos_type, 7, 14))
        elif i == 4:
            return (Utility.is_mill(board, pos_type, 0, 2))
        elif i == 5:
            return (Utility.is_mill(board, pos_type, 6, 11) or Utility.is_mill(board, pos_type, 1, 3))
        elif i == 6:
            return (Utility.is_mill(board, pos_type, 5, 11) or Utility.is_mill(board, pos_type, 7, 8))
        elif i == 7:
            return (Utility.is_mill(board, pos_type, 6, 8) or Utility.is_mill(board, pos_type, 3, 14))
        elif i == 8:
            return (Utility.is_mill(board, pos_type, 7, 6) or Utility.is_mill(board, pos_type, 1, 17))
        elif i == 9:
            return (Utility.is_mill(board, pos_type, 10, 11) or Utility.is_mill(board, pos_type, 12, 15))
        elif i == 10:
            return (Utility.is_mill(board, pos_type, 9, 11) or Utility.is_mill(board, pos_type, 13, 16))
        elif i == 11:
            return (Utility.is_mill(board, pos_type, 5, 6) or Utility.is_mill(board, pos_type, 14, 17))
        elif i == 12:
            return (Utility.is_mill(board, pos_type, 9, 15) or Utility.is_mill(board, pos_type, 13, 14))
        elif i == 13:
            return (Utility.is_mill(board, pos_type, 12, 14) or Utility.is_mill(board, pos_type, 10, 16))
        elif i == 14:
            return (Utility.is_mill(board, pos_type, 11, 17) or Utility.is_mill(board, pos_type, 12, 13) or Utility.is_mill(board, pos_type, 3, 7))
        elif i == 15:
            return (Utility.is_mill(board, pos_type, 9, 12) or Utility.is_mill(board, pos_type, 16, 17))
        elif i == 16:
            return (Utility.is_mill(board, pos_type, 15, 17) or Utility.is_mill(board, pos_type, 10, 13))
        elif i == 17:
            return (Utility.is_mill(board, pos_type, 15, 16) or Utility.is_mill(board, pos_type, 11, 14) or Utility.is_mill(board, pos_type, 1, 8))
        else:
            return False

    def static_estimation_opening(board):
        w_count,b_count,x_count = 0,0,0
        for i in board:
            if i == "W":
                w_count += 1
            elif i == "B":
                b_count += 1
            elif i == "X":
                x_count += 1 

        return (w_count-b_count)   

    def flip(board):
        output = ['X']*18

        for i,pos_type in enumerate(board):
            
            if pos_type == "W":
                output[i] = "B"
            elif(pos_type == "B"):
                output[i] = "W"
            elif(pos_type == "X" or pos_type == "x"):
                output[i] = "X"

        #print(output)        
        return output

    def generate_move_opening_black(board):
        #print("initial_board ",board)
        flipped_board = Utility.flip(board)
        #print("flipped_board ",flipped_board)
        moves = Utility.generate_moves_opening(flipped_board)

        for i,move in enumerate(moves):
            b = move[:]
            moves[i] = Utility.flip(b)
        
        return moves

    def is_close_mill(i,board):
        pos_type = board[i]

        if (pos_type=='X' or pos_type =='x'):
            return False
        else:
            return Utility.check_mill_list(board,i,pos_type)


    def generate_remove(board,positions):
        for i in range(len(board)):
            if(board[i] == "B" or board[i] == "b"):
                if(not Utility.is_close_mill(i,board)):
                    board_copy = board[:]
                    board_copy[i] = 'X'
                    positions.append(board_copy)

        return positions

    def generate_add(board):
        positions = []

        for i in range(len(board)):
            if(board[i] == 'X' or board[i] == 'x'):
                ##print("generate add ", board)
                board_copy = []
                board_copy = board[:]
                board_copy[i] = 'W'

                ##print("generate add ", board_copy)

                if(Utility.is_close_mill(i,board_copy)):
                    positions = Utility.generate_remove(board_copy,positions)
                else:
                    positions.append(board_copy)
                
                
        return positions

    def generate_moves_opening(board):
        return Utility.generate_add(board)

    def get_neighbours(i):
            if i == 0:
                return [1, 2, 15]
            elif i == 1:
                return [0, 3, 8]
            elif i == 2:
                return [0, 3, 4, 12]
            elif i == 3:
                return [1, 2, 5, 7]
            elif i == 4:
                return [2, 5, 9]
            elif i == 5:
                return [3, 4, 6]
            elif i == 6:
                return [5, 7, 11]
            elif i == 7:
                return [3, 6, 8, 14]
            elif i == 8:
                return [1, 7, 17]
            elif i == 9:
                return [4, 10, 12]
            elif i == 10:
                return [9, 11, 13]
            elif i == 11:
                return [6, 10, 14]
            elif i == 12:
                return [2, 9, 13, 15]
            elif i == 13:
                return [10, 12, 14, 16]
            elif i == 14:
                return [7, 11, 13, 17]
            elif i == 15:
                return [0, 12, 16]
            elif i == 16:
                return [13, 15, 17]
            elif i == 17:
                return [8, 14, 16]
            else:
                return []

    def generateHopping(board):
        moves = []
        for i in range(len(board)):
            if(board[i] == 'W'):
                for j in range(len(board)):
                    if (board[j] == 'X' or board[j] == 'x'):
                        board_copy = board[:]
                        board_copy[i] = 'X'
                        board_copy[j] = 'W'

                        if Utility.is_close_mill(j,board_copy):
                            moves = Utility.generate_remove(board_copy,moves)
                        else:
                            moves.append(board_copy)
        return moves

    def generateMove(board):
        moves = []
        for i in range(len(board)):
            if(board[i] == 'W'):
                neighbours = Utility.get_neighbours(i)
                #print("neighbours",neighbours)
                for j in neighbours:
                    if (board[j] == 'X' or board[j] == 'x'):
                        board_copy = board[:]
                        board_copy[i] = 'X'
                        board_copy[j] = 'W'

                        if Utility.is_close_mill(j,board_copy):
                            #print("in close mill condition")
                            moves = Utility.generate_remove(board_copy,moves)
                        else:
                            #print("in not close mill condition")
                            moves.append(board_copy)
        #print("moves",moves)
        return moves    

       

    def generate_moves_midgame_endgame(board):
        w_count,b_count,x_count = 0,0,0
        for i in board:
            if i == "W":
                w_count += 1
            elif i == "B":
                b_count += 1
            elif i == "X":
                x_count += 1

        if(w_count == 3):
            return Utility.generateHopping(board)
        else:
            return Utility.generateMove(board)


    def generate_moves_midgame_endgame_black(board):
        flipped_board = Utility.flip(board)
        moves = Utility.generate_moves_midgame_endgame(flipped_board)
        output = []

        for move in moves:
            board = move[:]
            output.append(Utility.flip(board))
        
        return output

    def static_estimation_midgame_endgame(board):
        w_count,b_count,x_count = 0,0,0
        for i in board:
            if i == "W":
                w_count += 1
            elif i == "B":
                b_count += 1
            elif i == "X":
                x_count += 1

        moves = Utility.generate_moves_midgame_endgame_black(board)

        moves_cnt = len(moves)

        if b_count <= 2:
            return 10000
        elif w_count <= 2:
            return -10000
        elif moves_cnt == 0:
            return 10000
        else:
            return 1000*(w_count-b_count) - moves_cnt


    def static_estimation_opening_improved(board,curr_depth):
        w_count,b_count,x_count = 0,0,0
        for i in board:
            if i == "W":
                w_count += 1
            elif i == "B":
                b_count += 1
            elif i == "X":
                x_count += 1 

        return (w_count + Utility.possibleMillCount(board) - b_count - curr_depth)

    def possibleMillCount(board):
        cnt = 0

        for i in range(len(board)):
            pos_type = board[i]
            if pos_type == 'X' or pos_type == 'x':
                if (Utility.check_mill_list(board,i,pos_type)):
                    cnt += 1

        return cnt

    def static_estimation_midgame_endgame_mproved(board,curr_depth):
        w_count,b_count,x_count = 0,0,0
        for i in board:
            if i == "W":
                w_count += 1
            elif i == "B":
                b_count += 1
            elif i == "X":
                x_count += 1        

        moves = Utility.generate_moves_midgame_endgame_black(board)
        possibleMillCnt = Utility.possibleMillCount(board)
        moves_cnt = len(moves)

        if(b_count <= 2):
            return 10000
        elif(w_count <= 2):
            return -10000
        else:
            return(1000*(w_count - b_count + possibleMillCnt) - moves_cnt - curr_depth)



        
    
    

