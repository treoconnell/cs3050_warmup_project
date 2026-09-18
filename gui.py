import tkinter as tk

root = tk.Tk()
root.title("Movie Lookup")
root.geometry("720x720")

# Background
root.configure(bg="blue")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=0)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=0)


# Search entry
search_box = tk.Entry(
    root,
    width=50,
    font=("Arial", 12),
    bg="white",
    fg="black"
)
search_box.grid(column=0, row=0)

# Search button
search_button = tk.Button(
    root,
    text="Search",
    bg="white",
    fg="black",
    command=lambda: print(search_box.get()) # Not going to print, going to feed the message into the parser
)
search_button.grid(column=1, row=0)

# List Box
# Whenever the parser returns the movies, we're going to display them in this list
list_box = tk.Listbox(
    root,
    width=50,
    font=("Arial", 12),
    bg="white",
    fg="black"
)
list_box.grid(column=0, columnspan=2, row=1, sticky="nsew", padx=10, pady=10)

# Exit Button
exit_button = tk.Button(
    root,
    text="Exit",
    bg="white",
    fg="black",
    command=lambda: root.destroy()
)
exit_button.grid(column=0, row=2)

# Help Button
help_button = tk.Button(
    root,
    text="Help",
    bg="white",
    fg="black"
    # Command will launch the help window
)
help_button.grid(column=1, row=2)


root.mainloop()