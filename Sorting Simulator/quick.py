import tkinter as tk
import time
from tkinter import *
from tkinter import messagebox
import random

class QuickSortSimulator:
    def __init__(self, master):
        self.master = master
        self.master.title("Quicksort Simulator")

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


    def draw_data(self, data, pivot_index=None, sorted_index=None):
        self.canvas.delete("all")
        bar_width = self.canvas_width / len(data)
        for i, value in enumerate(data):
            x0 = i * bar_width
            y0 = self.canvas_height - value
            x1 = (i + 1) * bar_width
            y1 = self.canvas_height
            color = "blue"
            if pivot_index is not None and i == pivot_index:
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

    def partition(self, data, low, high):
        pivot = data[high]
        i = low - 1

        for j in range(low, high):
            if data[j] <= pivot:
                i += 1
                data[i], data[j] = data[j], data[i]

            # Update the visualization (highlighting the current pivot)
            self.draw_data(data, pivot_index=high)

            # Pause for a short duration to visualize the sorting process
            time.sleep(0.02)

        data[i + 1], data[high] = data[high], data[i + 1]

        return i + 1

    def quicksort(self, data, low, high):
        if low < high:
            pivot_index = self.partition(data, low, high)
            self.draw_data(data, sorted_index=pivot_index)

            self.quicksort(data, low, pivot_index - 1)
            self.quicksort(data, pivot_index + 1, high)

    def sort_data(self):
        self.sort_button["state"] = DISABLED
        try:
            input_str = self.input_entry.get()
            data = [int(num) for num in input_str.split(",")]

            n = len(data)
            if(n<=50):
                # Perform quicksort
                self.quicksort(data, 0, n - 1)

                # Draw the final sorted state
                self.draw_data(data, sorted_index=n - 1)
                self.sort_button["state"] = NORMAL
            else:
                self.sort_button["state"] = NORMAL
                messagebox.showwarning("Wrong","Can not hendle this all inputs..")
        except:
            self.sort_button["state"] = NORMAL
            messagebox.showerror("error","Invalid Input")

if __name__ == "__main__":
    root = tk.Tk()
    quick_sort_simulator = QuickSortSimulator(root)
    root.mainloop()
