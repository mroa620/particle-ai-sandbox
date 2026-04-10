# Particle AI Sandbox

Repositorio de aprendizaje aplicado para construir las primeras piezas del **Particle AI Accelerator**.

Ahora mismo este repo recoge utilidades y scripts sencillos de Python orientados a:

- limpiar datos de ejemplo de una simulación,
- generar un archivo básico de configuración,
- practicar pequeñas herramientas de apoyo para CFD,
- mantener una estructura de proyecto clara desde el inicio.

La idea no es presentar un producto cerrado, sino una base que pueda ir creciendo de forma ordenada a medida que avance el máster.

## Estado actual

Este repositorio está en una fase temprana.

Incluye una primera versión funcional de:

- un extractor de datos físicos desde CSV a JSON,
- un generador interactivo de configuración,
- un módulo con utilidades CFD básicas.

Seguirá evolucionando con mejoras de estructura, documentación y calidad de código.

## Estructura del proyecto

```text
.
├── data/
│   ├── private/
│   ├── raw/
│   └── sample/
├── docs/
├── outputs/
├── private_study/
└── src/
```

## Archivos principales

### `src/physical_data_extractor_v0.py`

Lee un CSV de ejemplo, valida su estructura, convierte campos numéricos, renombra variables y guarda un JSON limpio.

### `src/config_gen.py`

Pide por consola varios datos del caso y genera un `config.json` con una estructura organizada.

### `src/cfd_tools.py`

Incluye funciones sencillas para calcular e interpretar números adimensionales como Reynolds y Froude.

## Datos de ejemplo

En `data/sample/` hay ficheros públicos de demo para poder probar el proyecto sin usar datos privados.

Ejemplos actuales:

- `simulacion_particulas.csv`
- `datos_limpios.json`
- `config.json`

## Cómo ejecutar los scripts

Desde la raíz del proyecto:

```bash
python src/physical_data_extractor_v0.py
```

```bash
python src/config_gen.py
```

## Objetivo de esta primera versión pública

El objetivo de esta versión no es enseñar una arquitectura avanzada, sino mostrar:

- una progresión real de aprendizaje,
- scripts funcionales y entendibles,
- una base seria para seguir construyendo.

## Qué iré mejorando

Algunas mejoras previstas para siguientes iteraciones:

- tests básicos,
- mejor separación entre lógica y ejecución por consola,
- documentación más completa,
- refactor progresivo de estructura,
- nuevos módulos relacionados con el Accelerator.

## Documentación adicional

- `docs/estructura_proyecto.md`
- `docs/config_gen_tecnica.md`
- `docs/cfd_tools_tecnica.md`

## Nota

Este repositorio forma parte de un proceso de aprendizaje orientado a producto. Por eso el foco está en construir bien la base, documentar con claridad y evolucionar el código paso a paso.