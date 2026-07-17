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
Sentence-per-line formatting is preferred for editability.
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

The Brain Imaging Data Structure (BIDS) specification repository includes the schema, schematools (validation & code generation), and the BIDS 2.0 refactor branch.

The organization https://github.com/bids-standard/ provides relevant repositories satellite to this project, which is developed in the open and made available under OSI-compliant licenses.  E.g.  bids-website (source of project-wide https://bids.neuroimaging.io/), uptime monitor, etc.

- Software license: Permissive (was: CC-BY 4.0 (specification text) / MIT (schema tooling))
- Main programming language: Markdown (spec) + YAML (schema); Python (schematools)
- Canonical citation: Gorgolewski KJ, et al. (2016). "The Brain Imaging
  Data Structure, a format for organizing and describing outputs of
  neuroimaging experiments." Scientific Data 3, 160044.
  https://doi.org/10.1038/sdata.2016.44
- Code of Conduct: https://bids.neuroimaging.io/collaboration/bids_github/CODE_OF_CONDUCT.html
- End-user documentation: https://bids-specification.readthedocs.io/
- Contributor / developer guidelines: https://github.com/bids-standard/bids-specification/blob/master/CONTRIBUTING.md
- Package manager entry: RTD+GitHub (spec), schematools: PyPI `bidsschematools`
- Community / Q&A forum: https://neurostars.org/tag/bids
- Metrics (​Software Project usage and impact metrics​ : List whole numbers and add optional​
​comments (max 200 characters), as needed.​)
  - 10000
  - notes: no telemetry!  https://bids.neuroimaging.io/impact and https://bids.neuroimaging.io/datasets collect some stats on BIDS use. Over 1PB of data in BIDS.
  - how many depend on it: 13
  - notes: 13 is just packages from https://github.com/bids-standard/bids-specification/network/dependents . BIDS specification itself is CORE for 50+ Apps etc
  - citations: 2312
  - notes: 2312 is just for the canonical BIDS paper. There are extra papers for many BEPs etc, not included in the count.
  - not used: 1+ PBs of data in 1000+ datasets, created by 1000+ of "creators", used by 1000+/month users. https://bids.neuroimaging.io/impact and https://bids.neuroimaging.io/datasets . 
  - (Gorgolewski 2016) cited 2k+ times.

---

**Project 2 — BIDS validator(s)** (30 chars: `BIDS validator(s)`)

- Repository URL: https://github.com/bids-standard/bids-validator
- Website URL: https://bids-validator.readthedocs.io/en/latest/
- Short description (max 500 chars): TEXT

Reference BIDS validators: the Deno/TypeScript schema-driven implementation used by OpenNeuro deposit and dataset authors, and the Python validator (bids-standard/python-validator) used inside Python pipelines and by pybids. Both consume the same machine-readable BIDS schema. This proposal drives cross-implementation convergence, adds machine-consumable validation records, and integrates cross-standard checks (HED, NWB, Zarr).

- Software license: Permissive # MIT
- Main programming language: TypeScript (Deno) / Python
- Canonical citation: https://doi.org/10.5281/zenodo.17902244
- Code of Conduct: https://github.com/bids-standard/.github/blob/main/CODE_OF_CONDUCT.md
- End-user documentation: https://bids-validator.readthedocs.io/en/latest/
- Contributor / developer guidelines: https://github.com/bids-standard/bids-validator/blob/main/CONTRIBUTING.md
- Package manager entry: https://jsr.io/@bids/validator
  could not enter: npm `bids-validator`  (legacy); deno.land / JSR distribution for current TS validator; PyPI: `bids-validator-deno`
