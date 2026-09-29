# Contributing

Thanks for helping people cut through AI noise. The whole project rests on one idea: **readers can trust every line because every line has a source.**

## The rules

1. **Link a primary source** for every fact: the vendor's changelog, pricing page, docs, or official blog. Reputable news is fine for events (incidents, acquisitions). Social posts and forums only as supporting evidence.
2. **Date everything.** Update `last_verified` whenever you re-check a tool.
3. **Neutral language.** "Removed manual model selection" rather than "ruined the plan". Strengths and limits both belong.
4. **No affiliate or referral links.** Ever.
5. **Rumors are not changes.** Unconfirmed reports can become a reality check with the verdict `unproven`, never a changelog entry.

## What to edit

| You want to... | Edit |
|---|---|
| Add or update a tool | `data/tools/<id>.yaml` (start from `_TEMPLATE.yaml`) |
| Record a change | `data/changelog/YYYY-MM.yaml` |
| Fact-check a claim | `data/reality-checks/<id>.yaml` (needs at least 2 sources) |
| Watch a new official page | `data/sources.yaml` |

Don't edit the parts of `README.md` between `<!-- ...:START -->` and `<!-- ...:END -->` markers, or `docs/data.json`. They are generated.

## Verdicts

| Verdict | Use when |
|---|---|
| `"true"` | The claim matches primary sources (quote it in YAML) |
| `partly-true` | Core is right but important detail is missing or wrong |
| `misleading` | Technically based on something real, but the framing gives the wrong impression |
| `"false"` | Primary sources contradict it (quote it in YAML) |
| `unproven` | Not enough reliable evidence either way |

## Reviewing bot drafts

The watcher bot opens PRs containing files in `data/changelog/_drafts/`. To handle one:

1. Open the source URL in the draft and confirm the change yourself.
2. Write a proper entry in the right `YYYY-MM.yaml` (and update the tool file if needed).
3. Delete the draft file.
4. If it was noise (layout change, cookie banner), just delete the draft.

## Local checks

```bash
pip install -r requirements.txt
make check   # schema validation + tests + generated files up to date
make build   # regenerate README tables and docs/data.json
```

CI runs the same checks on every pull request.
