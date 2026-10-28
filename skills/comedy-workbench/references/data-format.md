# Local tool and data contract (schema 1)

Run the script directly with Python 3.10+. It uses only the standard library. The
repository's workbench.py is a convenience launcher; the skill's script is portable
with its references and assets. No install step, model, account, or GPU is needed.

## Text or annotations

Analyze accepts UTF-8 .txt/.md/.fountain as raw text. Paragraphs get temporary IDs;
every word-like unit is counted, including headings and stage directions. The tool
does not recognize Fountain elements or infer setups, punchlines, or callbacks.
Use annotated .json for separate speech/directions and dependency checks. All
analyzed inputs stay unchanged. Reports cannot overwrite an existing file.

```json
{
  "schema_version": 1,
  "title": "Example",
  "format": "short",
  "language": "es-PE",
  "target_seconds": [20, 50],
  "delivery": {"wpm_min": 125, "wpm_max": 165},
  "constraints": {"required_phrases": ["mi lavadora"], "max_words": 100},
  "beats": [
    {"id": "plant", "kind": "setup", "text": "Ahora mi lavadora me escribe."},
    {"id": "turn", "kind": "punch", "setup_id": "plant", "text": "Le dejé en visto.", "pause_seconds": 1},
    {"id": "look", "kind": "hold", "text": "", "direction": "Mira la ropa acumulada.", "action_seconds": 2}
  ]
}
```

Required root fields are schema_version, format, and a non-empty beats list. Format
is joke, short, or monologue. Every beat needs id, kind, and text. IDs are stable
ASCII letters/digits/periods/underscores/hyphens; spoken text is Unicode. Language
defaults to es if absent. Supported kinds are context, opener, setup, punch, tag,
callback, bridge, act-out, hold, closer. A hold has empty spoken text.

Optional root fields: title, language, premise, voice (object), audience (object),
facts (list of objects), delivery, target_seconds, constraints, review_settings.
Voice/audience/facts are human context; the tool does not verify their meaning.
Keep private personal material out of public examples and review bundles.

Optional beat fields: direction, block, setup_id, callback_to, pause_seconds,
action_seconds, notes, intentional_repetition (boolean). References must point to
an earlier existing beat. The tool checks order/existence, not whether the plant
actually earns the payoff. A declared callback without a link produces an editorial
question, not an artistic failure.

## Constraint and time semantics

- required_phrases: exact, case-sensitive NFC-normalized substring in spoken text.
  A phrase spanning differently formatted line breaks is considered changed.
- forbidden_phrases: case-insensitive consecutive word-like tokens. 'mal' will not
  match 'normal'. Punctuation-only forbidden phrases are unsupported and rejected.
- max_words: positive integer, using the documented word-like tokenizer.
- target_seconds: null or [minimum, maximum], non-negative minimum and positive
  maximum. No format receives a mandatory default duration.
- delivery: positive finite wpm_min/wpm_max. If omitted, 125–165 words/minute is
  explicitly labeled an illustrative assumption, not measured performance.
- pause_seconds/action_seconds: non-negative finite seconds added sequentially.
  Record only additional time; simultaneous action and speech must not be added
  twice. Untimed silent directions produce a warning.

The estimate is words × 60 / rate + explicit extra seconds. Its limits are shown
with every report. Word-based timing is unavailable for zh/ja/th/lo/km/my; use
timed observations. Token counts are approximate word-like units, not linguistic
segmentation for every writing system. There is no page-to-minute conversion.

Review settings are optional: repeat_min_words (default 8), repeat_similarity
(default .72, range >0 to 1), max_words_without_payoff (no default). The last is
an author's own inspection threshold, never a universal laugh quota. Similarity
is Jaccard overlap of word bigrams; intentional repetition stays visible as such.

## Commands and exit codes

```text
python workbench.py analyze draft.json --output-format json --output report.json
python workbench.py check draft.json
python workbench.py compare original.json revision.json --output-format json
python workbench.py search draft.txt old-script.txt another-script.json
python workbench.py rehearsal draft.json observations.json
python workbench.py review-pack draft.json review-v1
```

Analyze/compare/rehearsal/search return 0 when a report was produced; that means no
artistic approval. Check returns 1 for explicit phrase/word-limit violations.
Estimated timing mismatches are warnings because no recording was measured. Invalid
input, missing files, or refusal to overwrite returns 2. Compare keeps original
constraints, duration/rate assumptions, language, and format for its constraint
analysis and separately lists any brief fields changed in the revision.

Output defaults to Markdown except search, which supports JSON only. --ui-language
es changes report headings; detailed diagnostic messages currently remain English.
Spoken source text is never translated by the CLI. The skill itself responds in
the user's language. JSON is the most complete, reproducible report form.

Review-pack writes a new directory with original bytes, hashes, context, analysis,
the appropriate method reference, and REVIEW.md. It does not generate a revision
or call a model. Do not distribute a pack containing a private draft unintentionally.
In its manifest, source_sha256 hashes the original file bytes. draft_sha256 hashes
UTF-8 spoken text formed by joining non-empty beat.text values with two LF newlines;
directions and other JSON fields are excluded. It is a different hash by design.

## Rehearsal annotations

```json
{
  "source": "human_read",
  "recording_reference": "optional local recording or session note",
  "events": [{"beat_id": "plant", "start": 0, "end": 3.5, "notes": "Ritmo conversacional"}]
}
```

Source is live_audience, human_read, synthetic_rehearsal, or edited_track. Events
use unique existing beat IDs and chronological start times; end > start. Optional
audience_laughter_seconds cannot exceed its event interval and is retained only
for live_audience. These are supplied observations: the tool has not listened to
the recording. Interval rates include pauses. Unobserved beats are explicitly listed.
