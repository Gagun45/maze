from tkinter import Tk, Canvas

class Window:
    def __init__(self, width:int, height:int):
        self.root_widget = Tk()
        self.root_widget.title('Maze title')
        
        self.canvas_widget = Canvas(self.root_widget, width=width, height=height)
        self.canvas_widget.pack()
        self.running = False
        
        self.root_widget.protocol('MW_DELETE_WINDOW', self.close)
    
    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False