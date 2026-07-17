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
| work spans bids-specification, bids-examples, bids-website, pybids, etc., tracked at                                             |
| [[https://github.com/orgs/bids-standard/projects/10]{.underline}](https://github.com/orgs/bids-standard/projects/10).            |
|                                                                                                                                  |
| **Goal 2** continues the community-driven convergence of the Deno and Python validators on the shared schema, adds               |
| machine-consumable validation records, and integrates cross-standard checks (HED, NWB, Zarr) so that a "deep-valid" verdict    |
| means valid across formats and sibling standards which is critical for trustworthy AI results. This includes a BIDS-aligned Zarr |
| profile exercised on the NEMAR conversion datasets.                                                                              |
|                                                                                                                                  |
| **Goal 3** consolidates scattered helpers (across bids2table, bids2nda, cubids, datalad-neuroimaging, pybids) into a maintained  |
| pybids-adjacent bids-utils library, exposes both via MCP servers including HED-MCP and a shared tool-interface contract, and     |
| packages reusable agent skills (currently prototyped in                                                                          |
| [[K-Dense-AI/scientific-agent-skills]{.underline}](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/bids)) |
| so LLM agents can read, write, and reason about BIDS datasets through a stable interface. It also connects NEMAR's Zarr-backed, |
| BIDS/HED-annotated data to GPU training and agent workflows, exercised on the ongoing conversion test bed (>89% implemented:    |
| 760 datasets, 39,000 subjects, 57 TB).                                                                                           |
|                                                                                                                                  |
| **Goal 4** modernizes the BIDS-Apps execution contract (BEP027/BEP043) in coordination with the Boutiques / Niwrap / Styx        |
| descriptor stack and the BIDS-Apps registry --- including GPU/accelerator containers --- so AI agents can create scientific tool |
| metadata, as well as consume it to compose and run pipelines reliably.                                                           |
|                                                                                                                                  |
| **Goal 5** makes the Open Science Assistant (OSA) a deeper BIDS project by bringing BIDS data, the BIDS specification,           |
| validation results, and selected ecosystem tools into OSA through its existing YAML-driven tool/plugin architecture. It adds     |
| user feedback and reviewable agent activity for BIDS workflows. Goal 5 formalizes a study-state observability schema that        |
| records agent actions, supporting evidence, provenance, derivatives, and outstanding QC, so a dashboard or human reviewer can    |
| inspect what an agent did and why.                                                                                               |
|                                                                                                                                  |
| Overall organization of work for Goals 2-5 will be organized and prioritized within projects like                                |
| [[https://github.com/orgs/bids-standard/projects/24]{.underline}](https://github.com/orgs/bids-standard/projects/24). Beyond the |
| requested funds, each institution contributes existing personnel time (uncompensated by this grant) where people already work on |
| BIDS in related projects but not directly toward the goals established in this grant proposal. The BIDS Steering Group and the   |
| Maintainers organization contribute governance capacity in kind. [[DANDI]{.underline}](https://dandiarchive.org) (Dartmouth) and |
| [[OpenNeuro]{.underline}](https://openneuro.org) (Stanford) contribute deposit-side validation feedback as new datasets will be  |
| flowing into those repositories. DANDI (via nwb2bids) will also contribute feedback on alignment to microscopy / extracellular   |
| electrophysiology with CatalystNeuro contributing NeuroConv and NWB Inspector integration. Community activities include two      |
| annual BIDS hackathons / sprints organized by the PI & Project Manager (Kimberly Ray, UT Austin) --- targeting maintainers,      |
| downstream BIDS-App authors, and adjacent-standard maintainers (HED, NWB, Zarr). All code is developed in the open under         |
| OSI-Approved licenses (e.g. CC-BY-4.0 (specification text) / MIT / Apache-2.0 (tooling)), with releases published on GitHub and  |
| PyPI/conda-forge/npm as applicable.                                                                                              |
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
| **EXAMPLE**                                                           |
|                                                                       |
| **Goal 1: Interoperability with community standards**                 |
|                                                                       |
| **Outcome:** Users move data between \[project name\] and the rest of |
| their ecosystem without lossy, manual format conversion, so it fits   |
| cleanly into standard analysis workflows.                             |
|                                                                       |
| **Milestones & Deliverables:**                                        |
|                                                                       |
| > **1.1** Add native read/write support for the community-standard    |
| > data format(s). \[Year 1\]                                          |
| >                                                                     |
| > **1.2** Produce migration guidance and interactive notebooks        |
| > demonstrating interoperability. \[Year 1\]                          |
|                                                                       |
| **Success indicators:**                                               |
|                                                                       |
| - Native support for \[standard format\] released and validated       |
|   against reference datasets. \[Year 2\]                              |
|                                                                       |
| - \[N\] tutorials or notebooks published and adopted in community     |
|   training. \[Year 2\]                                                |
+=======================================================================+

+-----------------------------------------------------------------------+
| **EXAMPLE**                                                           |
|                                                                       |
| **Goal 2: AI-native, agent-callable interfaces**                      |
|                                                                       |
| **Outcome:** \[project name\] becomes a composable building block     |
| that automated pipelines and AI agents can call directly through a    |
| stable interface.                                                     |
|                                                                       |
| **Milestones & Deliverables:**                                        |
|                                                                       |
| > **2.1** Define and document a stable programmatic interface         |
| > covering core operations. \[Year 1\]                                |
| >                                                                     |
| > **2.2** Release stable version of agent-callable endpoints. \[Year  |
| > 1\]                                                                 |
|                                                                       |
| **Success indicators:**                                               |
|                                                                       |
| - At least \[N\] downstream tools or pipelines adopt the new          |
|   interface \[Year 2\].                                               |
+=======================================================================+

###

### How to use this Work Plan template

This template helps you describe how you will structure the work if your proposal is funded.
The shaded boxes with a coral edge are illustrative examples only: replace them with your own content.
Do not feel bound by the examples; they show the level of detail we are looking for, not a required topic or format.

### Work Plan 

Provide a narrative description of the proposed work for which funding is being requested, including resources you will contribute that are not part of the requested funding.
For software development work (engineering, product design, user research), explain how it fits into your existing project roadmap.
For community activities (sprints, training), describe how they will be organized, the target audience, and the expected outcomes.
You will summarize the goals, outcomes, and deliverables in the section below.

### Goals, Outcomes, Milestones and Deliverables 

Break the work into up to five goals.
For each goal, complete the four fields described below.
The examples that follow show how two goals might be written for a typical project.

> **Goal:** a short description of what this workstream aims to achieve.
>
> **Outcome:** a plain-language description of the main outcome for your target audience.
> What changes for them once every milestone and deliverable under this goal is met?
>
> **Milestones & Deliverables:** short descriptions of the key milestones or deliverables that support the goal, numbered (1.1, 1.2, and so on), and the expected completion date (Year 1 or Year 2).
>
> **Success indicators:** qualitative indicators or quantitative targets that will tell you whether you are making progress toward the expected outcome.

**Now complete your own work plan.** Replace the two examples above with your own goals (up to five), following the same four-field structure.

+-----------------------------------------------------------------------+
| ### How to submit                                                     |
|                                                                       |
| - Create a copy of this template                                      |
|                                                                       |
| - Fill in your **name** and the **full application title** (matching  |
|   information provided in the form)                                   |
|                                                                       |
| - Save this template as a PDF and upload it in the application form   |
+=======================================================================+
