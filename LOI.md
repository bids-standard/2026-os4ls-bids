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
  - Role on BIDS: Emeritus Steering Group member; core contributor to BIDS specification, bids-examples, bids-validator, pybids, bids-utils; initiator and lead of BIDS-Study, and BIDS 2.0 working group; lead of DataLad, ReproIn, ReproNim/containers; Co-PI and Co-I on National data archives using BIDS: DANDI, OpenNeuro, EMBER
  - Email: yaroslav.o.halchenko@dartmouth.edu
- **Host / fiscal sponsor:** Trustees of Dartmouth College — institutionally agreed to **10% indirect cost rate** (matching the RFA cap), and will issue subawards to the collaborating institutions
- **Co-PIs and key collaborating maintainers (representing core BIDS community buy-in):**
  - Chris Markiewicz — Stanford (BIDS Maintainer 'in charge', BEP043, bids-validator, pybids, nipreps)
  - Jean-Baptiste Poline — McGill PI (current Steering Group; Boutiques/Nipoppy)
  - Russell Poldrack — Stanford PI (BIDS co-founder; Emeritus Steering Group; bids-validator, OpenNeuro)
  - Seyed Yahya Shirazi — UCSD PI (BIDS Maintainer; BEP042/BEP044; HED; OSA — Open Science Assistant)
  - Oscar Esteban — Lausanne University Hospital / EPFL PI (nipreps; AI-assisted pipelines)
  - Gregory Kiar — Child Mind Institute PI (Niwrap, Styx, Boutiques)
  - Alejandro de la Vega — UT Austin PI (pybids, fitlins)
  - Cody Baker — Dartmouth/CatalystNeuro (BEP032, NWB ↔ BIDS interoperability, `*`omics scoping)
  - Franco Pestilli - UT Austin PI (current Steering Group; connectomics, brainlife)
  - Kimberly Ray - UT Austin PI (BIDS Maintainer; facilitates Steering Group meetings) to provide "Project Manager" role to orchestrate activities
  

---

## Form fields (with character limits)

### Proposal Title — *60 characters max*

**Candidate (50 chars):**

> BIDS 2.0+: AI-Ready Life Sciences Data Standard

---

### Short Summary — *3,000 characters max*

**BIDS (Brain Imaging Data Structure)** is the community-driven, openly governed standard that organizes scientific datasets to be unambiguously consumed by Human Intelligence (HI), conventional pipelines, and AI agents.
Since 2016, BIDS has grown from MRI-only to 10+ biological measurement and stimulation technologies (MRI, EEG/MEG/iEEG, PET, NIRS, microscopy, motion, MRS, physiological, behavioral, NIBS), with 1,500+ public datasets on OpenNeuro and multi-TB microscopy on DANDI.
Dozens of BIDS Apps (fMRIPrep, MRIQC, QSIPrep) consume it; thousands of papers cite it.
Active BEPs (BEP028 provenance; BEP036 phenotypes; BEP037 NIBS; BEP044/047 stimuli & A/V; BEP032 animal/extracellular) and `*`omics-archive dialogues pull BIDS into adjacent domains.

This proposal supports the **coordinated evolution of the BIDS ecosystem into a natively AI-ready standard**, on the premise that *what is good for HI is good for AI — only AI benefits even more from explicit structure*.
We will advance five tightly coupled components whose maintainers have collectively committed:

1. **BIDS specification & schema** — release BIDS 2.0 (more consistent, modular), scope the 3.0 roadmap, harden the machine-readable schema as a *Data Structure Standard*, and land the BEP backlog to broaden BIDS beyond neuro;
2. **BIDS validators** — **community-driven convergence** of implementations on the schema, machine-consumable records, and integration of cross-standard validators (HED, NWB, Zarr) — critical for trustworthy AI results;
3. **Python + CLI utilities with MCP interfaces and skills** — consolidate scattered, in-use helpers into a maintained, pybids-adjacent query/manipulation library, exposed via MCP servers and reusable agent skills so LLM agents can read, write, and reason about BIDS datasets;
4. **BIDS-Apps 2.0+** — on the mature BIDS-Apps registry (50+ apps) and Boutiques, modernize the contract between BIDS data and analysis containers (via Niwrap and the BIDS-Apps 2.0 execution spec) so AI agents can compose and run pipelines reliably — including GPU/accelerator containers (BEP032 Allen Institute + HuggingFace);
5. **BIDS Users Assistant** — extend OSA with deep BIDS awareness, and formalize a *study-state* observability layer so dashboards and human reviewers can introspect AI agents' actions.

