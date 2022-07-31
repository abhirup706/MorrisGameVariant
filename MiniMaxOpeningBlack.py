import sys
import time

from FileOperations import FileOperations
from Utility import Utility


def MiniMaxOpeningBlack(input_file,out_file,depth):

   #print(input_file)
   #print(out_file)
   #print(depth)

    initial_board = []

    initial_board = FileOperations.readBoardConfig(input_file)
   #print(initial_board)
    output_estimate,output_nodecount,output_position = MiniMax(depth,True,initial_board)
    FileOperations.write_out(output_estimate,output_nodecount,output_position,out_file)
   #print(initial_board)

def MiniMax(depth,is_black,initial_board):

    output_nodecount = 0
    output_position = []
    output_estimate = 0

    if(depth == 0):
        output_estimate = Utility.static_estimation_opening(initial_board)
        #print("output estimate ",output_estimate)
        output_nodecount += 1
        return output_estimate,output_nodecount,output_position

    moves_next = []
    in_estimate = 0

    if is_black:
        #print("In iswhite condition")
        moves_next = Utility.generate_move_opening_black(initial_board)
        #print(moves_next)
        output_estimate = -9999999999999999999999

    else:
        #print("In isblack condition")
        moves_next = Utility.generate_moves_opening(initial_board)
        output_estimate = 9999999999999999999999

    for move in moves_next:
        if is_black:
            in_estimate,in_nodecount,in_position = MiniMax(depth-1,False,move)
            output_nodecount += 1

            if(in_estimate>output_estimate):
                output_estimate = in_estimate
                output_position = move
        else:
            in_estimate,in_nodecount,in_position = MiniMax(depth-1,True,move)
            output_nodecount += 1

            if(in_estimate<output_estimate):
                output_estimate = in_estimate
                output_position = move                

    return output_estimate,output_nodecount,output_position


def main(input_file,out_file,depth):
    start = time.time()
    MiniMaxOpeningBlack(input_file,out_file,depth)
    print('Time Elapsed : ',time.time() - start,'seconds')

if __name__ == "__main__":
    input_file = sys.argv[1]
    out_file = sys.argv[2]

    depth = int(sys.argv[3])

    main(input_file,out_file,depth)