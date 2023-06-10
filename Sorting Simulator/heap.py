import tkinter as tk
import time
from tkinter import *
from tkinter import messagebox
import random

class HeapSortSimulator:
    def __init__(self, master):
        self.master = master
        self.master.title("Heapsort Simulator")

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

    def draw_data(self, data, heap_index=None, sorted_index=None):
        self.canvas.delete("all")
        bar_width = self.canvas_width / len(data)
        for i, value in enumerate(data):
            x0 = i * bar_width
            y0 = self.canvas_height - value
            x1 = (i + 1) * bar_width
            y1 = self.canvas_height
            color = "blue"
            if heap_index is not None and i <= heap_index:
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

    def heapify(self, data, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and data[i] < data[left]:
            largest = left

        if right < n and data[largest] < data[right]:
            largest = right

        if largest != i:
            data[i], data[largest] = data[largest], data[i]

            # Update the visualization (highlighting the current heap)
            self.draw_data(data, heap_index=i)

            # Pause for a short duration to visualize the sorting process
            time.sleep(0.02)

            self.heapify(data, n, largest)

    def heapsort(self, data):
        n = len(data)

        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(data, n, i)

        # Extract elements one by one
        for i in range(n - 1, 0, -1):
            data[i], data[0] = data[0], data[i]

            # Update the visualization (highlighting the sorted element)
            self.draw_data(data, sorted_index=i)

            # Pause for a short duration to visualize the sorting process
            time.sleep(0.02)

            self.heapify(data, i, 0)

    def sort_data(self):
        self.sort_button["state"] = DISABLED
        try:
            input_str = self.input_entry.get()
            data = [int(num) for num in input_str.split(",")]
            n = len(data)
            if(n<=50):
                # Perform heapsort
                self.heapsort(data)

                # Draw the final sorted state
                self.draw_data(data, sorted_index=0)
                self.sort_button["state"] = NORMAL
            else:
                self.sort_button["state"] = NORMAL
                messagebox.showwarning("Wrong","Can not hendle this all inputs..")
        except:
            self.sort_button["state"] = NORMAL
            messagebox.showerror("error","Invalid Input")


if __name__ == "__main__":
    root = tk.Tk()
    heap_sort_simulator = HeapSortSimulator(root)
    root.mainloop()
