# OS4LS Letter of Intent — BIDS Ecosystem

**Funding opportunity:** Open Source for the Life Sciences (OS4LS), Open Source for Science Fund / Renaissance Philanthropy
**Track:** Track 2 — Foundational Libraries and Ecosystem Initiatives
**Funding ceiling:** Up to $1,000,000 USD total over 24 months
**LOI due:** 2026-06-08, 2 pm PDT / 9 pm UTC
**Application portal:** https://renphil.fillout.com/os4ls

---

## Applicant & Host Organization

- **Principal Investigator:** Yaroslav O. Halchenko, Ph.D.
  - Center for Open Neuroscience, Dartmouth College
  - Role on BIDS: Emeritus Steering Committee member; core contributor to BIDS specification, bids-examples, bids-validator, pybids, bids-utils; initiator and lead of BIDS-Study, and BIDS 2.0 working group; lead of DataLad, ReproIn, ReproNim/containers; Co-PI and Co-I on National data archives using BIDS: DANDI, OpenNeuro, EMBER
  - Email: yaroslav.o.halchenko@dartmouth.edu
- **Host / fiscal sponsor:** Trustees of Dartmouth College — institutionally agreed to **10% indirect cost rate** (matching the RFA cap), and will issue subawards to the collaborating institutions
- **Co-PIs and key collaborating maintainers (representing core BIDS community buy-in):**
  - Chris Markiewicz — Stanford (BIDS Maintainer 'in charge', BEP043, bids-validator, pybids, nipreps)
  - Jean-Baptiste Poline — McGill PI (BIDS Steering, Boutiques/Nipoppy)
  - Russell Poldrack — Stanford PI (BIDS co-founder, bids-validator, OpenNeuro)
  - Seyed Yahya Shirazi — UCSD PI (BIDS Maintainer; BEP042/BEP044; HED; OSA — Open Science Assistant)
  - Oscar Esteban — Lausanne University Hospital / EPFL PI (nipreps; AI-assisted pipelines)
  - Gregory Kiar — Child Mind Institute PI (Niwrap, Styx, Boutiques)
  - Alejandro de la Vega — UT Austin PI (pybids, fitlins)
  - Dora Hermes — Mayo Clinic PI (BIDS Steering; iEEG)
  - Cody Baker — Dartmouth/CatalystNeuro (BEP032, NWB ↔ BIDS interoperability, `*`omics scoping)
  - Franco Pestilli - UT Austin PI (BIDS Steering; connectomics, brainlife)

---

## Form fields (with character limits)

### Proposal Title — *60 characters max*

**Candidate (53 chars):**

> AI-Ready BIDS: Structured Life Science Data for HI & AI

**Alternates (under 60 chars):**

- "Good for Humans, Better for AI: an AI-Ready BIDS Ecosystem" (58)

or we could make it more concrete as to target 2.0:

- "BIDS 2.0 Ecosystem: AI-Ready Standards and Tooling for Life Sciences" (56)

- "BIDS Ecosystem: Standardizing Life Science Data for AI" (54)

---

### Short Summary — *3,000 characters max*

The **Brain Imaging Data Structure (BIDS)** is a community-driven, openly governed standard that organizes scientific datasets so they can be unambiguously consumed by Human Intelligence (HI, also known as Humans), conventional pipelines, and increasingly autonomous AI agents.
Since 2016, BIDS has grown from an MRI-only convention into an ecosystem covering over 10 modalities at the moment: MRI, EEG, MEG, iEEG, PET, NIRS, microscopy, motion, MRS, physiological, behavioral.
There are over 1,500+ public BIDS datasets on OpenNeuro and some multi-TBs microscopy datasets on DANDI BRAIN Initiative archives.
Provides common data language for dozens of BIDS Apps (fMRIPrep, MRIQC, QSIPrep, …), and is cited by thousands of peer-reviewed papers.
Work on new extensions (BEP036 Phenotypic Data, BEP044/047 stimuli & audio/video, BEP028 provenance) is introducing BIDS into adjacent life-science domains — animal behavior, audiology, `*`omics-linked phenotyping, and animal pose estamation and tracking -- domains of interest for AI agentic workflows.

This proposal supports the **coordinated evolution of the BIDS ecosystem to be natively AI-ready**, on the premise: *what is good for human intelligence is good for AI — only AI benefits even more from explicit structure*.
We will fund five tightly coupled open-source pillars whose maintainers have collectively committed to this work:

