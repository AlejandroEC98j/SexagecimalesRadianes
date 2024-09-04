import tkinter as tk
from math import radians, degrees

class ConversorAngulos:
    def __init__(self, valor: float):
        self.valor = valor

    def convertir_a_radianes(self) -> float:
        return radians(self.valor)

    def convertir_a_grados(self) -> float:
        return degrees(self.valor)

# Función para manejar la conversión de grados a radianes
def convertir_a_radianes():
    try:
        valor_en_grados = float(entry_grados.get())
        conversor = ConversorAngulos(valor_en_grados)
        resultado = conversor.convertir_a_radianes()
        label_resultado.config(text=f"En radianes: {resultado:.4f}")
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor ingrese un valor numérico válido.")

# Función para manejar la conversión de radianes a grados
def convertir_a_grados():
    try:
        valor_en_radianes = float(entry_radianes.get())
        conversor = ConversorAngulos(valor_en_radianes)
        resultado = conversor.convertir_a_grados()
        label_resultado.config(text=f"En grados: {resultado:.2f}")
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor ingrese un valor numérico válido.")

# Crear la ventana principal
root = tk.Tk()
root.title("Conversor de Ángulos")

# Crear y colocar los widgets para grados a radianes
label_grados = tk.Label(root, text="Grados:")
label_grados.grid(row=0, column=0, padx=10, pady=10)

entry_grados = tk.Entry(root)
entry_grados.grid(row=0, column=1, padx=10, pady=10)

button_convertir_radianes = tk.Button(root, text="Convertir a Radianes", command=convertir_a_radianes)
button_convertir_radianes.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Crear y colocar los widgets para radianes a grados
label_radianes = tk.Label(root, text="Radianes:")
label_radianes.grid(row=2, column=0, padx=10, pady=10)

entry_radianes = tk.Entry(root)
entry_radianes.grid(row=2, column=1, padx=10, pady=10)

button_convertir_grados = tk.Button(root, text="Convertir a Grados", command=convertir_a_grados)
button_convertir_grados.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(root, text="Resultado:")
label_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Iniciar el bucle principal de la interfaz
root.mainloop()
