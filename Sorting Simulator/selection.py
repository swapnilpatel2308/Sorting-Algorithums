import tkinter as tk
import time
from tkinter import *
from tkinter import messagebox
import random


class SelectionSortSimulator:
    def __init__(self, master):
        self.master = master
        self.master.title("Selection Sort Simulator")

        # Configure the canvas
        self.canvas_width = 800
        self.canvas_height = 400
        self.canvas = tk.Canvas(master, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        # Input entry field
        self.input_entry = tk.Entry(master)
        self.input_entry.pack()

        # Sort button
        self.sort_button = tk.Button(master, text="Sort", command=self.sort_data)
        self.sort_button.pack()

        #take random data and sort
        self.randomdatasort_button = tk.Button(master, text="Random Data", command=self.random_data_sort)
        self.randomdatasort_button.pack()


    def draw_data(self, data, selected_index=None, sorted_index=None):
        self.canvas.delete("all")
        bar_width = self.canvas_width / len(data)
        for i, value in enumerate(data):
            x0 = i * bar_width
            y0 = self.canvas_height - value
            x1 = (i + 1) * bar_width
            y1 = self.canvas_height
            color = "blue"
            if selected_index is not None and i == selected_index:
                color = "red"
            if sorted_index is not None and i <= sorted_index:
                color = "green"
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)

        self.master.update()

    def random_data_sort(self):
        text = ''
        n = 10
        for i in range(n):
            if(i!=n-1):
                text = text + str(random.randrange(10,200))
                text = text + ','
            else:
                text = text + str(random.randrange(10,200))

        self.input_entry.insert(0,text)

    def sort_data(self):
        self.sort_button["state"] = DISABLED
        try:
            input_str = self.input_entry.get()
            data = [int(num) for num in input_str.split(",")]

            n = len(data)
            if(n<=50):
                for i in range(n - 1):
                    min_index = i

                    for j in range(i + 1, n):
                        if data[j] < data[min_index]:
                            min_index = j

                        # Update the visualization (highlighting the current selection)
                        self.draw_data(data, selected_index=j, sorted_index=i)

                        # Pause for a short duration to visualize the sorting process
                        time.sleep(0.02)

                    data[i], data[min_index] = data[min_index], data[i]

                    # Update the visualization (highlighting the sorted element)
                    self.draw_data(data, sorted_index=i)

                    # Pause for a short duration to visualize the sorting process
                    time.sleep(0.02)

                # Draw the final sorted state
                self.draw_data(data, sorted_index=n-1)
                self.sort_button["state"] = NORMAL
            else:
                self.sort_button["state"] = NORMAL
                messagebox.showwarning("Wrong","Can not hendle this all inputs..")
        except:
            self.sort_button["state"] = NORMAL
            messagebox.showerror("error","Invalid Input")

if __name__ == "__main__":
    root = tk.Tk()
    selection_sort_simulator = SelectionSortSimulator(root)
    root.mainloop()
