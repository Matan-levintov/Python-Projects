import tkinter as tk
from tkinter.constants import FLAT, N, RAISED, TOP


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self)
        self.label['text'] = "What's my favorite video?"
        self.label.pack(side="top")
        self.click_to_find_out = tk.Button(self)
        self.click_to_find_out["text"] = "Click to find out"
        self.click_to_find_out["command"] = self.showImg
        self.click_to_find_out.pack()

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def showImg(self):
        self.photo = tk.PhotoImage(file="FavoritePhoto.png")
        self.label1 = tk.Label(self)
        self.label1['image'] = self.photo
        self.label1.pack()


root = tk.Tk()
root.geometry("1280x720")
app = Application(master=root)
app.mainloop()
