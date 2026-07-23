# Diseño técnico 4+1 - Máquina de Café TDD

## Información general

**Proyecto:** Máquina de Café TDD  
**Lenguaje:** Python  
**Framework de pruebas:** unittest  
**Repositorio:** https://github.com/AMartinez-04/maquina-cafe-tdd  
**Integrante:** Anfeerny Martinez

## Objetivo del sistema

El sistema implementa una máquina dispensadora de café aplicando la metodología TDD. Permite seleccionar el tamaño del vaso, seleccionar la cantidad de azúcar y servir café, validando la disponibilidad de vasos, café y azúcar antes de descontar los insumos.

## Requisitos principales

- Seleccionar vaso pequeño con 3 Oz de café.
- Seleccionar vaso mediano con 5 Oz de café.
- Seleccionar vaso grande con 7 Oz de café.
- Seleccionar la cantidad de cucharadas de azúcar.
- Mostrar un mensaje cuando no hay vasos disponibles.
- Mostrar un mensaje cuando no hay café disponible.
- Mostrar un mensaje cuando no hay azúcar disponible.
- Descontar los insumos solamente cuando el café se sirve correctamente.

## Modelo 4+1

El modelo 4+1 describe la arquitectura del software desde cinco vistas: lógica, desarrollo, procesos, física y escenarios. Para este proyecto, el modelo se adapta a una aplicación pequeña de dominio orientada a pruebas unitarias.

## 1. Vista lógica

La vista lógica describe las clases principales del sistema y sus responsabilidades.

### Componentes principales

- **MaquinaCafe:** coordina el flujo de servir café. Valida existencia de vasos, café y azúcar.
- **Vaso:** representa un tipo de vaso, su cantidad disponible y las onzas de café que requiere.
- **Cafetera:** administra la cantidad disponible de café en onzas.
- **Azucarero:** administra la cantidad disponible de azúcar en cucharadas.
- **Pruebas unitarias:** validan los criterios de aceptación usando TDD.

### Relaciones

- `MaquinaCafe` depende de `Cafetera`, `Azucarero` y una lista de `Vaso`.
- `MaquinaCafe` consulta disponibilidad antes de descontar insumos.
- Las pruebas verifican cada regla funcional del sistema.

## 2. Vista de desarrollo

La vista de desarrollo muestra cómo está organizado el código fuente.

```text
maquina-cafe-tdd/
├── cafe/
│   ├── __init__.py
│   └── maquina.py
├── tests/
│   └── test_maquina_cafe.py
├── .github/
│   └── workflows/
│       └── ci-pipeline.yml
├── README.md
├── pyproject.toml
└── run_tests.bat
```

### Organización

- `cafe/maquina.py`: contiene la lógica del dominio.
- `tests/test_maquina_cafe.py`: contiene los casos de prueba TDD.
- `.github/workflows/ci-pipeline.yml`: ejecuta el pipeline de integración continua.
- `README.md`: documenta el objetivo y cómo ejecutar las pruebas.
- `run_tests.bat`: facilita la ejecución de pruebas en Windows.

## 3. Vista de procesos

La vista de procesos describe el flujo de ejecución del sistema.

### Flujo para servir café

1. El usuario selecciona el tamaño del vaso.
2. El usuario selecciona la cantidad de azúcar.
3. La máquina busca el vaso seleccionado.
4. La máquina valida si hay vasos disponibles.
5. La máquina valida si hay café suficiente.
6. La máquina valida si hay azúcar suficiente.
7. Si todas las validaciones son correctas, descuenta vaso, café y azúcar.
8. La máquina retorna el mensaje `Cafe servido`.
9. Si falta algún insumo, retorna el mensaje correspondiente sin descontar inventario.

### Flujo de CI/CD

1. Se realiza un `push` o un `pull_request` en GitHub.
2. GitHub Actions clona el repositorio.
3. Se configura Python.
4. Se compila el proyecto con `python -m compileall cafe`.
5. Se ejecutan las pruebas con `python -m unittest discover -s tests -v`.
6. Si todo pasa, el pipeline termina en estado exitoso.

## 4. Vista física

La vista física describe dónde se ejecuta el sistema.

### Entorno local

- Sistema operativo: Windows.
- Ejecución de pruebas: PowerShell usando `run_tests.bat`.
- Código fuente almacenado en el equipo local.

### Entorno remoto

- Repositorio remoto: GitHub.
- Automatización: GitHub Actions.
- Sistema del pipeline: `ubuntu-latest`.
- Versión de Python del pipeline: 3.12.

## 5. Vista de escenarios

La vista de escenarios conecta la arquitectura con casos de uso reales.

### Escenario 1: Servir vaso pequeño

**Dado** que hay vasos pequeños, café y azúcar disponibles.  
**Cuando** el consumidor selecciona vaso pequeño y una cantidad válida de azúcar.  
**Entonces** la máquina sirve 3 Oz de café y descuenta los insumos.

### Escenario 2: Servir vaso mediano

**Dado** que hay vasos medianos, café y azúcar disponibles.  
**Cuando** el consumidor selecciona vaso mediano.  
**Entonces** la máquina sirve 5 Oz de café.

### Escenario 3: Servir vaso grande

**Dado** que hay vasos grandes, café y azúcar disponibles.  
**Cuando** el consumidor selecciona vaso grande.  
**Entonces** la máquina sirve 7 Oz de café.

### Escenario 4: No hay vasos

**Dado** que no hay vasos del tamaño seleccionado.  
**Cuando** el consumidor intenta servir café.  
**Entonces** la máquina retorna el mensaje `No hay vasos`.

### Escenario 5: No hay café

**Dado** que la cafetera no tiene café suficiente.  
**Cuando** el consumidor intenta servir café.  
**Entonces** la máquina retorna el mensaje `No hay cafe`.

### Escenario 6: No hay azúcar

**Dado** que el azucarero no tiene azúcar suficiente.  
**Cuando** el consumidor intenta servir café.  
**Entonces** la máquina retorna el mensaje `No hay azucar`.

## Decisiones técnicas

- Se usó Python porque la práctica no exigía un lenguaje específico.
- Se usó `unittest` porque viene incluido con Python y permite aplicar TDD sin dependencias externas.
- Se separó la lógica del dominio de las pruebas para mantener una estructura simple y clara.
- Se configuró GitHub Actions para validar automáticamente el proyecto con cada cambio.

## Conclusión

La arquitectura propuesta es sencilla y adecuada para el alcance de la práctica. El diseño separa responsabilidades entre la máquina, los vasos, la cafetera y el azucarero, y se apoya en pruebas unitarias para garantizar que los criterios de aceptación se cumplen.
