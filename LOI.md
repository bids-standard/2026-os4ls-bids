# OS4LS Letter of Intent — BIDS Ecosystem

Funding opportunity: Open Source for the Life Sciences (OS4LS), Open Source for Science Fund / Renaissance Philanthropy
Track: Track 2 — Foundational Libraries and Ecosystem Initiatives
Funding ceiling: Up to $1,000,000 USD total over 24 months
LOI due: 2026-06-08, 2 pm PDT / 9 pm UTC
Application portal: https://renphil.fillout.com/os4ls

---

Auxiliary materials in LOI-MISC.md. Here we contain only what is to be submitted.

## Applicant & Host Organization

- Principal Investigator: Yaroslav O. Halchenko, Ph.D.
  - Center for Open Neuroscience, Dartmouth College
  - Role on BIDS: Emeritus Steering Group member; core contributor to BIDS specification, bids-examples, bids-validator, pybids, bids-utils; initiator and lead of BIDS-Study, and BIDS 2.0 working group; lead of DataLad, ReproIn, ReproNim/containers; Co-PI and Co-I on National data archives using BIDS: DANDI, OpenNeuro, EMBER
  - Email: yaroslav.o.halchenko@dartmouth.edu
- Host / fiscal sponsor: Trustees of Dartmouth College — institutionally agreed to 10% indirect cost rate (matching the RFA cap), and will issue subawards to the collaborating institutions
  

---

## Form fields (with character limits)

### Proposal Title — 60 characters max

BIDS 2.0+: AI-Ready Life Sciences Data Standard

---

### Short Summary — 3,000 characters max

BIDS (Brain Imaging Data Structure) is the community-driven, openly governed standard that organizes scientific datasets to be unambiguously consumed by Human Intelligence (HI), conventional pipelines, and AI agents.

Since 2016, BIDS has grown from MRI-only to 10+ biological measurement and stimulation technologies (MRI, EEG/MEG/iEEG, PET, NIRS, microscopy, motion, MRS, physiological, behavioral, NIBS), with 1,500+ public datasets on OpenNeuro and multi-TB microscopy on DANDI.
Dozens of BIDS Apps (fMRIPrep, MRIQC, QSIPrep) consume it; thousands of papers cite it.
Active BEPs (BEP028 provenance; BEP036 phenotypes; BEP037 NIBS; BEP044/047 stimuli & A/V; BEP032 animal/extracellular) and *omics-archive dialogues pull BIDS into adjacent domains.

This proposal supports the coordinated evolution of the BIDS ecosystem into a natively AI-ready standard, on the premise that what is good for HI is good for AI — only AI benefits even more from explicit structure.
We will advance five tightly coupled components whose maintainers have collectively committed:

1. BIDS specification & schema — release BIDS 2.0 (more consistent, modular), scope the 3.0 roadmap, harden the machine-readable schema as a Data Structure Standard, and land the BEP backlog to broaden BIDS beyond neuro;

2. BIDS validators — community-driven convergence of implementations on the schema, machine-consumable records, and integration of cross-standard validators (HED, NWB, Zarr) — critical for trustworthy AI results;

3. Python + CLI utilities with MCP interfaces and skills — consolidate scattered, in-use helpers into a maintained, pybids-adjacent query/manipulation library, exposed via MCP servers and reusable agent skills so LLM agents can read, write, and reason about BIDS datasets;

4. BIDS-Apps 2.0+ — on the mature BIDS-Apps registry (50+ apps) and Boutiques, modernize the contract between BIDS data and analysis containers (via Niwrap and the BIDS-Apps 2.0 execution spec) so AI agents can compose and run pipelines reliably — including GPU/accelerator containers (BEP032 Allen Institute + HuggingFace);

5. BIDS Users Assistant — extend OSA with deep BIDS awareness, and formalize a study-state observability layer so dashboards and human reviewers can introspect AI agents' actions.

Together, these five close the loop for AI-enabled, large-scale data analysis by formalizing the data and application contracts agentic workflows and training pipelines need.

The work is explicitly modular — each component delivers standalone value; advance in any one lifts every downstream tool. Funds support hackathons, conference travel, and dedicated cross-project coordination (PM + maintainer support) as enabling infrastructure for BIDS 2.0.
Scope guard: no new datasets (beyond examples), no new ML models, no archive/repository infrastructure — only the standard, the tools, and the AI-readiness layer the rest of the life sciences can adopt.

---

### Expected Value — 1,500 characters max

