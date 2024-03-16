def calcular_costo_llamada(destino, duracion):
  precios_por_minuto = {
    "Estados Unidos": 900,
    "Canada": 800,
    "Europa": 950,
    "Resto del mundo": 1250
  }

  costo_sin_descuento = precios_por_minuto.get(destino, 0) * duracion

  if duracion > 15:
    descuento = costo_sin_descuento * 0.2
    costo_total = costo_sin_descuento - descuento
  else:
    costo_total = costo_sin_descuento

  return costo_total


destino = "Canada"
duracion = 20

costo_llamada = calcular_costo_llamada(destino, duracion)

print(f"El costo de la llamada a {destino} de {duracion} minutos es de {costo_llamada} pesos")