**Together, these five close the loop for AI-enabled, large-scale data analysis** by formalizing the data and application contracts agentic workflows and training pipelines need.

The work is **explicitly modular** — each component delivers standalone value; advance in any one lifts every downstream tool. Funds support hackathons, conference travel, and **dedicated cross-project coordination (PM + maintainer support) as enabling infrastructure for BIDS 2.0**.
**Scope guard:** no new datasets (beyond examples), no new ML models, **no archive/repository infrastructure** — only the standard, the tools, and the AI-readiness layer the rest of the life sciences can adopt.

---

### Expected Value — *1,500 characters max*

**Capabilities unlocked.** By month 24, any life-sciences researcher *or* LLM agent will be able to:

(i) check whether a dataset is BIDS "deep-valid" against every format and sibling standard (HED, NWB, OME-Zarr) — **verdict consumed identically by agents, pipelines, and humans** (not deposit-pipeline tooling);

(ii) query and manipulate it via maintained CLI, Python API, and MCP servers, plus a collection of domain-specialized SKILLs;

(iii) wrap any analysis tool as a Boutiques/Niwrap descriptor and run it as a BIDS App 2.0 — including GPU/accelerator containers — directly or via an agent;

(iv) introspect provenance, derivatives state, and outstanding QC through a common observability schema regardless of who acted;

(v) get human- and agent-readable explanations and guidance through the OSA AI assistant.

**Upstream impact.** A versioned schema-first specification with machine-readable extension points unlocks BEPs in `*`omics-linked phenotypes, animal behavior, stimuli, and audio/video — pulling new life-sciences communities into BIDS.

**Downstream impact.** Every BIDS App, every OpenNeuro dataset (and soon DANDI via nwb2bids), every nipreps pipeline, brainlife/Nipoppy dashboard, and every emerging AI agent (KOSMOS-style, OSA, custom MCP clients) inherits cleaner inputs, stricter validation, and well-defined endpoints.

**The same investment that makes BIDS easier for humans makes it more usable for AI** — and exposes a template other life-science standards can mirror.

---

### Landscape Analysis — *1,500 characters max*

BIDS is the near-monopoly *organization* standard across neuroscience, biomedical imaging, and adjacent life-science subfields: OpenNeuro (1,500+ datasets), DANDI (1,000+ joining BIDS), EU/HBP, NIH BRAIN, ABCD, UK Biobank derivatives, and major pipelines (fMRIPrep, QSIPrep, etc) consume or produce BIDS.
**No peer exists at the data-organization layer**, proprietary or open: vendor formats (BrainVision, CTF, Plexon) and DICOM are *inputs* BIDS ingests and organizes. At the analysis layer, **Boutiques / Niwrap / Styx** is the leading open descriptor stack with no true peer; commercial alternatives (Flywheel, QMENTA) are closed-source and BIDS-consuming.
Adjacent open standards — **NWB**, **NIfTI**, **HED**, **Zarr/OME-Zarr** — are *integrated* into BIDS; this proposal invests in interoperability, not re-implementation. **BEP43 + Boutiques descriptors map legacy (AFNI, FreeSurfer) and HPC (parquet, zarr) outputs into BIDS** — across legacy tooling and accelerator storage.

**AI use.** BIDS is the de-facto input contract for AI in this field: ML training pipelines (ABCD, UK Biobank, BIDS-Brain-Score), foundation-model efforts (KOSMOS, BrainLM), and AI assistants like **OSA** rely on BIDS layout to make data legible.
Yet the BIDS 1.x series evolved with validators, APIs, and pipeline descriptors designed for human authors; the major 2.0 (and queued 3.0) revisions are required to raise consistency — gaps this proposal closes.

