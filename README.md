# UK-Road-Casualty-Severity-Scalable-Analytics
End-to-end road safety analytics project using UK DfT casualty data: Python predictive modelling, Third Normal Form (3NF) relational schema and SQL queries, distributed scaling &amp; alerting architecture, and GDPR-aligned privacy governance.


# UK Road Casualty Severity & Scalable Analytics

An end-to-end data analytics, database engineering, and distributed systems project investigating UK Department for Transport (DfT) Road Safety Casualty Statistics (2024) under the Open Government Licence (OGL v3.0).

## Project Overview

This repository demonstrates applied techniques across predictive modelling, relational database normalisation, distributed big data architecture, and privacy-by-design governance to identify factors associated with serious and fatal road traffic casualties and support public road safety insights.

## Key Components & Architecture

### 1. Casualty Severity Investigation & Predictive Modelling
* **Exploratory & Statistical Analysis:** Investigated discrete variables and casualty demographics (such as age, casualty type, and injury severity) using statistical tests and visualisations to identify high-risk groups and key predictors of serious or fatal outcomes.
* **Data Preprocessing & Feature Engineering:** Cleaned and prepared raw DfT casualty records, documented handling of missing/ambiguous values, and engineered features suitable for supervised learning.
* **Classification / Regression Modelling (`Python 3` / `WEKA`):** Trained, justified, and evaluated predictive models using appropriate classification/regression evaluation metrics to predict casualty severity outcomes.

### 2. Relational Database Design (3NF) & SQL Analytics
* **Normalised Schema Design:** Transitioned flat-file CSV records into a Third Normal Form (3NF) relational schema (documented via Entity-Relationship Diagrams) separating casualty demographics, pedestrian attributes, collision context, and lookup entities to eliminate redundancy and enforce referential integrity.
* **SQL Implementation:**
  * **Data Ingestion (`INSERT`):** Structured statements for adding validated casualty records across normalised tables.
  * **Targeted Filtering (`SELECT`):** Queries isolating serious or fatal pedestrian-related casualties under specific collision conditions.
  * **Descriptive Aggregation (`GROUP BY`):** Breakdown of Fatal, Serious, and Slight casualty counts across casualty types.

### 3. Distributed Storage, Scaling & Real-Time Alerting
* **Scalable Architecture:** Designed a distributed processing pipeline (evaluating batch and streaming frameworks such as Apache Spark and Hadoop ecosystems) to scale from hundreds of thousands of annual DfT casualty records to millions of multi-year records alongside high-frequency telematics and near-miss data.
* **Automated Safety Alerting:** Outlined threshold- and trend-based alerting workflows to flag regional, road-type, local-authority, or time-period spikes in fatal casualties upon data refresh or stream ingestion.

### 4. Privacy, Ethics & Governance (Public-Facing Application)
* **Privacy Risk Mitigation:** Evaluated risks across public casualty map visualisations, optional user location/travel habit collection, and predictive safety recommendations.
* **GDPR-Aligned Controls:** Mapped technical and organisational safeguards—including spatial/temporal aggregation, k-anonymity, encryption, explicit opt-in consent, purpose limitation, and data minimisation—to UK GDPR principles.

## Data Source & Licensing

* **Dataset:** UK Department for Transport (DfT) — *Road Safety Data - Casualties - 2024*
* **Licence:** [UK Open Government Licence (OGL) v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)

## Repository Structure

```text
uk-road-casualty-analytics/
├── README.md
├── src/                  # Python preprocessing, analysis, and modelling scripts
├── sql/                  # 3NF schema DDL, INSERT, filtering, and aggregation queries
└── docs/                 # ERD diagrams and visualisations