Capabilities unlocked. By month 24, any life-sciences researcher or LLM agent will be able to:

(i) check whether a dataset is BIDS "deep-valid" against every format and sibling standard (HED, NWB, OME-Zarr) — verdict consumed identically by agents, pipelines, and humans (not deposit-pipeline tooling);

(ii) query and manipulate it via maintained CLI, Python API, and MCP servers, plus a collection of domain-specialized SKILLs;

(iii) wrap any analysis tool as a Boutiques/Niwrap descriptor and run it as a BIDS App 2.0 — including GPU/accelerator containers — directly or via an agent;

(iv) introspect provenance, derivatives state, and outstanding QC through a common observability schema regardless of who acted;

(v) get human- and agent-readable explanations and guidance through the OSA AI assistant.

Upstream impact. A versioned schema-first specification with machine-readable extension points unlocks BEPs in *omics-linked phenotypes, animal behavior, stimuli, and audio/video — pulling new life-sciences communities into BIDS.

Downstream impact. Every BIDS App, every OpenNeuro dataset (and soon DANDI via nwb2bids), every nipreps pipeline, brainlife/Nipoppy dashboard, and every emerging AI agent (KOSMOS-style, OSA, custom MCP clients) inherits cleaner inputs, stricter validation, and well-defined endpoints.

The same investment that makes BIDS easier for humans makes it more usable for AI — and exposes a template other life-science standards can mirror.

---

### Landscape Analysis — 1,500 characters max

BIDS is the near-monopoly organization standard across neuroscience, biomedical imaging, and adjacent life-science subfields: OpenNeuro (1,500+ datasets), DANDI (1,000+ joining BIDS), ABCD, UK Biobank derivatives, and major pipelines (fMRIPrep, QSIPrep, etc) consume or produce BIDS.
BIDS received the 2023 Neuro – Cooper Foundation Open Science International Prize. Two co-PIs (Poline, Esteban) led CZI EOSS-funded BIDS-adjacent projects (Nilearn, NiPreps).

No peer exists at the data-organization layer, proprietary or open: vendor formats (BrainVision, CTF, Plexon) and DICOM are inputs BIDS ingests and organizes. At the analysis layer, Boutiques / Niwrap / Styx is the leading open descriptor stack with no true peer; commercial alternatives (Flywheel, QMENTA) are closed-source.
Adjacent open standards — NWB, NIfTI, HED, Zarr/OME-Zarr — are integrated into BIDS; this proposal invests in interoperability, not re-implementation. BEP43 + Boutiques descriptors map legacy (AFNI, FreeSurfer) and HPC outputs into BIDS.

AI use. BIDS is the de-facto input contract for AI in this field: ML training pipelines (ABCD, UK Biobank, EEG2025 — NeurIPS, 1,100 teams), foundation-model efforts (KOSMOS, BrainLM), and AI assistants like OSA rely on BIDS layout to make data legible.
Yet the BIDS 1.x series evolved with validators, APIs, and pipeline descriptors designed for human authors; the major 2.0 (and queued 3.0) revisions are required to raise consistency — gaps this proposal closes.

---

### Software Projects to be Supported — up to 5

A tricky part since only up to 5 so we need to either choose or somehow bundle . Submission form has

Software Project Name * 30 characters maximum
Software Project's Repository URL *
Software Project's Website URL

below I am listing only what is submitted. LOI-MISC.md will have more associated info etc

1. BIDS spec, schema, schematools
   - Repo: https://github.com/bids-standard/bids-specification
   - Website: https://bids-specification.readthedocs.io/

2. BIDS validator(s)
   - Repo: https://github.com/bids-standard/bids-validator
   - Website: https://bids-validator.readthedocs.io/en/latest/

3. PyBIDS
   - Repo: https://github.com/bids-standard/pybids
   - Website: https://bids-standard.github.io/pybids/

4. BIDS-Apps
   - "Repo" (org): https://github.com/bids-apps
   - Website: https://bids-apps.neuroimaging.io/

5. OSA — Open Science Assistant
   - Repo: https://github.com/OpenScience-Collective/osa/
   - Website: https://demo.osc.earth/bids

---

### Categories — up to 3 tags

- Neuroscience
- Biological and biomedical imaging
- Data formats and storage

---

### Funding Track

- [x] Track 2 — Foundational Libraries and Ecosystem Initiatives (up to $1,000,000 / 24 months)
- [ ] Track 1 — Domain-specific Tools

