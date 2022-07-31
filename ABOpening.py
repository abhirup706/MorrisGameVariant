import sys
import time

from FileOperations import FileOperations
from Utility import Utility


def ABOpening(input_file,out_file,depth):

   #print(input_file)
   #print(out_file)
   #print(depth)

    initial_board = []

    initial_board = FileOperations.readBoardConfig(input_file)
   #print(initial_board)
    output_estimate,output_nodecount,output_position = ABMiniMax(depth,True,initial_board,-9999999999999999999999,9999999999999999999999)
    FileOperations.write_out(output_estimate,output_nodecount,output_position,out_file)
   #print(initial_board)

def ABMiniMax(depth,is_white,initial_board,alpha,beta):

    output_nodecount = 0
    output_position = []
    output_estimate = 0

    if(depth == 0):
        output_estimate = Utility.static_estimation_opening(initial_board)
        #print("output estimate ",output_estimate)
        output_nodecount += 1
        return output_estimate,output_nodecount,output_position

    moves_next = []


    if is_white:
        #print("In iswhite condition")
        moves_next = Utility.generate_moves_opening(initial_board)
        #print(moves_next)
        output_estimate = -9999999999999999999999

    else:
        #print("In isblack condition")
        moves_next = Utility.generate_move_opening_black(initial_board)
        output_estimate = 9999999999999999999999

    for move in moves_next:
        if is_white:
            in_estimate,in_nodecount,in_position = ABMiniMax(depth-1,False,move,alpha,beta)
            output_nodecount += in_nodecount

           #print("in_estimate",in_estimate)
            if(in_estimate>alpha):
                
                alpha = in_estimate
                output_position = move
        else:
            in_estimate,in_nodecount,in_position = ABMiniMax(depth-1,True,move,alpha,beta)
            output_nodecount += in_nodecount

           #print("in_estimate",in_estimate)
            if(in_estimate<beta):
                
                beta = in_estimate
                output_position = move  

        if(alpha >= beta):
            break              

    if is_white:
        output_estimate = alpha
    else:
        output_estimate = beta

    return output_estimate,output_nodecount,output_position


def main(input_file,out_file,depth):
    start = time.time()
    ABOpening(input_file,out_file,depth)
    print('Time Elapsed : ',time.time() - start,'seconds')

if __name__ == "__main__":
    input_file = sys.argv[1]
    out_file = sys.argv[2]

    depth = int(sys.argv[3])

    main(input_file,out_file,depth)