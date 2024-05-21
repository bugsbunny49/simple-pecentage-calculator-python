import tkinter as tk

def calculate_percentage():
    try:
        initial_val = float(initial_entry.get())
        final_val = float(final_entry.get())

        cal = ((initial_val - final_val) / initial_val) * 100
        inte = int(cal)

        if initial_val > final_val:
            result_label.config(text=f"Value is decreased to: {inte}%")
        else:
            result_label.config(text=f"Value is increased to: {inte}%")
    except ValueError:
        result_label.config(text="Please enter valid numeric values.")

root = tk.Tk()
root.geometry("350x300")
root.title("Percentage Calculator")

initial_label = tk.Label(root, text="Initial Value:")
initial_label.pack()
initial_entry = tk.Entry(root)
initial_entry.pack()

final_label = tk.Label(root, text="Final Value:")
final_label.pack()
final_entry = tk.Entry(root)
final_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_percentage)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

#created by CMT 21 May 2024


