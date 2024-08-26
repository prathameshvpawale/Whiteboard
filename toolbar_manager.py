import tkinter as tk
from tkinter import colorchooser, simpledialog
from save_manager import SaveManager
from theme_manager import ThemeManager

class ToolbarManager:
    def __init__(self, root, canvas_manager):
        self.canvas_manager = canvas_manager
        self.toolbar = tk.Frame(root, bg='gray')
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        self.color_button = tk.Button(self.toolbar, text="Color", command=self.choose_color)
        self.color_button.pack(side=tk.LEFT, padx=2, pady=2)

        self.eraser_button = tk.Button(self.toolbar, text="Eraser", command=self.use_eraser)
        self.eraser_button.pack(side=tk.LEFT, padx=2, pady=2)

        self.text_button = tk.Button(self.toolbar, text="Text", command=self.use_text)
        self.text_button.pack(side=tk.LEFT, padx=2, pady=2)

        self.pencil_button = tk.Button(self.toolbar, text="Pencil Type", command=self.choose_pencil)
        self.pencil_button.pack(side=tk.LEFT, padx=2, pady=2)

        tk.Label(self.toolbar, text="Shapes:").pack(side=tk.LEFT, padx=5)
        self.line_radio = tk.Radiobutton(self.toolbar, text="Line", variable=self.canvas_manager.shape_mode, value="line")
        self.line_radio.pack(side=tk.LEFT)
        self.rect_radio = tk.Radiobutton(self.toolbar, text="Rectangle", variable=self.canvas_manager.shape_mode, value="rectangle")
        self.rect_radio.pack(side=tk.LEFT)
        self.oval_radio = tk.Radiobutton(self.toolbar, text="Oval", variable=self.canvas_manager.shape_mode, value="oval")
        self.oval_radio.pack(side=tk.LEFT)
        self.freehand_radio = tk.Radiobutton(self.toolbar, text="Freehand", variable=self.canvas_manager.shape_mode, value="freehand")
        self.freehand_radio.pack(side=tk.LEFT)

        self.theme_button = tk.Button(self.toolbar, text="Change Theme", command=self.change_theme)
        self.theme_button.pack(side=tk.LEFT, padx=2, pady=2)

        self.clear_button = tk.Button(self.toolbar, text="Clear", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT, padx=2, pady=2)

        self.save_button = tk.Button(self.toolbar, text="Save", command=self.save_file)
        self.save_button.pack(side=tk.LEFT, padx=2, pady=2)

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        self.canvas_manager.set_color(color)
        self.canvas_manager.disable_eraser()

    def use_eraser(self):
        self.canvas_manager.enable_eraser()

    def use_text(self):
        text = simpledialog.askstring("Input", "Enter text:", parent=self.toolbar)
        self.canvas_manager.text_mode = True
        self.canvas_manager.disable_eraser()
        self.canvas_manager.shape_mode.set("freehand")
        self.canvas_manager.text_mode = True
        self.canvas_manager.canvas.bind("<Button-1>", lambda event: self.add_text(event, text))

    def add_text(self, event, text):
        if text:
            x, y = event.x, event.y
            self.canvas_manager.canvas.create_text(x, y, text=text, fill=self.canvas_manager.current_color, font=("Arial", 16))
            self.canvas_manager.draw.text((x, y), text, fill=self.canvas_manager.current_color)
        self.canvas_manager.text_mode = False

    def choose_pencil(self):
        width = simpledialog.askinteger("Pencil Width", "Enter pencil width:", parent=self.toolbar, minvalue=1, maxvalue=10)
        if width:
            self.canvas_manager.set_width(width)
            self.canvas_manager.disable_eraser()
            self.canvas_manager.shape_mode.set("freehand")

    def change_theme(self):
        ThemeManager.change_theme(self.canvas_manager)

    def clear_canvas(self):
        self.canvas_manager.clear_canvas()

    def save_file(self):
        SaveManager.save_file(self.canvas_manager.image)
