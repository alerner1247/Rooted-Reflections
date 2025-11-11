import tkinter as tk
from tkinter import messagebox


def submit():
    rose = rose_entry.get()
    bud = bud_entry.get()
    thorn = thorn_entry.get()
    mood = mood_var.get()


def main():
    global rose_entry, bud_entry, thorn_entry, mood_var

    root = tk.Tk()
    root.title("Rooted Reflections")
    root.geometry("450x400")
    root.configure(bg="#F8B4B4")

    header = tk.Label(root, text="Rooted Reflections", font=("Arial", 18, "bold"), bg="#F8B4B4")
    header.pack(pady=15)

    # Frame 
    frame = tk.Frame(root, bg="#F8B4B4")
    frame.pack(pady=10)

    # Rose
    tk.Label(frame, text="Rose:", font=("Arial", 12), bg="#F8B4B4").grid(row=0, column=0, sticky="e", padx=10, pady=5)
    rose_entry = tk.Entry(frame, width=30)
    rose_entry.grid(row=0, column=1, pady=5)

    # Bud
    tk.Label(frame, text="Bud:", font=("Arial", 12), bg="#F8B4B4").grid(row=1, column=0, sticky="e", padx=10, pady=5)
    bud_entry = tk.Entry(frame, width=30)
    bud_entry.grid(row=1, column=1, pady=5)

    # Thorn
    tk.Label(frame, text="Thorn:", font=("Arial", 12), bg="#F8B4B4").grid(row=2, column=0, sticky="e", padx=10, pady=5)
    thorn_entry = tk.Entry(frame, width=30)
    thorn_entry.grid(row=2, column=1, pady=5)

    # Mood dropdown
    tk.Label(frame, text="Mood:", font=("Arial", 12), bg="#F8B4B4").grid(row=3, column=0, sticky="e", padx=10, pady=5)
    mood_var = tk.StringVar(value="Happy")
    mood_options = ["Happy","Tired", "Sad", "Excited", "Calm", "Worried", "Joyous", "Cool", "Angered", "Overstimulated", "Helpless"]
    mood_dropdown = tk.OptionMenu(frame, mood_var, *mood_options)
    mood_dropdown.grid(row=3, column=1, pady=5)

    # Submit button
    submit_btn = tk.Button(root, text="Submit Reflection", font=("Arial", 12, "bold"), bg="white", command=submit)
    submit_btn.pack(pady=20)
    root.mainloop()


if __name__ == "__main__":
    main()