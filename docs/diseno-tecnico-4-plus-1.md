# Diseno tecnico 4+1 - Maquina de Cafe TDD

## Informacion general

**Proyecto:** Maquina de Cafe TDD  
**Lenguaje:** Python  
**Framework de pruebas:** unittest  
**Repositorio:** https://github.com/AMartinez-04/maquina-cafe-tdd  
**Integrante:** Anfeerny Martinez

## Objetivo del sistema

El sistema implementa una maquina dispensadora de cafe aplicando la metodologia TDD. Permite seleccionar el tamano del vaso, seleccionar la cantidad de azucar y servir cafe, validando la disponibilidad de vasos, cafe y azucar antes de descontar los insumos.

## Requisitos principales

- Seleccionar vaso pequeno con 3 Oz de cafe.
- Seleccionar vaso mediano con 5 Oz de cafe.
- Seleccionar vaso grande con 7 Oz de cafe.
- Seleccionar la cantidad de cucharadas de azucar.
- Mostrar un mensaje cuando no hay vasos disponibles.
- Mostrar un mensaje cuando no hay cafe disponible.
- Mostrar un mensaje cuando no hay azucar disponible.
- Descontar los insumos solamente cuando el cafe se sirve correctamente.

## Modelo 4+1

El modelo 4+1 describe la arquitectura del software desde cinco vistas: logica, desarrollo, procesos, fisica y escenarios. Para este proyecto, el modelo se adapta a una aplicacion pequena de dominio orientada a pruebas unitarias.

## 1. Vista logica

La vista logica describe las clases principales del sistema y sus responsabilidades.

### Componentes principales

- **MaquinaCafe:** coordina el flujo de servir cafe. Valida existencia de vasos, cafe y azucar.
- **Vaso:** representa un tipo de vaso, su cantidad disponible y las onzas de cafe que requiere.
- **Cafetera:** administra la cantidad disponible de cafe en onzas.
- **Azucarero:** administra la cantidad disponible de azucar en cucharadas.
- **Pruebas unitarias:** validan los criterios de aceptacion usando TDD.

### Relaciones

- `MaquinaCafe` depende de `Cafetera`, `Azucarero` y una lista de `Vaso`.
- `MaquinaCafe` consulta disponibilidad antes de descontar insumos.
- Las pruebas verifican cada regla funcional del sistema.

## 2. Vista de desarrollo

La vista de desarrollo muestra como esta organizado el codigo fuente.

```text
maquina-cafe-tdd/
  cafe/
    __init__.py
    maquina.py
  tests/
    test_maquina_cafe.py
  .github/
    workflows/
      ci-pipeline.yml
  README.md
  pyproject.toml
  run_tests.bat
```

### Organizacion

- `cafe/maquina.py`: contiene la logica del dominio.
- `tests/test_maquina_cafe.py`: contiene los casos de prueba TDD.
- `.github/workflows/ci-pipeline.yml`: ejecuta el pipeline de integracion continua.
- `README.md`: documenta el objetivo y como ejecutar las pruebas.
- `run_tests.bat`: facilita la ejecucion de pruebas en Windows.

## 3. Vista de procesos

La vista de procesos describe el flujo de ejecucion del sistema.

### Flujo para servir cafe

1. El usuario selecciona el tamano del vaso.
2. El usuario selecciona la cantidad de azucar.
3. La maquina busca el vaso seleccionado.
4. La maquina valida si hay vasos disponibles.
5. La maquina valida si hay cafe suficiente.
6. La maquina valida si hay azucar suficiente.
7. Si todas las validaciones son correctas, descuenta vaso, cafe y azucar.
8. La maquina retorna el mensaje `Cafe servido`.
9. Si falta algun insumo, retorna el mensaje correspondiente sin descontar inventario.

### Flujo de CI/CD

1. Se realiza un `push` o un `pull_request` en GitHub.
2. GitHub Actions clona el repositorio.
3. Se configura Python.
4. Se compila el proyecto con `python -m compileall cafe`.
5. Se ejecutan las pruebas con `python -m unittest discover -s tests -v`.
6. Si todo pasa, el pipeline termina en estado exitoso.

## 4. Vista fisica

La vista fisica describe donde se ejecuta el sistema.

### Entorno local

- Sistema operativo: Windows.
- Ejecucion de pruebas: PowerShell usando `run_tests.bat`.
- Codigo fuente almacenado en el equipo local.

### Entorno remoto

- Repositorio remoto: GitHub.
- Automatizacion: GitHub Actions.
- Sistema del pipeline: `ubuntu-latest`.
- Version de Python del pipeline: 3.12.

## 5. Vista de escenarios

La vista de escenarios conecta la arquitectura con casos de uso reales.

### Escenario 1: Servir vaso pequeno

**Dado** que hay vasos pequenos, cafe y azucar disponibles.  
**Cuando** el consumidor selecciona vaso pequeno y una cantidad valida de azucar.  
**Entonces** la maquina sirve 3 Oz de cafe y descuenta los insumos.

### Escenario 2: Servir vaso mediano

**Dado** que hay vasos medianos, cafe y azucar disponibles.  
**Cuando** el consumidor selecciona vaso mediano.  
**Entonces** la maquina sirve 5 Oz de cafe.

### Escenario 3: Servir vaso grande

**Dado** que hay vasos grandes, cafe y azucar disponibles.  
**Cuando** el consumidor selecciona vaso grande.  
**Entonces** la maquina sirve 7 Oz de cafe.

### Escenario 4: No hay vasos

**Dado** que no hay vasos del tamano seleccionado.  
**Cuando** el consumidor intenta servir cafe.  
**Entonces** la maquina retorna el mensaje `No hay vasos`.

### Escenario 5: No hay cafe

**Dado** que la cafetera no tiene cafe suficiente.  
**Cuando** el consumidor intenta servir cafe.  
**Entonces** la maquina retorna el mensaje `No hay cafe`.

### Escenario 6: No hay azucar

**Dado** que el azucarero no tiene azucar suficiente.  
**Cuando** el consumidor intenta servir cafe.  
**Entonces** la maquina retorna el mensaje `No hay azucar`.

## Decisiones tecnicas

- Se uso Python porque la practica no exigia un lenguaje especifico.
- Se uso `unittest` porque viene incluido con Python y permite aplicar TDD sin dependencias externas.
- Se separo la logica del dominio de las pruebas para mantener una estructura simple y clara.
- Se configuro GitHub Actions para validar automaticamente el proyecto con cada cambio.

## Conclusion

La arquitectura propuesta es sencilla y adecuada para el alcance de la practica. El diseno separa responsabilidades entre la maquina, los vasos, la cafetera y el azucarero, y se apoya en pruebas unitarias para garantizar que los criterios de aceptacion se cumplen.
