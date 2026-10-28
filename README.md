# Comedy Workbench

**Un taller abierto para revisar chistes, shorts y monólogos largos con ayuda de
una IA, conservando la voz del autor.**

[English](README.en.md) · [Skill](skills/comedy-workbench/SKILL.md) ·
[Ejemplos](examples/EDITORIAL_NOTES.md) · [Fuentes y decisiones](research/DECISIONS.md)

El paquete combina una skill editorial y un analizador local. La skill ayuda a
examinar premisas, expectativas, remates, desarrollo, retornos y actuación. El
analizador aporta evidencia repetible: duración estimada, restricciones explícitas,
dependencias entre beats, comparación de versiones y observaciones de ensayo.

Es una implementación propia informada por estudio de software y publicaciones;
no reúne código de esas aplicaciones ni contiene sus corpus, modelos o servicios.
Su método no tiene una mejora de respuesta del público demostrada.

## Usarlo sin instalar nada

Descarga el repositorio y abre [SKILL.md](skills/comedy-workbench/SKILL.md) en tu
asistente de IA, o pídele que lo lea. No hace falta instalar la skill para estudiarla.

Ejemplos de solicitudes:

> Usa esta skill para mejorar el remate de mi chiste. Conserva mi español y mi
> personaje. Dame alternativas que cambien el mecanismo, con la razón del cambio.

> Convierte este fragmento de monólogo en un short autónomo de 35 segundos.
> Conserva la premisa; separa el texto hablado de la reacción visual.

> Revisa este monólogo completo. Primero localiza bloques repetidos y callbacks
> sin preparación. Después propón una revisión con cambios justificados.

La skill no incluye un modelo de lenguaje: la capacidad de redacción procede del
asistente que la utilice. Una revisión ordinaria puede hacerse directamente en la
conversación, sin JSON, carpetas ni informes extensos.

## Analizador opcional

Requiere **Python 3.10 o posterior**, sin dependencias adicionales. Ejecútalo desde
la carpeta del repositorio:

```bash
python workbench.py analyze examples/short.json --ui-language es
python workbench.py compare examples/joke-original.json examples/joke-revision.json
python workbench.py analyze examples/monologue.json --output-format json
python workbench.py review-pack examples/short.json review-short-v1
```

En Windows puedes sustituir `python` por `py -3.11` si ese es tu intérprete disponible.
Los comandos de análisis no modifican el guion. Los archivos de salida existentes
no se sobrescriben. `review-pack` crea una carpeta nueva con el original, su hash,
el contexto, el informe y la guía del formato para una revisión posterior.

| Comando | Resultado |
|---|---|
| `new joke/short/monologue archivo.json` | Plantilla editable, sin duración obligatoria |
| `analyze archivo.txt --format short` | Análisis de texto sin inventar anotaciones |
| `analyze archivo.json` | Métricas y comprobaciones sobre beats declarados |
| `check archivo.json` | Código de salida 1 si incumple frases/límite de palabras explícitos |
| `compare original.json revision.json` | Diff y revisión contra las restricciones originales |
| `search texto.txt archivo-previo.txt otro.json` | Coincidencia léxica, sin embeddings ni certificado de originalidad |
| `rehearsal guion.json observaciones.json` | Intervalos anotados; identifica qué beats no se observaron |
| `review-pack guion.json carpeta-nueva` | Paquete de revisión; no llama a un modelo |

Consulta el [contrato de datos y límites](skills/comedy-workbench/references/data-format.md)
antes de interpretar los resultados. Los encabezados del informe pueden mostrarse
en español o inglés; los mensajes técnicos detallados están actualmente en inglés.
La skill responde en el idioma del usuario.

## Qué formatos contempla

- **Chistes cortos:** información necesaria, expectativa, giro, naturalidad y remates
  adicionales que realmente agregan una consecuencia.
- **Shorts:** contexto autónomo, relación entre voz e imagen, acción legible,
  reacción, duración y adaptación desde un texto largo.
- **Monólogos largos:** desarrollo por bloques, cambio de perspectiva, contraste
  de ritmo, preparación de callbacks, continuidad y cierre ganado.

No impone un número universal de risas, palabras, actos o segundos. El ejemplo de
monólogo tiene 923 unidades de palabra y una duración **estimada** aproximada de
6–8 minutos según sus supuestos; el método puede usarse con textos más largos.

## Cómo juzgar una mejora

Mantén el original en la comparación, identifica el problema concreto y escucha
versiones con interpretación comparable. Separa una hipótesis editorial de una
reacción observada. Las risas añadidas en edición y las personas simuladas por una
IA no son un público que haya probado el guion.

El analizador no puntúa gracia, verdad factual, originalidad mundial ni calidad
actoral. La duración supone ritmos de palabra constantes y pausas/acciones
adicionales sin superposición. El texto sin anotaciones cuenta también títulos
y acotaciones. Verifica los hechos de una sátira de actualidad con fuentes actuales.

## Estudio y atribución

El [catálogo](research/sources.json) conserva URLs, revisiones, hashes, alcance de
lectura y decisiones. Las descargas se mantuvieron fuera del repositorio público.
Hay fuentes abiertas, fuentes con restricciones y servicios propietarios; sus
licencias no se unifican con la de este proyecto. [Detalle de procedencia](NOTICE.md).

Se conservaron criterios aprovechables y se descartaron reglas ajenas al formato,
cuotas rígidas, automatización sin una ventaja demostrada y evaluaciones que
confunden una nota del modelo con una reacción humana. Ver [decisiones](research/DECISIONS.md).

## Verificar y contribuir

```bash
python -m unittest discover -s tests -v
python tools/verify_project.py
```

Las pruebas técnicas no certifican calidad cómica. Las pruebas editoriales de uso
se documentan por separado en [evaluación](evaluation/REPORT.md).
Lee [CONTRIBUTING.md](CONTRIBUTING.md) para aportar correcciones, nuevos formatos o
evidencia de uso. Código e instrucciones propios bajo [MIT](LICENSE).
