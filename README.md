# Maquina de Cafe TDD

Implementacion de la practica TDD para una maquina dispensadora de cafe.

## Reglas cubiertas

- Vaso pequeno: 3 Oz de cafe.
- Vaso mediano: 5 Oz de cafe.
- Vaso grande: 7 Oz de cafe.
- El consumidor puede seleccionar cucharadas de azucar.
- La maquina muestra mensajes cuando faltan vasos, cafe o azucar.
- Los insumos solo se descuentan cuando el cafe se sirve correctamente.

## Ejecutar pruebas

```powershell
.\run_tests.bat
```

Tambien se pueden ejecutar directamente con Python:

```powershell
python -m unittest discover -s tests -v
```
