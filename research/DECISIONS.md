# Qué se conservó, qué se descartó y por qué

Estudio realizado el 28 de octubre de 2026. El [catálogo](sources.json) contiene las
40 entradas de adquisición: 20 repositorios descargados, 18 documentos descargados
y dos entradas no disponibles. Conserva commit, hash del archivo descargado y hash
de los archivos inspeccionados cuando corresponde. Las copias completas están en
la carpeta de estudio externa al repositorio público; ningún código descargado fue
instalado, compilado, importado o ejecutado como parte de este trabajo.

La lectura fue dirigida a los módulos pertinentes y a sus límites: no una auditoría
de todas las líneas de aplicaciones grandes. Los artículos PDF se examinaron por
extracción de texto; DeHumor también mediante su versión HTML en arXiv. Se consultó
documentación de servicios cerrados sin obtener ni reconstruir su implementación.

## Decisiones editoriales

| Observación del estudio | Decisión en nuestra implementación |
|---|---|
| Una instrucción repetible puede enfocar la revisión, pero sigue dependiendo del modelo que la lea. | Skill autónoma y legible directamente; no se incluye ni se promete un modelo superior. |
| Una preparación débil no se arregla necesariamente puliendo la última palabra. | Diagnosticar nivel: premisa, desarrollo, orden de información, frase o interpretación. |
| La especificidad, la voz y el contexto cambian lo que el público entiende. | Mantener un brief del autor; separar hechos de invención y conservar dialecto. |
| Las alternativas pueden explorar mecanismos diferentes o repetir el mismo molde. | Generar opciones donde ayuden; conservar original y justificar selección, sin cuota fija. |
| Un short extraído puede perder el contexto que sostenía el final. | Replantar antecedentes dentro del clip y registrar qué se pierde al adaptar. |
| Un monólogo necesita desarrollo y distribución de experiencias. | Mapa por bloques y dependencias; no convertirlo en una lista de chistes sueltos. |
| La repetición puede ser un defecto, una anticipación, un running gag o un callback. | Mostrar coincidencias como preguntas editoriales; conservar intención declarada. |
| Los ritmos de comedia dependen de voz, acción y reacción. | Tiempo estimado con supuestos visibles; ensayo anotado como categoría separada. |

## Decisiones de ingeniería

El helper se escribió desde cero con Python estándar. La búsqueda incorporada usa
bigramas léxicos; no finge las capacidades de Sentence Transformers. La comparación
usa el brief original, por lo que quitar una restricción del archivo nuevo no la
elimina de la revisión. Los IDs permiten detectar referencias inexistentes o
posteriores, pero no deciden si el giro es bueno.

Las salidas conservan hashes y dejan intactos los originales. Un paquete de revisión
contiene el texto y el método aplicable; no ejecuta instrucciones dentro del guion
ni llama a un servicio. Las integraciones más grandes permanecen opcionales y
externas. Su ausencia está documentada en vez de ocultarse detrás de un nombre.

## Reglas descartadas

- Cuotas de risas por página o minuto como prueba universal de calidad.
- Formatos, actos, márgenes o extensiones de sitcom aplicados automáticamente a
  un monólogo, un one-liner o una escena visual.
- Un gancho obligatorio de tres segundos o una duración fija para todos los shorts.
- Reescribir siempre para acortar, eliminar cualquier silencio o tratar toda
  repetición como redundancia.
- Cambiar hechos personales para que encajen mejor sin decir que se están inventando.
- Sustituir la voz del autor por una imitación de un famoso.
- Escalas precisas de gracia generadas por el mismo sistema, aprobación por llegar
  a la tercera ronda o personas simuladas presentadas como público independiente.
- Incorporar un framework de agentes, embeddings o generación audiovisual sin que
  resuelva una necesidad observable de esta versión.

## Evidencia que limita las promesas

[RAGthoven](https://arxiv.org/html/2607.13189v1) aporta un procedimiento reproducible
y resultados en español, pero su mayor puntuación bruta no fue una victoria
estadística sobre la referencia simple. Las variantes de agentes se compararon
cualitativamente sobre una muestra pequeña en inglés. No se puede convertir ese
resultado en una mejora demostrada de monólogos largos.

[Jokeasy](https://arxiv.org/abs/2602.09496) estudia ideación temática con usuarios
chinohablantes y control del autor. Sus límites reconocen que no cubre la edición
completa de un guion de stand-up. Aprovechamos la atención al material/contexto;
no declaramos haber reproducido su sistema o su evaluación.

[OpenMic](https://arxiv.org/html/2601.08288v1) distingue funciones de escritura,
audiencia e interpretación, pero sus puntuaciones por modelo no equivalen a una
audiencia española. El repositorio enlazado por el artículo no estaba accesible.
La implementación alternativa inspeccionada queda identificada como tal.

[DeHumor](https://arxiv.org/html/2107.08356v1) hace visible la relación entre contexto,
repetición e interpretación. Su segmentación que toma la frase anterior a una risa
como punchline es una heurística de análisis, no una regla causal que adoptemos.
[TIC-TALK](https://arxiv.org/abs/2603.21803) analiza señales multimodales de especiales
editados; sus correlaciones no justifican ordenar a todo comediante moverse menos.

El [estudio con comediantes](https://arxiv.org/html/2405.20956v1) identifica problemas
de voz, contexto y resultados genéricos en los modelos evaluados entonces. Eso
motiva una comparación contra el autor y su público, sin extender la conclusión
a todos los modelos actuales o futuros.

## Procedencia y licencias

El catálogo atribuye también LanguageTool, Vale, textstat, Sentence Transformers,
Audacity, WhisperX, laughter-detection, Trelby, Dramatron, las colecciones de skills,
Scrite, Story Architect y Beat. Sus implementaciones fueron material de estudio,
no piezas copiadas a este paquete. Las restricciones de Moltline y el NOTICE de
screenwriting-skills se revisaron expresamente. Ver [NOTICE.md](../NOTICE.md).

Esta versión aporta una herramienta revisable y comprobaciones técnicas. No es
un benchmark de todos los programas descargados, un reemplazo de su software ni
una mejora artística demostrada con público. Los [ejemplos](../examples/EDITORIAL_NOTES.md)
y la [prueba de consumo](../evaluation/REPORT.md) permiten examinar qué hace realmente.
