class FileOperations:
    def readBoardConfig(filename):

        f = open(filename,"r")
        board_position = f.read()

        output = list(board_position)
        f.close()

        return output

    def write_out(output_estimate,output_nodecount,output_position,filename):
        f = open(filename,"w")


        f.write("BoardPosition:\t\t\t" + ''.join(output_position[:-1]) + "\nPositions Evaluated:\t" + str(output_nodecount) + "\nMINIMAX estimate:\t\t" + str(output_estimate))
        #f.write(''.join(output_position[:]))
        f.close()

