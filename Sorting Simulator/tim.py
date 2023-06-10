import tkinter as tk
import time
from tkinter import *
from tkinter import messagebox
import random


class TimSortSimulator:
    def __init__(self, master):
        self.master = master
        self.master.title("Timsort Simulator")

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

    def draw_data(self, data, sorted_indices=None):
        self.canvas.delete("all")
        bar_width = self.canvas_width / len(data)
        for i, value in enumerate(data):
            x0 = i * bar_width
            y0 = self.canvas_height - value
            x1 = (i + 1) * bar_width
            y1 = self.canvas_height
            color = "blue"
            if sorted_indices and i in sorted_indices:
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

    def insertion_sort(self, data, left, right):
        for i in range(left + 1, right + 1):
            key = data[i]
            j = i - 1
            while j >= left and data[j] > key:
                data[j + 1] = data[j]
                j -= 1

            data[j + 1] = key

    def merge(self, data, left, mid, right):
        len1 = mid - left + 1
        len2 = right - mid

        left_half = [0] * len1
        right_half = [0] * len2

        for i in range(len1):
            left_half[i] = data[left + i]

        for i in range(len2):
            right_half[i] = data[mid + 1 + i]

        i = 0
        j = 0
        k = left

        while i < len1 and j < len2:
            if left_half[i] <= right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1

            k += 1

        while i < len1:
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len2:
            data[k] = right_half[j]
            j += 1
            k += 1

    def tim_sort(self, data):
        n = len(data)
        min_run = 32

        # Perform insertion sort for small subarrays
        for i in range(0, n, min_run):
            self.insertion_sort(data, i, min((i + min_run - 1), n - 1))

        size = min_run
        while size < n:
            for left in range(0, n, 2 * size):
                mid = left + size - 1
                right = min((left + 2 * size - 1), (n - 1))
                self.merge(data, left, mid, right)

                # Update the visualization (highlighting the sorted indices)
                sorted_indices = range(left, right + 1)
                self.draw_data(data, sorted_indices=sorted_indices)

                # Pause for a short duration to visualize the sorting process
                time.sleep(0.5)

            size *= 2

    def sort_data(self):
        self.sort_button["state"] = DISABLED
        try:
            input_str = self.input_entry.get()
            data = [int(num) for num in input_str.split(",")]
            n = len(data)
            if(n<=50):
                # Perform timsort
                self.tim_sort(data)

                # Draw the final sorted state
                self.draw_data(data, sorted_indices=range(len(data)))
                self.sort_button["state"] = NORMAL
            else:
                self.sort_button["state"] = NORMAL
                messagebox.showwarning("Wrong","Can not hendle this all inputs..")
        except:
            self.sort_button["state"] = NORMAL
            messagebox.showerror("error","Invalid Input")

if __name__ == "__main__":
    root = tk.Tk()
    timsort_simulator = TimSortSimulator(root)
    root.mainloop()
