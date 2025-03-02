import base64
import streamlit as st
st.set_page_config(layout="wide")


st.sidebar.image("LorinBales_Mirror_Circular.png", width=200)
st.sidebar.subheader(":gray[Lorin Bales]", divider="gray")
st.sidebar.caption("_Data_ _Scientist_")
st.sidebar.caption("_Based_ _in_ _Huntsville_, _AL_ or '_Rocket_ _City_' :rocket:")
col_linkedin, col_github, col_email = st.sidebar.columns(3, border=True)
with st.sidebar:
    with col_linkedin:
        col_linkedin.markdown(
            """<a href="https://www.linkedin.com/in/lorinarnold/">
            <img src="data:image/png;base64,{}" width="25">
            </a>""".format(
                base64.b64encode(open("icons8-linkedin-50.png", "rb").read()).decode()
            ),
            unsafe_allow_html=True,
        )
    with col_github:
        col_github.markdown(
            """<a href="https://github.com/ettuniversum">
            <img src="data:image/png;base64,{}" width="25">
            </a>""".format(
                base64.b64encode(open("icons8-github-50.png", "rb").read()).decode()
            ),
            unsafe_allow_html=True,
        )
    with col_email:
        col_email.markdown('<a href="mailto:lorinbales@gmail.com">Email</a>', unsafe_allow_html=True)
st.sidebar.write("--")
st.sidebar.subheader(":gray[About]")
st.sidebar.text("Exceptional technical lead in data science pairing hardware, software, and data for rapid development of "
        "products. Enjoys mentoring young professionals through sharing academic literature, latest course "
        "certificates, or project coding templates.")
st.sidebar.subheader(":gray[Skills]")
st.sidebar.text("Llama Index, Ollama, Docker, pandas, numpy, tensorflow, Scikit-learn, CNN, LSTM, DBSCAN, FastAPI, "
        "asyncio, AWS S3 Elasticsearch, Knowledge Graphs, mySQL, Microsoft Access db, GitLab CI/CD, Kotlin, C++, "
        "Javascript, Jira, Bash Shell Scripting, Windows, Linux (Ubuntu), Latex")

# Projects
st.subheader(":gray[PROJECTS]", divider="gray")
col_ppg, col_astro = st.columns(2)
with col_ppg:
    st.subheader("Over-the-ear PPG monitor")
    st.text("Over-the-ear photoplethysmographic (PPG) monitor is a cost effective and high-precision device to "
            "measure the effects of blood flow to the head. Engineered a lightweight, ergonomic over-ear form "
            "factor through 3D printing, that encases continuous streaming via bluetooth on a minimal embedded "
            "device and lithium ion battery")
    st.image("Wearout.gif", caption="Android app developed in Kotlin displaying PPG signal")
with col_astro:
    st.image('AstroHardware.png', caption="Astro hardware and software integration for deep space object"
                                          " acquisition")
    st.subheader("Amateur Astronomer")
    st.text("Amateur astrophotographer specializing in deep-sky object acquisition and processing. "
            "Employs tracking for precise celestial object targeting, utilizing multi-frame integration techniques "
            "to optimize signal-to-noise ratios. Post-processing workflow incorporates computational deconvolution "
            "algorithms for point spread function (PSF) correction, multi-scale noise reduction, and selective stellar "
            "signature removal to enhance nebulosity and galactic detail in final compositions.")
    col_HDR, col_noise = st.columns(2)
    with col_HDR:
        st.image("Orion_Contrast_Lum.gif", caption="High Dynamic Range Multi Transform (HDR) for contrast of Orion"
                                                   " Nebula")
    with col_noise:
        st.image("Cigar_NoiseXterminator.gif", caption="AI noise reduction of Cigar Galaxy")

# Education
st.subheader(":gray[EDUCATION]", divider="gray")
st.caption("_Bachelor's_ _of_ _Science_ _in_ _Physics_")
st.caption("_University_ _of_ _Alabama_ _in_ _Huntsville_ (_UAH_)")
st.caption("_Graduation_: _Spring_, _2013_")

# Publications
st.subheader(":gray[PUBLICATION]", divider="gray")
st.write("Checkout my publication for [OBSERVATION OF FLUX-TUBE CROSSINGS IN THE SOLAR WIND](https://iopscience.iop.org/article/10.1088/0004-637X/766/1/2)")
st.image('FluxTube.PNG', caption="Schematics illustrating (a) a single-current-sheet event, (b) a double-current-sheet event, and (c) a triple-current-sheet event.")

st.subheader(":gray[EXPERIENCE]", divider="gray")
st.caption(":blue[Tech Lead & Senior Data Scientist], _NOV_, _2023_, COLSA, Huntsville AL ")
st.text("Description: \nReduced evaluation of vulnerable software from weeks to days leveraging AI Large Language Model (LLM) "
        "through prompt engineering and knowledge graph ontologies. VET (Vet Enhancement Tool) ingests SwA results "
        "from the Cyber team for static code analysis, automatically classifying vulnerabilities and reducing manual "
        "effort. LLM attention aided Retrieval Augmented Generation (RAG) framework prompted by C++ abstract syntax "
        "tree or Code Property Graph.  Team of data scientists unit tested and developed CI/CD pipeline in six-months "
        "delivering a docker container onsite for offline mode.")

