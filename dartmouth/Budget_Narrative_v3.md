**Budget Description**

**Budget Narrative**

**PERSONNEL**

[Yaroslav O. Halchenko, Principal Investigator]{.underline}, will provide overall project leadership and coordinate the work across the institutions supporting the five components of BIDS 2.0+ project (specification & schema; validators; Python/CLI utilities with MCP servers and agent skills; BIDS-Apps 2.0 execution contract; and the BIDS Users Assistant with a study-state observability layer).
His direct technical contributions include BIDS specification and schema, consolidation of scattered ecosystem helpers into a maintained PyBIDS-adjacent bids-utils library, extension of the BIDS agent-skills prototype currently developed at K-Dense-AI (scientific-agent-skills) into a reusable production skill set, and integration of the BIDS-Apps 2.0 execution specification with the ///repronim/containers reproducibility infrastructure.
He will also coordinate BIDS 2.0+ integration with adjacent federally funded archives and infrastructures on which he works (DANDI, OpenNeuro, EMBER, ReproNim), and ensure that they would align with AI-assisted analytics (via DANDI's Neurosift agents or the BIDS Users Assistant developed in this effort).

[Cody Baker, Research Software Engineer, Key Personnel]{.underline} will contribute to landing the BEP032 revision (animal / extracellular electrophysiology), ensuring BIDS 2.0+ readiness of the NWB<->BIDS bridge (nwb2bids), support for BIDS Motion+Pose estimation tracking refinements, and scoping of *omics-relevant extensions that widen BIDS coverage beyond neuroimaging.
He will work in close coordination with CatalystNeuro (NeuroConv, NWB Inspector) and DANDI so that NWB-native datasets can be exposed as BIDS 2.0-valid datasets, and that agentic pipelines (via Neurosift and DANDI compute) benefit from BIDS Apps 2.0 specifications and interfaces.

**SUPPLIES**

Supplies include LLM API credits (for developing, evaluating, and running the BIDS agent skills, the BIDS-aware Open Science Assistant, and CI-integrated agent-evaluation harnesses), coding-assistant and tooling subscriptions used across the maintainer team, and some storage and cloud resources for container-registry and reference-dataset hosting.
AI credits and related infrastructure are also budgeted at partner sites where the work is site-specific (notably UCSD for HED-MCP / OSA / NEMAR compute, and McGill for local AI-model subscriptions); Dartmouth retains an additional reserve here to respond flexibly to the rapidly evolving AI-tooling ecosystem over the two-year performance period (e.g., new model providers, agentic runtimes, MCP servers) without renegotiating subawards.

**TRAVEL**

Travel funds are included to support approximately 20-25 participants of a BIDS Hackathon (AKA BIDS Community Meetings) each year.
These figures are guesstimates based on prior BIDS in-person gatherings (two hackathons held in Copenhagen, one in Seattle, and additional maintainer sprints elsewhere), where actual attendance ranged in the same order.
Because the annual BIDS hackathons and sprints intentionally draw the wider BIDS contributor and maintainer community, these travel funds cover not only the personnel named in this proposal but also active BIDS steering and maintainer teams, BEP leads, and other contributors who are not directly funded by this award, yet whose participation remains essential to the specification, validator, and downstream-tool convergence work.
Site-specific travel is also already included in the per-site budgets below (Stanford, UT Austin, McGill, UCSD, CatalystNeuro); the Dartmouth line therefore provides the shared community-travel fund on top of those, so that attendance of those participants can be supported without individually negotiating a subaward for each attendee.

Some additional funds are also included to support some representation at project-related meetings and to present results at professional conferences such as the Organization for Human Brain Mapping (OHBM) Annual Meeting or other relevant events.
Travel costs include transportation, lodging, meals, and other allowable travel expenses in accordance with standard college travel policies.

**MEETINGS/HACKATHONS/SPRINTS**

Funding to support Hackathon venue costs each year has been included, covering two annual BIDS hackathons / sprints, coordinated by the Project Manager (Kimberly Ray, UT Austin).
Costs may include venue rental expenses and food for participants.

**CONSULTANTS**

Two consulting arrangements are budgeted through Dartmouth to engage Key Personnel whose contributions to the BIDS ecosystem are essential to the proposed work but do not require a full subaward.

***[Child Mind Institute --- Gregory Kiar and team]{.underline}***

> [Gregory Kiar, Key Personnel]{.underline}, will lead the Child Mind Institute team's contributions to the BIDS-Apps 2.0 execution specification (BEP027), the Niwrap and Styx tool-interface descriptors that let AI agents compose and run pipelines reliably, and the bids2table dataset-loading tool --- expanding it to fully support the BIDS 2.0 schema and to track future schema versions dynamically, with validation-on-load semantics that complement the reference validators.
> Current team contributors under his direction include Florian Rupprecht and Jason Kai.
> Consulting fees are budgeted at \$4,000/year to Dr. Kiar, and a travel pool of \$11,000/year supports attendance of 2-3 Child Mind Institute contributors at the annual BIDS Hackathons and community meetings.

***[HES-SO Valais-Wallis (Lausanne) --- Oscar Esteban]{.underline}***

> [Oscar Esteban, Key Personnel]{.underline}, will contribute to provenance modelling and QA/QC annotations for BIDS derivatives (with reference implementations drawing from the NiPreps ecosystem), the query and manipulation layer via MCP servers and agent Skills, RAG/Wiki retrieval over the BIDS specifications, the fit+transform execution model and autonomous-workflow patterns, and OSA integration --- in coordination with UCSD (Dr. Shirazi).
> Consulting fees are budgeted at \$11,000/year to Dr. Esteban, and \$4,000/year of travel funds support his attendance at BIDS community meetings and one project-related conference per year.

**SUBCONTRACTS**

***[Stanford University]{.underline}***

> **PERSONNEL**
>
> [Russell A. Poldrack, Co-PI]{.underline}, will provide strategic scientific leadership as a BIDS co-founder and Emeritus member of the BIDS Steering Group, and as director of OpenNeuro.
> He will ensure alignment of the proposed work with the BIDS community's governance and long-term goals, and ground the specification, validation, and derivatives work in the operational needs of the world's largest BIDS-native deposit archive.
> He will direct the work of the Stanford-based BIDS Key Personnel listed below.
>
> [Chris Markiewicz, Research Scholar, Key Personnel]{.underline}, will provide technical leadership across the BIDS 2.0 specification, the schema-based validator (the Deno/TypeScript reference implementation), Python validator, and PyBIDS.
> As the BIDS Maintainer-in-charge, he will drive convergence between the Deno and Python validator implementations, lead the machine-consumable validation-record schema, and shepherd BIDS Extension Proposals through Steering Group review (including BEP043).
>
> [Nell Hardcastle, Software Developer, Key Personnel]{.underline}, will contribute to developing and testing the schema-based validator for the new standard, with particular focus on deposit-side validation on OpenNeuro --- so that BIDS 2.0 lands in the community's principal deposit workflow to OpenNeuro.
>
> [Ross Blair, Software Developer, Key Personnel]{.underline}, will contribute to developing and testing the schema-based validator for the BIDS 2.0 enhancements to the standard, with particular focus on the shared BIDS schema tooling, the reference test corpus underpinning cross-implementation convergence, and the machine-readable validator output consumed by downstream pipelines and AI agents.
>
> **TRAVEL**
>
> To support the research of the project, the team is requesting travel to support Chris Markiewicz, Nell Hardcastle, and Ross Blair at BIDS community hackathons, and conferences (OHBM or similar).
>
> **INDIRECTS**
>
> Stanford University has included indirect costs calculated on their total direct costs using 10% approved rate for the Open Source for the Life Sciences.

***[University of Texas at Austin]{.underline}***

> **PERSONNEL**
>
> [Franco Pestilli, Co-PI]{.underline}, will provide scientific leadership for the development of BIDS standards supporting structural connectivity and BRAIN CONNECTS.
> As a current member of the BIDS Steering Group, he will lead the development of BIDS Extension Proposals (BEPs) related to structural connectivity, contribute machine-readable metadata standards, and oversee the development of AI-ready infrastructure, including Model Context Protocol (MCP) servers that enable AI agents to discover, access, and interact with BIDS-compliant datasets.
> He will also develop interoperable APIs and BIDS-compliant computational pipelines that support agent-enabled scientific workflows, advancing BIDS as foundational infrastructure for AI-enabled neuroscience.
>
> [Kimberly Ray, Co-PI]{.underline}, will provide scientific infrastructure leadership for BIDS 2.0+, leading the development of the governance, operational, and ecosystem infrastructure required to support the long-term sustainability and evolution of the BIDS standard.
> She is currently a BIDS maintainer and will coordinate scientific activities across the BIDS Steering Group, Maintainers, and Working Groups to ensure alignment of technical roadmaps, standards development, and community priorities.
> Dr. Ray will establish scalable governance frameworks, maintainer enablement resources, contributor onboarding pathways, and community operating procedures that facilitate efficient standards development and sustained community engagement.
> She will also lead ecosystem-wide scientific coordination, including BIDS Town Halls, maintainer meetings, BEP communications, dissemination activities, and partnerships with downstream projects, while developing systems for documentation, institutional knowledge management, and long-term sustainability.
> Her effort is essential for providing the scientific infrastructure and ecosystem leadership that enables coordinated technical development, broad community adoption, and sustainable delivery of BIDS 2.0+.
>
> [Alejandro De La Vega, Co-PI]{.underline}, will lead the refactoring of PyBIDS as the core querying interface supporting BIDS 2.0+.
> He will extend PyBIDS to be fully BIDS-Schema compliant and self-updating as the BIDS 2.0+ specification develops, and integrate with bids-utils for core operations on the BIDS 2.0 datasets.
> He will expose PyBIDS as an MCP server for robust and predictable agentic access to BIDS datasets, and develop agent Skills to best-practice dataset querying and access.
> He will also contribute software engineering, testing, continuous integration, and developer documentation to accelerate adoption of BIDS 2.0+ across the neuroinformatics community.
>
> **TRAVEL**
>
> Funds are requested for domestic travel for Dr. Kimberly Ray, Dr. Franco Pestilli, and Dr. Alejandro De La Vega to attend BIDS community meetings during each project year.
>
> **INDIRECTS**
>
> University of Texas at Austin has included indirect costs calculated on their total direct costs using 10% approved rate for the Open Source for the Life Sciences.

***[McGill University]{.underline}***

> **PERSONNEL**
>
> [Jean-Baptiste Poline, Co-PI]{.underline}, will provide scientific leadership on behalf of McGill and the BIDS Steering Group for the extension of the BIDS ecosystem into a fully AI-ready standard for the life sciences.
> He will oversee integration of BIDS-Apps 2.0 pipeline-description standards and tooling (Boutiques and Styx) within the Nipoppy pipelines and NeuroBagel federated-learning platforms developed by his group, ensure alignment with AI-assisted tooling within them, and ensure coverage of the BIDS-study specification within BIDS 2.0+ beyond pure brain imaging, as needed across the NeuroBagel worldwide network of sites.
>
> [TBD, Research Software Engineer]{.underline}, will work on the transition of BIDS to a fully AI ready ecosystem for the life sciences community.
> This will in particular involve work to include standards for BIDS ecosystem pipeline descriptions (cf. the Boutiques and Styx standards), including more new BIDS-Apps 2.0 pipelines in Nipoppy, extending the BIDS-study specification for AI.
> The RSE will also contribute to maintenance of the BIDS specification and website, their integration with AI assistants, support the development of the "study" specification and implementation, and extending capacity beyond the academic brain imaging community.
>
> **SUPPLIES**
>
> Funds for partial support for laptop and USB drive for local backups are requested.
>
> **TRAVEL**
>
> To support attendance at the BIDS meeting.
>
> **OTHER DIRECT COSTS**
>
> Funds are requested for AI models subscriptions for coding and other uses, as well as bibliography handling and for publication and communication fees (e.g. poster printing, article publishing, etc).
>
> **INDIRECTS**
>
> McGill University has included indirect costs calculated on total direct costs using 10% approved rate for the Open Source for the Life Sciences.

***[University of California, San Diego]{.underline}***

> **PERSONNEL**
>
> [Seyed Yahya Shirazi, Co-PI]{.underline}, will direct UCSD's agentic-integration work: deepening the Open Science Assistant (OSA), which UCSD initiated and leads, so it uses BIDS data, the BIDS specification, validation results, and selected ecosystem tools through its existing architecture, with a user/agent feedback and observability loop.
> His effort then extends outward to seamless HED integration and cross-standard (HED/NWB/Zarr) validation, landing the stimuli standard (BEP044, with BEP046/BEP047 maintenance), coordinating the NEMAR Zarr work and connecting the Zarr-backed data to the NEMAR 2.0 data-to-GPU path used by agents.
> He maintains the HED AI-native layer (hed-lsp, hed-mcp, HEDit) and is the technical lead for NEMAR, the archive and compute gateway used as the project's training/analysis target.
>
> **TRAVEL**
>
> Domestic travel to support participation in maintainer and community meetings where the work is coordinated and disseminated: BIDS and HED working-group meetings and maintainer sprints, community hackathons organized under this project, and one relevant scientific/standards conference per year (e.g., OHBM, INCF/BIDS, or a NeurIPS/EEG-benchmark venue).
>
> **OTHER DIRECT COSTS**
>
> Computing costs supports the operational infrastructure the proposed software and demonstrations require: GPU/accelerator compute for the NEMAR 2.0 data-to-training and agent demonstrations; cloud storage and transfer for the BIDS-aligned Zarr metadata schema and the data-to-GPU/agent bridge work on NEMAR; and LLM API tokens, model hosting, and tooling subscriptions for developing and evaluating the hed-mcp server and OSA agent integration.
> These are allowable operational needs under the RFA (cloud computing, storage, AI/ML infrastructure including API tokens and model hosting).
>
> **INDIRECTS**
>
> University of California, San Diego has included indirect costs calculated on total direct costs using 10% approved rate for the Open Source for the Life Sciences.

***[Centre for Addiction and Mental Health (CAMH)]{.underline}***

> **PERSONNEL**
>
> [Ariel Rokem, Co-PI]{.underline}, will contribute scientific leadership on diffusion MRI (dMRI) and structural connectivity workflows within the BIDS ecosystem, including maintenance and uptake of the TRX tractography exchange format, contributions to BIDS Extension Proposals covering dMRI derivatives and connectivity outputs, and support for BIDS-Apps 2.0 execution-contract development for dMRI-focused pipelines.
> As an Emeritus member of the BIDS Steering Group, he will also contribute to governance continuity and cross-standard alignment (HED, NWB, TRX/Zarr).
>
> **INDIRECTS**
>
> CAMH has included indirect costs calculated on total direct costs using 10% approved rate for the Open Source for the Life Sciences.

***[CatalystNeuro, LLC]{.underline}***

> **PERSONNEL**
>
> [Benjamin Dichter, Co-PI]{.underline}, will lead CatalystNeuro's contributions across the five work areas of the proposal, with particular focus on the animal / extracellular electrophysiology extensions (BEP032) and the audio / video stimuli work (BEP047); the NWB<->BIDS and HED interoperability layer via NeuroConv and NWB Inspector; and the DANDI-side integration through nwb2bids so that NWB-native datasets deposited in DANDI can be consumed and validated as BIDS derivatives without duplication.
> He will also be involved in testing of the BIDS 2.0+ AI interfaces and harness as applied to datasets on OpenNeuro and DANDI for AI-driven scientific discovery loop.
>
> **TRAVEL**
>
> Travel is requested to support one international trip per year to a BIDS maintainer or community meeting where in-person coordination directly advances the specification work and reference implementations.
> This does not include funding for BIDS community meetings, which are covered separately within the Dartmouth community-travel envelope.
>
> **INDIRECTS**
>
> CatalystNeuro has included indirect costs calculated on total direct costs using 10% approved rate for the Open Source for the Life Sciences.

**INDIRECTS**

Dartmouth has included indirect costs calculated on their total direct costs (excluding equipment and subcontracts) using the 10% rate approved for the Open Source for the Life Sciences program.

****

**High-Level Budget Summary**

TODO: need Personnel adjustment to account for added 4+11=15k of consultant fees (their travel included in travel...)

  -----------------------------------------------------------------------------------------------------------------
  **Budget       **Description**        **Personnel (if    **Year 1 Estimated Costs**    **Year 2 Estimated Costs**
  Category**                            known)**                                      
  -------------- ---------------------- --------------- ----------------------------- -----------------------------
  Personnel      Salaries and fringe    Yaroslav               \$[37,459]{.underline}        \$[31,618]{.underline}
                 benefits for project   Halchenko, PI;                                
                 staff                  Cody Baker                                    

  Supplies       Software, cloud                               \$[10,000]{.underline}        \$[10,000]{.underline}
                 services, consumables                                                

  Travel         Hackathon participant  Project team           \$[72,446]{.underline}        \$[72,446]{.underline}
                 travel, Project                                                      
                 meetings, Conferences,                                               
                 Partner Coordination                                                 
                 Meetings                                                             

  Meetings /     Workshops, technical   Project team           \$[10,000]{.underline}        \$[10,000]{.underline}
  Hackathons /   sprints, community                                                   
  Sprints        engagement,                                                          
                 collaboration events                                                 

  Consultants    Child Mind Institute   Gregory Kiar +         \$[15,000]{.underline}        \$[15,000]{.underline}
                 (BEP027, Niwrap/Styx,  team                                          
                 bids2table)                                                          

                 HES-SO Valais-Wallis   Oscar Esteban          \$[15,000]{.underline}        \$[15,000]{.underline}
                 (Lausanne) (OSA/MCP,                                                 
                 provenance, QA/QC,                                                   
                 hackathon                                                            
                 organization)                                                        

  Subcontracts   Stanford University    Russell                \$[88,752]{.underline}        \$[91,248]{.underline}
                                        Poldrack,                                     
                                        Co-PI; Chris                                  
                                        Markiewicz;                                   
                                        Nell                                          
                                        Hardcastle;                                   
                                        Ross Blair                                    

                 University of Texas at Franco                 \$[78,553]{.underline}        \$[78,812]{.underline}
                 Austin                 Pestilli,                                     
                                        Co-PI; Kimberly                               
                                        Ray, Co-PI;                                   
                                        Alejandro De La                               
                                        Vega, Co-PI                                   

                 McGill University      Jean-Baptiste          \$[60,000]{.underline}        \$[60,000]{.underline}
                                        Poline, Co-PI                                 

                 University of          Seyed Yahya            \$[60,000]{.underline}        \$[60,000]{.underline}
                 California, San Diego  Shirazi, Co-PI                                

                 Centre for Addiction   Ariel Rokem,            \$[6,800]{.underline}        \$[10,470]{.underline}
                 and Mental Health      Co-PI                                         
                 (CAMH)                                                               

                 CatalystNeuro, LLC     Benjamin               \$[30,000]{.underline}        \$[30,000]{.underline}
                                        Dichter, Co-PI                                

  Indirect Costs Excluding equipment    N/A                    \$[15,990]{.underline}        \$[15,406]{.underline}
  (≤10%)         and subcontract costs                                                

  **Total                                                 **\$[500,000]{.underline}**   **\$[500,000]{.underline}**
  Requested                                                                           
  Funding**                                                                           
  -----------------------------------------------------------------------------------------------------------------
