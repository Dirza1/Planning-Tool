import tkinter as tk

def program_selection(possible_programs: list[str]) -> list[str]:
    window = tk.Tk()
    window.geometry("500x800")
    window.title("What programs need to be added?")

    selected_vars: dict = {}
    selected_programs: list = []

    container = tk.Frame(window)
    container.pack(fill="both", expand=True)


    canvas = tk.Canvas(container)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)


    checkbox_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=checkbox_frame, anchor="nw")

    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    checkbox_frame.bind("<Configure>", on_frame_configure)

    def confirm_selection() -> None:
        nonlocal selected_programs
        selected_programs = [program for program, var in selected_vars.items() if var.get()]
        window.destroy()

    for program in sorted(possible_programs):
        if program.strip() == "":
            continue
        var = tk.BooleanVar()
        checkbox = tk.Checkbutton(checkbox_frame, text=program, variable=var)
        checkbox.pack(anchor="w", padx=5, pady=2)
        selected_vars[program] = var

    btn = tk.Button(window, text="Confirm selection", command=confirm_selection)
    btn.pack(pady=10)

    window.mainloop()

    return selected_programs






if __name__ == "__main__":
    program_selection(["test"])