st.caption(":blue[Tech Lead & Senior Software Developer], *Torch Technologies*, *Feb 2022 - Nov 2023*, Huntsville AL ")
st.text("Description: \nLed development of 'Maverick' (MAVRC), a same-day dashboard for analysis of Digital and HWIL " 
        "evaluation across the kill chain of MDS. Implemented ETL processes from AWS S3 Elasticsearch data store into " 
        "object-oriented analysis framework with Bokeh visualization. Parsed various data formats including ATOMS, GFC, "
        "and SMHR proprietary formats into compressed Python formats. Researched and developed minimization of Fréchet "
        "distance and DBSCAN clustering to pair trajectories, leveraging open source propagation and coordinate "
        "transformation for system analysis.")

st.caption(":blue[Sabbatical], *Jul 2019 - Feb 2022* ")
st.text("Description: \nHoned optical skills in astrophotography, focusing on AI-powered deconvolution, noise reduction, "
        "and star removal techniques.")

st.caption(":blue[AI Software Engineer], *Modern Technology Solutions Inc. (MTSI)*, *Apr 2018 - Dec 2019*, Huntsville AL ")
st.text("Description: \nLed Object Pattern EXtractor (OPEX) team in solving single sensor 4-parameter motion solution "
        "problems using Convolution Neural Networks (CNN) to reduce solution ambiguity. Analyzed and presented OPEX "
        "Measures of Performance results against Discrimination Improvement for Homeland Defense (DIHD) truth trajectories "
        "for Integrated Performance Reviews. Proposed and demonstrated knowledge base and knowledge graph implementation "
        "with Grakn AI, coupled with CNN to address scene-based reasoning for contextual analysis across various "
        "potential engagements.")

st.caption(":blue[Software Engineer], *deciBel Research Inc.*, *Feb 2015 - Apr 2018*, Huntsville AL ")
st.text("Description: \nReverse engineered object classification for GMD sensors in Python, delivering full analysis "
        "product and briefing to government customers and Tech Fellows. Remotely supported Lockheed Martin Aegis "
        "contract and UEWR CD BIT contract at COLSA Advanced Research Center. Developed reusable file browser interface "
        "for viewing and plotting data in HDF files. Refactored tools to Python for efficiency, modernization, and "
        "standardization, creating parsers 5x faster than previous implementations.")

st.caption(":blue[deciBel Honorary Junior Tech Fellow], *deciBel Research Inc.*, *Feb 2017 - Apr 2018*, Huntsville AL ")
st.text("Description: \nSelected to join a cross-functional group of subject matter experts collaborating across programs "
        "to bring understanding to complex technical problems.")

st.caption(":blue[System Analyst], *nou Systems Inc.*, *Jan 2014 - Feb 2015*, Huntsville AL ")
st.text("Description: \nDeveloped analysis toolset and plots for AN/TPY-2 (FBM) FSP (Focus Search Plan) and Threat "
        "Acquisition analysis involving cancelled, extended, or tasked FSPs. Created post-mission linkage between truth "
        "data trajectories and intended FSP tasks. Developed 3D search plans with globe plots for presentation visual "
        "aids. Presented briefing on preliminary results for C2BMC FSP tasking and AN/TPY-2 threat acquisition for "
        "GTI-04e Part 2.")

st.caption(":blue[System Engineer], *Northrop Grumman*, *Jan 2013 - Jan 2014*, Huntsville AL ")
st.text("Description: \nDeveloped reliable and user-friendly data collection software in a team environment, pulling "
        "data from various devices including Motorola radios, warn and network devices, and proprietary software. "
        "Created robust data management algorithm using MD5 checksum, reducing a manual procedure from approximately "
        "4 hours to 4 minutes per week.")

st.caption(":blue[Research Assistant], *CSPAR (Center for Space Physics and Aeronomic Research)*, *May 2011 - Jan 2013*, Huntsville AL ")
st.text("Description: \nDeveloped and optimized searching algorithm for Current Sheet structures within the solar wind. "
        "Analyzed approximately 11,400 structures, proving them to be boundaries between flux tubes and significant "
        "sources of electromagnetic intermittent turbulence in the solar wind. Analyzed large datasets from spacecraft "
        "including Advanced Composition Explorer, Helios, Ulysses, and WIND, proving existence of these structures "
        "throughout the Heliosphere. Conducted systematic analysis of Magnetohydrodynamics using mathematical Structure "
        "Function. Presented results at Von Braun Symposium Poster Presentation (2011) and AGU Conference (2012).")