1. **BIDS specification & schema** — finalize BIDS 2.0, harden the machine-readable schema as a true *Data Structure Standard*, land BEP036 (phenotypes) and the BEP044 (Stimuli) and BEP047 (behavior) audio-video extensions that broaden BIDS beyond neuro;
2. **BIDS validators (Deno bids-validator + Python bids-validator)** — converge implementations on the schema, produce machine-consumable, agent-friendly validation records, and integrate with cross-standard validators (HED, NWB-Inspector, Zarr, DANDI) via the con/validation common schema;
3. **PyBIDS + a consolidated `bids-utils` library + MCP/skills** — replace today's scattered helper code with a maintained query/manipulation core, exposed through Model Context Protocol servers and reusable agent skills so any LLM agent can read, write, and reason about BIDS datasets;
4. **BIDS-Apps 2.0 + Boutiques / Niwrap / Styx + bids-models / fitlins** — modernize the interface contract between BIDS data and analysis containers, enabling AI agents (e.g. AI-assisted nipreps) to compose, parametrize, and run pipelines reliably;
5. **OSA (Open Science Assistant) + dataset/study observability** — extend the existing OSA AI-assistance framework with deep BIDS awareness, and formalize a *study-state* observability layer so dashboards (Nipoppy, brainlife, OpenNeuroStudies), archives (OpenNeuro, DANDI, registry.datalad.org) and human-in-the-loop reviewers can introspect what AI agents have done.

The work is **explicitly horizontal**: every advance lifts every downstream tool.
Funds also support an annual cross-project hackathon to keep the ecosystem coherent.
No new datasets (besides new example ones), no new ML models — only the standard, the tools, and the AI-readiness layer that the rest of the life sciences can adopt.

---

### Expected Value — *1,500 characters max*

**Capabilities unlocked.** Success means that, by month 24, any life-sciences researcher *or* any LLM agent operating in the life sciences can: 

(i) discover whether a dataset (tool, HI or AI constructed) is BIDS "deep-valid" - valid recursively, against all used formats and standards (e.g. HED, NWB, OME-Zarr); 

(ii) query and manipulate it via maintained Command Line interfaces (CLI), Python API and MCP servers, and collection of domain- and target- specialized SKILLs;

(iii) wrap any analysis tool as a Boutiques/Niwrap descriptor and run it as a BIDS App 2.0 direcly or by an agent;

(iv) introspect provenance, derivatives state, and outstanding QC through a common observability schema regardless on what performed an action;

(v) get human- and agent-readable explanations and guidance through the OSA AI assistant.

**Upstream impact.** A versioned schema-first specification with first-class machine-readable extension points enables BEPs in `*`omics-linked phenotypes, animal behavior, stimuli, and audio/video — pulling new life-sciences communities into BIDS.

**Downstream impact.** Every BIDS App, every OpenNeuro dataset (potentially DANDI datasets since nwb2bids work is ongoing), every nipreps pipeline, brainlife/Nipoppy dashboard, and every emerging AI agent (KOSMOS-style, OSA, custom MCP clients) inherits cleaner inputs, stricter validation, and well-defined endpoints.
**The same investment that makes BIDS easier for humans makes it actually usable for AI** — and exposes a template other life-science communities and standards can mirror.

---

### Landscape Analysis — *1,500 characters max*

BIDS occupies a near-monopoly position as the *organization* standard for the neuroscience and broader biomedical-imaging audience: OpenNeuro (1,500+ datasets), DANDI, the EU/HBP, NIH BRAIN, ABCD, UK Biobank derivatives, and most major pipelines (fMRIPrep, QSIPrep, MRIQC, EEGLAB-BIDS, MNE-BIDS, fitlins) consume and/or produce BIDS.
There is no proprietary equivalent; vendor formats (BrainVision, CTF, Plexon) and industry standards (DICOM) are *inputs* that BIDS organizes and collaborates with, not competitors.
Adjacent open standards — **NWB** (neurophysiology data model), **NIfTI** (file format), **HED** (event annotation), **Zarr/OME-Zarr** (large arrays), **git/git-annex/DataLad** (data versioning and logistics) — are *complementary*, not substitutable: this proposal explicitly invests in their interoperability rather than re-implementation.
For the analysis layer, **Boutiques / Niwrap / Styx** is the leading open descriptor stack and lacks a true peer; commercial alternatives (Flywheel, QMENTA) are closed-source software and BIDS-consuming.

