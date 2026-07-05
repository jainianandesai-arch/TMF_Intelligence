# TMF Intelligence System — Meridian Clinical

A Trial Master File (TMF) document intelligence platform built for a fictional
CRO, **Meridian Clinical**. This is a capstone rebuild of an earlier prototype
built as a job application exercise for a real CRO — this version is a
distinct project with new architecture, new data, and new branding, built to
demonstrate a from-scratch LangGraph rebuild of the ingestion pipeline plus a
full McKinsey-style visual redesign.

> Meridian Clinical is a fictional company. All studies use real, public data
> from ClinicalTrials.gov but are reassembled here for demonstration purposes
> only.

---

## What this is

Clinical trial sponsors and CROs are required to maintain a Trial Master File
(TMF) — the complete document record proving a trial was run to protocol and
regulation (ICH E6 GCP). This system does two things:

1. **Dashboard** — gives clinical operations staff a portfolio-wide view of
   TMF completeness, missing/expired documents, and per-study detail, plus
   Claude-powered querying, communication drafting, and executive summaries.
2. **Governed ingestion pipeline** — when a new protocol PDF arrives, a
   5-node LangGraph pipeline extracts its identifiers, checks it against a
   read-only Excel registry (the system of record for Study IDs), and only
   indexes/registers it if a confident match is found. Anything that doesn't
   match is quarantined, not silently dropped or guessed at.

---

## Architecture

### The pipeline (`agents.py`)

```
upload → metadata → registry → indexing → sync → END
              ↘                    ↘
               END (failed)    END (duplicate / unregistered)
```

Five agent classes (`UploadAgent`, `MetadataAgent`, `RegistryAgent`,
`IndexingAgent`, `PortfolioSyncAgent`) each do one job. They're wired together
as a LangGraph `StateGraph` (`build_ingestion_graph()`), not a linear script:

- **`upload`** — stages the PDF, always clears the source location
- **`metadata`** — tiered Claude Sonnet 4.6 extraction (cover page → headers/
  footers → full document) to pull protocol number, NCT ID, EudraCT, sponsor,
  phase, condition, version/amendment info
- **`registry`** — the gatekeeper. Looks up the study in the read-only Excel
  registry. This is a conditional-edge fork:
  - no match → `outcome="unregistered"`, file quarantined, graph ends
  - already indexed → `outcome="duplicate"`, graph ends
  - matched → Study ID assigned from Excel (never generated), proceeds to indexing
- **`indexing`** — chunks the document, has Claude write a one-sentence
  summary per chunk, embeds each chunk with OpenAI `text-embedding-3-small`,
  and stores in ChromaDB (+ a JSON keyword-fallback index)
- **`sync`** — clears the dashboard's module cache so new data shows up
  without a restart

`TMFOrchestrator.run()` streams the full state dict after every node
completes, so callers (the CLI and the dashboard) can show live progress
rather than waiting for the whole run to finish.

### The dashboard (`app.py`)

Eight modules, navigable from the sidebar:

| Module | What it shows |
|---|---|
| Study Overview | Searchable, per-study detail (design, criteria, amendment history) |
| TMF Tracker | Document completeness per study |
| Flags Dashboard | Every missing/expired/review-needed document across the portfolio |
| Query Studies | Claude-powered Q&A over the structured data + indexed protocol text |
| Draft Communications | Auto-drafted, single-document site follow-up emails |
| Executive Summary | Audit-ready portfolio summaries, exportable to PDF |
| Ingestion Tracker | Historical view — file queues, audit log, and a **Document Lifecycle Timeline** reconstructing each file's full history (e.g. quarantined → registry updated → re-ingested) from `logs/ingestion_audit.log` |
| Live Ingestion Demo | Upload a PDF and watch it move through the LangGraph pipeline in real time — the static graph diagram at the top highlights the currently-active node as each step completes |

The Live Ingestion Demo tab is the primary demo surface: it renders the
compiled graph's actual Mermaid diagram, then live-highlights each node as
the pipeline runs, and visibly shows when a run diverges down the
duplicate/unregistered branch instead of reaching indexing.

---

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Create `.env` in the project root:
   ```
   ANTHROPIC_API_KEY=sk-ant-...
   OPENAI_API_KEY=sk-...
   ```
3. Run the dashboard:
   ```
   streamlit run app.py
   ```

