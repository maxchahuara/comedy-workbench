# Independent use case: long-to-short adaptation

The evaluating assistant was asked to extract an autonomous 25–45-second short
from the end of [the long example](../examples/monologue.json), preserving voice
without relying on an introduction viewers would not see.

## Performance draft produced

El vendedor me dijo que mi casa inteligente estaría bajo mi control. Hasta me puso
título: usuario administrador.

Una noche se fue la luz. La lavadora no reclamó. El refrigerador no opinó sobre mi
cena. Mi esposa encendió una vela.

Volvió la luz: «Hemos detectado inactividad. ¿Desea reiniciar?».

Miré el teléfono, miré la vela… y pedí cinco minutos más de garantía.

La casa ya era inteligente. El que todavía estaba en período de prueba era el
usuario administrador.

Dirección: empieza seguro; después de la vela, disfruta dos segundos de silencio.
Termina como quien admite la derrota, con una pausa de un segundo antes de la
última frase.

## Inspection

The [annotated version](short-from-monologue.json) has 78 word-like units and three
explicit extra seconds. At 125–155 words/minute its estimated range is 33.19–40.44
seconds. No reading was timed or listened to.

The adaptation replants the administrator title, omits the earlier ocean-lighting
reference and reduces the longer emotional development. The closing return can
therefore be inspected within the short itself. Whether the warranty line and
delivery land remains an artistic question for rehearsal, not a passing unit test.
