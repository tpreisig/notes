from pathlib import Path
import tkinter as tk
from tkinter import messagebox, scrolledtext
from datetime import datetime

try:
    from docx import Document
    from docx.shared import Pt, RGBColor
except ImportError:
    raise SystemExit("Missing dependency. Install it with: pip install python-docx")

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("560x480")
        self.root.minsize(420, 360)
        self.root.title("Python Office Note App")

        self.notes_dir = Path(__file__).resolve().parent / "notes"
        self.notes_dir.mkdir(exist_ok=True)

        self._build_ui()
    def _build_ui(self):
        header = tk.Label(
            self.root,
            text="Quick Note Saver",
            font=("Segoe UI", 16, "bold"),
            pady=10
        )
        header.pack()
        
        instructions = tk.Label(
            self.root,
            text=(
                "Type your note below. It will be saved as a Word document "
                "named with the current date and time."
            ),
            wraplength=500,
            justify="left",
        )
        instructions.pack(padx=12)
        
    def clear_note(self):
        pass
    
    def save_note(self):
        pass
    
if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
