# OS4LS Full Application — BIDS 2.0+ Ecosystem

- Funding opportunity: Open Source for the Life Sciences (OS4LS), Open Source for Science Fund / Renaissance Philanthropy
- Track: Track 2 — Foundational Libraries and Ecosystem Initiatives
- Funding ceiling: up to $1,000,000 USD total / 24 months (max $500,000 USD/year)
- Full Application due: 2026-07-21, 2 pm PDT / 9 pm UTC
- Project start date: 2026-12-01
- Project end date: 2028-11-30

Structure of this document mirrors the Full Application Instructions (`docs/Full-Application-Instructions_-OS4LS.pdf`, June 2026).
Each field below is annotated with its character/word limit as documented there.
Fields pre-filled from the LOI are marked `[pre-filled from LOI [x]]`.
Text intended for direct paste into the Fillout portal is kept plain (no markdown emphasis) so it renders identically in a plain textarea.
Some outstanding Work items are listed at the end of the document in "Working notes". It is preferable to have sentence-a-line formatting.
Short PI / Co-PI biosketches for the optional 4-page supporting-documentation PDF live under `subs/`.

---

## Section 1 — Applicant and Key Personnel Information

### Applicant (PI) [pre-filled from LOI [x]]

- First Name: Yaroslav
- Last Name: Halchenko
- Email: yaroslav.o.halchenko@dartmouth.edu
- Organizational or Institutional Affiliation: Center for Open Neuroscience, Department of Psychological and Brain Sciences, Dartmouth College
- Country of Residence: United States
- Previous Funding: Previously received funding as a PI under CZI EOSS: No (Co-I on multiple BIDS-adjacent federally funded grants; not an EOSS PI)

### Proposal Team (Co-PIs and Key Personnel)

Do NOT list the Applicant here. Roles:
- Co-PI = jointly responsible with the Applicant for leading the work
- Key personnel = individual(s) to be supported by the grant or contribute to the project(s)

Co-PIs (jointly responsible for leading the work):

| Name | Email | Affiliation | Country | Role |
|---|---|---|---|---|
| Russell A. Poldrack | russpold@stanford.edu | Stanford University | USA | Co-PI (BIDS co-founder; Emeritus Steering) |
| Franco Pestilli | pestilli@utexas.edu | The University of Texas at Austin | USA | Co-PI (Steering Group; connectomics) |
| Kimberly Ray | kimray@utexas.edu | The University of Texas at Austin | USA | Co-PI (BIDS Maintainer; Project Manager) |
| Jean-Baptiste Poline | jean-baptiste.poline@mcgill.ca | McGill University | Canada | Co-PI (Steering Group; Boutiques/Nipoppy) |
| Alejandro de la Vega | delavega@utexas.edu | The University of Texas at Austin | USA | Co-PI (PyBIDS, fitlins) |
| Seyed Yahya Shirazi | syshirazi@ucsd.edu | University of California, San Diego | USA | Co-PI (BIDS Maintainer; OSA; HED; BEP044) |
| Ariel Rokem | ariel.rokem@camh.ca | Centre for Addiction and Mental Health (CAMH) | Canada | Co-PI (Emeritus Steering; dMRI/TRX) |
| Ben Dichter | ben.dichter@catalystneuro.com | CatalystNeuro | USA | Co-PI (BEP032, BEP047; NWB<->BIDS) |

Key personnel to be supported by the grant (or contributing to the work):

| Name | Email | Affiliation | Role |
|---|---|---|---|
| Cody Baker | (via Dartmouth) | Dartmouth College | Key (BEP032, NWB<->BIDS, nwb2bids, \*omics scoping) |
| Christopher J. Markiewicz | (via Stanford) | Stanford University | Key (BIDS Maintainer in charge; bids-validator, pybids, BEP043) |
| Ross W. Blair | rosswilsonblair@gmail.com | Stanford University | Key (bids-validator, bids-schema) |
| Nell Hardcastle | (via Stanford / OpenNeuro) | Stanford University / OpenNeuro | Key (bids-validator, OpenNeuro integration) |
| Gregory Kiar | Gregory.Kiar@childmind.org | Child Mind Institute | Key (BEP027 execution spec, Niwrap/Styx, bids2table) |
| Oscar Esteban | phd@oscaresteban.es | HES-SO Valais-Wallis (Lausanne) | Key (nipreps; AI-assisted pipelines (consultant/travel)) |

Potentially list as Key but likely not:

| Name | Email | Affiliation | Role |
|---|---|---|---|
| Florian Rupprecht | (via Child Mind Institute) | Child Mind Institute | Niwrap/Styx |
| Jason Kai | (via Child Mind Institute) | Child Mind Institute | Niwrap/Styx |
| Kay Robbins | (via UTSA, emeritus) | UT San Antonio | HED (unpaid contributor) |

Note: additional personnel supported under the confirmed subawards —
e.g., at McGill (Julia, Rémi, Michelle/Nikhil, Christine)
and Stanford (Jeanette Mumford, fitlins) — are indicated in the
sub-award planning worksheet
(`gdrive/2026-os4ls-bids_subawards_and_consultants.tsv`) and will be
added here as the subaward paperwork is finalized. Dartmouth OSP has
confirmed prior experience issuing subawards to McGill, so the McGill
subaward is not expected to introduce international-collaboration
risk.

