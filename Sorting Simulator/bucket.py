import tkinter as tk
import time
from tkinter import *
from tkinter import messagebox
import random

class BucketSortSimulator:
    def __init__(self, master):
        self.master = master
        self.master.title("Bucket Sort Simulator")

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

    def draw_data(self, data, bucket_index=None, sorted_index=None):
        self.canvas.delete("all")
        bar_width = self.canvas_width / len(data)
        for i, value in enumerate(data):
            x0 = i * bar_width
            y0 = self.canvas_height - value
            x1 = (i + 1) * bar_width
            y1 = self.canvas_height
            color = "blue"
            if bucket_index is not None and i == bucket_index:
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

    def insertion_sort(self, bucket):
        for i in range(1, len(bucket)):
            key = bucket[i]
            j = i - 1
            while j >= 0 and bucket[j] > key:
                bucket[j + 1] = bucket[j]
                j -= 1

            bucket[j + 1] = key

    def bucket_sort(self, data):
        n = len(data)
        num_buckets = min(n, 10)
        max_value = max(data)
        min_value = min(data)
        range_value = (max_value - min_value) / num_buckets

        buckets = [[] for _ in range(num_buckets)]

        for value in data:
            bucket_index = min(int((value - min_value) / range_value), num_buckets - 1)
            buckets[bucket_index].append(value)

        for i in range(num_buckets):
            self.insertion_sort(buckets[i])

        sorted_index = 0
        for i in range(num_buckets):
            for value in buckets[i]:
                data[sorted_index] = value
                sorted_index += 1

                # Update the visualization (highlighting the current bucket and sorted elements)
                self.draw_data(data, bucket_index=i, sorted_index=sorted_index - 1)

                # Pause for a short duration to visualize the sorting process
                time.sleep(0.02)

    def sort_data(self):
        self.sort_button["state"] = DISABLED
        try:
            input_str = self.input_entry.get()
            data = [int(num) for num in input_str.split(",")]
            n = len(data)
            if(n<=50):
                # Perform bucket sort
                self.bucket_sort(data)

                # Draw the final sorted state
                self.draw_data(data, sorted_index=len(data) - 1)
                self.sort_button["state"] = NORMAL
            else:
                self.sort_button["state"] = NORMAL
                messagebox.showwarning("Wrong","Can not hendle this all inputs..")
        except:
            self.sort_button["state"] = NORMAL
            messagebox.showerror("error","Invalid Input")

if __name__ == "__main__":
    root = tk.Tk()
    bucket_sort_simulator = BucketSortSimulator(root)
    root.mainloop()
