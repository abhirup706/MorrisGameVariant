import sys
import time

from FileOperations import FileOperations
from Utility import Utility


def MiniMaxGameImproved(input_file,out_file,depth):

    #print(input_file)
    #print(out_file)
    #print(depth)

    initial_board = []

    initial_board = FileOperations.readBoardConfig(input_file)
    #print(initial_board)
    output_estimate,output_nodecount,output_position = MiniMaxImproved(depth,True,initial_board,depth)
    FileOperations.write_out(output_estimate,output_nodecount,output_position,out_file)
    #print(initial_board)

def MiniMaxImproved(depth,is_white,initial_board,initial_depth):

    current_depth = initial_depth - depth

    #print("depth",depth)
    output_nodecount = 0
    output_position = []
    output_estimate = 0

    if(depth == 0):
        output_estimate = Utility.static_estimation_opening_improved(initial_board,current_depth)
        #print("output estimate ",output_estimate)
        output_nodecount += 1
        return output_estimate,output_nodecount,output_position

    moves_next = []


    if is_white:
        #print("In iswhite condition")
        moves_next = Utility.generate_moves_midgame_endgame(initial_board)
        ##print(moves_next)
        output_estimate = -9999999999999999999999

    else:
        #print("In isblack condition")
        moves_next = Utility.generate_move_opening_black(initial_board)
        output_estimate = 9999999999999999999999

    ##print("isWhite 1",is_white)
    ##print("moves",len(moves_next))
    
    for move in moves_next:
        ##print("isWhite 2",is_white)
        if is_white:
            #if depth == 1:
                ##print("in depth 1 condition white")
            in_estimate,in_nodecount,in_position = MiniMaxImproved(depth-1,False,move,initial_depth)
            output_nodecount += in_nodecount

            ##print("in_estimate white",in_estimate,depth)
            if(in_estimate>output_estimate):
                
                output_estimate = in_estimate
                output_position = move
        else:
            #if depth == 1:
                ##print("in depth 1 condition white")
            in_estimate,in_nodecount,in_position = MiniMaxImproved(depth-1,True,move,initial_depth)
            output_nodecount += in_nodecount

            ##print("in_estimate black",in_estimate,depth)
            if(in_estimate<output_estimate):
                
                output_estimate = in_estimate
                output_position = move                

    return output_estimate,output_nodecount,output_position


def main(input_file,out_file,depth):
    start = time.time()
    MiniMaxGameImproved(input_file,out_file,depth)
    print('Time Elapsed : ',time.time() - start,'seconds')

if __name__ == "__main__":
    input_file = sys.argv[1]
    out_file = sys.argv[2]

    depth = int(sys.argv[3])

    main(input_file,out_file,depth)