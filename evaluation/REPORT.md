# Verification and independent use test

Version: 0.1.0. Date: 2026-10-28. Local execution: Windows, Python 3.11.9.
The GitHub Actions matrix is provided for Linux/Windows and Python 3.10–3.13;
those remote combinations are not claimed as locally executed here.

## Technical verification

The local unit run completed with **37 tests passing**, including the regression
below. The standalone skill metadata validator also passed. These are observed
local results for the stated interpreter, not a claim about the unrun CI matrix.

Run the unit suite and tools/verify_project.py. The suite exercises real CLI IO,
portable asset lookup, source preservation, exact constraints, Unicode, dependency
order, original-brief retention, invalid inputs, timing assumptions and observation
provenance. The project verifier checks examples, local references, source metadata
and packaging inputs. Its results establish those behaviors, not comic quality.

The release builder produces both a full-repository ZIP and a self-contained skill
ZIP. It validates a temporary extracted skill from an unrelated working directory.
Hashes identify the particular files; they are not artistic approvals.

## Independent forward test

A separate assistant received the skill and realistic requests, without an intended
answer or a proposed bug fix. It read the complete long example before adapting it
and tested a copy of the skill from a folder with spaces/diacritics and an unrelated
working directory. No dependencies, models, recordings, renders or audience were used.
The retained evidence satisfied 19 artifact/behavior checks in that independent
pass. The [joke case](joke-case.md) and [short case](short-case.md) show its editorial
deliverables; the [annotated short](short-from-monologue.json) is machine-readable.

1. **Compact joke:** preserved the requested phrase 'qué piña', the supermarket
   situation and the self-defeating efficient persona; removed an explanation of
   the turn. The response was proportionate. This was an editorial proposal, not a
   measured improvement in laughter.
2. **Long-to-short adaptation:** replanted 'usuario administrador' within the clip,
   removed a visual reference requiring unseen context, and kept a silent reaction.
   Its 78 word-like units plus three seconds of pauses give an estimated 33.19–40.44
   seconds at the source's 125–155 words/minute. No timed reading was performed.
3. **Consumer CLI use:** analyze, check, compare, new, review-pack and rehearsal
   worked from the isolated copy. Existing outputs and originals remained unchanged.
   Altering the revised brief did not hide the missing protected phrase. Synthetic
   fixture laughter did not become live-audience evidence. Partial observations
   remained explicitly partial.

## Defect found and corrected

The default Markdown report omitted the actual word-rate assumptions and extra
seconds even though JSON retained them. A regression test reproduced the omission
and failed before the fix. The renderer now shows rate range, rate source, explicit
extra seconds, measurement status and target. The regression passed after the fix,
and the independent assistant revalidated the corrected source separately.

## Known limits

- Detailed CLI diagnostics remain English; Spanish localizes report headings. The
  editorial skill itself follows the user's language.
- Hand-entered rehearsal intervals may overlap if their starts are chronological.
  The tool reports per-interval rates and does not sum them into a total.
- The helper does not verify voice, facts, humor, global originality, semantic
  similarity, acting or real audience reaction. An annotation can be wrong artistically.
- There has been no controlled human-audience comparison showing that the skill
  beats an ordinary assistant review. This is a use/behavior test, not that benchmark.

See the [data contract](../skills/comedy-workbench/references/data-format.md) and
[worked examples](../examples/EDITORIAL_NOTES.md) for reproducible inputs and limits.
