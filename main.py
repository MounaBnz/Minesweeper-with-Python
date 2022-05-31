from tkinter import *
import settings
import utiles
from cell import  Cell

root =Tk()  #window
#override the settings of the window
root.configure(bg="#856ff8")
#to make the window look nicer
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game In Python")
root.resizable(False, False) #for width and height
#top frame
top_frame = Frame(
    root,
    bg="#856ff8",
    width=settings.WIDTH,
    height=utiles.height_prct(25)
)
top_frame.place(x=0,y=0)
#left frame
left_frame = Frame(
    root,
    bg='#856ff8',
    width=utiles.width_prct(25),
    height=utiles.height_prct(75)
)
left_frame.place(x=0, y=utiles.height_prct(25))
#the game frame
center_frame =Frame(
    root,
    bg='#856ff8',
    width=utiles.width_prct(75),
    height=utiles.height_prct(75)
)
center_frame.place(x=utiles.width_prct(25), y=utiles.height_prct(25))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column = x,
            row = y
        )
game_title = Label(
    top_frame,
    bg= 'black',
    fg = 'white',
    text ='Minesweeper Game with Python',
    font=('',45)
)
game_title.place(
    x = utiles.width_prct(25),
    y = 0
)
#call the label from the cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0,y=0)
# print(Cell.all)
Cell.randomize_mines()
# for c in Cell.all:
#     print(c.is_mine)

#run the window
root.mainloop()