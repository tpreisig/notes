class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("560x480")
        self.root.minsize(420, 360)
        self.root.title("Python Office Note App")

        self.notes_dir = Path(__file__).resolve().parent / "notes"
        self.notes_dir.mkdir(exist_ok=True)

        self._build_ui()
