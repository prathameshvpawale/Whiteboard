import tkinter as tk
from PIL import Image, ImageDraw

class CanvasManager:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, bg='white', cursor='cross')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.image = Image.new("RGB", (800, 600), "white")
        self.draw = ImageDraw.Draw(self.image)

        self.current_color = "black"
        self.current_width = 3
        self.eraser_on = False
        self.text_mode = False
        self.shape_mode = tk.StringVar(value="freehand")

        self.last_x, self.last_y = None, None
        self.start_x, self.start_y = None, None

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)
        self.canvas.bind("<Button-1>", self.start_draw)

    def paint(self, event):
        if self.shape_mode.get() == "freehand":
            if self.last_x is not None and self.last_y is not None:
                x1, y1 = (self.last_x, self.last_y)
                x2, y2 = (event.x, event.y)
                self.canvas.create_line(x1, y1, x2, y2, fill=self.current_color, width=self.current_width)
                self.draw.line([x1, y1, x2, y2], fill=self.current_color, width=self.current_width)
            self.last_x, self.last_y = event.x, event.y

    def start_draw(self, event):
        if self.shape_mode.get() != "freehand":
            self.start_x, self.start_y = event.x, event.y

    def reset(self, event):
        if self.shape_mode.get() == "line" and self.start_x is not None and self.start_y is not None:
            end_x, end_y = event.x, event.y
            self.canvas.create_line(self.start_x, self.start_y, end_x, end_y, fill=self.current_color, width=self.current_width)
            self.draw.line([self.start_x, self.start_y, end_x, end_y], fill=self.current_color, width=self.current_width)
        elif self.shape_mode.get() == "rectangle" and self.start_x is not None and self.start_y is not None:
            end_x, end_y = event.x, event.y
            self.canvas.create_rectangle(self.start_x, self.start_y, end_x, end_y, outline=self.current_color, width=self.current_width)
            self.draw.rectangle([self.start_x, self.start_y, end_x, end_y], outline=self.current_color, width=self.current_width)
        elif self.shape_mode.get() == "oval" and self.start_x is not None and self.start_y is not None:
            end_x, end_y = event.x, event.y
            self.canvas.create_oval(self.start_x, self.start_y, end_x, end_y, outline=self.current_color, width=self.current_width)
            self.draw.ellipse([self.start_x, self.start_y, end_x, end_y], outline=self.current_color, width=self.current_width)
        self.last_x, self.last_y = None, None
        self.start_x, self.start_y = None, None

    def set_color(self, color):
        self.current_color = color

    def set_width(self, width):
        self.current_width = width

    def set_shape_mode(self, mode):
        self.shape_mode.set(mode)

    def enable_eraser(self):
        self.eraser_on = True
        self.current_color = "white"

    def disable_eraser(self):
        self.eraser_on = False
    def clear_canvas(self):
        # Clear the Tkinter canvas
        self.canvas.delete("all")
        
        # Reset the PIL image to a blank white image
        self.image = Image.new("RGB", (self.width, self.height), self.canvas["bg"])
        self.draw = ImageDraw.Draw(self.image)