---

### Software Projects to be Supported — *up to 5*

A tricky part since only up to 5 so we need to either choose or somehow bundle . Submission form has

Software Project Name * 30 characters maximum
Software Project's Repository URL *
Software Project's Website URL

1. **BIDS spec, schema, schematools**
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

- **Neuroscience**
- **Biological and biomedical imaging**
- **Data formats and storage**

others considered

- **Platforms interoperability**
- **Agentic frameworks**
- **Software ecosystem infrastructure**

---

### Funding Track

- [x] **Track 2 — Foundational Libraries and Ecosystem Initiatives** (up to $1,000,000 / 24 months)
- [ ] Track 1 — Domain-specific Tools

---

### Statement of PI Involvement

The PI (Yaroslav Halchenko) is an Emeritus member of the BIDS Steering Group and a long-standing core contributor across the BIDS specification and ecosystem at large. He is a Co-PI or Co-I on a number of national US data archives (DANDI, OpenNeuro, EMBER) which facilitate archival of data in BIDS standard. He will be responsible to direct the work under this funding. PIs work will be done in coordination with Co-PIs subcontracted at a number of other sites, as BIDS is a global decentralized project at large: Poldrack, Poline, Ray, Esteban, and we have prior rich history of collaboration and joint funded work (e.g. PI Halchenko is currently Co-PI or Co-I with Poldrack and Poline on a number of federally funded grants).

**Governance roles.** Current **BIDS Steering Group** members among the named team are co-PIs **Poline** (McGill) and **Pestilli** (UT Austin). Emeritus Steering members: PI Halchenko and co-PI Poldrack. Current **BIDS Maintainers**: **Markiewicz** (Stanford, "in charge"), and co-PIs **Shirazi** (UCSD) and **Ray** (UT Austin, who also facilitates Steering Group meetings). The PI leads the published roadmap (`bids-standard/bids-2-devel` and the BIDS 2.0 Project).

**Funder lineage.** Multiple BIDS-adjacent projects that consume BIDS were CZI EOSS grantees: **MNE-Python** (Cycle 2), **Nilearn** (Cycle 5, PI Poline), **NiPreps/fMRIPrep** (Cycle 5, PI Esteban), **NeuroDesk** (Cycle 6). **Two of those EOSS PIs (Poline, Esteban) are co-PIs on this proposal** — direct continuity from EOSS into the OS4LS successor program. In 2023 the BIDS Steering Group received **The Neuro – Irv and Helga Cooper Foundation Open Science International Prize** for *"longstanding community-driven approach to standardizing neuroimaging data"*; the PI is one of five named recipients (with Rokem, Pernet, Niso, Oostenveld).

**HPC and accelerated workloads.** The PI engages with the HPC container community (e.g., virtual meetings of the "HPC Containers Advisory Council") to keep BIDS-related design choices coordinated with the HPC and accelerator-container ecosystem that runs BIDS workloads at scale. He also maintains the sunset archive of the singularity-hub.org portal, and the ///repronim/containers DataLad dataset/collection of BIDS-Apps Singularity containers which are widely used in the ecosystem to guarantee reuse, availability, and reproducibility of BIDS derivatives.

**Coordination as enabling infrastructure.** The PI is actively engaged across the active BEP queue to varying degrees — BEP028 (provenance), BEP036 (phenotypes), BEP037 (NIBS), BEP044/047 (stimuli, A/V), and BEP032 (animal/extracellular electrophysiology) — and together with collaborating contributor **Cody Baker** (Dartmouth) initiated the ongoing dialogues with `*`omics archives that are extending BIDS into adjacent life-science domains. This PI-plus-maintainer pattern scales only with dedicated coordination capacity, which this proposal funds via **Kim Ray** (UT Austin / BIDS Maintainer) as Project Manager — operational infrastructure for cross-WG/BEP synchronization and downstream-tool coordination, yoked to the five technical pillars throughout.

