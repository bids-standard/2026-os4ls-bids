<!--
    PI and Co-PI biographies for the OS4LS Full Application "BIDS 2.0+
    ecosystem: AI-Ready Life-Science Data Standard".

    References are rendered by pandoc citeproc against ../BIDS.bib in
    Vancouver (numeric) style; see the Makefile target
    `subs/biographies.pdf`.

    All cite keys resolve against the current BIDS.bib
    (verified via `scripts/verify-bio-keys.sh`).  Re-run after any
    `make -B BIDS.bib`.  That file is exported from our BIDS Zotero
	collection available at https://www.zotero.org/groups/5111637/bids/library .
	Articles which related to this BIDS but not necessarily to BIDS itself,
	should go under "Related/" subcollection:
	https://www.zotero.org/groups/5111637/bids/collections/BZ69VS62/collection

    Refs deliberately NOT cited (kept out on purpose):
    - Ray KL et al. 2013 "Modeling and mapping cognitive-control
      networks" — flagged as hallucination; removed from Ray's bio.
    - VAME (Luxem 2022) and GuPPy (Sherathiya 2021) — tools
      CatalystNeuro integrates into NWB but Dichter is not a
      co-author on either paper; removed from his biosketch.
-->
---
title: "BIDS 2.0+ ecosystem — PI and Co-PI Biographies"
link-citations: true
reference-section-title: "References"
---

## Yaroslav O. Halchenko, PhD — PI (Dartmouth)

