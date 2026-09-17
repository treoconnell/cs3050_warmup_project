import tkinter as tk

root = tk.Tk()
root.title("Movie Lookup")
root.geometry("720x720")

# Background
root.configure(bg="blue")

# Search entry
search_box = tk.Entry(
    root,
    width=50,
    font=("Arial", 12),
    bg="white",
    fg="black"
)
search_box.pack()

# Search button
search_button = tk.Button(
    root,
    text="Search",
    bg="white",
    fg="black",
    command=lambda: print(search_box.get())
)
search_button.pack()

# Exit Button
exit_button = tk.Button(
    root,
    text="Exit",
    bg="white",
    fg="black",
    command=lambda: root.destroy()
)
exit_button.pack()

# Help Button
help_button = tk.Button(
    root,
    text="Help",
    bg="white",
    fg="black"
    # Command will launch the help window
)
help_button.pack()


root.mainloop()