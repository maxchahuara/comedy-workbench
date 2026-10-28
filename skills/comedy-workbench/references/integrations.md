# Optional integrations and boundaries

The bundled helper needs no integration. Select another tool only when it adds
evidence needed for this draft. Nothing here installs software or supplies keys.

- **LanguageTool:** a local instance can supply grammar suggestions. Review each
  suggestion against dialect, persona, and intentional phrasing. The local open
  core excludes the cloud AI rules. If writing an adapter, remember that text
  offsets may use UTF-16 units; an emoji can make a Python character index differ.
- **Vale:** useful for a recurring publication with explicit vocabulary and style
  conventions. Custom rules should quote evidence and permit intentional exceptions.
  Rules written for English technical documentation are not a comedy style guide.
- **textstat:** reading metrics may direct attention to a dense passage. They are
  not speaking-time measurements, naturalness judgments, or comic-quality goals.
- **Sentence Transformers:** optional semantic retrieval over an authorized archive
  can find related ideas. Choose language-appropriate models and inspect their own
  licenses. Retrieval scores are not originality certificates. The bundled search
  does only lexical word-bigram overlap; it does not load this dependency.
- **Audacity or an existing audio editor:** use timed labels and comparable readings.
  Do not count the same interval twice when speech and action overlap.
- **WhisperX:** optional alignment aid when actual audio exists. Model and dictionary
  coverage affect times. Installation, model downloads, and generated files are
  separate actions; this package performs none of them.
- **Laughter detectors:** useful for locating candidate reaction intervals in real
  recordings. Review false positives, background tracks, and temporal attribution.
  The helper's rehearsal records are annotations, not detector output.
- **Trelby, Beat, Scrite, Story Architect:** can organize versions and performance
  documents. Their pagination rules do not predict monologue duration. Their license
  and commercial-component terms apply independently of this project.

For generative tools, include the same source text, brief, and constraints when
comparing methods. A second model or an extra critic does not become independent
human audience evidence. Do not add an orchestration framework merely to reproduce
a small editorial pass that can already be performed in the current conversation.