**AI use.** BIDS is already the de-facto input contract for AI tools in the field: ML training pipelines (ABCD-derived, UK Biobank, BIDS-Brain-Score, Facebook's Neuro AI), virtual scientist and foundation-model efforts (KOSMOS, BrainLM), and AI assistants like **OSA** all rely on BIDS layout.
Yet BIDS standard has various "evolutional quirks" requiring more work toward consistency, and validators, APIs, and pipeline descriptors were designed for human authors — this proposal closes those gaps.

---

### Software Projects to be Supported — *up to 5*

A tricky part since only up to 5 so we need to either choose or somehow bundle . Submission form has

Software Project Name * 30 characters maximum
Software Project's Repository URL *
Software Project's Website URL

1. **BIDS specification & schema & schematools**
   - Repo: https://github.com/bids-standard/bids-specification
   - Schema: https://github.com/bids-standard/bids-specification/tree/master/src/schema
   - BIDS 2.0 dev ('fork' to streamline management, overarching): https://github.com/bids-standard/bids-2-devel
   - License: CC-BY 4.0 (text) / MIT (schema tooling) — open

2. **BIDS validators (Deno + Python)**
   - Deno (current): https://github.com/bids-standard/bids-validator
   - Python validator: https://github.com/bids-standard/bids2-validator
   - License: MIT — open

3. **bids-utils (query/manipulation + MCP/skills layer)**
   - bids-utils: https://github.com/bids-standard/bids-utils , to be developed/coordinated under the `bids-standard/` org (umbrella issue forthcoming); **complements** pybids — it does not supplant or merge with it. Roughly: pybids covers structured query/indexing; bids-utils covers the smaller, agent- and CLI-friendly read/write/inspect verbs and integrations with sibling standards
   - PyBIDS: https://github.com/bids-standard/pybids
   - License: Apache-2.0 — open

4. **Boutiques / Niwrap / Styx + BIDS-Apps 2.0 (pipeline interoperability)**
   - Boutiques: https://github.com/boutiques/boutiques
   - BIDS-Apps: https://github.com/bids-apps
   - Niwrap: https://github.com/childmindresearch/niwrap
   - Styx: https://github.com/childmindresearch/styx
   - License: MIT / Apache-2.0 — open

5. **OSA (Open Science Assistant) — AI assistance with BIDS awareness**
   - Repo: https://github.com/OpenScience-Collective/osa/
   - Maintainer: Seyed Yahya Shirazi (UCSD), under the Open Science Collective org
   - License: open (to confirm in full application)

---

### Categories — *up to 3 tags*

select/vote from candidates (potentially add others)

- [ ] **Data formats and storage**
- [ ] **Interoperability**
- [ ] **Neuroscience**

- [ ] **Biological and biomedical imaging**
- [ ] **Agentic frameworks**
- [ ] **Software ecosystem infrastructure**

---

### Funding Track

- [x] **Track 2 — Foundational Libraries and Ecosystem Initiatives** (up to $1,000,000 / 24 months)
- [ ] Track 1 — Domain-specific Tools

---

### Statement of PI Involvement

The PI (Yaroslav Halchenko) is an emeritus member of the BIDS Steering Committee and a long-standing core contributor across the BIDS specification, bids-validator, pybids, bids-examples, and bids-utils repositories.

Target wording TODO, along the lines of :
The proposed work has been discussed and endorsed by the BIDS Steering Committee, by the maintainers of each of the five named software projects (named above as co-Is/collaborating maintainers), and is *aligned with the published BIDS roadmap*: BIDS 2.0 (bids-standard/bids-2-devel), the active BEP queue (BEP028 provenance, BEP036 phenotypic, BEP044/047 stimuli & A/V), and the bids-standard validator convergence effort.
No proposed activity introduces work outside the existing community roadmap but community contributions could potentially augment the roadmap.

---

## Mapping of proposed work → RFA priority bullets

For internal use; not part of the LOI form, but useful to ensure the narrative above squarely lands on the RFA's stated priorities.

- **Representing, managing, curating, structuring scientific data for model training**
  - Pillar 1 — spec/schema, BEP036 phenotypes, `*`omics scoping
  - Pillar 3 — pybids/bids-utils for dataset assembly

- **Benchmarks, standards, endpoints, protocols unlocking open source tools in agentic workflows**
  - Pillar 2 — machine-readable validation records
  - Pillar 3 — MCP servers and agent skills
  - Pillar 5 — OSA endpoints

- **Scalability & performance improvements, hardware acceleration**
  - *Demonstrated scale today.* BIDS already operates at scale: 1,500+ public OpenNeuro datasets and multi-TB BIDS microscopy on DANDI — evidence that the standard's design holds up under both **dataset count** and **per-dataset size**.
  - *Inherent parallelism (Pillars 1, 4).* BIDS treats subjects and sessions as first-class structural units; the standard *is* the parallelization boundary, enabling clean, near-embarrassingly-parallel pipeline execution without per-tool sharding logic.
  - *Modular composition — within a dataset (Pillar 1).* The standard's nesting and cross-referencing of `sourcedata/`, raw, and `derivatives/` datasets is what makes large studies tractable today; BIDS 2.0 hardens these contracts so AI agents and pipelines can navigate them programmatically.
  - *Modular composition — across datasets (Pillars 1, 5).* **BIDS-Study** composes datasets within a study; [OpenNeuroStudies](https://github.com/OpenNeuroStudies/OpenNeuroStudies) and the nipoppy study network compose *across* studies, reusing the same modularity via git / git-submodules / DataLad — no per-dataset glue code.
  - *Summarization bubbling up (Pillars 4, 5).* Standardized derivative records and pipeline outputs aggregate cleanly through subject → study → cross-study → dashboard layers (brainlife, Nipoppy, OpenNeuroStudies). The observability work in Pillar 5 formalizes this bubbling so that the same summarization runs at any level without rewriting.
  - *Validator throughput (Pillar 2).* The schema-driven Deno validator and the Python validator are the canonical AI-callable verbs for "is this dataset valid?"; converging implementations on the shared schema removes the current performance/coverage gaps and makes validation cheap enough to run inside agent loops.

- **Interoperability frameworks composable in AI-driven pipelines**
  - Pillar 4 — Boutiques / Niwrap / Styx, BIDS-Apps 2.0
  - Pillar 2 — cross-standard validation with HED / NWB / Zarr
  - Pillar 4 — analytics standardization via bids-models / fitlins

## Mapping of proposed work → OS4LS review criteria

- **Existing impact**
  - 1,500+ OpenNeuro datasets, multi-TB BIDS microscopy on DANDI, dozens of BIDS Apps, thousands of citing papers, 300+ contributors

- **Quality (governance, contributor base, roadmap)**
  - Open BIDS Steering Committee, published BEP process, public roadmap (`bids-standard/bids-2-devel`), documented contributor guide, active CI across all five named projects

- **Feasibility**
  - Co-Is are the actual maintainers of the named projects
  - Every named workstream is already in motion; this funding closes a known resourcing gap rather than starting from zero

- **Value of proposed work**
  - One investment lifts every downstream user — humans, conventional pipelines, and AI agents simultaneously
  - Enables BIDS adoption in adjacent life-science domains (phenotypic, behavioral, `*`omics-linked, audio/video)


---

## Open items before submission

- [x] **Fiscal sponsor decided: Dartmouth College.** Dartmouth has agreed to cap indirect costs at 10% (matching the RFA limit) and will issue subawards to all collaborating institutions. An external fiscal sponsor (e.g., INCF, Code for Science & Society) remains a theoretical fallback if Dartmouth's machinery proves too slow for the June 8 LOI / July 21 full-app timeline, but the short runway makes switching unlikely to be feasible. *Driver:* the RFA (p.5) requires that "one individual must complete the application and a single organization or fiscal sponsor must coordinate the dispersal of funds" for Track 2 multi-project proposals.
- [ ] Final title choice — currently recommending: *"AI-Ready BIDS: Structured Life Science Data for HI & AI"* (53 chars)
- [ ] Steering Committee formal sign-off email thread (already in progress per the email Message-ID `<agscKEH3Tceh4Ei2@bilena>`)
- [ ] Confirm category selection (Data formats and storage / Interoperability / Agentic frameworks vs. swapping in Software ecosystem infrastructure)
