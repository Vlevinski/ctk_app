import tkinter as tk

# <- import the CustomTkinter module
import customtkinter as ctk 

class ChildrenUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("400x240")
        self.title("CustomTkinter Children's UI")

        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, 
            text="Welcome to Children's App!", 
            font=("Helvetica", 16))
        label.pack(pady=20)

        # Use CTkButton instead of tkinter Button
        button = ctk.CTkButton(
            master=self,
            text="Press me",
            corner_radius=10,
            command=self.button_function
        )
        button.pack(pady=20)

    def button_function(self):
        print("Button pressed!")

if __name__ == "__main__":
    app = ChildrenUI()
    app.mainloop()
