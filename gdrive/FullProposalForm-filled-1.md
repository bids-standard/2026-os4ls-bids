### **Please review your submission.**

##### Update any relevant information as needed.

Edit

First Name

Yaroslav

Last Name

Halchenko

Email

yoh@dartmouth.edu

Applicant Organizational or Institutional Affiliation

Dartmouth College, USA

Country of Residence

United States

Have you ever received funding as a grantee under the CZI EOSS program?

No

Proposal Team

Record chosen

Edit

Organization Name

Trustees of Dartmouth College

Street Address

11 Rope Ferry Road, #6210

City

Hanover

State / Province

NH

Country

United States

Organization Website

https://www.dartmouth.edu/\~osp

Organization Tax ID

02-0222111

Organization Type

Academic Institution

First Name

Stephanie

Last Name

Morgan

Email

sponsored.projects@dartmouth.edu

First Name

Colleen

Last Name

Sullivan

Email

sponsored.projects@dartmouth.edu

First Name

Shelagh

Last Name

Eastridge

Email

sponsored.projects@dartmouth.edu

Organizational Approval and Sign Off Form

Organizational-Approval-and-Sign-off-Form_Signed.pdf

Edit

Proposal Title

BIDS 2.0+ ecosystem: AI-Ready Life-Science Data Standard

Proposal Purpose

BIDS 2.0 spanning spec, validators, PyBIDS, BIDS-Apps, Assistant: closing spec-consistency gaps for humans and machines, adding AI-agent interfaces (MCP, skills), broadening across life sciences.

Funding Track

Track 2: Foundational Libraries and Ecosystem Initiatives

Software Projects to be Supported

Record chosen

Categories

Data formats and storage, Biological and biomedical imaging, Neuroscience

Edit

Short Summary

