Instrucciones para NotebookLM 2

Puntos pendientes
2. loadcsv debe devolver algo consistente si falla

Quiero que revises mi función de carga para que tenga un contrato claro:

si el archivo existe y se puede leer, devuelve la lista de filas;
si falla por FileNotFoundError, debe devolver [];
evita comportamientos ambiguos;
deja el flujo del programa claro y fácil de entender para nivel Python desde cero.
3. Mejorar trazabilidad de errores por fila

Quiero que el procesamiento de filas siga siendo simple, pero más útil:

si una fila falla, no debe romper todo el proceso;
quiero saber qué fila falló y por qué;
idealmente mostrar:
índice de la fila, o
algún identificador como id_particle si existe;
mantener el enfoque sencillo, sin logging avanzado.
5. Resumen final del procesamiento

Quiero que al final del script se imprima un pequeño resumen útil:

cuántas filas se leyeron,
cuántas filas válidas se guardaron,
cuántas filas se descartaron.
Restricción importante

Quiero mantener esto en nivel Python desde cero / A1.1:

funciones simples,
nada de arquitectura compleja,
nada de clases extra,
nada de logging avanzado,
cambios pequeños y claros sobre mi código actual.
Lo que necesito de ti

Quiero que me propongas:

los cambios mínimos necesarios,
el código corregido de esas partes,
una explicación breve y didáctica de por qué esos cambios mejoran la reproducibilidad y la robustez del extractor.