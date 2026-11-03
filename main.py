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
            pady=10,
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

        self.text_area = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            font=("Segoe UI", 11),
            height=14,
            padx=8,
            pady=8,
            undo=True,
        )
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=12, pady=10)
        self.text_area.focus_set()

        button_row = tk.Frame(self.root)
        button_row.pack(fill=tk.X, padx=12, pady=(0, 6))

        tk.Button(
            button_row,
            text="Save to file",
            command=self.save_note,
            padx=12,
            pady=6,
        ).pack(side=tk.LEFT)

        tk.Button(
            button_row,
            text="Clear",
            command=self.clear_note,
            padx=12,
            pady=6,
        ).pack(side=tk.LEFT, padx=(8, 0))

        self.status = tk.Label(
            self.root,
            text=f"Notes folder: {self.notes_dir}",
            fg="#3a7ca5",
            anchor="w",
        )
        self.status.pack(fill=tk.X, padx=12, pady=(0, 10))

        self.root.bind("<Control-s>", lambda event: self.save_note())

    def clear_note(self):
        self.text_area.delete("1.0", tk.END)
        self.status.config(text="Cleared.")

    def save_note(self):
        content = self.text_area.get("1.0", tk.END).strip()
        if not content:
            messagebox.showwarning("Empty note", "Type a note before saving.")
            return

        now = datetime.now()
        timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")
        filename = f"note_{now.strftime('%Y%m%d_%H%M%S')}.docx"
        path = self.notes_dir / filename

        try:
            doc = Document()
            doc.add_heading("Quick Note", level=1)

            time_para = doc.add_paragraph()
            label = time_para.add_run("Saved on: ")
            label.bold = True
            time_para.add_run(timestamp_str)

            body = doc.add_paragraph(content)
            for run in body.runs:
                run.font.size = Pt(12)
                run.font.color.rgb = RGBColor(0x22, 0x22, 0x22)

            doc.save(path)
        except OSError as exc:
            messagebox.showerror("Save failed", f"Could not write the file:\n{exc}")
            return

        self.status.config(text=f"Saved: {path.name}")
        messagebox.showinfo("Saved", f"Note saved to:\n{path}")


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
