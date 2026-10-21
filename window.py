from tkinter import Tk, Canvas, Button, Frame

from line import Line

class Window:
    def __init__(self, width:int, height:int, on_start, on_solve):
        self.root_widget = Tk()
        self.root_widget.title('Maze title')
        self.on_start = on_start
        self.on_solve = on_solve
        
        self.canvas_widget = Canvas(self.root_widget, width=width, height=height)
        self.canvas_widget.pack()
        self.controls = Frame(self.root_widget)
        self.controls.pack(pady=10)
        
        self.start_button = Button(
            self.controls,
            text='Start',
            command=self.start
        )
        self.start_button.pack(side='left', padx=5)
        
        self.solve_button = Button(
                self.controls,
                text='Solve',
                command=self.solve
            )
        self.solve_button.pack(side='left', padx=5)
        
        self.pause_button = Button(
            self.controls,
            text='Pause',
            command=self.pause
        )
        self.pause_button.pack(side='left', padx=5)
        
        self.running = False
        self.paused = False
        
        self.root_widget.protocol('MW_DELETE_WINDOW', self.close)
    def start(self):
        self.start_button.config(state='disabled')
        self.solve_button.config(state='disabled')
        try:
            self.canvas_widget.delete('all')
            self.on_start()
            self.solve_button.config(state='normal')
            self.start_button.config(text='Restart')
        finally:
            self.start_button.config(state='normal')

    def pause(self):
        self.paused = not self.paused
        if self.paused:
            self.pause_button.config(text='Resume')
        else:
            self.pause_button.config(text='Pause')
    
    def solve(self):
        self.start_button.config(state='disabled')
        self.solve_button.config(state='disabled')
        
        try:
            self.on_solve()
            self.pause_button.config(state='disabled')
        finally:
            self.start_button.config(state='normal')

    
    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False
    
    def draw_line(self, line: Line, fill_color: str = 'black'):
        line.draw(self.canvas_widget, fill_color)