# OS4LS Full Application — BIDS 2.0+ Ecosystem

- Funding opportunity: Open Source for the Life Sciences (OS4LS), Open Source for Science Fund / Renaissance Philanthropy
- Track: Track 2 — Foundational Libraries and Ecosystem Initiatives
- Funding ceiling: up to $1,000,000 USD total / 24 months (max $500,000 USD/year)
- Full Application due: 2026-07-21, 2 pm PDT / 9 pm UTC
- Project start date: 2026-12-01
- Project end date: 2028-11-30

Structure of this document mirrors the Full Application Instructions
(`docs/Full-Application-Instructions_-OS4LS.pdf`, June 2026). Each field
below is annotated with its character/word limit as documented there.
Fields pre-filled from the LOI are marked `[pre-filled from LOI [x]]`.
Text intended for direct paste into the Fillout portal is kept
plain (no markdown emphasis) so it renders identically in a plain
textarea. Auxiliary strategy / internal-review material lives in
`LOI-MISC.md`; short PI / Co-PI biosketches for the optional 4-page
supporting-documentation PDF live under `subs/`.

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
| Alejandro de la Vega | aleph4@gmail.com | The University of Texas at Austin | USA | Co-PI (PyBIDS, fitlins) |
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

Note: additional McGill personnel (Julia, Rémi, Michelle/Nikhil, Christine)
and Stanford’s Jeanette Mumford (fitlins) are indicated in the
sub-award planning worksheet
(`gdrive/2026-os4ls-bids_subawards_and_consultants.tsv`) and may be
added here while subaward paperwork is being finalized.

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
collaborating institutions.

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
- Metrics (fill verified whole numbers before submit; TODO):
  - https://bids.neuroimaging.io/impact/index.html collects various stats
  - Monthly users estimate: TBD (spec readers via Read the Docs analytics)
  - Dependent projects/packages: TBD (BIDS Apps registry ≈50+, plus validators, PyBIDS, bids2nda, brainlife/Nipoppy, etc.)
  - Scholarly citations estimate: TBD (Gorgolewski 2016 + BEP-cited papers — fetch from Google Scholar / OpenAlex)

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
- Metrics (TODO — verified whole numbers): TODO https://github.com/bids-standard/bids-validator/issues/431
  - Monthly users estimate: TBD
  - Dependent projects/packages: TBD
  - Scholarly citations estimate: TBD

---

**Project 3 — PyBIDS + bids-utils** (30 chars: `PyBIDS + bids-utils`)

- Repository URL: https://github.com/bids-standard/pybids
- Website URL: https://bids-standard.github.io/pybids/
- Short description (max 500 chars): TEXT

  PyBIDS is the reference Python library for querying and manipulating BIDS
  datasets — used by fMRIPrep, MRIQC, QSIPrep, fitlins, and most downstream
  BIDS Apps. This proposal maintains PyBIDS and consolidates scattered
  ecosystem helpers into a maintained, pybids-adjacent bids-utils (under the
  same organization) library exposed via MCP servers and reusable agent
  skills, so LLM agents can read, write, and reason about BIDS datasets through
  a stable interface.

- Software license: Apache-2.0 (PyBIDS and bids-utils)
- Main programming language: Python
- Canonical citation: Yarkoni T, et al. (2019). "PyBIDS: Python tools for
  BIDS datasets." Journal of Open Source Software 4(40), 1294.
  https://doi.org/10.21105/joss.01294
- Code of Conduct: https://github.com/bids-standard/.github/blob/main/CODE_OF_CONDUCT.md
- End-user documentation: https://bids-standard.github.io/pybids/
- Contributor / developer guidelines: https://github.com/bids-standard/.github/blob/main/CONTRIBUTING.md
- Package manager entry: PyPI `pybids`; conda-forge `pybids`
- Community / Q&A forum: https://neurostars.org/tag/pybids
- Metrics (TODO):
  - Monthly users estimate: TBD (PyPI downloads/month via pypistats)
  - Dependent projects/packages: TBD (libraries.io / pypistats reverse deps)
  - Scholarly citations estimate: TBD (Yarkoni 2019)

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

  BIDS Apps are containerized analysis tools that consume BIDS input
  and emit BIDS derivatives; the registry lists ≈50+ apps
  (fMRIPrep, MRIQC, QSIPrep, etc.). This proposal modernizes the
  contract between BIDS data and analysis containers via the
  execution-spec (BEP027/BEP043) and the Boutiques / Niwrap / Styx
  descriptor stack — so agents can compose and run pipelines
  reliably, including GPU / accelerator containers (Allen Institute,
  HuggingFace-model workloads).

