from MAP import MAP
from os.path import isdir
import h5py as h5


def parse_input(input_file):
    # check if it is a directory
    if isinstance(input_file, str):
        if input_file.endswith('.h5') or input_file.endswith('.hdf5') or input_file.endswith('.hdf') or input_file.endswith('.he5'):
            f = h5.File(input_file, 'r')
        else:
            raise ValueError('invalid input file, supported formats are: .h5, .hdf5, .hdf, .he5, .nwb')

    else: # if it's not a directory, we assume it's an h5 file
        f = input_file
    return f

def drawh5(input_file, **kwargs):
    
    f = parse_input(input_file)

    # create a map object and fill it with the h5 file
    map = MAP()
    f.visititems(map.add)
    map.split()
    map.draw()

# take input from command line
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=str, help='path to the h5 file')
    args = parser.parse_args()
    drawh5(args.input_file)