---

## Section 2 — Organization Information

- Organization Name [pre-filled from LOI [x]]: Trustees of Dartmouth College
- Organization Address (from Dartmouth OSP):
  - Street Address: Office of Sponsored Projects, 11 Rope Ferry Road, #6210
  - City: Hanover
  - State / Province: NH
  - Zip: 03755-1421
  - Country: United States
- Organization Website [pre-filled from LOI [x]]: www.dartmouth.edu/~osp
- Organization Tax ID (EIN, XX-XXXXXXX; 10 chars): 02-0222111
- Type of organization [pre-filled from LOI [x]]: academic institution
- Organizational / Administrative Contact (from Dartmouth OSP):
  - Name: Stephanie Morgan
  - Email: sponsored.projects@dartmouth.edu
- Signing Official (SO / AOR): Colleen Sullivan, sponsored.projects@dartmouth.edu
- Financial Contact: Shelagh Eastridge, sponsored.projects@dartmouth.edu
- Organizational Approval and Sign-Off Form: single PDF, signed by an
  institutional Signing Official. Not encrypted or password-protected;
  digital signatures OK.
  - Local staging path (do NOT commit signed form): `.signed/` — plan
    to keep the signed PDF outside git; add a placeholder note in the
    PR description.

Indirect-cost commitment: Dartmouth has agreed to cap indirect costs at
10% (matching the RFA limit) and to issue subawards to all
collaborating institutions. All subaward institutions have
separately confirmed acceptance of the 10% IDC rate for the Open
Source for the Life Sciences program via their respective
sponsored-projects offices.

---

## Section 3 — Proposal Information

### Title [pre-filled from LOI [x]] — max 60 characters

BIDS 2.0+: AI-Ready Life Sciences Data Standard

### Proposal Purpose — max 200 characters

Briefly describe the software project(s) and the specific technical
bottleneck or capability gap this proposal will address.

TEXT (195/200 chars; re-count before paste):

BIDS 2.0 spanning spec, validators, PyBIDS, BIDS-Apps, Assistant: closing spec-consistency gaps for humans and machines, adding AI-agent interfaces (MCP, skills), broadening across life sciences.

### Funding Track [pre-filled from LOI [x] — cannot change from LOI]

- [x] Track 2 — Foundational Libraries and Ecosystem Initiatives (up to $1,000,000 USD / 24 months)
- [ ] Track 1

### List of Software Projects to be Supported (up to 5)

For each: Project Name (max 30 chars), Repository URL, Website URL
(optional), Short description (max 500 chars), License, Main
programming language, Canonical citation (if available), Code of
conduct link, End-user docs link, Contributor / developer guidelines
link, Package-manager entry (if applicable), Community / Q&A forum
link, plus impact metrics (whole numbers; optional comment ≤200 chars):
Monthly users, Dependent projects/packages, Scholarly citations.

---

**Project 1 — BIDS spec, schema, schematools** (30 chars: `BIDS spec, schema, schematools`)

