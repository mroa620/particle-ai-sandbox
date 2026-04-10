# `cfd_tools.py`

## Qué hace

Este módulo reúne funciones pequeñas de apoyo para cálculos CFD sencillos.

Ahora mismo incluye:

- cálculo y validación del número de Reynolds,
- cálculo y validación del número de Froude.

## Para qué sirve dentro del proyecto

Su función principal en esta etapa es doble:

- practicar modularización en Python,
- empezar a reunir utilidades reutilizables con sentido ingenieril.

## Funciones disponibles

### `reynolds_calculator(...)`

Calcula el número de Reynolds a partir de densidad, velocidad, longitud característica y viscosidad dinámica.

### `validate_reynolds(Re)`

Interpreta el valor de Reynolds e indica si el régimen es laminar, transitorio o turbulento.

### `froude_calculator(...)`

Calcula el número de Froude a partir de velocidad, longitud y gravedad.

### `froude_validation(Fr)`

Interpreta el valor de Froude e indica si el régimen es subcrítico, crítico o supercrítico.

## Cómo se usa

Ejemplo sencillo:

```python
from src.cfd_tools import reynolds_calculator, validate_reynolds

Re = reynolds_calculator(1000, 2.5, 0.1, 0.001)
validate_reynolds(Re)
```

## Idea de diseño

El módulo está pensado como una librería pequeña de funciones simples y fáciles de leer.

No busca todavía una arquitectura avanzada. La prioridad aquí es que el código sea entendible y útil como base.

## Limitaciones actuales

Por ahora:

- no hay tests,
- no hay type hints,
- algunas funciones mezclan cálculo y mensajes por pantalla,
- el módulo todavía es pequeño y muy inicial.

## Posibles mejoras futuras

A medida que el repositorio crezca, se podrá:

- añadir más utilidades CFD,
- separar mejor cálculo y presentación,
- introducir tests,
- refactorizar el módulo cuando haya más experiencia con Python intermedio.