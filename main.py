import tkinter as tk
from canvas_manager import CanvasManager
from toolbar_manager import ToolbarManager

class WhiteboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Whiteboard")
        self.root.geometry("800x600")
        
        # Initialize canvas and toolbar
        self.canvas_manager = CanvasManager(root)
        self.toolbar_manager = ToolbarManager(root, self.canvas_manager)

if __name__ == "__main__":
    root = tk.Tk()
    app = WhiteboardApp(root)
    root.mainloop()