The proposed work has been discussed and endorsed by the BIDS Steering Group, and with the involved maintainers, and is *aligned with the published BIDS roadmap*: BIDS 2.0 (bids-standard/bids-2-devel), the active BEP queue, and the bids-standard validator convergence effort. All proposed activities track the existing community roadmap; new community contributions during the grant may extend it but not redirect it.

**Sustainability.** Post-grant maintenance will continue through PI and Co-PIs involvement through existing governance and maintenance structure and their involvement in BIDS related projects. Track 2 fits perfectly since the work bridges many related projects in the same ecosystem, where PI and Co-PIs participate and the integration story across spec → validators → utilities → apps → assistant and AI agentic systems at large is the value, which Track 1's single-tool grain would lose.

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
  - Open BIDS Steering Group, published BEP process, public roadmap (`bids-standard/bids-2-devel`), documented contributor guide, active CI across all five named projects

- **Feasibility**
  - Co-Is are the actual maintainers of the named projects
  - Every named workstream is already in motion; this funding closes a known resourcing gap rather than starting from zero

- **Value of proposed work**
  - One investment lifts every downstream user — humans, conventional pipelines, and AI agents simultaneously
  - Enables BIDS adoption in adjacent life-science domains (phenotypic, behavioral, `*`omics-linked, audio/video)


---

## Open items before submission

- [x] **Fiscal sponsor decided: Dartmouth College.** Dartmouth has agreed to cap indirect costs at 10% (matching the RFA limit) and will issue subawards to all collaborating institutions. An external fiscal sponsor (e.g., INCF, Code for Science & Society) remains a theoretical fallback if Dartmouth's machinery proves too slow for the June 8 LOI / July 21 full-app timeline, but the short runway makes switching unlikely to be feasible. *Driver:* the RFA (p.5) requires that "one individual must complete the application and a single organization or fiscal sponsor must coordinate the dispersal of funds" for Track 2 multi-project proposals.
- [x] **Title chosen:** *"BIDS 2.0+: AI-Ready Life Sciences Data Standard"* (47 chars).
- [x] **Categories chosen:** Neuroscience / Biological and biomedical imaging / Data formats and storage.
- [ ] Steering Group formal sign-off email thread (already in progress per the email Message-ID `<agscKEH3Tceh4Ei2@bilena>`).

---

## Remaining responsiveness items (for follow-up before submission)

Items deferred from the OS4LS responsiveness review; none block the current draft but each can lift the LOI further.

### Verifications

