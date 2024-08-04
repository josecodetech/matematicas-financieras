precio = 25000
entrada = 15000
tasa_interes = 0.06
periodos = 5
prestamo_solicitado = precio - entrada
tasa_interes_mensual = tasa_interes / 12
num_pagos = periodos * 12
cuota_mensual = prestamo_solicitado * (tasa_interes_mensual * (1+tasa_interes_mensual)**num_pagos)/((1+tasa_interes_mensual)**num_pagos-1)
print("Necesitaras pedir prestado "+str(round(prestamo_solicitado,2)))
print("La cuota mensual es de "+str(round(cuota_mensual, 2)))
