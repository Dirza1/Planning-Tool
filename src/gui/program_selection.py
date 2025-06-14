import tkinter as tk

def program_selection(possible_programs: list[str]) -> list[str]:
    roots = tk.Tk()
    roots.geometry("500x800")
    roots.title("What programs need to be added?")

    selected_vars = {}
    selected_programs = []

    container = tk.Frame(roots)
    container.pack(fill="both", expand=True)

    canvas = tk.Canvas(container)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    checkbox_frame = tk.Frame(canvas)
    canvas_window = canvas.create_window((0, 0), anchor="nw", window=checkbox_frame)

    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
        canvas.itemconfig(canvas_window, width=event.width)

    canvas.bind("<Configure>", on_configure)

    for program in sorted(possible_programs):
        if program.strip() == "":
            continue
        var = tk.BooleanVar()
        cb = tk.Checkbutton(checkbox_frame, text=program, variable=var)
        cb.pack(anchor="w", padx=5, pady=2)
        selected_vars[program] = var

    def confirm_selection():
        nonlocal selected_programs
        selected_programs = [p for p, var in selected_vars.items() if var.get()]
        roots.quit()
        roots.destroy()

    tk.Button(roots, text="Confirm selection", command=confirm_selection).pack(pady=10)

    roots.mainloop()

    return selected_programs

if __name__ == "__main__":
    select = program_selection(["Test","Test again","Realy, another test?"])
    print(select)
