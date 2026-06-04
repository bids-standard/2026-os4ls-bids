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
  - Cody Baker — Dartmouth/CatalystNeuro (BEP032, NWB ↔ BIDS interoperability, `*`omics scoping)
  - Franco Pestilli - UT Austin PI (BIDS Steering; connectomics, brainlife)
  - Kimberly Ray - UT Austin PI (BIDS Steering) to provide "Project Manager" role to orchestrate activities
  

---

## Form fields (with character limits)

### Proposal Title — *60 characters max*

**Candidate (50 chars):**

> BIDS 2.0+: Life Sciences Data Standard for HI & AI

---

### Short Summary — *3,000 characters max*

The **Brain Imaging Data Structure (BIDS)** is a community-driven, openly governed standard that organizes scientific datasets so they can be unambiguously consumed by Human Intelligence (HI), conventional pipelines, and AI agents.
Since 2016, BIDS has grown from an MRI-only convention into an ecosystem covering 10+ modalities (MRI, EEG/MEG/iEEG, PET, NIRS, microscopy, motion, MRS, physiological, behavioral), with 1,500+ public datasets on OpenNeuro and multi-TB microscopy on DANDI.
It provides the common data language for dozens of BIDS Apps (fMRIPrep, MRIQC, QSIPrep, …) and is cited by thousands of peer-reviewed papers.
Active BIDS Extension Proposals (BEPs) — BEP036 (phenotypes), BEP044/047 (stimuli, audio/video) — and initial dialogue with `*`omics archives are pulling BIDS into adjacent life-science domains (animal behavior, audiology, pose estimation, `*`omics-linked phenotyping) of growing interest for AI agentic workflows.

This proposal supports the **coordinated evolution of the BIDS ecosystem into a natively AI-ready standard**, on the premise that *what is good for HI is good for AI — only AI benefits even more from explicit structure*.
Funding will advance five tightly coupled components whose maintainers have collectively committed to the work:

1. **BIDS specification & schema** — release BIDS 2.0 (more consistent, more modular), scope the 3.0 roadmap, harden the machine-readable schema as a true *Data Structure Standard*, and land queued BEPs (BEP036 phenotypes, BEP044 stimuli, BEP047 behavior) to broaden BIDS beyond neuro;
2. **BIDS validators** — converge implementations on the schema, produce machine-consumable, agent-friendly validation records, and integrate cross-standard validators (HED, NWB-Inspector, Zarr, DANDI) — the critical step toward trustworthy AI-produced results;
3. **Python + CLI utilities with MCP interfaces and skills** — replace scattered helper code with a maintained query/manipulation core, exposed through Model Context Protocol servers and reusable agent skills so any LLM agent can read, write, and reason about BIDS datasets;
4. **BIDS-Apps 2.0+** — modernize the interface contract between BIDS data and analysis containers (BIDS-Apps 2.0 + Boutiques + Niwrap), so AI agents (e.g. AI-assisted nipreps) can compose, parametrize, and run pipelines reliably;
5. **BIDS Users Assistant** — extend the OSA AI-assistance framework with deep BIDS awareness, and formalize a *study-state* observability layer so dashboards (Nipoppy, brainlife, OpenNeuroStudies), archives (OpenNeuro, DANDI), and human-in-the-loop reviewers can introspect what AI agents have done.

The work is **explicitly modular**: advance in any component lifts every downstream tool.
Funds also support annual cross-project hackathons and conference participation for dissemination.
No new datasets (beyond examples), no new ML models — only the standard, the tools, and the AI-readiness layer that the rest of the life sciences can adopt.

---

### Expected Value — *1,500 characters max*

**Capabilities unlocked.** By month 24, any life-sciences researcher *or* LLM agent will be able to:

(i) check whether a dataset is BIDS "deep-valid" — valid recursively against every used format and sibling standard (HED, NWB, OME-Zarr);

(ii) query and manipulate it via maintained CLI, Python API, and MCP servers, plus a collection of domain-specialized SKILLs;

(iii) wrap any analysis tool as a Boutiques/Niwrap descriptor and run it as a BIDS App 2.0, directly or via an agent;

(iv) introspect provenance, derivatives state, and outstanding QC through a common observability schema regardless of who performed the action;

(v) get human- and agent-readable explanations and guidance through the OSA AI assistant.

**Upstream impact.** A versioned schema-first specification with machine-readable extension points unlocks BEPs in `*`omics-linked phenotypes, animal behavior, stimuli, and audio/video — pulling new life-sciences communities into BIDS.

**Downstream impact.** Every BIDS App, every OpenNeuro dataset (and soon DANDI via nwb2bids), every nipreps pipeline, brainlife.io App or Nipoppy dashboard, and every emerging AI agent (KOSMOS-style, OSA, custom MCP clients) inherits cleaner inputs, stricter validation, and well-defined endpoints.

**The same investment that makes BIDS easier for humans makes it more usable for AI** — and exposes a template other life-science standards can mirror.

---

### Landscape Analysis — *1,500 characters max*

