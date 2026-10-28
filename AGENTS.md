# Working on Comedy Workbench

Read SKILL.md for editorial scope, references/data-format.md for helper behavior,
and research/DECISIONS.md for provenance. The portable skill lives under
skills/comedy-workbench. Do not install it globally while developing this repository.

Use Python 3.10+ and the standard library. Keep original drafts unchanged, source
hashes explicit, and technical checks separate from editorial judgments. Do not
invent audience tests or imply that lexical overlap is semantic/originality proof.
Preserve format and dialect choices rather than enforcing the examples' conventions.

Run python -m unittest discover -s tests -v and python tools/verify_project.py for
relevant changes. Research snapshots, private review packs, user scripts, media,
upstream corpora and credentials do not belong in the public repository. Publication
requires the human's authorization; a writing request alone does not supply it.
