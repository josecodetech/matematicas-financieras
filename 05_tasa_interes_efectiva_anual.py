# 6% con capitalizacion trimestral
# 5.5% con capitalizacion mensual
# datos primera opcion
tasa_nominal_1 = 0.06
capitalizacion_1 = 4
tasa_interes_efectiva_1 = ((1+tasa_nominal_1/capitalizacion_1)**capitalizacion_1)-1
# datos segunda opcion
tasa_nominal_2 = 0.055
capitalizacion_2 = 12
tasa_interes_efectiva_2 = ((1+tasa_nominal_2/capitalizacion_2)**capitalizacion_2)-1
# resultado 
print(f"Tasa interes efectiva 1 anual con capitalizacion trimestral es: {round(tasa_interes_efectiva_1*100,2)}%")
print(f"Tasa interes efectiva 2 anual con capitalizacion mensual es: {round(tasa_interes_efectiva_2*100, 2)}%")
