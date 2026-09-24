import tkinter as tk

def help_window():
    help_win = tk.Tk()
    help_win.title("Search Query Help Window")
    help_win.geometry("720x720")

    #Background
    help_win.configure(bg="blue")



    # Textbox
    text_box = tk.Text(
        help_win,
        height=20,
        width=70,
        bg="white",
        fg="black",
        wrap="word"
        )
    text_box.insert(tk.INSERT, ('Query language description: You can search by Title, Year, Rating, and Box Office.'
                                '\nThe format is Title == “movie title” or Year <relop> #### or Rating <relop> #.# or '
                                'Box Office <relop> ####. Search criteria can be strung together by using the words '
                                '“and” and “or.” If an incorrectly formatted search is provided, the help menu with a '
                                'description of this query language will be provided.\n\nEx)\nTitle  == “The Shawshank '
                                'Redemption”\nYear > 1980 and Rating < 9.5\nYear > 2000 or Year < 1970\n\nYou can also '
                                'search for a specific field of movie.\nTitle == “Taxi Driver” Get Rating\nTitle == “The '
                                'Shawshank Redemption” Get Year'))
    text_box.pack()

    # Exit Button
    help_exit_button = tk.Button(
        help_win,
        text="Exit",
        bg="white",
        fg="black",
        command=lambda: help_win.destroy()
    )
    help_exit_button.pack()
    help_win.mainloop()

root = tk.Tk()
root.title("Movie Lookup")
root.geometry("720x720")

# Background
root.configure(bg="blue")

# Grid setup
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
    command=lambda: print(search_box.get()) #TODO: Not going to print, going to feed the message into the parser
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
    fg="black",
    command=lambda: help_window()
)
help_button.grid(column=1, row=2)


root.mainloop()