import h5py 
from colorama import Fore, Back, Style
class MAP():
    
    def __init__(self):
        self.names = []
        self.objects = []


    def add(self, name, obj):
        self.names.append(name)
        self.objects.append(obj)

    def split(self):
        self.levels = [i.split('/') for i in self.names]
        self.lengths = [len(i) for i in self.levels]
        self.lengths_functional = [i-1 for i in self.lengths]

    def draw(self, pad='------'):
        tab = '\t'
        tabpipe = tab + '|'
        pipetab = '|' + tab

        for i, j in enumerate(self.lengths_functional):
            # padding vertically
            if j == 0:
                tempv = ''
            if j>0 and self.lengths_functional[i+1] > j:
                tempv = (j-1)*tab + '|'
            if j>0 and self.lengths_functional[i+1] >1:
                tempv = '|' + (j-1)*tab + '|'
            
            # padding horizontally
            temph = Back.RESET + Fore.BLUE+(j-1)*tab+ pad if j > 0 else Back.RED+'*'
            
            # if current level is a dataset, print its shape 
            obj = self.objects[i]
            if hasattr(obj, 'shape'):
                info = obj.shape
            else:
                info = obj.__class__.__name__
            # 
            print(tempv+'  ')
            print(f" {temph} {self.levels[i][j]} {Style.RESET_ALL} <-> {info}  ")
        print('')

if __name__ == '__main__':
    pass