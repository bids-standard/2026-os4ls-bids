Open Source for the Life Sciences (**OS4LS**)

**Proposal Title: BIDS 2.0+ ecosystem: AI-Ready Life-Science Data Standard**

**Applicant Name: Yaroslav Halchenko**

**Work plan** (max 750 words)

+----------------------------------------------------------------------------------------------------------------------------------+
| BIDS is a widely used open-source specification and tooling ecosystem for structured, machine- and human-legible organization of |
| life-science data, maintained by an international and multi-institution community of contributors and a public Steering and      |
| Maintenance Groups following established Governance procedures. This request supports a 24-month plan to integrate the BIDS      |
| ecosystem at the core of computational scientists' preferred harnesses, organized around the five coordinated goals below.      |
|                                                                                                                                  |
| **Goal 1** delivers the BIDS 2.0 release (more consistent, modular, schema-first) with a scoped 3.0 roadmap and hardens the      |
| machine-readable schema as a Data Structure Standard, landing the active BEP backlog to broaden BIDS beyond neuroimaging. This   |
| work spans bids-specification, bids-examples, bids-website, etc., tracked at                                                     |
| [[https://github.com/orgs/bids-standard/projects/10]{.underline}](https://github.com/orgs/bids-standard/projects/10).            |
|                                                                                                                                  |
| **Goal 2** continues the community-driven convergence of the Deno and Python validators on the shared schema, adds               |
| machine-consumable validation records, and integrates cross-standard checks (HED, NWB, Zarr) so that a "deep-valid" verdict    |
| means valid across included formats and standards which is critical for trustworthy AI results. This includes a BIDS-aligned     |
| Zarr profile exercised on the NEMAR conversion datasets.                                                                         |
|                                                                                                                                  |
| **Goal 3** consolidates scattered helpers (across bids2table, bids2nda, cubids, datalad-neuroimaging) into a maintained          |
| pybids-adjacent bids-utils library, exposes both via MCP servers including HED-MCP and a shared tool-interface contract, and     |
| packages reusable agent skills (currently prototyped in                                                                          |
| [[K-Dense-AI/scientific-agent-skills]{.underline}](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/bids)) |
| so LLM agents can read, write, and reason about BIDS datasets through a stable interface. It also connects NEMAR's Zarr-backed, |
| BIDS/HED-annotated data to GPU training and agent workflows, exercised on the ongoing conversion test bed (>89% implemented:    |
| 760 datasets, 39,000 subjects, 57 TB).                                                                                           |
|                                                                                                                                  |
| **Goal 4** modernizes the BIDS-Apps execution contract in coordination with the Boutiques / Niwrap / Styx descriptor stack and   |
| the BIDS-Apps registry, including GPU/accelerator containers, so AI agents can assemble scientific tool metadata, and consume it |
| to compose and run pipelines reliably.                                                                                           |
|                                                                                                                                  |
| **Goal 5** makes the Open Science Assistant (OSA) an overarching BIDS agent bringing BIDS data, the BIDS specification,          |
| validation results, and selected ecosystem tools into OSA. It adds user feedback and reviewable agent activity for BIDS          |
| workflows. Goal 5 formalizes a study-state observability schema that records agent actions, supporting evidence, provenance,     |
| derivatives, and outstanding QC, so a dashboard or human reviewer can inspect what an agent did and why.                         |
|                                                                                                                                  |
| Overall organization of work for Goals 2-5 will be organized and prioritized within projects like                                |
| [[https://github.com/orgs/bids-standard/projects/24]{.underline}](https://github.com/orgs/bids-standard/projects/24). Beyond the |
| requested funds, each institution contributes existing personnel time (uncompensated by this grant) where people already work on |
| BIDS in related projects but not directly toward the goals established in this grant proposal. The BIDS Steering and Maintainers |
| groups contribute governance capacity in kind. [[DANDI]{.underline}](https://dandiarchive.org) (Dartmouth) and                   |
| [[OpenNeuro]{.underline}](https://openneuro.org) (Stanford) contribute deposit-side validation feedback as new datasets will be  |
| flowing into those repositories. DANDI (via nwb2bids) will also contribute feedback on alignment to microscopy/extracellular     |
| electrophysiology with CatalystNeuro contributing tool integrations.                                                             |
|                                                                                                                                  |
| Community activities will include two annual BIDS meetings/hackathons organized by the PI & Project Manager (Kimberly Ray, UT    |
| Austin) targeting maintainers, downstream BIDS-App authors, and adjacent-standard maintainers (HED, NWB, Zarr). They will be     |
| organized following the pattern of prior successful BIDS Maintainer meetings we had in Copenhagen and Seattle. Exact venue yet   |
| to be decided, but likely to happen at Dartmouth and/or UT Texas Austin.                                                         |
|                                                                                                                                  |
| All materials (code, documentation, schema, etc) are to be released under OSI-Approved permissible licenses (e.g. CC-BY-4.0 /    |
| MIT / Apache-2.0), with releases published on GitHub and PyPI/conda-forge/npm as applicable.                                     |
|                                                                                                                                  |
| **Scalability and modular composition:** BIDS already operates at scale --- OpenNeuro hosts 1,500+ public datasets brainlife.io  |
| stores dozens of PB multimodal datasets from NIH BRAIN CONNECTS and DANDI stores multi-TB BIDS microscopy datasets. Its          |
| standardized subject/session hierarchy provides a natural unit of parallelization, enabling human workflows, HPC pipelines, and  |
| AI agents to scale without custom sharding logic.                                                                                |
|                                                                                                                                  |
| Composition works within a dataset (nested \`sourcedata/\`, raw, \`derivatives/\`) and across datasets via BIDS-Study,           |
| OpenNeuroStudies, and the Nipoppy study network, so summarization bubbles up cleanly through subject → study → cross-study →     |
| dashboard layers (brainlife, NeuroBagel/Nipoppy), thus also facilitating adherence to Self-containment and Modularity principles |
| of https://stamped-principles.org (developed by the PIs group).                                                                  |
|                                                                                                                                  |
| Goal 2's schema-driven validator convergence keeps validation cheap enough to run inside agent loops; Goal 4's                 |
| execution-spec + Boutiques / Niwrap / Styx path preserves this modularity when wrapping GPU / accelerator containers as BIDS     |
| Apps 2.0, so hardware-accelerated workloads inherit the same composition semantics as CPU pipelines.                             |
|                                                                                                                                  |
| **Sustainability**: Post-grant maintenance continues through the PI's and Co-PIs' involvement via the existing BIDS governance |
| and maintenance structure and adjacent federally-funded work (DANDI, OpenNeuro, EMBER, nipreps, brainlife.io, Nipoppy), all      |
| benefiting from the work done under this funding.                                                                                |
+==================================================================================================================================+

**Goals, Outcomes, Milestones and Deliverables** (up to 5 goals, not included in the 750-word limit)

+-----------------------------------------------------------------------+
| **Goal 1: Release BIDS 2.0 specification and schema**                 |
|                                                                       |
| **Outcome:** The BIDS 2.0 specification is released --- more          |
| consistent, modular, schema-first --- with hardened derivatives       |
| contracts (provenance, connectivity, stimuli), and the 3.0 roadmap is |
| scoped.\                                                              |
| Downstream tools (validators, PyBIDS, BIDS Apps) adopt the new schema |
| without loss, and the active BEP backlog (BEP028, BEP032, BEP036,     |
| BEP037, BEP044/047) is landed so BIDS covers phenotypes, animal /     |
| extracellular electrophysiology, NIBS, stimuli and A/V.               |
|                                                                       |
| **Milestones & Deliverables:**                                        |
|                                                                       |
| > **1.1** Prepare, finalize, merge and tag BIDS 2.0                   |
| > (\`bids-standard/bids-specification\` \`bids-2-devel\` branch →     |
| > main). \[Year 1\]                                                   |
| >                                                                     |
| > **1.2** Publish BIDS 3.0 roadmap document with community sign-off.  |
| > \[Year 2\]                                                          |
| >                                                                     |
| > **1.3** Land BEPs from the active queue (subset to be selected with |
| > Steering Group at kickoff; not blocked by BIDS 2.0 release per se). |
| > \[Years 1--2\]                                                      |
|                                                                       |
| **Success indicators:**                                               |
|                                                                       |
| - BIDS 2.0 tagged and adopted by ≥3 downstream tools (validators,     |
|   PyBIDS, ≥1 major BIDS App) \[Year 2\].                              |
|                                                                       |
| - ≥3 BEPs from the active queue merged. \[Year 2\]                    |
|                                                                       |
| - Schema 2.x+ release consumed by both validators and PyBIDS. \[Year  |
|   2\]                                                                 |
+=======================================================================+

+-----------------------------------------------------------------------+
| **Goal 2: Converge BIDS validators on machine-consumable records, and |
| cross-standard checks**                                               |
|                                                                       |
| **Outcome:** Validation is a first-class, agent-callable operation:   |
| the Deno and Python validators consume the same schema and produce    |
| identical, machine-consumable verdicts; cross-standard validators     |
| (HED, NWB, Zarr / OME-Zarr) are integrated so a "deep-valid"        |
| verdict means valid across formats and sibling standards. The Zarr    |
| work includes a BIDS-aligned profile exercised on NEMAR conversion    |
| datasets.                                                             |
|                                                                       |
| **Milestones & Deliverables:**                                        |
|                                                                       |
| > **2.1** Converge Deno and Python validators on the shared schema    |
| > --- identical CLI behavior and machine-readable output. \[Year 1\]  |
| >                                                                     |
| > **2.2** Publish the machine-consumable validation-record schema     |
| > (JSON Schema + example datasets). \[Year 1\]                        |
| >                                                                     |
| > **2.3** Integrate HED, NWB (via nwb-inspector), and Zarr / OME-Zarr |
| > cross-standard validation as pluggable checks, including a          |
| > BIDS-aligned Zarr profile exercised on NEMAR conversion datasets.   |
| > \[Year 2\]                                                          |
| >                                                                     |
| > **2.4** Ship validators in Deno / npm / PyPI / conda-forge with     |
| > reproducible container images. \[Year 2\]                           |
|                                                                       |
| **Success indicators:**                                               |
|                                                                       |
| - Identical machine-readable output across Deno and Python validators |
|   on the reference test corpus \[Year 2\].                            |
|                                                                       |
| - ≥2 sibling standards (HED, NWB, OME-Zarr) integrated as pluggable   |
|   checks \[Year 2\].                                                  |
|                                                                       |
| - Adoption by OpenNeuro deposit and ≥2 downstream pipelines           |
|   (fMRIPrep, MRIQC, or QSIPrep) \[Year 2\].                           |
+=======================================================================+

###

+-----------------------------------------------------------------------+
| **Goal 3: Provide Python + CLI utilities with MCP interfaces and      |
| agent skills**                                                        |
|                                                                       |
| **Outcome:** LLM agents, CLI users, and Python users read, write, and |
| reason about BIDS datasets through a stable, maintained interface --- |
| via pybids for structured queries and bids-utils for the smaller,     |
| agent- and CLI-friendly read/write/inspect verbs, plus MCP servers    |
| (including HED-MCP), a shared tool-interface contract, and reusable   |
| agent skills. Critically, the modernized PyBIDS query API will be     |
| semantically consistent and interpretable by both humans and agents,  |
| and backend-agnostic --- decoupling querying logic from               |
| implementation so it can be reimplemented in other languages (e.g.,   |
| Rust) while keeping that logic consistent and verifiable across       |
| backends. The same interfaces connect NEMAR's Zarr-backed,           |
| BIDS/HED-annotated data to GPU training and agent workflows, using    |
| the ongoing conversion test bed (>89% implemented: 760 datasets,     |
| 39,000 subjects, 57 TB).                                              |
|                                                                       |
| **Milestones & Deliverables:**                                        |
|                                                                       |
| > **3.1** Consolidate scattered helpers into                          |
| > \`bids-standard/bids-utils\` (release 0.1). \[Year 1\]              |
| >                                                                     |
| > **3.2** Publish MCP servers wrapping the BIDS schema, validation,   |
| > and bids-utils, including HED-MCP; publish the shared               |
| > tool-interface contract and agent skills (extending the current     |
| > K-Dense-AI/scientific-agent-skills prototypes). \[Year 1\]          |
| >                                                                     |
| > **3.3** Maintain and modernize PyBIDS; align its Layout / query API |
| > with the schema 2.x release. \[Years 1--2\]                         |
| >                                                                     |
| > **3.4** Connect NEMAR's Zarr-backed, BIDS/HED-annotated data to    |
| > GPU training and agent workflows through the shared interfaces,     |
| > using the ongoing conversion test bed (>89% implemented: 760       |
| > datasets, 39,000 subjects, 57 TB). \[Year 2\]                       |
| >                                                                     |
| > **3.5** Ship stable, versioned Python and CLI API. \[Year 2\]       |
|                                                                       |
| **Success indicators:**                                               |
|                                                                       |
| - ≥3 downstream tools or agent workflows (fMRIPrep, brainlife,        |
|   Nipoppy, KOSMOS-class agents) call the new MCP servers or agent     |
|   skills \[Year 2\].                                                  |
|                                                                       |
| - bids-utils 1.0 release with public API stability policy. \[Year 2\] |
|                                                                       |
| - PyBIDS release supporting BIDS 2.0 schema and adopted by ≥3         |
|   downstream libraries \[Year 2\].                                    |
|                                                                       |
| - Backend-agnostic query API validated by a reference                 |
|   reimplementation (e.g., Rust) producing verifiably identical query  |
|   results. \[Year 2\]                                                 |
|                                                                       |
| - A NEMAR Zarr-backed, BIDS/HED-annotated dataset reaches a GPU       |
|   training or agent workflow through the shared interfaces. \[Year    |
|   2\]                                                                 |
+=======================================================================+

###

+-----------------------------------------------------------------------+
| **Goal 4: Modernize execution contract through BIDS-Apps 2.0+ and     |
| make GPU-ready**                                                      |
|                                                                       |
| **Outcome:** Analysis tools wrap as Boutiques / Niwrap descriptors    |
| and run as BIDS Apps 2.0 --- including GPU / accelerator containers   |
| --- so AI agents can compose and run pipelines reliably.              |
|                                                                       |
| **Milestones & Deliverables:**                                        |
|                                                                       |
| > **4.1** Update the BIDS-Apps execution spec (BEP027) to align with  |
| > the latest Boutiques + Styx developments. \[Year 1\]                |
| >                                                                     |
| > **4.2** Publish reference implementation demonstrating a GPU /      |
| > accelerator container running as a BIDS App 2.0 (using an Allen     |
| > Institute / HuggingFace-model pipeline). \[Year 2\]                 |
| >                                                                     |
| > **4.3** Update BIDS-Apps registry (bids-apps.neuroimaging.io) to    |
| > surface BIDS-Apps 2.0 metadata. \[Year 2\]                          |
| >                                                                     |
| > **4.4** Integrate execution-spec self-description into              |
| > ///repronim/containers Singularity collection for reproducibility.  |
| > \[Year 2\]                                                          |
|                                                                       |
| **Success indicators:**                                               |
|                                                                       |
| - Execution-spec 2.x tagged and adopted by ≥3 BIDS Apps \[Year 2\].   |
|                                                                       |
| - ≥1 GPU / accelerator container demo in the registry \[Year 2\].     |
|                                                                       |
| - Niwrap / Styx / Boutiques descriptors published for ≥3 new packages |
|   (in addition to current 11 packages covering 1k+ tools) \[Year 2\]. |
+=======================================================================+

###

+-----------------------------------------------------------------------+
| **Goal 5: Provide Open Science Assistant (OSA) with deep BIDS         |
| integration + study-state observability**                             |
|                                                                       |
| **Outcome:** OSA is an extensible, community-facing AI-assistant      |
| platform. The funded BIDS work makes OSA able to use BIDS data, the   |
| BIDS specification, validation results, and selected ecosystem tools  |
| through its YAML-driven community registry and specialized            |
| tool/plugin architecture. OSA produces a common, human-readable and   |
| machine-consumable study-state record of agent actions, supporting    |
| evidence, provenance, derivatives, and outstanding QC.                |
|                                                                       |
| **Milestones & Deliverables:**                                        |
|                                                                       |
| > **5.1** Integrate BIDS data, the BIDS specification, validation     |
| > results, and selected ecosystem tools into OSA through its existing |
| > YAML-driven community registry and specialized tool/plugin          |
| > architecture. \[Year 1\]                                            |
| >                                                                     |
| > **5.2** Establish a user/agent feedback loop that documents where   |
| > OSA succeeds or fails in BIDS workflows. \[Year 1\]                 |
| >                                                                     |
| > **5.3** Publish study-state observability schema 1.0 (JSON Schema,  |
| > examples, and implementation guidance) covering agent actions,      |
| > supporting evidence, provenance, derivatives, and QC state. \[Year  |
| > 2\]                                                                 |
| >                                                                     |
| > **5.4** Demonstrate consumption of observability records in a       |
| > dashboard or human-reviewer workflow; incorporate the evaluation    |
| > feedback into OSA. \[Year 2\]                                       |
|                                                                       |
| **Success indicators:**                                               |
|                                                                       |
| - OSA's BIDS assistant uses BIDS data, specification, validation,    |
|   and selected ecosystem tools, with published evaluation cases and a |
|   release changelog covering the funded work \[Year 2\].              |
|                                                                       |
| - Study-state observability schema 1.0 is released and consumed by at |
|   least one dashboard or human-reviewer workflow \[Year 2\].          |
|                                                                       |
| - OSA evaluation feedback produces documented improvements to an OSA  |
|   release \[Year 2\].                                                 |
|                                                                       |
| - Quantitative agent-task success rate reported for an evaluation     |
|   suite of typical tasks on a BIDS dataset (baseline vs. MCP-server + |
|   agent-skills-enabled agent), demonstrating measurable improvement   |
|   \[Year 2\].                                                         |
+=======================================================================+