**Role:** PI (Applicant); overall coordination; BIDS specification, schema, bids-utils.
**Position:** Research Professor of Psychological and Brain Sciences (adjunct in Computer Science) and Founding Director, [Center for Open Neuroscience](https://centerforopenneuroscience.org/), Dartmouth College.
**IDs:** yaroslav.o.halchenko@dartmouth.edu · [ORCID 0000-0003-3456-2493](https://orcid.org/0000-0003-3456-2493) · [GitHub yarikoptic](https://github.com/yarikoptic) · [Scholar](https://scholar.google.com/citations?user=EbtfZcwAAAAJ) · [centerforopenneuroscience.org](https://centerforopenneuroscience.org/)

Dr. Halchenko is an Emeritus member of BIDS [@gorgolewski_brain_2016] Steering Group and one of five named recipients of the 2023 Neuro-Cooper Foundation Open Science International Prize awarded to the BIDS Steering Group.
He leads DataLad [@halchenko_datalad_2021], through which thousands of BIDS-formatted datasets from archives (OpenNeuro, DANDI, etc.) and portals (like [GIN](https://gin.g-node.org/)) are made available, and discoverable via [registry.datalad.org](https://registry.datalad.org) which his group created.
He leads the ReproNim reproducibility center's TRD3 effort [@kennedy_everything_2019], and serves as Co-PI on DANDI, and Co-I on OpenNeuro [@markiewicz_openneuro_2021], and EMBER national data archives which use and promote BIDS standard.
He co-authored PyMVPA and Nipype [@gorgolewski_nipype_2011], created ReproIn (heuristic DICOM-to-BIDS conversion), maintains HeuDiConv [@halchenko_heudiconv_2024], and created NeuroDebian which served base container for various BIDS-Apps and packaged core libraries (such as nipype).
Halchenko remains one of the most active contributors to bids-specification & bids-website, leads OpenNeuroStudies initiative to compose "study" BIDS datasets for all datasets on OpenNeuro, contributed and maintains [BIDS SKILL](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/bids) within [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills), and coordinates and contributes to various BEPs.
His group, which includes Key Personnel Cody C. Baker, is actively participating in coordinating efforts across standardization efforts [@rubel_ecosystem_2025], creating new and improving existing digital infrastructure for neuroscience and beyond, as many solutions are generic and not neuroscience specific.

## Russell A. Poldrack, PhD — Co-PI (Stanford)

**Role:** Co-PI (Stanford lead); BIDS specification, bids-validator, PyBIDS, OpenNeuro integration.
**Position:** Albert Ray Lang Professor of Psychology (courtesy: Psychiatry & Behavioral Sciences); Chair of Psychology;  Director, Center for Open and Reproducible Science, Stanford University.
**IDs:** russpold@stanford.edu · [ORCID 0000-0001-6755-0259](https://orcid.org/0000-0001-6755-0259) · [GitHub poldrack](https://github.com/poldrack) · [Scholar](https://scholar.google.com/citations?user=RbmLvDIAAAAJ) · [poldracklab.org](http://poldracklab.org/)

Dr. Poldrack is a BIDS [@gorgolewski_brain_2016] co-founder and Emeritus member of its Steering Group.
He established OpenfMRI in 2009 and currently leads its successor OpenNeuro [@markiewicz_openneuro_2021], the primary open archive for neuroimaging data; originated the Cognitive Atlas ontology, and co-founded Neurosynth.
His group develops widely used open-source tools including fMRIPrep, MRIQC, PyBIDS [@yarkoni_pybids_2019], and the bids-validator, and drives community standardization efforts for reproducible neuroimaging [@gorgolewski_bids_2017; @poldrack_scanning_2017].
He has also developed open-source educational materials including [Better Code, Better Science](https://bettercode-book.org) and [Statistical Thinking](https://statsthinking21.org/).

## Franco Pestilli, PhD — Co-PI (UT Austin)

**Role:** Co-PI (UT Austin); BIDS Connectivity BEPs; brainlife.io integration; BIDS-compliant pipelines and MCP servers for BRAIN CONNECTS.
**Position:** Professor of Psychology (Neuroscience, by courtesy), Center for Perceptual Systems, The University of Texas at Austin.
**IDs:** pestilli@utexas.edu · [ORCID 0000-0002-2469-0494](https://orcid.org/0000-0002-2469-0494) · [GitHub francopestilli](https://github.com/francopestilli) · [Scholar](https://scholar.google.com/citations?user=gh_KorwAAAAJ) · [brainlife.io](https://brainlife.io) · [pestillilab.github.io](https://pestillilab.github.io)

Dr. Pestilli founded and directs [brainlife.io](https://brainlife.io/) [@hayashi_brainlifeio_2024], an open-source cloud platform for reproducible neuroscience.
He is a Principal Investigator on the NIH BRAIN CONNECTS Axonal Projectome EXchange (APEX) data-coordinating center, chairs the INCF Infrastructure Committee, serves on the BIDS Steering Group [@poldrack_past_2023], and leads the BIDS Connectivity BEPs.
He authored the Linear Fascicle Evaluation (LiFE) tractography-evaluation toolbox and contributes to community efforts on tractography reliability [@schilling_tractography_2021], AI-scale imaging datasets [@allen_massive_2022], and reproducibility infrastructure [@niso_open_2022].
Fellow of the Association for Psychological Science and the Psychonomic Society; recipient of the APS Janet Taylor Spence Award and a Microsoft Investigator Fellowship.


## Kimberly L. Ray, PhD — Co-PI / Project Manager (UT Austin)

**Role:** Co-PI, Project Manager — BIDS 2.0+ community coordination, Steering Group facilitation, Maintainers coordination, Town Halls, hackathon planning.
**Position:** Research Assistant Professor, Department of Psychology, The University of Texas at Austin; Engagement & Communication Manager, brainlife.io.
**IDs:** kimray@utexas.edu · [ORCID 0000-0003-1302-2834](https://orcid.org/0000-0003-1302-2834) · [GitHub kimberlylray](https://github.com/kimberlylray) · [Scholar](https://scholar.google.com/citations?user=Qt6OuAkAAAAJ) · [UT faculty page](https://liberalarts.utexas.edu/psychology/faculty/klr3342)

Dr. Ray research spans cognitive neuroscience, fMRI, meta-analytic connectivity modeling, and data governance for FAIR neuroscience.
She is a current BIDS Maintainer and facilitates the BIDS Steering Group, coordinating governance across Maintainers, Working Groups, and elected leadership.
Through brainlife.io she runs community engagement — town halls, tutorials, documentation, and onboarding — for open neuroimaging platforms.


## Jean-Baptiste Poline, PhD — Co-PI (McGill)

**Role:** Co-PI (McGill); BIDS Steering Group; Boutiques / Nipoppy integration; Niwrap coordination.
**Position:** Professor, Department of Neurology and Neurosurgery, McGill University / Montreal Neurological Institute (The Neuro); Director, Neuro Data Science ORIGAMI Laboratory; Co-Director of Neuroinformatics, McConnell Brain Imaging Centre.
**IDs:** jean-baptiste.poline@mcgill.ca · [ORCID 0000-0002-9794-749X](https://orcid.org/0000-0002-9794-749X) · [GitHub jbpoline](https://github.com/jbpoline) · [Scholar](https://scholar.google.ca/citations?user=BU7Zdi4AAAAJ) · [neurodatascience.github.io](https://neurodatascience.github.io/)

Dr. Poline is a pioneering fMRI methodologist and co-developer of Statistical Parametric Mapping (SPM) - one of the initial and dominant toolkits for neuroimaging data analytics.
His work spans imaging genetics, statistical modeling of brain data, data harmonization, and reproducible / FAIR neuroscience infrastructure [@poldrack_scanning_2017].
He co-chairs NeuroHub, chairs the CONP Technical Steering Committee and the INCF Technical Steering Committee, is a current member of the BIDS Steering Group [@gorgolewski_brain_2016], and is PI on the Nipoppy [@bhagwat_nipoppy_2026] and Neurobagel projects.
He served as PI on the CZI EOSS Cycle 5 award "Improving Standard Practice for Neuroimaging Analyses with Nilearn" (2022-2024) [@abraham_machine_2014], and his lab maintains Boutiques [@glatard_boutiques_2018] which underlies specification of interfaces of the BIDS-Apps 2.0.


## Alejandro de la Vega, PhD — Co-PI (UT Austin)

**Role:** Co-PI (UT Austin); PyBIDS refactor for BIDS 2.0+; PyBIDS-as-MCP server and agent Skills; fitlins / BIDS StatsModels.
**Position:** Research Assistant Professor, Department of Psychology, The University of Texas at Austin.
**IDs:** aleph4@gmail.com · [ORCID 0000-0001-9062-3778](https://orcid.org/0000-0001-9062-3778) · [GitHub adelavega](https://github.com/adelavega) · [adelavega.github.io](https://adelavega.github.io/)

Dr. de la Vega leads Neuroscout [@de_la_vega_neuroscout_2022], a BIDS-native platform for generalizable and reproducible fMRI meta-analysis, and is a core author and maintainer of PyBIDS [@yarkoni_pybids_2019] — the reference Python library for querying and manipulating BIDS datasets that underlies fMRIPrep, MRIQC, QSIPrep, fitlins, and most BIDS-Apps.
Under this proposal he will lead the PyBIDS refactor for BIDS 2.0+ — making it fully BIDS-Schema compliant and self-updating as the specification develops — integrate PyBIDS with bids-utils for core dataset operations, and expose PyBIDS as an MCP server with reusable agent Skills for robust and predictable agentic access to BIDS datasets.
He also contributes to fitlins / BIDS StatsModels and to the BIDS specification and community roadmap [@poldrack_past_2023].


## Seyed Yahya Shirazi, PhD — Co-PI (UCSD)

**Role:** Co-PI (UCSD); OSA (Open Science Assistant); [BEP044](https://bids.neuroimaging.io/bep044) lead; [BEP046](https://bids.neuroimaging.io/bep046) / [BEP047](https://bids.neuroimaging.io/bep047) maintainer; HED tooling; NEMAR integration; HED-MCP.
**Position:** Assistant Project Scientist, Swartz Center for Computational Neuroscience (SCCN), Institute for Neural Computation, University of California, San Diego.
**IDs:** syshirazi@ucsd.edu · [ORCID 0000-0001-5557-259X](https://orcid.org/0000-0001-5557-259X) · [GitHub neuromechanist](https://github.com/neuromechanist) · [Scholar](https://scholar.google.com/citations?user=9QzpcEoAAAAJ) · [neuromechanist.github.io](https://neuromechanist.github.io/)

Dr. Shirazi builds open-source neuroinformatics infrastructure for ExG (EEG, EMG, iEEG), and multimodal biosignal research (Mobile Brain/Body Imaging) with a strong emphasis on FAIR standards.
He is a current BIDS Maintainer, lead of [BEP044](https://bids.neuroimaging.io/bep044) (Stimuli), and a maintainer on [BEP046](https://bids.neuroimaging.io/bep046) and [BEP047](https://bids.neuroimaging.io/bep047); a core contributor to EEGLAB and the HED working group [@hermes_hierarchical_2025]; a co-author of the Lab Streaming Layer [@kothe_lab_2025], with curent and prior contributions to data acquisition and quality [@shirazi_more_2019].
He leads the [Open Science Assistant](https://osc.earth/osa), and drives HBN-EEG curation [@shirazi_hbn-eeg_2024], the largest open-EEG dataset, the EEG 2025 NeurIPS foundation-model challenge [@aristimunha_eeg_2025], and [NEMAR 2.0](https://ww2.nemar.org) integration.
He also is the archtiext of AI-agentic and native tools including [hed-lsp](https://github.com/hed-standard/hed-lsp), [HEDit](https://github.com/Annotation-Garden/HEDit), and [matlab-mcp-tools](https://github.com/neuromechanist/matlab-mcp-tools).


## Ariel Rokem, PhD — Co-PI (CAMH)

**Role:** Co-PI (CAMH); dMRI-derivative BEPs; TRX validation; cloud-friendly connectivity backends (Zarr); GPU-accelerated BIDS-Apps 2.0.
**Position:** Senior Scientist, Krembil Centre for Neuroinformatics (KCNI), Centre for Addiction and Mental Health (CAMH); Faculty Affiliate, Vector Institute for Artificial Intelligence.
**IDs:** ariel.rokem@camh.ca · [ORCID 0000-0003-0679-1985](https://orcid.org/0000-0003-0679-1985) · [GitHub arokem](https://github.com/arokem) · [Scholar](https://scholar.google.com/citations?user=hrBeLVYAAAAJ) · [rokemlab.github.io](https://rokemlab.github.io) · [arokem.org](http://arokem.org)

Dr. Rokem develops open-source computational methods for diffusion MRI, tractometry, and connectomics [@kruper_evaluating_2021; @legarreta_what_2026], applied to brain development, aging, and mental health.
He is lead developer of pyAFQ and a core contributor to DIPY [@garyfallidis_dipy_2014]; an Emeritus member of the BIDS Steering Group [@poldrack_past_2023]; and a named co-recipient of the 2023 Neuro-Cooper Foundation Open Science International Prize.
Contributes to QSIPrep [@cieslak_qsiprep_2021], to the BIDS Connectivity BEPs ([BEP16](https://bids.neuroimaging.io/bep16) diffusion derivatives, [BEP46](https://bids.neuroimaging.io/bep46) connectivity derivatives), and to the TRX tractography container format.
Co-founder / co-director of the Summer Institute in Neuroimaging and Data Science (Neurohackademy); recipient of the 2024 OHBM Education in Neuroimaging Award.


## Ben Dichter, PhD — Co-PI (CatalystNeuro)

**Role:** Co-PI (CatalystNeuro); [BEP032](https://bids.neuroimaging.io/bep032) lead; [BEP047](https://bids.neuroimaging.io/bep047) contributor; NWB/BIDS interoperability; AI tools for NeuroConv and NWB Inspector.
**Position:** Founder and CEO, [CatalystNeuro](https://catalystneuro.com/).
**IDs:** ben.dichter@catalystneuro.com · [ORCID 0000-0001-5725-6910](https://orcid.org/0000-0001-5725-6910) · [GitHub bendichter](https://github.com/bendichter) · [Scholar](https://scholar.google.com/citations?user=_IwI_oEAAAAJ) · [bendichter.com](https://bendichter.com) · [catalystneuro.com](https://www.catalystneuro.com)

Dr. Dichter earned his PhD in Bioengineering from the UC Berkeley-UCSF Joint Program in Edward Chang's lab, studying cortical control of voice pitch via electrocorticography [@dichter_control_2018].
Under his direction CatalystNeuro is the primary maintainer of the Neurodata Without Borders (NWB) tooling ecosystem [@rubel_neurodata_2022; @rubel_ecosystem_2025] — including NeuroConv (converting 40+ proprietary neurophysiology formats to NWB), the NWB Inspector, and substantial contributions to PyNWB — and coordinates data-conversion partnerships with dozens of experimental labs and DANDI Archive.
He leads BIDS [BEP032](https://bids.neuroimaging.io/bep032) (microelectrode / animal electrophysiology) and contributes to [BEP047](https://bids.neuroimaging.io/bep047) [@holdgraf_ieeg-bids_2019], sits at the NWB↔BIDS interoperability seam central to this proposal, and supports downstream tools that CatalystNeuro integrates into the NWB ecosystem, including VAME (behavior) and GuPPy (fiber photometry).
Co-author on [Neurosift](https://neurosift.app/) which provides NWB visualization, OpenNeuro and DANDI archives navigation and AI-assisted "search".
Active proponent in using AI coding agents for answering fundamental research questions [@dichter_ai_2026].