BIDS is the near-monopoly *organization* standard for neuroscience and broader biomedical imaging: OpenNeuro (1,500+ datasets), DANDI (1,000+ joining BIDS), EU/HBP, NIH BRAIN, ABCD, UK Biobank derivatives, and most major pipelines (fMRIPrep, QSIPrep, MRIQC, EEGLAB-BIDS, MNE-BIDS, fitlins) consume or produce BIDS.
There is no proprietary equivalent; vendor formats (BrainVision, CTF, Plexon) and industry standards (DICOM) are *inputs* BIDS organizes, not competitors.
Adjacent open standards — **NWB** (neurophysiology), **NIfTI** (file format), **HED** (event annotation), **Zarr/OME-Zarr** (large arrays), **git/git-annex/DataLad** (data versioning) — are *complementary* and used by or with BIDS; this proposal invests in interoperability rather than re-implementation.
For the analysis layer, **Boutiques / Niwrap / Styx** is the leading open descriptor stack and lacks a true peer; commercial alternatives (Flywheel, QMENTA) are closed-source and BIDS-consuming.

**AI use.** BIDS is already the de-facto input contract for AI tools in the field: ML training pipelines (ABCD-derived, UK Biobank, BIDS-Brain-Score, Facebook's Neuro AI), virtual-scientist and foundation-model efforts (KOSMOS, BrainLM), and AI assistants like **OSA** all rely on BIDS layout to make data legible.
Yet the BIDS 1.x series evolved with validators, APIs, and pipeline descriptors designed for human authors; the major 2.0 (and queued 3.0) revisions are required to raise consistency — gaps this proposal closes.

---

### Software Projects to be Supported — *up to 5*

A tricky part since only up to 5 so we need to either choose or somehow bundle . Submission form has

Software Project Name * 30 characters maximum
Software Project's Repository URL *
Software Project's Website URL

1. **BIDS spec, schema, schematools"
   - Repo: https://github.com/bids-standard/bids-specification
   - Website: https://bids-specification.readthedocs.io/
   - Unused extras:
     - Schema: https://github.com/bids-standard/bids-specification/tree/master/src/schema
     - BIDS 2.0 dev ('fork' to streamline management, overarching): https://github.com/bids-standard/bids-2-devel
     - License: CC-BY 4.0 (text) / MIT (schema tooling) — open

2. **BIDS validator(s)**
   - Repo: https://github.com/bids-standard/bids-validator
   - Website: https://bids-validator.readthedocs.io/en/latest/
   - Unused extras:
     - Deno (current): https://github.com/bids-standard/bids-validator
     - Python validator: https://github.com/bids-standard/python-validator
     - License: MIT — open

3. **PyBIDS**
   - Repo: https://github.com/bids-standard/pybids
   - Website: https://bids-standard.github.io/pybids/
   - Unused extras:
     - **bids-utils (query/manipulation + MCP/skills layer)**
     - bids-utils: https://github.com/bids-standard/bids-utils , to be developed/coordinated under the `bids-standard/` org (umbrella issue forthcoming); **complements** pybids — it does not supplant or merge with it. Roughly: pybids covers structured query/indexing; bids-utils covers the smaller, agent- and CLI-friendly read/write/inspect verbs and integrations with sibling standards
     - License: Apache-2.0 — open

4. **BIDS-Apps**
   - "Repo" (org): https://github.com/bids-apps
   - Website: https://bids-apps.neuroimaging.io/
   - Unused extra(s) (we better incorporate refs at least into above!):
     - Repo: https://github.com/bids-standard/execution-spec
     - Website: https://bids-standard.github.io/execution-spec/
     - Boutiques / Niwrap / Styx + BIDS-Apps 2.0 (pipeline interoperability)
     - Boutiques: https://github.com/boutiques/boutiques
     - BIDS-Apps: https://github.com/bids-apps
     - Niwrap: https://github.com/childmindresearch/niwrap
     - Styx: https://github.com/childmindresearch/styx
     - License: MIT / Apache-2.0 — open

5. **OSA — Open Science Assistant** *(submit as: "OSA — Open Science Assistant" — 28 chars)*
   - Repo: https://github.com/OpenScience-Collective/osa/
   - Website: https://demo.osc.earth/bids
   - Unused extras:
     - Maintainer: Seyed Yahya Shirazi (UCSD), under the Open Science Collective org
     - License: MIT — open

---

### Categories — *up to 3 tags*

select/vote from candidates (potentially add others)

- [ ] **Neuroscience**
- [ ] **Biological and biomedical imaging**
- [ ] **Data formats and storage**
- [ ] **Platforms interoperability**
- [ ] **Agentic frameworks**
- [ ] **Software ecosystem infrastructure**

---

### Funding Track

- [x] **Track 2 — Foundational Libraries and Ecosystem Initiatives** (up to $1,000,000 / 24 months)
- [ ] Track 1 — Domain-specific Tools

---

### Statement of PI Involvement

The PI (Yaroslav Halchenko) is an emeritus member of the BIDS Steering Committee and a long-standing core contributor across the BIDS specification and ecosystem at large. He is a Co-PI or Co-I on a number of national data archives (DANDI, OpenNeuro, EMBER) which facilitate archival of data in BIDS standard. He will be responsible to direct the work under this funding.

The proposed work has been discussed and endorsed by the BIDS Steering Committee, and by the maintainers of involved software projects, and is *aligned with the published BIDS roadmap*: BIDS 2.0 (bids-standard/bids-2-devel), the active BEP queue (BEP028 provenance, BEP036 phenotypic, BEP044/047 stimuli & A/V), and the bids-standard validator convergence effort.
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