- [x] **Cooper Foundation Prize wording — VERIFIED** (2026-06-04). Awarded to the **BIDS Steering Group** (organizational entity; McGill's press release styles it "Steering Committee" but the BIDS-internal official term is "Steering Group"), 2023, by The Neuro at McGill. Exact citation: *"for its longstanding community-driven approach to standardizing neuroimaging data, resulting in widespread adoption."* Five named team members: Rokem (U.Washington), Pernet (Copenhagen), Niso (Cajal Institute), Halchenko (Dartmouth), Oostenveld (Donders). Press release: https://www.mcgill.ca/neuro/article/rewarding-excellence-open-science. *Updated in PI Involvement.*
- [x] **EOSS-funded BIDS-adjacent projects — VERIFIED** (2026-06-04) with exact cycle numbers: **MNE-Python** Cycle 2; **Nilearn** Cycle 5 (PI: Poline / McGill); **NiPreps/fMRIPrep** Cycle 5 (PI: Esteban / Lausanne); **NeuroDesk** Cycle 6 (co-funded with Wellcome Trust). **Bonus signal: two of those EOSS PIs (Poline, Esteban) are co-PIs on this LOI** — direct EOSS-to-OS4LS continuity. *Updated in PI Involvement.*
- [~] **HPC Containers Advisory Council attribution — UNVERIFIABLE** (restricted Google Doc). Softened in PI Involvement to "HPC container community (e.g., the annual HPC Container Workshop at ISC)" — the HPC Container Workshop at ISC (container-in-hpc.org) is the public, verifiable analog. If the original council is documented somewhere I can cite, update with the precise name; otherwise the current softened wording is the safer claim.
- [ ] **Categories — alternative swap to consider.** The current three (Neuroscience / Biological and biomedical imaging / Data formats and storage) anchor BIDS in its origin community. If the form offers it, consider swapping **Neuroscience** → **Platforms interoperability** or **Agentic frameworks** — both map directly to RFA-named priority bullets and amplify the AI-native pitch. Decision deferred until portal opens and actual category list is visible.
- [ ] **PI Involvement char limit.** Current PI Involvement is ~2,500 chars. RFA does not document a limit; check the Fillout form when the portal opens — if there's a cap, the EOSS/Cooper Prize / HPC-Council / Sustainability / Track-2-fit additions can be tightened or moved to the full application.

### PR #2 review-derived items (from co-PI reviewers)

- [x] **Kim Ray (kimberlylray) — community coordination as enabling infrastructure** — *addressed.* Summary now ends with "Funds support annual hackathons, conference travel, and **dedicated cross-project coordination (PM + maintainer support) as enabling infrastructure for BIDS 2.0**." PI Involvement adds a "Coordination as enabling infrastructure" paragraph naming Kim Ray as Project Manager and positioning the work as *operational infrastructure that directly enables delivery*, yoked to the five technical pillars (so the RFA's "general maintenance" exclusion does not apply).
- [ ] **arokem + yarikoptic — TRX (tractography file format) mention** (PR comment #3306796129 + #3344236981). Reference: https://tee-ar-ex.github.io/. Could add to Landscape "Adjacent open standards" list as **TRX** (tractography). Cost: ~25 chars; Landscape has 3 chars headroom — would require trimming elsewhere.
- [x] **effigies — BEP43 + Boutiques for legacy/heterogeneous outputs** — *addressed.* Landscape Analysis now includes "**BEP43 + Boutiques descriptors map legacy outputs (AFNI, FreeSurfer) and HPC formats (parquet, zarr) into BIDS** — extending it across legacy tool output and accelerator-friendly storage." Placed in Landscape rather than Summary because it lives more naturally next to the adjacent-standards/interoperability framing, and Landscape had the headroom after the no-peer consolidation.
- [x] **adelavega — fitlins/bids-stats-models scope decision** — *decision: stays dropped from form fields* (matches adelavega's "leave it out" recommendation; fitlins still appears once in Landscape as a pipeline example to demonstrate ecosystem breadth). The fuller "dive deeper" option is preserved as a possible focus for the full application if reviewers ask.
- [x] **arokem — "modalities" jargon** (PR comment #3306778021) — *addressed.* Summary now reads "10+ **biological measurement and stimulation technologies**" (covers BEP037 NIBS — non-invasive brain stimulation — which extends BIDS beyond pure measurement into stimulation/intervention). BEP037 also added to the active BEP list, and the Coordination paragraph in PI Involvement now enumerates the BEP queue to reinforce the scope-expansion → coordination-need argument.
- [x] **arokem — close-the-loop / "horizontal" → "modular" / Cooper Prize-style positive framing.** Addressed in current draft.
- [x] **Dora Hermes (dorahermes) — won't need support.** Already removed from co-PI list per commit b959de0.

### Info-session-derived items (from the 2026-05-29 OS4LS info session — RFA-OS4LS.pdf + transcript + slides 833/1000)

- [x] **R1 — Track-2 "single-domain bundling" misread risk** — *addressed.* Dario noted (~24:00 in transcript) that proposals representing "coordination between tightly aligned projects within the same domain" may be bumped from Track 2 to Track 1. Defense: Landscape opening now reads "BIDS is the near-monopoly *organization* standard **across neuroscience, biomedical imaging, and adjacent life-science subfields**" — broadening from the prior "neuroscience and broader biomedical imaging" framing. Combined with the "biological measurement and stimulation technologies" + BEP037 NIBS additions from earlier rounds, the cross-domain Track-2 scope is now explicit.
- [x] **R2 — Validators misread as "data-prep before repository deposit"** — *addressed.* Dario flagged (~39:17) that "preparation, curation, publication of metadata associated with data repository" is out of scope. Defense: Expected Value (i) now reads "verdict consumed identically by agents, pipelines, and humans **(not deposit-pipeline tooling)**" — explicit anti-misread inside the form text itself.
- [x] **R3 — Schema convergence misread as "AI-assisted rewrite of legacy tool"** — *addressed.* Dario clarified (~10:45) that AI-assisted rewrites are in scope only when "from the same maintainer community." Defense: Pillar 2 now reads "**community-driven convergence** of implementations on the schema" — explicit qualifier defusing the rewrite-of-niche-tool reading.
- [x] **EOSS in-flight claim — CORRECTED** (2026-06-05). My earlier "remain in flight" framing was inaccurate: per CZI's published cycle dates, Cycles 2 (~2020) and 5 (Nov 2022, 2-yr term) have concluded, and Cycle 6 (Jun 2024, 2-yr term) is concluding right around the 2026-06 LOI deadline. PI Involvement now uses cycle dates and 2-yr term language without making in-flight claims, and adds the verified 2025-transition-year fact from Dario at ~58:00 of the info session.
- [x] **PI %FTE flexibility** — *addressed.* Per Megan Mitch at ~49:18, the call does not require a specific PI %FTE; funds can go fully to non-PI personnel. PI Involvement now records this with a "Personnel allocation" paragraph stating the PI's planned ~5% FTE and that the majority of funds support co-Is, maintainers, and the Project Manager.
- [ ] **"Combining overlapping proposals" is welcomed** (Dario, ~57:08). No action needed — validates our 5-pillar bundling without further change.
- [ ] **UX / user-centered design is in scope** (Dario, ~54:00). Could be leaned into for the OSA UX work in the *full application*; LOI is fine.

### Strengtheners (would lift "Existing impact" and "Quality" scores)

- [ ] **Concrete numbers.** Replace "dozens", "thousands", "300+" placeholders with verifiable counts before the full application:
  - bids-specification repo: contributor count, merged PRs in last 12 months
  - BIDS-Apps registry: app count (currently estimated "50+")
  - fMRIPrep + MRIQC + QSIPrep citation counts (Google Scholar / OpenAlex)
  - OpenNeuro dataset count (currently "1,500+")
- [x] **Governance specificity** — *addressed and corrected (2026-06-05).* PI Involvement "Governance roles" paragraph now names verified Steering Group members (co-PIs Poline, Pestilli as current; PI Halchenko + co-PI Poldrack as Emeritus) and current Maintainers (Markiewicz "in charge", co-PIs Shirazi and Ray; Ray also facilitates Steering Group meetings). Prior wording (which had Poldrack as current and Ray as Steering) was wrong per verification against https://bids.neuroimaging.io/collaboration/governance.html.
- [x] **Landscape — explicit "no peer" at organization layer** — *addressed.* Landscape now opens its 2nd paragraph with "**No peer exists at the data-organization layer**, proprietary or open" and folds the analysis-layer Boutiques/Niwrap/Styx no-peer claim into the same sentence for a louder unified statement.

### Pre-paste hygiene (before pasting any field into the Fillout form)

- [ ] **Strip internal-only sections.** "Mapping of proposed work → RFA priority bullets", "Mapping of proposed work → OS4LS review criteria", "Open items before submission", and this "Remaining responsiveness items" section are working notes — none belong in the form.
- [ ] **Strip the email Message-ID** (`<agscKEH3Tceh4Ei2@bilena>`) from any text pasted externally.
- [ ] **Project 1 form name typo.** Line 107 has `**BIDS spec, schema, schematools"` (mismatched bold/quote delimiters in this markdown file). The form-field text to paste is the plain string `BIDS spec, schema, schematools` (30 chars).
- [ ] **Markdown rendering check.** The Fillout form is likely a plain textarea — bold (`**...**`), italics, and `\`backticks\`` will render as raw characters. Decide which fields to strip formatting on (Short Summary and Expected Value will look noisy with raw asterisks).
- [ ] **`*`omics escapes.** `\`*\`omics` is markdown-safe in this file but pastes as backtick-asterisk-backtick into a textarea. Replace with plain `*omics` or `multi-omics` for portal paste.