### Ingesting a new protocol

Either drop a PDF in `TMF_Ingestion_Agent/inbox/` and run:
```
python TMF_Ingestion_Agent/ingest_protocol.py
```
or use the **Live Ingestion Demo** tab in the dashboard to upload one directly
in the browser.

To bulk-index every PDF already sitting in `data/pdfs/` against the Excel
registry:
```
python setup_data.py
```

---

## Data

- **Registry** (`data/exports/eTMF_Status_Report.xlsx`) — the read-only
  system of record. One row per tracked document, keyed by `MER Study ID`.
  The pipeline never writes to this file.
- **`trial_data.py`** — the dashboard's working data. Pre-seeded with
  MER-2026-001 through 005 (five real GI/IBD trials sourced from
  ClinicalTrials.gov: QUASAR, True North, SELECTION, HICKORY, ADVANCE).
  MER-2026-006 and 007 exist as rows in the Excel registry but are
  deliberately absent from this file until ingested live — one was run ahead
  of time as a rehearsal, the other is meant to be uploaded live during a
  demo so the pipeline's first-time behavior is genuinely observed, not
  replayed.
- Adding more studies is just adding more rows to the Excel file — nothing in
  the pipeline or dashboard assumes a fixed count of seven.

---

## Design decisions

These are the judgment calls behind the architecture, not just the code that
resulted from them.

**Architecture before implementation.** The state schema and node/edge
structure for the LangGraph rebuild were decided up front — inputs, what each
node reads/writes, and where the conditional forks are — rather than
discovered through trial and error while writing the nodes.

**No manual data patches.** If something is wrong, the fix belongs in code,
not a one-off edit to data to make a symptom disappear. The one deliberate
exception is the Excel registry rename (Study ID column header, company name
in the title row) — that's cosmetic text, not a data-correctness patch, and
editing generated data directly for a rename is reasonable where editing code
to do it isn't.

**Agent/node ordering matters.** The registry node must resolve a Study ID
before the indexing node runs, because nothing should be written to the
vector store under an ID that hasn't been confirmed against the system of
record. This ordering constraint is enforced structurally by the graph's
edges, not by convention.

**Sentinel values over fake defaults.** When metadata can't be confidently
extracted from a PDF, the system says so explicitly (e.g. `"Needs Metadata
Review"`, `None` for an unparsed date) rather than guessing a
plausible-looking value. A visibly missing field can be caught and fixed; a
silently wrong one usually isn't.

**Single source of truth discipline.** The Excel registry is read-only, and
Study IDs are only ever assigned from it, never generated by the pipeline.
The dashboard never reads Excel directly — it only ever reads through the
pipeline's already-resolved data in `trial_data.py`.

**Separation of concerns.** Pipeline logic lives in `agents.py`; dashboard
and reporting logic lives in `app.py`, `pdf_generator.py`, and
`query_engine.py`. LLM calls are contained to the files that need them
rather than scattered throughout the codebase.

**Ingestion as a backend process, not a user-facing feature.** By design,
ingestion is meant to be triggered by automation (a scheduler, or a CLI run)
rather than operated by end users. The Live Ingestion Demo tab is a
deliberate, explicit exception made purely for demonstration — it doesn't
change the intended production shape of the system.

**AI handles summarization and pattern-surfacing, not regulated analysis.**
In a clinical trial context, Claude extracts, summarizes, and flags. It does
not make statistical or regulatory judgment calls — those stay with the
structured, deterministic rules in `agents.py` (e.g. what counts as
"Expired", what routes to quarantine).

**Embedding choice and storage choice are independent decisions.** Moving
from a hash-based placeholder embedding to real OpenAI embeddings
(`text-embedding-3-small`) required changing exactly one function
(`embed_text()`); ChromaDB, the storage layer, didn't need to change at all.
That's the point of keeping those two decisions decoupled in the first place.

---

## Tech stack

- **Orchestration:** LangGraph (`StateGraph`)
- **LLM:** Claude Sonnet 4.6 (extraction, summarization, chat, drafting)
- **Embeddings:** OpenAI `text-embedding-3-small`
- **Vector store:** ChromaDB (persistent, local)
- **Dashboard:** Streamlit
- **Registry:** Excel (`openpyxl`), read-only
- **PDF generation:** ReportLab
