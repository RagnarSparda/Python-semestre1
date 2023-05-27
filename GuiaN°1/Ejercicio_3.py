tarifa_diurna = 12000
tarifa_nocturna = 16000
recargo_domingo_diurno = 2000
recargo_domingo_nocturno = 3000

empleados = {
    1: {"turnos": ["nocturno", "nocturno", "nocturno", "diurno", "diurno"]},
    2: {"turnos": ["", "nocturno", "nocturno", "", "diurno", "", ""]},
    3: {"turnos": ["", "", "diurno", "diurno", "nocturno", "nocturno", ""]}
}

for empleado, info in empleados.items():
    turno = 0  
    pago_diario = 0  
    for dia in info["turnos"]:
        if dia == "":  
            pago_diario += 0
        else:
            if dia == "diurno":
                pago_dia = tarifa_diurna
                if turno == 5:  
                    pago_dia += recargo_domingo_diurno
            else:  
                pago_dia = tarifa_nocturna
                if turno == 6: 
                    pago_dia += recargo_domingo_nocturno
            pago_diario += pago_dia
        turno += 1  
    pago_semanal = pago_diario * 5  
    info["pago_diario"] = pago_diario
    info["pago_semanal"] = pago_semanal

for empleado, info in empleados.items():
    print(f"Empleado {empleado}:")
    print