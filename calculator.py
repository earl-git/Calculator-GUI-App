import tkinter as tk
import math

class RightTriangleCalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Right Triangle Calculator")
        self.window.geometry("400x100")

        # Create the frames
        self.side_a_frame = tk.Frame(self.window)
        self.side_b_frame = tk.Frame(self.window)
        self.side_c_frame = tk.Frame(self.window)
        self.button_frame = tk.Frame(self.window)

        # Create the widgets for Side A
        self.side_a_label = tk.Label(self.side_a_frame, text="Side A:")
        self.side_a_entry = tk.Entry(self.side_a_frame, width=90)
        # Pack
        self.side_a_label.pack(side='left')
        self.side_a_entry.pack(side='left')

        # Create the widgets for Side B
        self.side_b_label = tk.Label(self.side_b_frame, text="Side B:")
        self.side_b_entry = tk.Entry(self.side_b_frame, width=90)
        # Pack
        self.side_b_label.pack(side='left')
        self.side_b_entry.pack(side='left')

        # Create the widgets for Side C
        self.side_c_label = tk.Label(self.side_c_frame, text="Side C:")
        self.side_c = tk.StringVar()
        self.side_c_entry = tk.Label(self.side_c_frame, width=90, textvariable=self.side_c)
        # Pack
        self.side_c_label.pack(side='left')
        self.side_c_entry.pack(side='left')

        # button widgets
        self.calculate_button = tk.Button(self.button_frame, text='Calculate', width=10, command=self.calculate_hypotenuse)
        self.exit_button = tk.Button(self.button_frame, text='Exit', width=10, command=self.window.quit)
        self.calculate_button.pack(side='left')  
        self.exit_button.pack(side='left') 
        
        # Pack the frames
        self.side_a_frame.pack()
        self.side_b_frame.pack()
        self.side_c_frame.pack()
        self.button_frame.pack()

        self.window.mainloop()

    def calculate_hypotenuse(self):
        try:
            side_a = float(self.side_a_entry.get())
            side_b = float(self.side_b_entry.get())

            side_c = round(math.sqrt(side_a ** 2 + side_b ** 2), 3)
            self.side_c.set(str(side_c))
        #  non-numeric character or an empty input
        except ValueError:
            self.side_c.set("Invalid input")

if __name__ == "__main__":
    calculator = RightTriangleCalculator()
