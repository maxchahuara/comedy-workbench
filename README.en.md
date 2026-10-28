# Comedy Workbench

**An open workshop for revising jokes, comedy shorts, and long monologues with an
AI assistant while preserving the author's voice.**

[Español](README.md) · [Skill](skills/comedy-workbench/SKILL.md) ·
[Worked examples](examples/EDITORIAL_NOTES.md) · [Research decisions](research/DECISIONS.md)

The package combines an editorial Agent Skill with an optional local evidence tool.
The skill helps an existing assistant inspect premises, expectations, payoffs,
development, callbacks, and performance dependencies. The tool checks explicit
constraints, estimates duration, compares versions, and records rehearsal intervals.

This is an original implementation informed by source review and research. It does
not bundle upstream application code, joke corpora, weights, or commercial services.
There is no demonstrated audience-response improvement for this method.

## Try it without installing anything

Download this repository and ask your assistant to read
[SKILL.md](skills/comedy-workbench/SKILL.md). It is self-contained under
`skills/comedy-workbench/`. For example:

> Use this skill to revise my existing comedy draft. Keep my dialect and persona,
> explain the important changes, and offer different mechanisms only where useful.

> Adapt this monologue excerpt into a standalone 35-second short. Separate spoken
> text from visual directions and preserve the payoff's necessary context.

An ordinary editorial request needs no JSON or formal project. The skill is a
reusable workflow, not an included language model. It can be read directly without
adding it to any global skill directory.

## Optional local tool

Python **3.10+**, standard library only. No dependency installation, model downloads,
GPU, network, account, or telemetry is required by the helper.

```bash
python workbench.py analyze examples/short.json
python workbench.py compare examples/joke-original.json examples/joke-revision.json
python workbench.py analyze examples/monologue.json --output-format json
python workbench.py review-pack examples/short.json review-short-v1
python workbench.py new joke new-joke.json --language en
```

On Windows, `py -3.11` can replace `python` if that interpreter is available.
The CLI works on UTF-8 raw text or optional annotated JSON. Analysis never rewrites
the input, and existing outputs are not overwritten. A review pack contains the
original bytes, hashes, brief, analysis, and appropriate editorial method; it does
not call a model or generate a revision.

Other commands: `check` returns 1 for explicit phrase/word-limit violations;
`search` retrieves lexical word-bigram matches; `rehearsal` summarizes hand-entered
observations. See the complete [data contract](skills/comedy-workbench/references/data-format.md)
for schema, limitations, and exit codes. Report headings support English/Spanish;
detailed diagnostics currently use English. The skill uses the author's language.

## Format-specific decisions

- **Jokes:** necessary setup, the changed expectation, natural wording, and useful tags.
- **Shorts:** standalone context, division of work between speech/image, visible action,
  reaction, timing assumptions, and adaptation from longer material.
- **Long monologues:** block development, changes in stance, rhythm, callback continuity,
  transitions, and earned endings.

There are no universal laugh quotas, page-to-minute conversions, mandatory hooks,
or fixed set lengths. The long Spanish example contains 923 word-like units and
has an illustrative estimated duration of approximately 6–8 minutes; the workflow
also supports substantially longer drafts.

## Evidence and limits

Keep the original in the comparison and distinguish mechanical facts, editorial
hypotheses, and observed audience reactions. Edited laughter and simulated audience
personas are not audience validation. Timing assumes constant word rates plus
non-overlapping explicit actions/pauses; raw text counts headings/directions too.
Word timing is unavailable for writing systems without the supported word-boundary
assumption. The tool computes no funniness, factuality, acting, or originality score.

The [research catalogue](research/sources.json) records pinned snapshots and actual
reading scope. [Research decisions](research/DECISIONS.md) explain what was retained,
rejected, or deferred. Full study downloads remain outside the public project.
Upstream licenses, proprietary components, and model terms remain independent.
See [NOTICE.md](NOTICE.md).

## Verify and contribute

```bash
python -m unittest discover -s tests -v
python tools/verify_project.py
```

Technical tests and [editorial forward testing](evaluation/REPORT.md) are separate.
See [CONTRIBUTING.md](CONTRIBUTING.md). Original code and instructions: [MIT](LICENSE).