- Software license: MIT / Apache-2.0 (across the stack)
- Main programming language: Python (Boutiques, Niwrap, Styx); shell (container recipes)
- Canonical citation: Gorgolewski KJ, et al. (2017). "BIDS apps:
  Improving ease of use, accessibility, and reproducibility of
  neuroimaging data analysis methods." PLOS Computational Biology
  13(3): e1005209. https://doi.org/10.1371/journal.pcbi.1005209
- Code of Conduct: per project (bids-standard org / boutiques org / childmindresearch org)
- End-user documentation: https://bids-apps.neuroimaging.io/
- Contributor / developer guidelines: per project (see repos)
- Package manager entry: PyPI `boutiques`, `niwrap`, `styx` (as applicable)
- Community / Q&A forum: https://neurostars.org/tag/bids-apps
- Metrics (TODO):
  - Monthly users estimate: TBD
  - Dependent projects/packages: TBD
  - Scholarly citations estimate: TBD

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

Since 2016, BIDS has grown from MRI-only to 10+ biological measurement and stimulation technologies (MRI, EEG/MEG/iEEG, PET, NIRS,
microscopy, motion, MRS, physiological, behavioral, NIBS), with 1,500+ public datasets on OpenNeuro and multi-TB microscopy on DANDI.
Dozens of BIDS Apps (fMRIPrep, MRIQC, QSIPrep) consume it; thousands of papers cite it.
Active BEPs (BEP028 provenance; BEP036 phenotypes; BEP037 NIBS; BEP044/047 stimuli & A/V; BEP032 animal/extracellular) and *omics-archive dialogues pull BIDS into adjacent domains.

This proposal — a Track 2 ecosystem initiative — supports the coordinated evolution of the BIDS ecosystem into a natively AI-ready standard, on the premise that what is good for HI is good for AI — only AI benefits more from explicit structure.
We will advance five coordinated components, whose maintainers have collectively committed:

1. BIDS specification & schema — release BIDS 2.0 (more consistent, modular), scope the 3.0 roadmap, harden the machine-readable schema as a Data Structure Standard, and land the BEP backlog to broaden BIDS beyond neuro.

2. BIDS validators — community-driven convergence of implementations on the schema, machine-consumable records, and integration of cross-standard validators (HED, NWB, Zarr) — critical for trustworthy AI results.

3. Python + CLI utilities with MCP interfaces and skills — consolidate scattered, in-use helpers into a maintained, pybids-adjacent query/manipulation library, exposed via MCP servers and reusable agent skills so LLM agents can read, write, and reason about BIDS datasets.

4. BIDS-Apps 2.0+ — on the mature BIDS-Apps registry and Boutiques, modernize the contract between BIDS data and analysis containers (via Niwrap and the BIDS-Apps 2.0 execution spec) so AI agents can compose and run pipelines reliably — including GPU/accelerator containers.

5. BIDS Users Assistant — extend OSA with deep BIDS awareness, and formalize a study-state observability layer so dashboards and human reviewers can introspect AI agents' actions.

Together, these five close the loop for AI-enabled, large-scale data analysis by formalizing the data and application contracts agentic workflows and training pipelines need.

The work is explicitly modular — each component delivers standalone value; advance in any one lifts every downstream tool.
Outputs: enhanced spec, validator, new MCP-server, BIDS-Apps 2.0 contract, observability schema releases — coordinated by PM and via community hackathons.
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

Downstream impact. Every BIDS App, every OpenNeuro dataset (and soon DANDI via nwb2bids), every nipreps pipeline, brainlife/Nipoppy dashboard, and every emerging AI agent (KOSMOS-style, OSA, custom MCP clients) inherits cleaner inputs, stricter validation, and well-defined endpoints.