- Repository URL: https://github.com/bids-standard/bids-specification
- Website URL: https://bids-specification.readthedocs.io/
- Short description (max 500 chars): TEXT

  The Brain Imaging Data Structure (BIDS) — the community-driven,
  openly governed specification and machine-readable schema that
  organizes life-science datasets (MRI, EEG/MEG/iEEG, PET, NIRS,
  microscopy, motion, MRS, physiology, behavior, NIBS) into a
  standard, unambiguous layout so humans, pipelines, and AI agents
  read them identically. Also includes the schema (`src/schema`),
  schematools (validation & code generation), and the BIDS 2.0
  refactor branch (`bids-2-devel`).

  The umbrella organization https://github.com/bids-standard/ provides other
  relevant repositories sattelite to this project, which is developed fully in
  the open and all components are made available under OSI-compliant licenses.
  See https://github.com/orgs/bids-standard/repositories to find bids-website
  (source of project-wide https://bids.neuroimaging.io/), uptime monitor,
  etc.

- Software license: CC-BY 4.0 (specification text) / MIT (schema tooling)
- Main programming language: Markdown + YAML (schema); Python (schematools)
- Canonical citation: Gorgolewski KJ, et al. (2016). "The Brain Imaging
  Data Structure, a format for organizing and describing outputs of
  neuroimaging experiments." Scientific Data 3, 160044.
  https://doi.org/10.1038/sdata.2016.44
- Code of Conduct: https://bids.neuroimaging.io/collaboration/bids_github/CODE_OF_CONDUCT.html
- End-user documentation: https://bids-specification.readthedocs.io/
- Contributor / developer guidelines: https://github.com/bids-standard/bids-specification/blob/master/CONTRIBUTING.md
- Package manager entry: N/A (spec) — schematools: PyPI `bidsschematools`
- Community / Q&A forum: https://neurostars.org/tag/bids
- Metrics (​Software Project usage and impact metrics​ : List whole numbers and add optional​
​comments (max 200 characters), as needed.​)
  - 1+ PBs of data in 1k+ datasets, created by 1k+ of "creators", used by 10k+ users. https://bids.neuroimaging.io/impact and https://bids.neuroimaging.io/datasets . (Gorgolewski 2016) cited 2k+ times.

---

**Project 2 — BIDS validator(s)** (30 chars: `BIDS validator(s)`)

- Repository URL: https://github.com/bids-standard/bids-validator
- Website URL: https://bids-validator.readthedocs.io/en/latest/
- Short description (max 500 chars): TEXT

  Reference BIDS validators — the Deno/TypeScript schema-driven
  implementation used by OpenNeuro deposit and dataset authors, and
  the Python validator (bids-standard/python-validator) used inside
  Python pipelines and by pybids. Both consume the same
  machine-readable BIDS schema. This proposal drives cross-implementation
  convergence, adds machine-consumable validation records, and
  integrates cross-standard checks (HED, NWB, Zarr).

- Software license: MIT
- Main programming language: TypeScript (Deno) / Python
- Canonical citation: bids-standard/bids-validator (software) — cite as
  the specification paper above for scientific use.
- Code of Conduct: https://github.com/bids-standard/.github/blob/main/CODE_OF_CONDUCT.md
- End-user documentation: https://bids-validator.readthedocs.io/en/latest/
- Contributor / developer guidelines: https://github.com/bids-standard/bids-validator/blob/main/.github/CONTRIBUTING.md
- Package manager entry: npm `bids-validator`
  (legacy); deno.land / JSR distribution for current TS validator; PyPI: `bids-validator-deno`
- Community / Q&A forum: https://neurostars.org/tag/bids-validator
- Metrics (verified 2026-07-15 by C. Markiewicz; https://github.com/bids-standard/bids-validator/issues/431):
  No telemetry by design; ~46k/month users from downloads, ~700 clones/month, ~1k runs of validator/mo on OpenNeuro.org; invoked by dandi-cli on each upload/validation of a BIDS DANDI package.

---

**Project 3 — PyBIDS + bids-utils** (30 chars: `PyBIDS + bids-utils`)

- Repository URL: https://github.com/bids-standard/pybids
- Website URL: https://bids-standard.github.io/pybids/
- Short description (max 500 chars): TEXT

  PyBIDS is the reference Python library for querying and manipulating BIDS
  datasets — used by fMRIPrep, MRIQC, QSIPrep, fitlins, and most downstream
  BIDS Apps. This proposal modernizes PyBIDS for BIDS 2.0 and consolidates scattered
  ecosystem helpers into bids-utils, a comanion tool under the
  same organization. Both libraries will be exposed via MCP servers and reusable agent
  skills, so LLM agents can read, write, and reason about BIDS datasets through
  a stable interface.

- Software license: Apache-2.0 (PyBIDS and bids-utils)
- Main programming language: Python
- Canonical citation: Yarkoni T, et al. (2019). "PyBIDS: Python tools for
  BIDS datasets." Journal of Open Source Software 4(40), 1294.
  https://doi.org/10.21105/joss.01294
- Code of Conduct: https://github.com/bids-standard/.github/blob/main/CODE_OF_CONDUCT.md
- End-user documentation: https://bids-standard.github.io/pybids/
- Contributor / developer guidelines: https://github.com/bids-standard/pybids/blob/main/CONTRIBUTING.md
- Package manager entry: PyPI `pybids`; conda-forge `pybids`
- Community / Q&A forum: https://neurostars.org/tag/pybids
- Metrics:
  - No telemetry; 125k/mo downloads (PyPI+conda-forge); 570 dependent repositories, 17 dependent PyPI packages; 70+ citations of (Yarkoni 2019) PyBIDS paper

---

**Project 4 — BIDS-Apps + execution spec** (30 chars: `BIDS-Apps + execution spec`)

- Repository URL: https://github.com/bids-standard/execution-spec
  (companion registry: https://github.com/bids-apps ;
  Boutiques/Niwrap/Styx: https://github.com/boutiques/boutiques ,
  https://github.com/childmindresearch/niwrap ,
  https://github.com/childmindresearch/styx)
- Website URL: https://bids-standard.github.io/execution-spec/ (registry:
  https://bids-apps.neuroimaging.io/)
- Short description (max 500 chars): TEXT

  Containerized analysis tools that consume BIDS input;
  the registry lists 50+ apps (fMRIPrep, MRIQC, etc.). This proposal modernizes the
  contract between BIDS data and analysis containers via the
  execution-spec (BEP027/BEP043) and the Boutiques/Niwrap/Styx
  descriptor stack — so agents can compose and run pipelines
  reliably, including GPU/accelerator containers (Allen Institute,
  HuggingFace-model workloads).

- Software license: CC Attribution 4.0 International; Tools & Apps - varying OSI-compliant
- Main programming language: Python (Boutiques, Niwrap, Styx); shell (container recipes)
- Canonical citation: Gorgolewski KJ, et al. (2017). "BIDS apps:
  Improving ease of use, accessibility, and reproducibility of
  neuroimaging data analysis methods." PLOS Computational Biology
  13(3): e1005209. https://doi.org/10.1371/journal.pcbi.1005209
- Code of Conduct: per project, e.g. https://github.com/bids-standard/.github/blob/main/CODE_OF_CONDUCT.md
- End-user documentation: https://bids-apps.neuroimaging.io/
- Contributor / developer guidelines: per project (see repos)
- Package manager entry: PyPI `boutiques`, `niwrap`, `styx` (as applicable)
- Community / Q&A forum: https://neurostars.org/tag/bids-apps
- Metrics (TODO): No telemetry in invocations, 50+ tools, thousands of produced derived datasets, varying use across BIDS-apps. BIDS-apps paper (Gorgolewski, 2017) cited 400+ times (Scholar).

---

**Project 5 — OSA — Open Science Assistant** (30 chars: `OSA — Open Science Assistant`)

- Repository URL: https://github.com/OpenScience-Collective/osa
- Website URL: https://demo.osc.earth/bids
- Short description (max 500 chars): TEXT

  OSA (Open Science Assistant) is an AI assistant for open-science
  workflows. This proposal extends OSA with deep BIDS awareness —
  wiring in the BIDS schema, validators, PyBIDS/bids-utils MCP
  servers, and BIDS-Apps 2.0 execution — and formalizes a study-state
  observability layer so dashboards and human reviewers can
  introspect AI agents' actions and derivatives state at any level.

- Software license: MIT
- Main programming language: Python + TypeScript (agent runtime)
- Canonical citation: (software; no paper yet — will use software heritage / Zenodo release DOI)
- Code of Conduct: https://github.com/OpenScience-Collective/osa/issues/347
- End-user documentation: https://demo.osc.earth/bids
- Contributor / developer guidelines: https://github.com/OpenScience-Collective/osa/issues/348
- Package manager entry: n/a
- Community / Q&A forum: https://github.com/OpenScience-Collective/osa/discussions
- Metrics (TODO):
  - Monthly users estimate: TBD
  - Dependent projects/packages: TBD
  - Scholarly citations estimate: TBD

### Categories [pre-filled from LOI [x]] — up to 3

- Neuroscience
- Biological and biomedical imaging
- Data formats and storage

---

## Section 4 — Project Details (part 2)

### Short Summary [pre-filled from LOI [x]] — max 3,000 characters

Edit as needed from LOI. Briefly describe the purpose of the proposal
and the software project(s) it involves. Details related to the work
plan can be moved to the Work Plan section.

<!-- Seeded verbatim from LOI.md — edit here for the Full App as
     scope details / roadmap references get sharper. -->

BIDS (Brain Imaging Data Structure) is the community-driven, openly governed standard that organizes scientific datasets to be
unambiguously consumed by Human Intelligence (HI), conventional pipelines, and AI agents.

Since 2016, BIDS has grown from MRI-only to 10+ biological measurement and stimulation technologies (MRI, EEG/MEG, PET, microscopy, motion, MRS, and others), with 1,500+ public datasets on OpenNeuro and multi-TB microscopy on DANDI.
Dozens of BIDS Apps (fMRIPrep, MRIQC, QSIPrep) consume it; thousands of papers cite it.
Active BIDS Extension Proposals (BEPs) — for provenance, phenotypes, non-invasive brain stimulation, stimuli & A/V, animal / extracellular electrophysiology — and *omics-archive dialogues pull BIDS into adjacent domains.

BIDS is a very open, wide ecosystem project spanning far more than the five software projects explicitly listed here: ~30 repositories under github.com/bids-standard plus adjacent tooling and data archives (OpenNeuro, DANDI) are anchored on the BIDS specification.
Years of practice have established a community-driven model where component authors lead their work while a public Steering Group and Maintainers coordinate under established (but evolving) governance principles (https://bids.neuroimaging.io/collaboration/governance.html).
This explains the higher-than-typical Co-PI count: each Co-PI is an existing lead or maintainer for one or more components, jointly responsible for coordinated delivery.

Altogether, this proposal supports the coordinated evolution of the BIDS ecosystem into a natively AI-ready standard, on the premise that what is good for HI is good for AI.
We advance five coordinated components (fully detailed in the Work Plan section), whose maintainers have collectively committed:

(1) BIDS specification & schema — release BIDS 2.0 and land the BEP backlog;

(2) validators — Deno/Python convergence with machine-consumable records and integrated cross-standard checks (HED, NWB, Zarr);

(3) Python + CLI utilities exposed via MCP servers and reusable agent skills;

(4) BIDS-Apps 2.0+ execution contract for reproducible pipelines including GPU / accelerator containers;

(5) BIDS Users Assistant (OSA) with a study-state observability layer.

Together they close the loop for AI-enabled, large-scale data analysis by formalizing the data and application contracts that agentic workflows and training pipelines need.

Outputs: enhanced spec, validators, MCP servers + agent skills, BIDS-Apps 2.0 contract, and OSA + observability releases — coordinated by the Project Manager and community hackathons.
Scope guard: no new datasets (beyond examples), no new ML models, no archive/repository infrastructure — only the standard, the tools, and the AI-readiness layer the rest of the life sciences can adopt.

### Expected Value [pre-filled from LOI [x]] — max 1,500 characters

<!-- Seeded verbatim from LOI.md — might need tune ups -->

Capabilities unlocked. By month 24, any life-sciences researcher or LLM agent will be able to:

(i) check whether a dataset is BIDS "deep-valid" against every format and sibling standard (HED, NWB, OME-Zarr) — verdict consumed identically by agents, pipelines, and humans (not deposit-pipeline tooling);

(ii) query and manipulate it via maintained CLI, Python API, and MCP servers, plus a collection of domain-specialized SKILLs;

(iii) wrap any analysis tool as a Boutiques/Niwrap descriptor and run it as a BIDS App 2.0 — including GPU/accelerator containers — directly or via an agent;

(iv) introspect provenance, derivatives state, and outstanding QC through a common observability schema regardless of who acted;

(v) get human- and agent-readable explanations and guidance through the OSA AI assistant.

Upstream impact. A versioned schema-first specification with machine-readable extension points unlocks BEPs in \*omics-linked phenotypes, animal behavior, stimuli, and audio/video — pulling new life-sciences communities into BIDS.

Downstream impact. Every BIDS App, every OpenNeuro and a majority of brainlife.io datasets (and soon DANDI via nwb2bids), every nipreps pipeline, the brainlife/Nipoppy dashboards, and every emerging AI agent (KOSMOS-style, OSA, custom MCP clients) inherits cleaner inputs, stricter validation, and well-defined endpoints.

The same investment that makes BIDS easier for humans makes it more usable for AI — and exposes a template other life-science standards can mirror.

### Landscape Analysis [pre-filled from LOI [x]] — max 1,500 characters

<!-- Seeded verbatim from LOI.md — might need tune ups -->

BIDS is the most widely adopted standard in neuroimaging, expanding into adjacent life-science subfields: OpenNeuro (1,500+ datasets), DANDI (1,000+ joining BIDS), ABCD, UK Biobank derivatives, and major pipelines (fMRIPrep, QSIPrep, etc) consume or produce BIDS.
BIDS received the 2023 Neuro – Cooper Foundation Open Science International Prize. A co-PI (Poline) led Nilearn's CZI EOSS-funded BIDS-adjacent project.

No peer exists at the data-organization layer, proprietary or open: vendor formats (BrainVision, CTF) and DICOM are inputs BIDS ingests and organizes. At the analysis layer, Boutiques / Niwrap / Styx is the leading open descriptor stack with no true peer; commercial alternatives (Flywheel, QMENTA) are closed-source.
Adjacent open standards — NWB, NIfTI, HED, Zarr/OME-Zarr — are integrated into BIDS; the overall BIDS project is an integration project which improves reuse and interoperability while avoiding re-implementation.
This proposal will facilitate internal consistency of the standard and improve interfaces to tools and AI. 
BEP43 + Boutiques descriptors map legacy (AFNI, FreeSurfer) and HPC outputs into BIDS.

AI use. BIDS is the de-facto input contract for AI: ML training pipelines and AI benchmarks (ABCD, UK Biobank, EEG2025 (NeurIPS, 1,100 teams)), AI "scientist" frameworks (KOSMOS, K-Dense-AI, Meta NeuroAI), and AI assistants like OSA benefit from BIDS to make data legible.
Yet the BIDS 1.x series evolved with validators, APIs, and pipeline descriptors designed for human authors; the major 2.0 (and queued 3.0) revisions are required to raise consistency — gaps this proposal closes.


### Work Plan and Goals, Outcomes, Milestones and Deliverables

This section is uploaded as a single PDF built from the Work Plan template
(originally on [google
drive](https://docs.google.com/document/d/1QeloUWQCiDwTPzZlJQ55tKHAoTHztuhIqSm90aEkuWo/edit?tab=t.0]
with a PDF render here under `docs/OS4LS_Work_Plan_template.pdf`). Local
Markdown source for that PDF is maintained here so Yarik will later plug
it as needed into the template to produce the PDF for submission.

#### Work Plan (max 750 words) — narrative

Word budget: 750 words.
Count with `wc -w` before submit.

TODO: heavy tune up!!!

TEXT (draft narrative):

BIDS is a widely used open-source specification and tooling ecosystem for structured, machine- and human-legible organization of life-science data, maintained by a international and multi-institution community of contributors and a public Steering and Maintainenance Groups following established Governance procedures.
This request supports a 24-month plan to integrate the BIDS ecosystem at the core of computational scientists' preferred harnesses, organized around the five coordinated goals below.

Goal 1 delivers the BIDS 2.0 release (more consistent, modular, schema-first) with a scoped 3.0 roadmap and hardens the machine-readable schema as a Data Structure Standard, landing the active BEP backlog to broaden BIDS beyond neuroimaging — work spans bids-specification, bids-examples, bids-website, pybids, etc., tracked at https://github.com/orgs/bids-standard/projects/10.
Goal 2 continues the community-driven convergence of the Deno and Python validators on the shared schema, adds machine-consumable validation records, and integrates cross-standard checks (HED, NWB, Zarr) so that a "deep-valid" verdict means valid across formats and sibling standards — critical for trustworthy AI results.
Goal 3 consolidates scattered helpers (across pybids, bids2nda, DataLad) into a maintained pybids-adjacent bids-utils library, exposes both via MCP servers, and packages reusable agent skills (currently prototyped in K-Dense-AI/scientific-agent-skills) so LLM agents can read, write, and reason about BIDS datasets through a stable interface.
Goal 4 modernizes the BIDS-Apps execution contract (BEP027/BEP043) in coordination with the Boutiques / Niwrap / Styx descriptor stack and the BIDS-Apps registry — including GPU/accelerator containers — so AI agents can compose and run pipelines reliably.
Goal 5 extends OSA with deep BIDS awareness and formalizes a study-state observability layer used today in ad-hoc form by brainlife.io and Nipoppy dashboards, so human reviewers and AI agents share a common view of a study's provenance, derivatives, and outstanding QC.

Overall organization of work for Goals 2-5 will be organized and prioritized within projects like https://github.com/orgs/bids-standard/projects/24.
Beyond the requested funds, each institution contributes existing personnel time (uncompensated by this grant) where people already work on BIDS in related projects but not directly toward the goals established in this grant proposal.
The BIDS Steering Group and the Maintainers organization contribute governance capacity in kind.
DANDI (Dartmouth) and OpenNeuro (Stanford) contribute deposit-side validation feedback as new datasets will be flowing into those repositories.
DANDI (via nwb2bids) will also contribute feedback on alignment to microscopy / extracellular electrophysiology with CatalystNeuro contributing NeuroConv and NWB Inspector integration.
Community activities include two annual BIDS hackathons / sprints organized by the PI & Project Manager (Kimberly Ray, UT Austin) — targeting maintainers, downstream BIDS-App authors, and adjacent-standard maintainers (HED, NWB, Zarr).
All code is developed in the open under OSI-Approved licenses (e.g. CC-BY-4.0 (specification text) / MIT / Apache-2.0 (tooling)), with releases published on GitHub and PyPI/conda-forge/npm as applicable.

Scalability and modular composition:
BIDS already operates at scale — OpenNeuro hosts 1,500+ public datasets brainlife.io stores dozens of PB multimodal datasets from NIH BRAIN CONNECTS and DANDI stores multi-TB BIDS microscopy datasets. Its standardized subject/session hierarchy provides a natural unit of parallelization, enabling human workflows, HPC pipelines, and AI agents to scale without custom sharding logic.
Composition works within a dataset (nested `sourcedata/`, raw, `derivatives/`) and across datasets via BIDS-Study, OpenNeuroStudies, and the Nipoppy study network, so summarization bubbles up cleanly through subject → study → cross-study → dashboard layers (brainlife, Nipoppy), thus also fascilitating adherence to Self-containment and Modularity principles of https://stamped-principles.org (developed by the PIs group).
Goal 2's schema-driven validator convergence keeps validation cheap enough to run inside agent loops; Goal 4's execution-spec + Boutiques / Niwrap / Styx path preserves this modularity when wrapping GPU / accelerator containers as BIDS Apps 2.0, so hardware-accelerated workloads inherit the same composition semantics as CPU pipelines.

Sustainability:
Post-grant maintenance continues through the PI's and Co-PIs' involvement via the existing BIDS governance and maintenance structure and adjacent federally-funded work (DANDI, OpenNeuro, EMBER, nipreps, brainlife.io, Nipoppy), all benefiting from the work done under this funding.

TODO before submission:
- Trim to under 750 words
- Cross-link each goal below by number to the pillars in Short
  Summary.
- Add a one-line "not-in-scope" reiteration mirroring the LOI
  scope guard.

#### Goals, Outcomes, Milestones and Deliverables (up to 5 goals; NOT counted in the 750-word narrative limit)

Each goal has four fields per the Work Plan template (`docs/OS4LS_Work_Plan_template.pdf`): Goal / Outcome / Milestones & Deliverables (numbered X.Y with Year 1 / Year 2 tag) / Success indicators.

TODOs: heavey overview/tuneup

---

**Goal 1: BIDS specification, schema, and BIDS 2.0 release**

Outcome: The BIDS 2.0 specification is released — more consistent, modular, schema-first — with hardened derivatives contracts (provenance, connectivity, stimuli), and the 3.0 roadmap is scoped.
Downstream tools (validators, PyBIDS, BIDS Apps) adopt the new schema without loss, and the active BEP backlog (BEP028, BEP032, BEP036, BEP037, BEP044/047) is landed so BIDS covers phenotypes, animal / extracellular electrophysiology, NIBS, stimuli and A/V.

Milestones & Deliverables:
1.1 Prepare, finalize, merge and tag BIDS 2.0 (`bids-standard/bids-specification` `bids-2-devel` branch → main). [Year 1]
1.2 Publish BIDS 3.0 roadmap document with community sign-off. [Year 2]
1.3 Land BEPs from the active queue (subset to be selected with Steering Group at kickoff; not blocked by BIDS 2.0 release per se). [Years 1–2]

Success indicators:
- BIDS 2.0 tagged and adopted by ≥3 downstream tools (validators, PyBIDS, ≥1 major BIDS App) [Year 2].
- ≥3 BEPs from the active queue merged. [Year 2]
- Schema 2.x+ release consumed by both validators and PyBIDS. [Year 2]

---

**Goal 2: BIDS validators — convergence, machine-consumable records, and cross-standard checks**

Outcome: Validation is a first-class, agent-callable operation: the Deno and Python validators consume the same schema and produce identical, machine-consumable verdicts; cross-standard validators (HED, NWB, Zarr / OME-Zarr) are integrated so a "deep-valid" verdict means valid across formats and sibling standards.

Milestones & Deliverables:
2.1 Converge Deno and Python validators on the shared schema — identical CLI behavior and machine-readable output. [Year 1]
2.2 Publish the machine-consumable validation-record schema (JSON Schema + example datasets). [Year 1]
2.3 Integrate HED, NWB (via nwb-inspector), and Zarr / OME-Zarr cross-standard validation as pluggable checks. [Year 2]
2.4 Ship validators in Deno / npm / PyPI / conda-forge with reproducible container images. [Year 2]

Success indicators:
- Identical machine-readable output across Deno and Python validators on the reference test corpus [Year 2].
- ≥2 sibling standards (HED, NWB, OME-Zarr) integrated as pluggable checks [Year 2].
- Adoption by OpenNeuro deposit and ≥2 downstream pipelines (fMRIPrep, MRIQC, or QSIPrep) [Year 2].

---

**Goal 3: Python + CLI utilities with MCP interfaces and agent skills**

Outcome: LLM agents, CLI users, and Python users read, write, and reason about BIDS datasets through a stable, maintained interface — via pybids for structured queries and bids-utils for the smaller, agent- and CLI-friendly read/write/inspect verbs, plus MCP servers and reusable agent skills.

Milestones & Deliverables:
3.1 Consolidate scattered helpers into `bids-standard/bids-utils` (release 0.1). [Year 1]
3.2 Publish MCP servers wrapping the BIDS schema, validation, and bids-utils; publish agent skills (extending the current K-Dense-AI/scientific-agent-skills prototypes). [Year 1]
3.3 Maintain and modernize PyBIDS; align its Layout / query API with the schema 2.x release. [Years 1–2]
3.4 Ship stable, versioned Python and CLI API. [Year 2]

Success indicators:
- ≥3 downstream tools (fMRIPrep, brainlife, Nipoppy, KOSMOS-class agents) call the new MCP servers or agent skills [Year 2].
- bids-utils 1.0 release with public API stability policy. [Year 2]
- PyBIDS release supporting BIDS 2.0 schema and adopted by ≥3 downstream libraries [Year 2].

---

**Goal 4: BIDS-Apps 2.0+ — modernized execution contract, GPU-ready**

Outcome: Analysis tools wrap as Boutiques / Niwrap descriptors and run as BIDS Apps 2.0 — including GPU / accelerator containers — so AI agents can compose and run pipelines reliably.

Milestones & Deliverables:
4.1 Update the BIDS-Apps execution spec (BEP027) to align with the latest Boutiques + Styx developments. [Year 1]
4.2 Publish reference implementation demonstrating a GPU / accelerator container running as a BIDS App 2.0 (using an Allen Institute / HuggingFace-model pipeline). [Year 2]
4.3 Update BIDS-Apps registry (bids-apps.neuroimaging.io) to surface BIDS-Apps 2.0 metadata. [Year 2]
4.4 Integrate execution-spec self-description into ///repronim/containers Singularity collection for reproducibility. [Year 2]

Success indicators:
- Execution-spec 2.x tagged and adopted by ≥3 BIDS Apps [Year 2].
- ≥1 GPU / accelerator container demo in the registry [Year 2].
- Niwrap / Styx / Boutiques descriptors published for ≥5 legacy tools (AFNI / FreeSurfer subset) [Year 2].

---

**Goal 5: BIDS Users Assistant (OSA) + study-state observability layer**

Outcome: Human reviewers and AI agents share a common, human-readable, agent-callable view of a BIDS study — its provenance, derivatives, and outstanding QC — via OSA and a formalized study-state observability schema.

Milestones & Deliverables:
5.1 Extend OSA with deep BIDS awareness by wiring the schema, validators, bids-utils MCP servers, and BIDS-Apps 2.0 execution. [Year 1]
5.2 Publish study-state observability schema (JSON Schema + example dashboards) covering provenance, derivatives, and QC state. [Year 1]
5.3 Reference dashboard integration with brainlife.io and Nipoppy consuming the observability schema. [Year 2]
5.4 User study of OSA-BIDS on real study datasets (with informed consent; no new data collection) to measure assistance quality and agent-action reviewability. [Year 2]

Success indicators:
- OSA-BIDS deployed at https://demo.osc.earth/bids with published changelog covering the funded work [Year 2].
- Study-state observability schema 1.0 released and consumed by ≥2 dashboards (brainlife, Nipoppy) [Year 2].
- User-study report published with quantitative agent-action reviewability metrics [Year 2].

### Optional Upload — PI/Co-PI biographies, references, figures (≤4 pages)

**External file(s):  [subs/biographies.md](subs/biographies.md)** (rendered to .pdf)

Potential TODOs:

- [ ] A single ecosystem figure showing spec → validators → PyBIDS /
   bids-utils / MCP → BIDS-Apps 2.0 → OSA / observability, with
   downstream consumers (OpenNeuro, DANDI, brainlife, Nipoppy,
   agent frameworks).

---

## Section 5 — Budget Description

### Amount Requested

Enter as whole numbers, USD, no commas / no dollar signs. Track 2 max:
$500,000 / year; $1,000,000 total. Numbers must match the Budget
Description (uploaded as PDF and/or XLSX).

Status: Will be matched on what near $1mil we have in official budget estimates spreadsheet submitted to Dartmouth.

### Budget Description (uploaded as PDF / XLSX)

**External file(s): [dartmouth/Budget_Narrative_v3.md](dartmouth/Budget_Narrative_v3.md)** (converted from/to .docx)

Stage: submitted to Dartmouth OSP for review.

### Recent Financial Support — max 1,500 characters

List active and recently completed grants (calendar years 2025 and
2026) plus in-kind support that the PI and Co-PIs have received to
directly or indirectly support this work — with duration, total USD
(for grants), and funding source.

TEXT (draft — collect from each Co-PI at kickoff and tighten to ≤1,500
chars before paste):

https://bids.neuroimaging.io/collaboration/acknowledgments.html page lists various grants which supported some parts of work on BIDS currently or in the past.

PI Halchenko is Co-I/Co-PI on federally funded U.S. archives that underpin BIDS in production: DANDI (2020–2029, NIH R24MH117295, $6,500,256 for 2024-2026), OpenNeuro (see below), EMBER (2024-2029, NIH R24MH136632, $3,526,488 for 2024-2026), and the ReproNim (2016-2026, NIH NIBIB P41EB019936, $1,174,836 for 2025) all of which use BIDS and contribute to it.
Co-PI Poldrack directs OpenNeuro (2018-2028, NIH BRAIN Initiative 5R24MH117179, $5,968,723 for 2023-2027).
Co-PI Pestilli is PI/Co-I on the BRAIN CONNECTS APEX (2024–2029, NIH, $9,485,000), the Center for Mesoscale Connectomics (2023–2028, NIH, $16,684,090),  ezBIDS, NiiVue, and dcm2niix (2023–2026, NIH, $2,039,629), which relate to development and use of BIDS spec and tools.
Co-PI Dichter leads CatalystNeuro's NWB work (NIH BRAIN Initiative).
Key person Kiar leads development work on Styx and NiWrap, core to the BIDS Execution standard, BIDS2Table funded by NIH (1RF1MH130859-01, 2022–2026, 1,504,004; 1R01MH139565, 2025–2027, $889,582) alongside grants from Private Foundations (cumulative awards value of over $16,300,000 received from 2021–2027) which rely on BIDS.
In-kind: Amazon Open Dataset program hosts over 1 PB of OpenNeuro and DANDI BIDS datasets (guestimate of 700k$/year cost for both store/egress).


---

## Policies & Attestations

Before submitting, applicant must confirm acceptance of:
- Renaissance Philanthropy Confidentiality Policy (proposal &
  reviews may be shared with the Fund's current and future funding
  partners without further restriction).
- Release of Liability.
- Non-negotiable grant conditions & policies.

Submitting official (Dartmouth): (obtain from OSP; Signing Official
above).

---

## Working notes (NOT part of submission — strip before paste)

- Strip this section, all Message-IDs, and any markdown emphasis /
  backticks before pasting into the Fillout form.

- **Length-cap overages** (must be fixed before final paste):
  - **Recent Financial Support**: 1,769 / 1,500 (269 over). Candidate
    cuts: drop the opening acknowledgments-page sentence (~135 chars);
    trim closing "which relate to development and use of BIDS spec and
    tools" and "which rely on BIDS" (~80 chars); compress Amazon Open
    Dataset in-kind line to "Amazon Open Dataset hosts >1 PB
    OpenNeuro+DANDI BIDS data (~$700k/yr in-kind)."
  - **Landscape Analysis**: 1,628 / 1,500 (128 over). Candidate to drop:
    "the overall BIDS project is an integration project which improves
    reuse and interoperability while avoiding re-implementation. This
    proposal will facilitate internal consistency of the standard and
    improve interfaces to tools and AI." — restates the prior sentence.
  - **Expected Value**: 1,514 / 1,500 (14 over). One-word tighten.

- **Section 3 — impact metrics remaining**:
  - Project 5 (OSA) — still all `TBD`. Session 3 (cue 305-314) permits
    note-field justification: e.g., "Pre-release; usage tracked via
    demo.osc.earth/bids web analytics; no PyPI/npm release yet."
  - Project 4 (BIDS-Apps + exec spec) — has content ("50+ tools,
    Gorgolewski 2017 cited 400+"), just needs the `(TODO)` tag stripped.
  - Projects 1 (spec), 2 (validators), 3 (PyBIDS) — filled with verified
    numbers ✓.

- **Section 3 — potential project-to-org upgrade** (per Session 3 cue
  107-117; Dario: "definitely encourages the GitHub organization as a
  whole is involved in the proposal, especially for a track two
  proposal"). The `bids-standard` org URL is currently referenced only
  inside Project 1's description text. Consider whether one of the five
  Project rows should be replaced by an org-level "project" (e.g.
  `github.com/bids-standard` covers spec + validator + pybids + schema
  + execution-spec + bids-2-devel + examples + website + more).
  Trade-off: less concrete per-repo milestones vs stronger ecosystem
  signal for a Track-2 review.

- **Section 4 — ecosystem figure** for the Optional Upload PDF still
  TODO. Session 3 (cue 68-75) confirms figures are welcome supporting
  material.

- **Section 5 — Amount Requested** — still pending final budget xlsx
  numbers from Dartmouth OSP.

- **Sign-off form** — Session 3 (cue 223-224) confirmed a blank PDF
  placeholder is acceptable at upload time; the signed version can be
  swapped in before final submission if OSP timing is tight.
