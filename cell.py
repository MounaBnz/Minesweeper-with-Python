import sys
from tkinter import Button,Label
import random
import settings
import ctypes
import sys

class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None
    def __init__(self,x,y,is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x =x
        self.y =y
        #append the object to the all list
        Cell.all.append(self)

    def create_btn_object(self,location):
        btn = Button(
            location,
            width =12,
            height =4,

        )
        btn.bind('<Button-1>',self.left_click_actions )#Left Click
        btn.bind('<Button-3>',self.right_click_actions ) #Right Click

        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label( location):
        lbl = Label(
            location,
            bg = 'black',
            fg= 'white',
            text =f"Cells Left :{Cell.cell_count}",
            width=12,
            height=4,
            font =("",30)
        )
        Cell.cell_count_label_object = lbl

    def left_click_actions(self, event):
        # print("LEFT CLICK !")
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_object in self.surrounded_cells:
                    cell_object.show_cell()
            self.show_cell()
            #if mines count = cells left, the player wins
            if Cell.cell_count == settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, ' You won the game!', 'Congratulations', 0)

        #cancel left and right click events if cell is already opened
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

    def show_mine(self):
        #interrupt the game and display a message that player lost
        ctypes.windll.user32.MessageBoxW(0, 'Tsk tsk ... You just clicked on a mine!', 'Game Over',0)
        sys.exit()
        self.cell_btn_object.configure(bg='black')


    def get_cell_by_axis(selfself,x,y):
        #return a cell based on the values of x and y
        for cell in Cell.all:
            if ((cell.x == x) and (cell.y == y)):
                return cell
    @property
    def surrounded_cells(self):
        # print(self.get_cell_by_axis(0,0))
       cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
       cells = [cell for cell in cells if cell is not None]  # eliminate the None values
       return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
            #replace the text of cell count label with the newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                text =f"Cells Left :{Cell.cell_count}"
                )
            #if this was a mine candidate, then configure the bg color to systembuttonface
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )
        #Mark the cell as opened
        self.is_opened = True
    def right_click_actions(self,event):
       if not self.is_mine_candidate:
           self.cell_btn_object.configure(
               bg = 'orange'
           )
           self.is_mine_candidate = True
       else:
           self.cell_btn_object.configure(
               bg = 'SystemButtonFace' #the default bg
           )
           self.is_mine_candidate = True
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all,
            settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
        # print(picked_cells)

    def __repr__(self):
        return f"Cell({self.x},{self.y})"