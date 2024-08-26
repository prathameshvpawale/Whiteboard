from tkinter import filedialog

class SaveManager:
    @staticmethod
    def save_file(image):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", 
                                                 filetypes=[("PNG files", "*.png"),
                                                            ("JPEG files", "*.jpg"),
                                                            ("All files", "*.*")])
        if file_path:
            image.save(file_path)
