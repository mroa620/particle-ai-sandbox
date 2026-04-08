Instrucciones para NotebookLM

Quiero que me ayudes a convertir mi physical_data_extractor_v0.py en una versión que sí apruebe el gate A1.1 del PRD.

Objetivo del trabajo

Construir una versión mínima pero completa y reproducible del extractor físico de datos.

Qué debe hacer esta versión v0

La nueva versión debe:

Leer un CSV real desde disco.
Convertir cada fila en una estructura manejable en Python.
Validar que cada fila tenga las columnas requeridas.
Sanear los campos numéricos relevantes convirtiéndolos a float.
Conservar también el resto de campos importantes, no perderlos por el camino.
Renombrar sensores/columnas usando un name_map.
Filtrar filas inválidas si faltan campos críticos o si algún valor crítico es None.

Guardar la salida final en un archivo estándar sencillo para esta fase, por ejemplo:

JSON o
CSV limpio

Para esta versión v0 no hace falta aún parquet, hdf5 ni PyTorch. Eso puede quedarse como extensión futura.

Incluir un ejemplo de uso reproducible, con:
archivo de entrada de ejemplo,
configuración de ejemplo,
ejecución completa,
archivo de salida generado.
Restricción pedagógica

Quiero una solución apropiada para alguien que está en Python desde cero, no en Python intermedio.
Por tanto:

prioriza funciones simples,
evita arquitectura compleja,
evita clases innecesarias,
evita decoradores o patrones avanzados,
usa solo Python estándar si es posible.
Qué problemas tiene mi versión actual y hay que corregir

Analiza mi código actual teniendo en cuenta estos puntos:

Ahora mismo el pipeline trabaja con una lista en memoria, pero no lee un CSV real.
Falta una salida persistida a archivo.
Falta una demo reproducible de extremo a extremo.
sanitize_data devuelve solo los campos convertidos a float y eso puede hacer que se pierdan columnas originales importantes.
Quiero que el manejo de errores sea simple pero útil:
si una fila falla, debe poder descartarse sin romper todo el proceso;
pero también quiero saber por qué fue descartada.
Qué quiero que me propongas

Quiero que me propongas, en este orden:

Una estructura mínima del script.
Qué funciones concretas debe tener.
Qué responsabilidad tiene cada función.
Qué nombre y contenido debe tener el config.
Un ejemplo de CSV de entrada pequeño.
Un ejemplo de salida esperada.
Una versión de código completa, simple y comentada.
Un bloque if __name__ == "__main__": para ejecutar el ejemplo.
Una mini checklist final para verificar que el extractor ya es reproducible.
Criterios de calidad

La solución debe cumplir estas reglas:

código claro y legible,
nombres comprensibles,
funciones cortas,
sin trucos avanzados,
sin perder columnas importantes accidentalmente,
con separación razonable entre:
lectura,
transformación,
guardado.
Decisión importante de diseño

Para esta fase, quiero que la salida estándar sea JSON o CSV limpio, elige la más sencilla para aprender mejor.
Explícame por qué la eliges.

Importante

No quiero solo correcciones locales de mi código actual.
Quiero que me ayudes a producir una versión v0 cerrable como mini-producto, pero manteniendo el nivel de dificultad adecuado para Python desde cero