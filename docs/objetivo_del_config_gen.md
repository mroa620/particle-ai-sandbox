# `config_gen.py`

## Qué hace

Este script genera un archivo `config.json` a partir de datos introducidos por consola.

Su objetivo es tener una forma simple y ordenada de guardar la configuración básica de un caso.

## Para qué sirve dentro del proyecto

En esta fase del repositorio, `config_gen.py` sirve para practicar tres cosas importantes:

- recoger datos de entrada de forma estructurada,
- validarlos antes de guardarlos,
- construir un JSON útil para futuras herramientas.

## Qué información pide

El script solicita varios datos agrupados en bloques lógicos:

- metadatos del caso,
- propiedades del fluido,
- parámetros de referencia,
- ajustes básicos del solver,
- condiciones iniciales.

## Estructura del JSON generado

El archivo final se organiza así:

```json
{
  "metadata": {},
  "physics": {
    "fluid_properties": {},
    "dimensionless_params": {}
  },
  "solver_settings": {},
  "initial_conditions": {}
}
```

## Validaciones que ya incluye

El script comprueba varias cosas básicas:

- que ciertos campos de texto no estén vacíos,
- que algunos valores numéricos sean positivos,
- que `total_time` sea mayor que `time_step`,
- que `particle_id` sea un entero no negativo,
- que posición y velocidad inicial tengan dos componentes.

También muestra un aviso si el `time_step` parece demasiado grande respecto al tiempo total.

## Cómo se ejecuta

Desde la raíz del proyecto:

```bash
python src/config_gen.py
```

## Salida

El archivo generado se guarda en:

```text
data/sample/config.json
```

## Idea de diseño

La idea aquí no es hacer un generador complejo, sino tener una primera herramienta sencilla, legible y útil para practicar entrada de datos, validación y guardado en JSON.

## Limitaciones actuales

Esta versión todavía es básica:

- funciona solo de forma interactiva,
- no usa tests,
- no separa del todo la lógica de la interfaz por consola,
- no valida coherencia física avanzada.

## Posibles mejoras futuras

Más adelante tendría sentido:

- separar la lógica de creación del JSON de la parte interactiva,
- permitir lectura desde archivo o argumentos,
- añadir tests,
- reutilizar esta configuración desde otros módulos del proyecto.