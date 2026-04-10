# Estructura del proyecto

## Visión general

La estructura actual del repositorio busca separar de forma clara:

- código fuente,
- datos,
- documentación,
- material privado de estudio.

Para una primera versión pública, esta organización es suficiente y bastante razonable.

## Árbol principal

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

## Carpetas principales

### `src/`

Contiene el código fuente del proyecto.

Aquí están los scripts principales:

- `physical_data_extractor_v0.py`
- `config_gen.py`
- `cfd_tools.py`

### `data/`

Contiene los datos del proyecto.

#### `data/sample/`

Incluye ejemplos públicos para hacer pruebas y enseñar el funcionamiento del repositorio.

#### `data/raw/`

Pensada para entradas en bruto.

#### `data/private/`

Reservada para datos que no conviene publicar.

### `docs/`

Contiene documentación técnica y descripciones del proyecto.

### `outputs/`

Reservada para futuras salidas generadas por scripts o pipelines.

### `private_study/`

Guarda material personal de estudio. No forma parte del núcleo público del proyecto.

## Criterio general de organización

La idea es que el repositorio pueda crecer sin mezclar cosas distintas.

En resumen:

- el código va en `src/`,
- los ejemplos públicos van en `data/sample/`,
- la documentación va en `docs/`,
- lo privado se mantiene aparte.

## Por qué esta estructura tiene sentido ahora

En esta etapa aún no hace falta una arquitectura más compleja.

Una estructura plana y clara ayuda más que una estructura demasiado avanzada, porque permite:

- entender rápido el proyecto,
- trabajar sin perderse,
- publicar una primera versión limpia,
- refactorizar más adelante con mejor criterio.

## Evolución futura probable

Cuando el proyecto crezca, será normal añadir:

- `tests/`
- una estructura más modular dentro de `src/`
- documentación más completa
- más separación entre scripts de prueba y componentes reutilizables

## Conclusión

La estructura actual es simple, pero válida para una primera publicación. Lo importante ahora es que sea clara, coherente y fácil de mantener mientras sigues aprendiendo y construyendo.
