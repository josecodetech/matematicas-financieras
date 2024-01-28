capital_inversion = 2000
tasa_interes_ahorro = 0.04
tasa_interes_inversion = 0.06
periodos = 5
# cuenta de ahorro
vf_ahorro = capital_inversion * (1 + tasa_interes_ahorro) ** periodos
# inversion
vf_inversion = capital_inversion * (1 + tasa_interes_inversion) ** periodos
# resultados
print(f"El valor futuro, despues de {periodos}, de la cuenta de ahorro es {round(vf_ahorro,2)}")
print(f"El valor futuro, despues de {periodos}, de la inversion es {round(vf_inversion,2)}")
