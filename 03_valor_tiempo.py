valor_futuro = 1100
tasa_interes = 0.05
periodos = 1

valor_presente = valor_futuro / ((1+tasa_interes)**periodos)
print(f"La opcion mas valiosa en terminos financieros es recibir {round(valor_presente,2)} hoy.")