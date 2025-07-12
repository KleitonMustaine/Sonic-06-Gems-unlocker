import tkinter as tk
from tkinter import filedialog, messagebox
from gem_editor import read_gem_status, write_gem_status
    
class GemEditorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sonic Gem Editor")

        self.filename = None
        self.check_vars = {}

        self.load_button = tk.Button(master, text="Open SonicNextSaveData.bin", command=self.load_file)
        self.load_button.pack(pady=10)

        self.check_frame = tk.Frame(master)
        self.check_frame.pack(padx=10, pady=10)

        self.save_button = tk.Button(master, text="Save Changes", command=self.save_file, state=tk.DISABLED)
        self.save_button.pack(pady=10)

    def load_file(self):
        file = filedialog.askopenfilename(filetypes=[("Binary Files", "*.bin")])
        if not file:
            return
        self.filename = file
        status = read_gem_status(file)

        for widget in self.check_frame.winfo_children():
            widget.destroy()
        self.check_vars.clear()

        for name, enabled in status.items():
            var = tk.IntVar(value=1 if enabled else 0)
            cb = tk.Checkbutton(self.check_frame, text=name, variable=var)
            cb.pack(anchor="w")
            self.check_vars[name] = var

        self.save_button.config(state=tk.NORMAL)

    def save_file(self):
        if not self.filename:
            return
        changes = {name: (var.get() == 1) for name, var in self.check_vars.items()}
        output_file = write_gem_status(self.filename, changes)
        messagebox.showinfo("Success", f"File saved as:\n{output_file}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GemEditorApp(root)
    root.mainloop()