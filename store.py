from Button import Button
from cell import Cell
from sneaker import sneaker

w, h = 500, 500
class store(Cell):
    def __init__(self, status, x, y):
        super().__init__(status, x, y)
        self.size = 68

    def check(self):
        print(self.x, self.y, self.status)

    def show_stuff(self, canvas):
        ambush = sneaker(60, 60, 'NIKE X AMBUSH dunk high "hyper royale"', 150, 'data/Ambush-dunk.png')
        
