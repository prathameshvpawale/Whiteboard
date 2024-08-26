from tkinter import colorchooser
from PIL import Image, ImageDraw

class ThemeManager:
    @staticmethod
    def change_theme(canvas_manager):
        # Prompt the user to choose a background color
        color = colorchooser.askcolor()[1]
        if color:
            # Change the background color of the canvas
            canvas_manager.canvas.config(bg=color)

            # Update the underlying image's background color
            width, height = canvas_manager.image.size

            # Create a new image with the selected background color
            new_background = Image.new("RGB", (width, height), color)

            # Copy the existing drawing onto the new background
            new_image = Image.alpha_composite(new_background.convert("RGBA"), canvas_manager.image.convert("RGBA"))

            # Replace the old image with the new one
            canvas_manager.image = new_image.convert("RGB")
            canvas_manager.draw = ImageDraw.Draw(canvas_manager.image)