- Community / Q&A forum: https://neurostars.org/tag/bids-validator
- Metrics (verified 2026-07-15 by C. Markiewicz; https://github.com/bids-standard/bids-validator/issues/431):
  No telemetry by design; ~46k/month users from downloads, ~700 clones/month, ~1k runs of validator/mo on OpenNeuro.org; invoked by dandi-cli on each upload/validation of a BIDS DANDI package.
  - Number of dependent packages: 55
    Note: 5 packages and over 50 BIDS-Apps since they should run bids-validator first to ensure that underlying dataset is valid first.
  - citations estimate: 20
    notes: https://rrid.site/data/record/nlx_144509-1/SCR_017255/resolver/mentions?q=R&i=rrid:scr_017255 lists 20, and there could be more for DOI

---

**Project 3 — PyBIDS**

- Note: @yarikoptic removed bids-utils, since there is nothing in here about it
- Repository URL: https://github.com/bids-standard/pybids
- Website URL: https://bids-standard.github.io/pybids/
- Short description (max 500 chars): TEXT

PyBIDS is the reference Python library for querying and manipulating BIDS datasets — used by fMRIPrep, MRIQC, QSIPrep, fitlins, and most downstream BIDS Apps. This proposal modernizes PyBIDS for BIDS 2.0 and consolidates scattered ecosystem helpers into bids-utils, a comanion tool under the same organization. Both libraries will be exposed via MCP servers and reusable agent skills, so LLM agents can read, write, and reason about BIDS datasets through a stable interface.

- Software license: Permissive # Apache-2.0 (PyBIDS and bids-utils)
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
  - Monthly users: 1000
    notes: No telemetry; 125k/mo downloads (PyPI+conda-forge).  Used by containerize BIDS-Apps fMRIPrep.
  - dependent packages: 17
    notes: https://github.com/bids-standard/pybids/network/dependents lists over 900 repos and mentions 124 packages.
  - scholarly citations: 74

---

**Project 4 — BIDS-Apps + Execution spec**

- Repository URL: https://github.com/bids-apps
- Website URL: https://bids-apps.neuroimaging.io/
- Short description (max 500 chars): TEXT

BIDS-Apps are containerized analysis tools that consume BIDS input; the registry lists 50+ apps (such as fMRIPrep and MRIQC), and BIDS-Apps 2.0 specification available in https://bids-standard.github.io/execution-spec/ .
Companion projects:  https://github.com/boutiques/boutiques for interface specifications and https://github.com/childmindresearch/niwrap, https://github.com/childmindresearch/styx-ts to assist wrapping existing tools in Python.

- Software license: Permissive # CC Attribution 4.0 International; Tools & Apps - varying OSI-compliant
- Main programming language: YAML for registry, Markdown (specification), Python (Boutiques, Niwrap, Styx, ...)
- Canonical citation: Gorgolewski KJ, et al. (2017). "BIDS apps:
  Improving ease of use, accessibility, and reproducibility of
  neuroimaging data analysis methods." PLOS Computational Biology
  13(3): e1005209. https://doi.org/10.1371/journal.pcbi.1005209
- Code of Conduct: https://github.com/BIDS-Apps/.github/blob/main/CODE_OF_CONDUCT.md
- End-user documentation: https://bids-apps.neuroimaging.io/
- Contributor / developer guidelines: https://bids.neuroimaging.io/faq/bids-apps.html
- Package manager entry: https://github.com/ReproNim/containers/tree/master/images/bids
- Community / Q&A forum: https://neurostars.org/tag/bids-apps
- Metrics: 
  - monthly users estimate: 1000
    notes: No telemetry in invocations, 50+ Apps, thousands of produced derived datasets, varying use across BIDS-apps.
  - # dependent pkgs:
    notes: BIDS-Apps are self-contained containers. The related/used tools have varying reuse. E.g. boutiques - 10 packages and 100 repos on github analytics.
  - citations: 400

---

**Project 5 — OSA — Open Science Assistant**

- Repository URL: https://github.com/OpenScience-Collective/osa
- Website URL: https://demo.osc.earth/bids
- Short description (max 500 chars): TEXT

OSA (Open Science Assistant) is an extensible AI-assistant platform for open-science communities. This BIDS project deepens OSA's ability to use BIDS data, the BIDS specification, validation, and ecosystem tools through its existing YAML-driven tool/plugin architecture. It adds user feedback and reviewable agent activity for BIDS workflows.

- Software license: Permissive  # MIT
- Main programming language: Python + TypeScript (agent runtime)
- Canonical citation: (software; no paper yet — will use software heritage / Zenodo release DOI)
- Code of Conduct: https://github.com/OpenScience-Collective/osa/blob/main/CODE_OF_CONDUCT.md
- End-user documentation: https://demo.osc.earth/bids
- Contributor / developer guidelines: https://github.com/OpenScience-Collective/osa/blob/main/CLAUDE.md
- Package manager entry: n/a
- Community / Q&A forum: https://github.com/OpenScience-Collective/osa/discussions
- Metrics: Pre-release; usage tracked via demo.osc.earth/bids web analytics; no PyPI/npm release yet.
  - Monthly users: 5
    notes: It is in pre-release stage. We (maintainers) test-drive it in https://github.com/bids-standard/bids-specification/pull/2442 
  - Dependent projects/packages:
  - Scholarly citations: 0
    notes: not published work yet!
	pre-release; software heritage / Zenodo release DOI planned

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

BIDS (Brain Imaging Data Structure) is the community-driven, openly governed standard that organizes scientific datasets to be unambiguously consumed by Human Intelligence (HI), conventional pipelines, and AI agents.

Since 2016, BIDS has grown from MRI-only to 10+ biological measurement and stimulation technologies (MRI, EEG/MEG, PET, microscopy, motion, MRS, and others), with 1,500+ public datasets on OpenNeuro and multi-TB microscopy on DANDI.  Dozens of BIDS Apps (fMRIPrep, MRIQC, QSIPrep) consume it; thousands of papers cite it.  Active BIDS Extension Proposals (BEPs) — for provenance, phenotypes, non-invasive brain stimulation, stimuli & A/V, animal / extracellular electrophysiology — and *omics-archive dialogues pull BIDS into adjacent domains.

BIDS is a very open, wide ecosystem project spanning far more than the five software projects explicitly listed here: ~30 repositories under github.com/bids-standard plus adjacent tooling and data archives (OpenNeuro, DANDI) are anchored on the BIDS specification.  Years of practice have established a community-driven model where component authors lead their work while a public Steering Group and Maintainers coordinate under established (but evolving) governance principles (https://bids.neuroimaging.io/collaboration/governance.html).  This explains the higher-than-typical Co-PI count: each Co-PI is an existing lead or maintainer for one or more components, jointly responsible for coordinated delivery.

Altogether, this proposal supports the coordinated evolution of the BIDS ecosystem into a natively AI-ready standard, on the premise that what is good for HI is good for AI.  We advance five coordinated components (fully detailed in the Work Plan section), whose maintainers have collectively committed:

(1) BIDS specification & schema — release BIDS 2.0 and land the BEP backlog;

(2) validators — Deno/Python convergence with machine-consumable records and integrated cross-standard checks (HED, NWB, Zarr);

(3) Python + CLI utilities exposed via MCP servers and reusable agent skills;

(4) BIDS-Apps 2.0+ execution contract for reproducible pipelines including GPU / accelerator containers;

(5) OSA: deep BIDS integration + study-state observability.

Together, these five coordinated components close the gap between HI and AI by formalizing the data and application contracts needed for collaborative, AI-enabled, large-scale scientific analysis.

Outputs: enhanced spec, validators, MCP servers + agent skills, BIDS-Apps 2.0 contract, and OSA + observability releases — coordinated by the Project Manager and community hackathons.  Scope guard: no new datasets (beyond examples), no new ML models, no archive/repository infrastructure — only the standard, the tools, and the AI-readiness layer the rest of the life sciences can adopt.

### Expected Value [pre-filled from LOI [x]] — max 1,500 characters

<!-- Seeded verbatim from LOI.md — might need tune ups -->

Capabilities unlocked: By month 24, any life-sciences researcher or LLM agent can:

(i) check whether a dataset is BIDS "deep-valid" against every format and sibling standard (HED, NWB, OME-Zarr) — verdict consumed identically by agents, pipelines, and humans (not deposit-pipeline tooling);

(ii) query and manipulate it via maintained CLI, Python API, and MCP servers, plus a collection of domain-specialized SKILLs;

(iii) wrap any analysis tool as a Boutiques/Niwrap descriptor and run it as a BIDS App 2.0 — including GPU/accelerator containers — directly or via an agent;

(iv) introspect provenance, derivatives state, and outstanding QC through a common observability schema regardless of who acted;

(v) get human- and agent-readable explanations and guidance through the OSA AI assistant.

Upstream impact. A versioned schema-first specification with machine-readable extension points unlocks BEPs in *omics-linked phenotypes, animal behavior, stimuli, and audio/video — pulling new life-sciences communities into BIDS.

Downstream impact. Every BIDS App, every OpenNeuro and most brainlife.io datasets (and soon DANDI via nwb2bids), every nipreps pipeline, the brainlife/Nipoppy dashboards, and every emerging AI agent (KOSMOS-style, OSA, custom MCP clients) inherits cleaner inputs, stricter validation, and well-defined endpoints.

The same investment that makes BIDS easier for humans makes it more usable for AI, and exposes a template other life-science standards can mirror.

### Landscape Analysis [pre-filled from LOI [x]] — max 1,500 characters

<!-- Seeded verbatim from LOI.md — might need tune ups -->

BIDS is the most widely adopted standard in neuroimaging, expanding into adjacent life-science subfields: OpenNeuro (1,500+ datasets), DANDI (1,000+ joining BIDS), ABCD, UK Biobank derivatives, and major pipelines (fMRIPrep, QSIPrep, etc) consume or produce BIDS.  BIDS received the 2023 Neuro – Cooper Foundation Open Science International Prize. A co-PI (Poline) led Nilearn's CZI EOSS-funded BIDS-adjacent project.

No peer exists at the data-organization layer, proprietary or open: vendor formats (BrainVision, CTF) and DICOM are inputs BIDS ingests and organizes. At the analysis layer, Boutiques / Niwrap / Styx is the leading open descriptor stack with no true peer; commercial alternatives (Flywheel, QMENTA) are closed-source.  Adjacent open standards — NWB, NIfTI, HED, Zarr/OME-Zarr — are integrated into BIDS.  This proposal improves internal consistency of the standard and its interfaces to tools and AI.  BEP43 + Boutiques descriptors map legacy (AFNI, FreeSurfer) and HPC outputs into BIDS.

BIDS is the de-facto input contract for AI: ML training pipelines and AI benchmarks (ABCD, UK Biobank, EEG2025 (NeurIPS, 1,100 teams)), AI "scientist" frameworks (KOSMOS, K-Dense-AI, Meta NeuroAI), and AI assistants like OSA benefit from BIDS to make data legible.  Yet the BIDS 1.x series evolved with validators, APIs, and pipeline descriptors designed for human authors; the major 2.0 (and queued 3.0) revisions are required to raise consistency for AI use which we want to tackle with this proposal.


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

TEXT (draft narrative):

BIDS is a widely used open-source specification and tooling ecosystem for structured, machine- and human-legible organization of life-science data, maintained by an international and multi-institution community of contributors and a public Steering and Maintainenance Groups following established Governance procedures.
This request supports a 24-month plan to integrate the BIDS ecosystem at the core of computational scientists' preferred harnesses, organized around the five coordinated goals below.

Goal 1 delivers the BIDS 2.0 release (more consistent, modular, schema-first) with a scoped 3.0 roadmap and hardens the machine-readable schema as a Data Structure Standard, landing the active BEP backlog to broaden BIDS beyond neuroimaging. This work spans bids-specification, bids-examples, bids-website, pybids, etc., tracked at https://github.com/orgs/bids-standard/projects/10.
Goal 2 continues the community-driven convergence of the Deno and Python validators on the shared schema, adds machine-consumable validation records, and integrates cross-standard checks (HED, NWB, Zarr) so that a "deep-valid" verdict means valid across formats and sibling standards which is critical for trustworthy AI results. This includes a BIDS-aligned Zarr profile exercised on the NEMAR conversion datasets.
Goal 3 consolidates scattered helpers (across bids2table, bids2nda, cubids, datalad-neuroimaging, pybids) into a maintained pybids-adjacent bids-utils library, exposes both via MCP servers including HED-MCP and a shared tool-interface contract, and packages reusable agent skills (currently prototyped in K-Dense-AI/scientific-agent-skills) so LLM agents can read, write, and reason about BIDS datasets through a stable interface. It also connects NEMAR's Zarr-backed, BIDS/HED-annotated data to GPU training and agent workflows, exercised on the ongoing conversion test bed (>89% implemented: 760 datasets, 39,000 subjects, 57 TB).
Goal 4 modernizes the BIDS-Apps execution contract (BEP027/BEP043) in coordination with the Boutiques / Niwrap / Styx descriptor stack and the BIDS-Apps registry — including GPU/accelerator containers — so AI agents can create scientific tool metadata, as well as consume it to compose and run pipelines reliably.
Goal 5 makes the Open Science Assistant (OSA) a deeper BIDS project by bringing BIDS data, the BIDS specification, validation results, and selected ecosystem tools into OSA through its existing YAML-driven tool/plugin architecture. It adds user feedback and reviewable agent activity for BIDS workflows. Goal 5 formalizes a study-state observability schema that records agent actions, supporting evidence, provenance, derivatives, and outstanding QC, so a dashboard or human reviewer can inspect what an agent did and why.

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

#### Goals, Outcomes, Milestones and Deliverables (up to 5 goals; NOT counted in the 750-word narrative limit)

Each goal has four fields per the Work Plan template (`docs/OS4LS_Work_Plan_template.pdf`): Goal / Outcome / Milestones & Deliverables (numbered X.Y with Year 1 / Year 2 tag) / Success indicators.

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

Outcome: Validation is a first-class, agent-callable operation: the Deno and Python validators consume the same schema and produce identical, machine-consumable verdicts; cross-standard validators (HED, NWB, Zarr / OME-Zarr) are integrated so a "deep-valid" verdict means valid across formats and sibling standards. The Zarr work includes a BIDS-aligned profile exercised on NEMAR conversion datasets.

Milestones & Deliverables:
2.1 Converge Deno and Python validators on the shared schema — identical CLI behavior and machine-readable output. [Year 1]
2.2 Publish the machine-consumable validation-record schema (JSON Schema + example datasets). [Year 1]
2.3 Integrate HED, NWB (via nwb-inspector), and Zarr / OME-Zarr cross-standard validation as pluggable checks, including a BIDS-aligned Zarr profile exercised on NEMAR conversion datasets. [Year 2]
2.4 Ship validators in Deno / npm / PyPI / conda-forge with reproducible container images. [Year 2]

Success indicators:
- Identical machine-readable output across Deno and Python validators on the reference test corpus [Year 2].
- ≥2 sibling standards (HED, NWB, OME-Zarr) integrated as pluggable checks [Year 2].
- Adoption by OpenNeuro deposit and ≥2 downstream pipelines (fMRIPrep, MRIQC, or QSIPrep) [Year 2].

---

**Goal 3: Python + CLI utilities with MCP interfaces and agent skills**

Outcome: LLM agents, CLI users, and Python users read, write, and reason about BIDS datasets through a stable, maintained interface — via pybids for structured queries and bids-utils for the smaller, agent- and CLI-friendly read/write/inspect verbs, plus MCP servers (including HED-MCP), a shared tool-interface contract, and reusable agent skills. Critically, the modernized PyBIDS query API will be semantically consistent and interpretable by both humans and agents, and backend-agnostic — decoupling querying logic from implementation so it can be reimplemented in other languages (e.g., Rust) while keeping that logic consistent and verifiable across backends. The same interfaces connect NEMAR's Zarr-backed, BIDS/HED-annotated data to GPU training and agent workflows, using the ongoing conversion test bed (>89% implemented: 760 datasets, 39,000 subjects, 57 TB).

Milestones & Deliverables:
3.1 Consolidate scattered helpers into `bids-standard/bids-utils` (release 0.1). [Year 1]
3.2 Publish MCP servers wrapping the BIDS schema, validation, and bids-utils, including HED-MCP; publish the shared tool-interface contract and agent skills (extending the current K-Dense-AI/scientific-agent-skills prototypes). [Year 1]
3.3 Maintain and modernize PyBIDS; align its Layout / query API with the schema 2.x release. [Years 1–2]
3.4 Connect NEMAR's Zarr-backed, BIDS/HED-annotated data to GPU training and agent workflows through the shared interfaces, using the ongoing conversion test bed (>89% implemented: 760 datasets, 39,000 subjects, 57 TB). [Year 2]
3.5 Ship stable, versioned Python and CLI API. [Year 2]

Success indicators:
- ≥3 downstream tools or agent workflows (fMRIPrep, brainlife, Nipoppy, KOSMOS-class agents) call the new MCP servers or agent skills [Year 2].
- bids-utils 1.0 release with public API stability policy. [Year 2]
- PyBIDS release supporting BIDS 2.0 schema and adopted by ≥3 downstream libraries [Year 2].
- Backend-agnostic query API validated by a reference reimplementation (e.g., Rust) producing verifiably identical query results. [Year 2]
- A NEMAR Zarr-backed, BIDS/HED-annotated dataset reaches a GPU training or agent workflow through the shared interfaces. [Year 2]

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
- Niwrap / Styx / Boutiques descriptors published for ≥3 new packages (in addition to current 11 packages covering 1k+ tools) [Year 2].

---

**Goal 5: Open Science Assistant (OSA) — deep BIDS integration + study-state observability**

Outcome: OSA is an extensible, community-facing AI-assistant platform. The funded BIDS work makes OSA able to use BIDS data, the BIDS specification, validation results, and selected ecosystem tools through its YAML-driven community registry and specialized tool/plugin architecture. OSA produces a common, human-readable and machine-consumable study-state record of agent actions, supporting evidence, provenance, derivatives, and outstanding QC.

Milestones & Deliverables:
5.1 Integrate BIDS data, the BIDS specification, validation results, and selected ecosystem tools into OSA through its existing YAML-driven community registry and specialized tool/plugin architecture. [Year 1]
5.2 Establish a user/agent feedback loop that documents where OSA succeeds or fails in BIDS workflows. [Year 1]
5.3 Publish study-state observability schema 1.0 (JSON Schema, examples, and implementation guidance) covering agent actions, supporting evidence, provenance, derivatives, and QC state. [Year 2]
5.4 Demonstrate consumption of observability records in a dashboard or human-reviewer workflow; incorporate the evaluation feedback into OSA. [Year 2]

Success indicators:
- OSA's BIDS assistant uses BIDS data, specification, validation, and selected ecosystem tools, with published evaluation cases and a release changelog covering the funded work [Year 2].
- Study-state observability schema 1.0 is released and consumed by at least one dashboard or human-reviewer workflow [Year 2].
- OSA evaluation feedback produces documented improvements to an OSA release [Year 2].
- Quantitative agent-task success rate reported for an evaluation suite of typical tasks on a BIDS dataset (baseline vs. MCP-server + agent-skills-enabled agent), demonstrating measurable improvement [Year 2].

### Optional Upload — PI/Co-PI biographies, references, figures (≤4 pages)

**External file(s):  [subs/biographies.md](subs/biographies.md)** (rendered to .pdf)

---

## Section 5 — Budget Description

### Amount Requested

Enter as whole numbers, USD, no commas / no dollar signs. Track 2 max:
$500,000 / year; $1,000,000 total. Numbers must match the Budget
Description (uploaded as PDF and/or XLSX).

1000000

### Budget Description (uploaded as PDF / XLSX)

**External file(s): [dartmouth/Budget_Narrative_v4.md](dartmouth/Budget_Narrative_v4.md)** (converted from/to .docx)

Stage: submitted to Dartmouth OSP for review.

### Recent Financial Support — max 1,500 characters

https://bids.neuroimaging.io/collaboration/acknowledgments.html lists various grants which supported work on parts of BIDS.
PI Halchenko is Co-PI/I on U.S. archives that underpin BIDS in production: DANDI (2020–2029, NIH R24MH117295, $6,500,256 for 2024-2026), OpenNeuro (see below), EMBER (2024-2029, NIH R24MH136632, $3,526,488 for 2024-2026), and the ReproNim (2016-2026, NIH NIBIB P41EB019936, $1,174,836 for 2025) all of which use and contribute to BIDS.
Co-PI Poldrack directs OpenNeuro (2018-2028, NIH BRAIN Initiative 5R24MH117179, $5,968,723 for 2023-2027).
Co-PI Shirazi is PI of the Meta BIDS/open-science gift (2025–2026, $130,000) and the AWS OSA Research Starter Fund (2026, $20,000), with BIDS-related work supported through NEMAR (NIH 2R24MH120037-06A1, 2026–2030, $4,845,051) and EEGLAB (NIH 2R01NS047293, 2023–2028, $2,589,740).
Co-PI Poline is PI of Canadian Institute of Health, CIHR PJT-197805, CAD204,000/year to partly support the Nipoppy/BIDS-Study.
Co-PI Pestilli is PI/Co-I on the BRAIN CONNECTS APEX (2024–2029, NIH, $9,485,000), the Center for Mesoscale Connectomics (2023–2028, NIH, $16,684,090), ezBIDS, NiiVue, and dcm2niix (2023–2026, NIH, $2,039,629), which use/develop BIDS spec and tools.
Key person Kiar leads Styx, NiWrap, BIDS2Table funded by NIH (1RF1MH130859-01, 2022–2026, $1,504,004; 1R01MH139565, 2025–2027, $889,582) alongside grants from Private Foundations ($16,300,000+ received from 2021–2027) which rely on BIDS.
Co-PI De La Vega is PI on (5R01MH096906; 2024–2030, NIH, $3,600,000), which supports related work on AI-assisted large-scale neuroimaging data analysis.
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