The same investment that makes BIDS easier for humans makes it more usable for AI — and exposes a template other life-science standards can mirror.

### Landscape Analysis [pre-filled from LOI [x]] — max 1,500 characters

<!-- Seeded verbatim from LOI.md — might need tune ups -->

BIDS is the near-monopoly organization standard in neuroimaging, expanding into adjacent life-science subfields: OpenNeuro (1,500+ datasets), DANDI (1,000+ joining BIDS), ABCD, UK Biobank derivatives, and major pipelines (fMRIPrep, QSIPrep, etc) consume or produce BIDS.
BIDS received the 2023 Neuro – Cooper Foundation Open Science International Prize. Two co-PIs (Poline, Esteban) led CZI EOSS-funded BIDS-adjacent projects (Nilearn, NiPreps).

No peer exists at the data-organization layer, proprietary or open: vendor formats (BrainVision, CTF) and DICOM are inputs BIDS ingests and organizes. At the analysis layer, Boutiques / Niwrap / Styx is the leading open descriptor stack with no true peer; commercial alternatives (Flywheel, QMENTA) are closed-source.
Adjacent open standards — NWB, NIfTI, HED, Zarr/OME-Zarr — are integrated into BIDS; this proposal invests in interoperability, not re-implementation. BEP43 + Boutiques descriptors map legacy (AFNI, FreeSurfer) and HPC outputs into BIDS.

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

BIDS (Brain Imaging Data Structure) is a widely used open-source specification and tooling ecosystem for structured, machine- and human-legible organization of life-science data, maintained by a international and multi-institution community of contributors and a public Steering and Maintainenance Groups following established Governance procedures.
This request supports a 24-month, multi-institution effort to carry the BIDS ecosystem across the "always 1.x" to the more consistent and AI-ready state, organized around the five coordinated goals below.
All work is inside our published roadmap: 

Goal 1 corresponds to addressing issues (primarily within bids-specification itself but also in related bids-examples, bids-website, pybids, and so on) assigned to BIDS 2.0 milestones tracked at https://github.com/orgs/bids-standard/projects/10;
Goal 2 continues the validator-convergence work already underway between the Deno and Python implementations; 
Goal 3 packages helpers that have accumulated across pybids, bids2nda, and DataLad into a maintained pybids-adjacent library plus MCP servers and reusable agent skills (currently prototyped in K-Dense-AI/scientific-agent-skills);
Goal 4 continues the BEP027/BEP043 execution-spec work in coordination with Boutiques / Niwrap / Styx and the BIDS-Apps registry;
and Goal 5 continues OSA's BIDS extension and formalizes a study-state observability layer used today in an ad-hoc form by brainlife.io and Nipoppy dashboards.

Overall organization of work for Goals 2-5 will be organized and prioritized within projects like https://github.com/orgs/bids-standard/projects/24 project.
Beyond the requested funds, each institution contributes existing personnel time (uncompensated by this grant) where people already work on BIDS in related projects but not directly toward the goals established in this grant proposal.
The BIDS Steering Group and the Maintainers organization contribute governance capacity in kind.
DANDI (Dartmouth) and OpenNeuro (Stanford) contribute deposit-side validation feedback as new datasets will be flowing into those repositories.
DANDI (via nwb2bids) will also contribute feedback on alignment to microscopy / extracellular electrophysiology with CatalystNeuro contributing NeuroConv and NWB Inspector integration.
Community activities include two annual BIDS hackathons / sprints organized by the PI & Project Manager (Kimberly Ray, UT Austin) — targeting maintainers, downstream BIDS-App authors, and adjacent-standard maintainers (HED, NWB, Zarr).
All code is developed in the open under OSI-Approved licenses (e.g. CC-BY-4.0 (specification text) / MIT / Apache-2.0 (tooling)), with releases published on GitHub and PyPI/conda-forge/npm as applicable.

