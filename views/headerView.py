import tkinter

def header_view(ventana):
    header_panel = tkinter.Frame(ventana, bg="white", height=50)
    header_panel.grid(row=0, column=0, columnspan=2, sticky="nsew")
    header_panel.grid_propagate(False)

    logo = tkinter.PhotoImage(file="logo.png")
    logo = logo.subsample(10, 10)
    logo_label = tkinter.Label(header_panel, image=logo, bg="white")
    logo_label.image = logo
    logo_label.pack(side="right", padx=5, pady=5)

    titulo = tkinter.Label(header_panel, text="Informe Base de Datos", font=("Arial", 16), bg="white")
    titulo.pack(side="left", padx=10)

    return header_panel

