# TMF Intelligence System — Meridian Clinical (Capstone)

## Status: Build complete
This file originally served as the build spec for the capstone rebuild.
That rebuild is now done — this version documents what was actually
implemented, what's still open, and the design principles to keep in
mind for any future changes. Treat this as the current source of truth
for the project's architecture, not a to-do list.

## Context
Rebuild of a TMF (Trial Master File) document management system,
originally built as a job-application prototype for a CRO ("TrialAxis
CRO" — not referenced, copied from, or reused for branding/data in this
project). This version demonstrates an upgraded architecture: real
embeddings, a LangGraph-orchestrated pipeline, and a full rebrand to a
fictional company, "Meridian Clinical."

## What's implemented

### 1. Real embeddings ✅
`embed_text()` in `agents.py` calls OpenAI `text-embedding-3-small`
(replacing the old MD5-hash placeholder). `OPENAI_API_KEY` required in
`.env` alongside `ANTHROPIC_API_KEY`. `openai` is in `requirements.txt`.
JSON fallback index (`data/trial_index.json`) still works the same way.

### 2. LangGraph orchestration ✅
`TMFOrchestrator` in `agents.py` wraps a compiled LangGraph `StateGraph`
(`build_ingestion_graph()`):

```
upload → metadata → registry → {indexing → sync} → END
   ↘         ↘           ↘
   END      END      END (duplicate / unregistered)
  (failed)  (failed)
```

- State schema: `IngestionState` (TypedDict) — carries metadata,
  full_text, tax_id, chunks, outcome, and an accumulating `log`.
- Conditional routing lives in `route_after_upload`,
  `route_after_metadata`, `route_after_registry`.
- Agent classes (`UploadAgent`, `MetadataAgent`, `RegistryAgent`,
  `IndexingAgent`, `PortfolioSyncAgent`) are unchanged internally — node
  functions just call them.
- `ingest_protocol.py` and `app.py` consume `TMFOrchestrator.run()`,
  which streams state after each node (`stream_mode="values"") instead
  of yielding sentinel strings.
- `langgraph` is in `requirements.txt`.

**State visualization ✅** — `app.py`'s "Live Ingestion Demo" module
renders the graph via `get_graph().draw_mermaid()` /
`draw_mermaid_png()`, streams live per-node progress, and visibly shows
the duplicate/unregistered branches ending early.

**Document Lifecycle Timeline ✅** — implemented in the "Ingestion
Tracker" module (`app.py`), reading `logs/ingestion_audit.log` and
grouping rows by `source_file` to reconstruct each file's history.

### 3. Trial data — Meridian Clinical, 7 GI/IBD studies ✅
`trial_data.py` uses `MER-2026-XXX` throughout, no `TAX-`/`TrialAxis`
references. Registry (`data/exports/eTMF_Status_Report.xlsx`) has 7
rows (MER-2026-001–007). `load_excel_registry()` checks for header
`"MER Study ID"`.

**⚠️ Open item — pre-seed split doesn't match the original demo plan.**
The original intent was:
- MER-2026-006 → pre-tested by the builder before the demo (rehearsed
  run), *present* in `trial_data.py`
- MER-2026-007 → left untested, *absent* from `trial_data.py`, for
  professors to ingest live during the demo

Current `trial_data.py` has this reversed: **007 is present, 006 is
absent.** Before the actual demo, confirm which study is meant to be
the "already proven" one vs. the "live, untested" one, and either
re-run the correct study through the pipeline or update this note to
match whatever the real intended demo flow is now.

**Not a hardcoded limit** — confirmed no code assumes exactly 7 studies
exist; registry size can grow without code changes.

### 4. Visual rebrand (McKinsey-style) ✅
`app.py` theming and `pdf_generator.py` chart colors use the
navy/charcoal + single accent palette in place of the old
navy/orange/sky-blue/lime scheme.

### 5. Rebrand to "Meridian Clinical" / MER-2026-XXX ✅
Confirmed no remaining `TrialAxis` or `TAX-` literal strings in
`agents.py`, `app.py`, `trial_data.py`, `pdf_generator.py`,
`query_engine.py`, `setup_data.py`, `tmf_importer.py`,
`reingest_study.py`, `ingest_protocol.py` (CLI banner now reads
`"TMF INGESTION AGENT | Meridian Clinical"`), or `README.md`.

## Folder structure (as built)
- `agents.py` — 5-agent pipeline + LangGraph orchestrator
- `app.py` — Streamlit dashboard, 8 modules (incl. Live Ingestion Demo)
- `trial_data.py` — MER-2026-001–005 and 007 (see open item above)
- `query_engine.py`, `pdf_generator.py`, `setup_data.py`,
  `reingest_study.py`, `tmf_importer.py` — unchanged in role from spec
- `TMF_Ingestion_Agent/ingest_protocol.py` — CLI entry point; imports
  `agents.py` via parent-path insert; looks for its own `.env`, falls
  back to parent. This nesting is preserved — do not flatten.
- `data/pdfs/`, `data/chroma_db/`, `data/trial_index.json` — generated
  at runtime, not committed to git
- `data/exports/eTMF_Status_Report.xlsx` — the one `data/` file that
  *is* committed; read-only source of truth for Study IDs
- `logs/ingestion_audit.log` — starts empty, grows via
  `write_audit_log()`

## Design principles (preserved, confirmed in code)
- **Architecture before implementation** — state schema and node/edge
  structure were fixed up front for the LangGraph rebuild.
- **No manual data patches** — code-level fixes only, except the
  deliberate cosmetic Excel rename (not a data-correctness patch).
- **Agent/node ordering** — Registry resolves before Indexing runs
  (`route_after_registry` gates entry to `indexing_node`).
- **Sentinel values over fake defaults** — `MetadataAgent` surfaces
  explicit warnings (e.g. missing identifier) rather than guessing.
- **Single source of truth** — Excel registry is read-only
  (`load_excel_registry()` never writes); `app.py` never reads Excel
  directly, only through pipeline-resolved data.
- **Separation of concerns** — `agents.py` (pipeline) and `app.py`
  (dashboard) stay cleanly separated.
- **Ingestion as backend process** — Live Ingestion Demo tab is an
  explicit, acknowledged demo-only exception to that norm.
- **AI role is bounded** — LLM extracts/summarizes/flags; no
  statistical or regulatory judgment calls.
- **Embedding choice vs. storage choice are independent** — swapping
  hash-based → OpenAI embeddings required no change to the ChromaDB
  storage layer.

## Environment setup
`.env` in project root (and optionally in `TMF_Ingestion_Agent/` as a
fallback source) needs:
```
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...
```
Never commit `.env` — use `.env.example` with placeholder values for
anyone cloning the repo.

## Before presenting — outstanding checklist
1. Resolve the MER-2026-006 / 007 pre-seed discrepancy above.
2. Capture the presentation screenshots (static graph diagram, live
   mid-run highlight, successful MER-2026-00X ingestion,
   unregistered/quarantine branch firing, lifecycle timeline
   quarantine→registered transition, rebranded dashboard overview,
   before/after comparison) once the 006/007 question is settled and
   the system is stable.
3. Confirm `.gitignore` excludes `.env`, `data/pdfs/`, `data/chroma_db/`,
   `data/trial_index.json`, `__pycache__/`, `logs/*.log`, and staging
   folders, while still including `data/exports/eTMF_Status_Report.xlsx`.
