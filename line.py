from tkinter import Canvas

from point import Point

class Line:
    def __init__(self, point_1: Point, point_2: Point):
        self.point_1 = point_1
        self.point_2 = point_2
    
    def draw(self, canvas: Canvas, fill_color: str):
        x1 = self.point_1.x
        y1 = self.point_1.y
        
        x2 = self.point_2.x
        y2 = self.point_2.y
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)