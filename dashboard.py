import customtkinter as ctk 
import tkinter as tk
from time import strftime

class ChildrenUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("400x240")
        self.title("CustomTkinter Children's UI")

        self.create_widgets()

    def create_widgets(self):
        # Create a main frame
        main_frame = tk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Create a left frame for buttons
        left_frame = tk.Frame(main_frame, bg="black")
        left_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Create a right frame for other widgets
        right_frame = tk.Frame(main_frame, bg="gray")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        label = tk.Label(right_frame, 
            text="Welcome to Children's App!", 
            font=("Helvetica", 16),
            bg="gray",
            fg="white")
        label.pack(pady=20)

        # Use CTkButton instead of tkinter Button
        button1 = ctk.CTkButton(
            master=left_frame,
            text="Image",
            corner_radius=10,
            command=self.read_color_image,
            width=len("Image") + 2
        )
        button1.pack(pady=20)

        button2 = ctk.CTkButton(
            master=left_frame,
            text="Process",
            corner_radius=10,
            command=self.process_image,
            width=len("Process") + 2
        )
        button2.pack(pady=20)

        button3 = ctk.CTkButton(
            master=left_frame,
            text="Result",
            corner_radius=10,
            command=self.grayscale_image,
            width=len("Result") + 2
        )
        button3.pack(pady=20)

        # Create a label for the clock
        clock_label = tk.Label(left_frame, font=("Helvetica", 16))
        clock_label.pack(side=tk.BOTTOM, pady=20)

        # Update the clock every second
        def update_clock():
            string = strftime('%H:%M:%S')
            clock_label.config(text=string)
            clock_label.after(1000, update_clock)

        update_clock()

    def read_color_image(self):
        print("Read color image button pressed!")

    def process_image(self):
        print("Process image button pressed!")

    def grayscale_image(self):
        print("Grayscale image button pressed!")

if __name__ == "__main__":
    app = ChildrenUI()
    app.mainloop()


