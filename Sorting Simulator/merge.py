import tkinter as tk
import time
from tkinter import *
from tkinter import messagebox
import random

class MergeSortSimulator:
    def __init__(self, master):
        self.master = master
        self.master.title("Merge Sort Simulator")

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

    def draw_data(self, data, split_index=None, merge_index=None):
        self.canvas.delete("all")
        bar_width = self.canvas_width / len(data)
        for i, value in enumerate(data):
            x0 = i * bar_width
            y0 = self.canvas_height - value
            x1 = (i + 1) * bar_width
            y1 = self.canvas_height
            color = "blue"
            if split_index is not None and i in split_index:
                color = "red"
            if merge_index is not None and i in merge_index:
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

    def merge(self, data, left, mid, right):
        left_data = data[left:mid + 1]
        right_data = data[mid + 1:right + 1]

        i = j = 0
        k = left

        while i < len(left_data) and j < len(right_data):
            if left_data[i] <= right_data[j]:
                data[k] = left_data[i]
                i += 1
            else:
                data[k] = right_data[j]
                j += 1

            k += 1

        while i < len(left_data):
            data[k] = left_data[i]
            i += 1
            k += 1

        while j < len(right_data):
            data[k] = right_data[j]
            j += 1
            k += 1

    def merge_sort(self, data, left, right):
        if left < right:
            mid = (left + right) // 2

            self.merge_sort(data, left, mid)
            self.merge_sort(data, mid + 1, right)

            self.merge(data, left, mid, right)

            # Update the visualization (highlighting the merged elements)
            merge_index = list(range(left, right + 1))
            self.draw_data(data, merge_index=merge_index)

            # Pause for a short duration to visualize the sorting process
            time.sleep(0.02)

    def sort_data(self):
        self.sort_button["state"] = DISABLED
        try:
            input_str = self.input_entry.get()
            data = [int(num) for num in input_str.split(",")]

            n = len(data)
            if(n<=50):
                # Perform merge sort
                self.merge_sort(data, 0, n - 1)

                # Draw the final sorted state
                self.draw_data(data)
                self.sort_button["state"] = NORMAL
            else:
                self.sort_button["state"] = NORMAL
                messagebox.showwarning("Wrong","Can not hendle this all inputs..")
        except:
            self.sort_button["state"] = NORMAL
            messagebox.showerror("error","Invalid Input")

if __name__ == "__main__":
    root = tk.Tk()
    merge_sort_simulator = MergeSortSimulator(root)
    root.mainloop()