Scalability and modular composition:
BIDS already operates at scale — OpenNeuro hosts 1,500+ public datasets and DANDI stores multi-TB BIDS microscopy dataset — because the standard's per-subject and per-session structure is the natural parallelization boundary: pipelines can run near-embarrassingly-parallel per subject/session without per-tool sharding logic.
Composition works within a dataset (nested `sourcedata/`, raw, `derivatives/`) and across datasets via BIDS-Study, OpenNeuroStudies, and the Nipoppy study network, so summarization bubbles up cleanly through subject → study → cross-study → dashboard layers (brainlife, Nipoppy), thus also fascilitating adherence to Self-containment and Modularity principles of https://stamped-principles.org (developed by the PIs group).
Goal 2's schema-driven validator convergence keeps validation cheap enough to run inside agent loops; Goal 4's execution-spec + Boutiques / Niwrap / Styx path preserves this modularity when wrapping GPU / accelerator containers as BIDS Apps 2.0, so hardware-accelerated workloads inherit the same composition semantics as CPU pipelines.

Sustainability:
Post-grant maintenance continues through the PI's and Co-PIs' involvement via the existing BIDS governance and maintenance structure and adjacent federally-funded work (DANDI, OpenNeuro, EMBER, nipreps, brainlife, Nipoppy), all benefiting from the work done under this funding.

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

Outcome: The BIDS 2.0 specification is released — more consistent, modular, schema-first — and the 3.0 roadmap is scoped.
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

**External file(s): [dartmouth/Budget_Narrative_v2.md](dartmouth/Budget_Narrative_v2.md)** (converted from/to .docx}

Stage: submitted to Dartmouth OSP for review.

### Recent Financial Support — max 1,500 characters

List active and recently completed grants (calendar years 2025 and
2026) plus in-kind support that the PI and Co-PIs have received to
directly or indirectly support this work — with duration, total USD
(for grants), and funding source.

TEXT (draft — collect from each Co-PI at kickoff and tighten to ≤1,500
chars before paste):

TODOs: verify, extend and add total amounts!

PI Halchenko is Co-I / Co-PI on federally funded U.S. archives that underpin BIDS in production: DANDI (2020–2029, NIH R24MH117295, $6,500,256 for 2024-2026), OpenNeuro (see details in Poldrack), EMBER (2024-2029, NIH R24MH136632, $3,526,488 for 2024-2026), and the ReproNim center work (2016-2026, NIH NIBIB P41EB019936, $1,174,836 for 2025) all of which use BIDS and contribute necessary developments to it.
Co-PI Poldrack directs OpenNeuro (2018-2028, NIH BRAIN Initiative 5R24MH117179, $5,968,723 for 2023-2027).
Co-PI Poline was CZI EOSS Cycle 5 PI for Nilearn (2022-2024).
Co-PI Esteban was CZI EOSS Cycle 5 PI for NiPreps / fMRIPrep (2022-2024).
Co-PI Pestilli leads NSF- and NIH-funded brainlife.io connectivity work (BRAIN CONNECTS).
Co-PI Shirazi maintains OSA and HED-related work at UCSD's Swartz Center.
Co-PI Rokem holds CAMH- and NIH-funded dMRI/TRX work.
Co-PI Dichter leads CatalystNeuro's NWB and NeuroConv work supported by the NIH BRAIN Initiative.
In-kind: existing maintainer time from the BIDS Steering Group and Maintainers; Amazon Open Dataset program hosts TBs of OpenNeuro and DANDI BIDS datasets (guestimate of 700k$/year cost for both store/egress).

TODO: verify exact grant numbers / durations / totals with each Co-PI before submission. Ensure ≤1,500 chars.

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

- Strip this section, `LOI-MISC.md` "Open items" content, all
  Message-IDs, and any markdown emphasis / backticks before pasting
  into the Fillout form.
- Verified vs. TODO status:
  - Personnel table Section 1 — Co-PI names verified against LOI &
    subawards TSV; emails from TSV.
  - Impact metrics under each software project — mostly TODO
    (need verified whole numbers before submit).
  - Recent Financial Support — draft only; verify with each Co-PI.
  - Budget subtotal $540 over cap — reconcile at Dartmouth line.
  - EIN / signing official / financial contact — obtain from
    Dartmouth OSP;