BIDS (Brain Imaging Data Structure) is the community-driven, openly governed standard that organizes scientific datasets to be unambiguously consumed by Human Intelligence (HI), conventional pipelines, and AI agents.
Since 2016, BIDS has grown from MRI-only to 10+ biological measurement and stimulation technologies (MRI, EEG/MEG, PET, microscopy, motion, MRS, and others), with 1,500+ public datasets on OpenNeuro and multi-TB microscopy on DANDI.
Dozens of BIDS Apps (fMRIPrep, MRIQC, QSIPrep) consume it; thousands of papers cite it.
Active BIDS Extension Proposals (BEPs) --- for provenance, phenotypes, non-invasive brain stimulation, stimuli & A/V, animal / extracellular electrophysiology --- and *omics-archive dialogues pull BIDS into adjacent domains.
BIDS is a very open, wide ecosystem project spanning far more than the five software projects explicitly listed here: \~30 repositories under github.com/bids-standard plus adjacent tooling and data archives (OpenNeuro, DANDI) are anchored on the BIDS specification.
Years of practice have established a community-driven model where component authors lead their work while a public Steering Group and Maintainers coordinate under established (but evolving) governance principles (https://bids.neuroimaging.io/collaboration/governance.html).
This explains the higher-than-typical Co-PI count: each Co-PI is an existing lead or maintainer for one or more components, jointly responsible for coordinated delivery.
Altogether, this proposal supports the coordinated evolution of the BIDS ecosystem into a natively AI-ready standard, on the premise that what is good for HI is good for AI.
We advance five coordinated components (fully detailed in the Work Plan section), whose maintainers have collectively committed: (1) BIDS specification & schema --- release BIDS 2.0 and land the BEP backlog; (2) validators --- Deno/Python convergence with machine-consumable records and integrated cross-standard checks (HED, NWB, Zarr); (3) Python + CLI utilities exposed via MCP servers and reusable agent skills; (4) BIDS-Apps 2.0+ execution contract for reproducible pipelines including GPU / accelerator containers; (5) OSA: deep BIDS integration + study-state observability.
Together, these five coordinated components close the gap between HI and AI by formalizing the data and application contracts needed for collaborative, AI-enabled, large-scale scientific analysis.
Outputs: enhanced spec, validators, MCP servers + agent skills, BIDS-Apps 2.0 contract, and OSA + observability releases --- coordinated by the Project Manager and community hackathons.
Scope guard: no new datasets (beyond examples), no new ML models, no archive/repository infrastructure --- only the standard, the tools, and the AI-readiness layer the rest of the life sciences can adopt.

Expected Value

Capabilities unlocked: By month 24, any life-sciences researcher or LLM agent can: (i) check whether a dataset is BIDS "deep-valid" against every format and sibling standard (HED, NWB, OME-Zarr) --- verdict consumed identically by agents, pipelines, and humans (not deposit-pipeline tooling); (ii) query and manipulate it via maintained CLI, Python API, and MCP servers, plus a collection of domain-specialized SKILLs; (iii) wrap any analysis tool as a Boutiques/Niwrap descriptor and run it as a BIDS App 2.0 --- including GPU/accelerator containers --- directly or via an agent; (iv) introspect provenance, derivatives state, and outstanding QC through a common observability schema regardless of who acted; (v) get human- and agent-readable explanations and guidance through the OSA AI assistant.
Upstream impact.
A versioned schema-first specification with machine-readable extension points unlocks BEPs in *omics-linked phenotypes, animal behavior, stimuli, and audio/video --- pulling new life-sciences communities into BIDS.
Downstream impact.
Every BIDS App, every OpenNeuro and most brainlife.io datasets (and soon DANDI via nwb2bids), every nipreps pipeline, the brainlife/Nipoppy dashboards, and every emerging AI agent (KOSMOS-style, OSA, custom MCP clients) inherits cleaner inputs, stricter validation, and well-defined endpoints.
The same investment that makes BIDS easier for humans makes it more usable for AI, and exposes a template other life-science standards can mirror.

Landscape Analysis

BIDS is the most widely adopted standard in neuroimaging, expanding into adjacent life-science subfields: OpenNeuro (1,500+ datasets), DANDI (1,000+ joining BIDS), ABCD, UK Biobank derivatives, and major pipelines (fMRIPrep, QSIPrep, etc) consume or produce BIDS.
BIDS received the 2023 Neuro -- Cooper Foundation Open Science International Prize.
A co-PI (Poline) led Nilearn's CZI EOSS-funded BIDS-adjacent project.
No peer exists at the data-organization layer, proprietary or open: vendor formats (BrainVision, CTF) and DICOM are inputs BIDS ingests and organizes.
At the analysis layer, Boutiques / Niwrap / Styx is the leading open descriptor stack with no true peer; commercial alternatives (Flywheel, QMENTA) are closed-source.
Adjacent open standards --- NWB, NIfTI, HED, Zarr/OME-Zarr --- are integrated into BIDS.
This proposal improves internal consistency of the standard and its interfaces to tools and AI.
BEP43 + Boutiques descriptors map legacy (AFNI, FreeSurfer) and HPC outputs into BIDS.
BIDS is the de-facto input contract for AI: ML training pipelines and AI benchmarks (ABCD, UK Biobank, EEG2025 (NeurIPS, 1,100 teams)), AI "scientist" frameworks (KOSMOS, K-Dense-AI, Meta NeuroAI), and AI assistants like OSA benefit from BIDS to make data legible.
Yet the BIDS 1.x series evolved with validators, APIs, and pipeline descriptors designed for human authors; the major 2.0 (and queued 3.0) revisions are required to raise consistency for AI use which we want to tackle with this proposal.

Work Plan and Milestones/Deliverables

BIDS2.0+\_OS4LS_WorkPlan.pdf

Optional Upload

biographies.pdf

Edit

Amount for Year 1 (including up to 10% indirect costs)

500000

Amount for Year 2 (including up to 10% indirect costs)

500000

Total Amount

1000000

Budget Description

Budget_Narrative_v4.pdf

Recent Financial Support

Halchenko is Co-PI/I on U.S. archives that underpin BIDS in production: DANDI (2020--2029, NIH R24MH117295, \$6,500,256 for 2024-2026), EMBER (2024-2029, NIH R24MH136632, \$3,526,488 for 2024-2026), and the ReproNim (2016-2026, NIH NIBIB P41EB019936, \$1,174,836 for 2025) all of which use and contribute to BIDS.
Poldrack directs OpenNeuro (2018-2028, NIH BRAIN Initiative 5R24MH117179, \$5,968,723 for 2023-2027).
Shirazi is PI of the Meta BIDS/open-science gift (2025--2026, \$130,000) and the AWS OSA Research Starter Fund (2026, \$20,000), with BIDS-related work supported through NEMAR (NIH 2R24MH120037-06A1, 2026--2030, \$4,845,051) and EEGLAB (NIH 2R01NS047293, 2023--2028, \$2,589,740).
Poline is PI of Canadian Institute of Health, CIHR PJT-197805, CAD204,000/year to partly support the Nipoppy/BIDS-Study.
Pestilli is PI/Co-I on the BRAIN CONNECTS APEX (2024--2029, NIH, \$9,485,000), the Center for Mesoscale Connectomics (2023--2028, NIH, \$16,684,090), ezBIDS, NiiVue, and dcm2niix (2023--2026, NIH, \$2,039,629), which use/develop BIDS spec and tools.
Kiar leads Styx, NiWrap, BIDS2Table funded by NIH (1RF1MH130859-01, 2022--2026, \$1,504,004; 1R01MH139565, 2025--2027, \$889,582) which rely on BIDS.
De La Vega is PI on (5R01MH096906; 2024--2030, NIH, \$3,600,000), supporting work on AI-assisted large-scale neuroimaging data analysis.
In-kind: Amazon Open Dataset program hosts over 1 PB of OpenNeuro and DANDI BIDS datasets (\~700k\$/year cost for both store/egress).

[← Back]{.mark}

> Save and Continue
