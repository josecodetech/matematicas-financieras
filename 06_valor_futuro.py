# datos iniciales
capital_inicial = 7000
tasa_interes = 0.05
periodos = 3
meta = 10000
# calcular el capital final
valor_futuro = capital_inicial * (1 + tasa_interes) ** periodos
# comprobamos alcance de meta
alcanza_meta = valor_futuro >= meta
# print(alcanza_meta)
# Resultado
if alcanza_meta:
    print(f"Alcanzaras tu meta de ahorro {meta} en 3 años")
else:
    print(f"No alcanzaras tu meta de ahorro {meta} en 3 años")
