"""
TMF Intelligence System — Trial Portfolio (Meridian Clinical)
Primary Key: MER Study ID (assigned by Meridian Clinical internal system)
External IDs (NCT, EudraCT, Protocol No) are reference fields only.
Statuses driven by eTMF Excel import — not hardcoded.

Only MER-2026-001 through MER-2026-005 are pre-seeded here. MER-2026-006 and
MER-2026-007 already exist as rows in data/exports/eTMF_Status_Report.xlsx
(so RegistryAgent can resolve them), but are deliberately left out of this
file until ingested live through the pipeline — see CLAUDE.md Section 3.
"""

TRIALS = {
    "MER-2026-001": {
        "tax_id": "MER-2026-001",
        "nct_id": "NCT04033445",
        "eudract": "N/A",
        "protocol_no": "CNTO1959UCO3001",
        "study_number": "QUASAR",
        "short_name": "QUASAR",
        "drug": "Guselkumab (Tremfya)",
        "sponsor": "Janssen Research & Development, LLC",
        "phase": "Phase 2b/3",
        "condition": "Ulcerative Colitis",
        "condition_type": ["UC"],
        "design": "Randomized, Double-Blind, Placebo-Controlled, Multicenter, "
                  "Parallel-Group (Induction Study 1, Induction Study 2, and "
                  "Maintenance Study)",
        "duration": "12-week induction, 44-week maintenance (56 weeks total)",
        "ind_number": "On file",
        "protocol_date": "2019-09-01",
        "latest_amendment": "Amendment 3",
        "latest_amendment_date": "2019-09-01",
        "countries": ["USA", "Canada", "Japan", "Germany", "France", "Spain",
                      "South Korea", "Australia", "Brazil"],
        "patients_screened": None,
        "patients_randomized": 701,
        "primary_objective": "To evaluate the efficacy and safety of guselkumab as "
                             "induction and maintenance therapy in participants with "
                             "moderately to severely active ulcerative colitis who had "
                             "inadequate response or intolerance to conventional or "
                             "advanced therapy.",
        "primary_endpoint": "Clinical remission at Week 12 (induction) and Week 44 "
                            "(maintenance) by modified Mayo score (stool frequency "
                            "subscore 0/1 not increased from baseline, rectal bleeding "
                            "subscore 0, endoscopic subscore 0/1 without friability).",
        "inclusion_criteria": [
            "Documented UC diagnosis, moderately to severely active (modified Mayo "
            "score 5-9)",
            "Disease extending 20 cm or more from the anal verge",
            "Demonstrated inadequate response, loss of response, or intolerance to "
            "conventional or advanced (biologic/JAK) therapy",
        ],
        "exclusion_criteria": [
            "Diagnosis of Crohn's disease, indeterminate, microscopic, or ischemic "
            "colitis",
            "UC limited to the rectum only (<20 cm)",
            "Presence of a stoma or fistula",
        ],
        "amendment_history": [
            {"version": "Amendment 3", "date": "2019-09-01",
             "patients_at_time": "Pre-enrollment"},
        ],
        "tmf_documents": {
            "Protocol (Final)": {"status": "Complete", "date": "2019-09-01", "version": "Amendment 3"},
            "Investigator Agreement": {"status": "Missing", "date": None, "version": None},
            "Ethics Committee Approval": {"status": "Missing", "date": None, "version": None},
            "IND Approval": {"status": "Missing", "date": None, "version": None},
            "Informed Consent Form": {"status": "Missing", "date": None, "version": None},
            "Monitoring Plan": {"status": "Missing", "date": None, "version": None},
            "Delegation of Authority Log": {"status": "Missing", "date": None, "version": None},
            "Lab Certification (Central)": {"status": "Missing", "date": None, "version": None},
        },
        "risk_level": "Medium",
        "notes": "Large multinational Phase 2b/3 program across 30+ countries. "
                 "Sourced from ClinicalTrials.gov (NCT04033445).",
    },
    "MER-2026-002": {
        "tax_id": "MER-2026-002",
        "nct_id": "NCT02435992",
        "eudract": "N/A",
        "protocol_no": "See ClinicalTrials.gov record",
        "study_number": "True North",
        "short_name": "True North",
        "drug": "Ozanimod (Zeposia)",
        "sponsor": "Bristol Myers Squibb",
        "phase": "Phase 3",
        "condition": "Ulcerative Colitis",
        "condition_type": ["UC"],
        "design": "Randomized, Double-Blind, Placebo-Controlled, Multicenter, two "
                  "induction cohorts (Cohort 1 blinded, Cohort 2 open-label) followed "
                  "by blinded re-randomization to maintenance",
        "duration": "10-week induction, 42-week maintenance (52 weeks total)",
        "ind_number": "On file",
        "protocol_date": "2015-06-01",
        "latest_amendment": "Amendment 5",
        "latest_amendment_date": "2015-06-01",
        "countries": ["USA", "Canada", "UK", "Germany", "France", "Poland", "Japan",
                      "Australia"],
        "patients_screened": 1831,
        "patients_randomized": 1012,
        "primary_objective": "To determine whether ozanimod is effective as induction "
                             "and maintenance therapy in patients with moderately to "
                             "severely active ulcerative colitis.",
        "primary_endpoint": "Clinical remission at Week 10 (induction) and Week 52 "
                            "(maintenance) per 3-component Mayo score (rectal bleeding "
                            "subscore 0, stool frequency subscore <=1 with decrease "
                            ">=1 from baseline, endoscopy subscore <=1).",
        "inclusion_criteria": [
            "Age 18-75 with UC confirmed by endoscopy",
            "Moderately to severely active disease (Mayo score 6-12, endoscopic "
            "subscore >=2)",
            "On stable aminosalicylate/corticosteroid or eligible immunomodulator use",
        ],
        "exclusion_criteria": [
            "Severe extensive colitis with anticipated need for colectomy within 12 "
            "weeks",
            "Fulminant colitis, toxic megacolon, or bowel perforation in prior 3 months",
            "Crohn's disease or other non-UC colitis diagnosis",
            "Clinically significant cardiovascular disease",
        ],
        "amendment_history": [
            {"version": "Amendment 5", "date": "2015-06-01",
             "patients_at_time": "Pre-enrollment"},
        ],
        "tmf_documents": {
            "Protocol (Final)": {"status": "Complete", "date": "2015-06-01", "version": "Amendment 5"},
            "Investigator Agreement": {"status": "Missing", "date": None, "version": None},
            "Ethics Committee Approval": {"status": "Missing", "date": None, "version": None},
            "IND Approval": {"status": "Missing", "date": None, "version": None},
            "Informed Consent Form": {"status": "Missing", "date": None, "version": None},
            "Monitoring Plan": {"status": "Missing", "date": None, "version": None},
        },
        "risk_level": "Medium",
        "notes": "Conducted at 285 sites across 30 countries. Sponsor protocol ID is "
                 "not publicly disclosed on ClinicalTrials.gov. Sourced from "
                 "ClinicalTrials.gov (NCT02435992).",
    },
    "MER-2026-003": {
        "tax_id": "MER-2026-003",
        "nct_id": "NCT02914522",
        "eudract": "2016-001392-78",
        "protocol_no": "GS-US-418-3898",
        "study_number": "SELECTION",
        "short_name": "SELECTION",
        "drug": "Filgotinib (Jyseleca)",
        "sponsor": "Gilead Sciences, Inc.",
        "phase": "Phase 2b/3",
        "condition": "Ulcerative Colitis",
        "condition_type": ["UC"],
        "design": "Randomized, Double-Blind, Placebo-Controlled, Multicenter, two "
                  "parallel induction studies (Study A biologic-naive, Study B "
                  "biologic-experienced) followed by a combined maintenance study",
        "duration": "11-week induction, 47-week maintenance (58 weeks total)",
        "ind_number": "On file",
        "protocol_date": "2016-09-22",
        "latest_amendment": "Amendment 4",
        "latest_amendment_date": "2016-09-22",
        "countries": ["USA", "Canada", "Australia", "New Zealand", "Japan", "Germany",
                      "Spain", "Brazil"],
        "patients_screened": 2040,
        "patients_randomized": 1348,
        "primary_objective": "To evaluate the efficacy of filgotinib in inducing and "
                             "maintaining remission in biologic-naive and "
                             "biologic-experienced patients with moderately to "
                             "severely active ulcerative colitis.",
        "primary_endpoint": "Endoscopy/Bleeding/Stool frequency (EBS) remission at "
                            "Week 10 (induction) and Week 58 (maintenance): endoscopic "
                            "subscore 0-1, rectal bleeding subscore 0, stool frequency "
                            "subscore 0-1 with >=1-point decrease.",
        "inclusion_criteria": [
            "Age 18-75, UC diagnosed >=6 months with >=15 cm disease extent",
            "Moderately to severely active UC",
            "Prior inadequate response, loss of response, or intolerance to >=1 of: "
            "corticosteroids, immunomodulators, TNF antagonists, or vedolizumab",
        ],
        "exclusion_criteria": [
            "Crohn's disease, indeterminate colitis, ischemic/fulminant colitis, or "
            "toxic megacolon",
            "Active or untreated latent tuberculosis",
        ],
        "amendment_history": [
            {"version": "Amendment 4", "date": "2016-09-22",
             "patients_at_time": "Pre-enrollment"},
        ],
        "tmf_documents": {
            "Protocol (Final)": {"status": "Complete", "date": "2016-09-22", "version": "Amendment 4"},
            "Investigator Agreement": {"status": "Missing", "date": None, "version": None},
            "Ethics Committee Approval": {"status": "Missing", "date": None, "version": None},
            "IND Approval": {"status": "Missing", "date": None, "version": None},
            "Informed Consent Form": {"status": "Missing", "date": None, "version": None},
        },
        "risk_level": "Medium",
        "notes": "341 centers across 40 countries; dual biologic-naive/experienced "
                 "cohort design. Sourced from ClinicalTrials.gov (NCT02914522).",
    },
    "MER-2026-004": {
        "tax_id": "MER-2026-004",
        "nct_id": "NCT02100696",
        "eudract": "2013-004278-88",
        "protocol_no": "GA28950",
        "study_number": "HICKORY",
        "short_name": "HICKORY",
        "drug": "Etrolizumab",
        "sponsor": "Hoffmann-La Roche",
        "phase": "Phase 3",
        "condition": "Ulcerative Colitis",
        "condition_type": ["UC"],
        "design": "Randomized, Double-Blind, Placebo-Controlled, Multicenter, "
                  "previously-TNF-exposed population, responders re-randomized into "
                  "a maintenance phase",
        "duration": "14-week induction, maintenance through Week 66",
        "ind_number": "On file",
        "protocol_date": "2014-01-10",
        "latest_amendment": "Amendment 6",
        "latest_amendment_date": "2014-01-10",
        "countries": ["USA", "Canada", "UK", "Germany", "France", "Australia",
                      "South Korea", "Mexico"],
        "patients_screened": 1081,
        "patients_randomized": 609,
        "primary_objective": "To evaluate the efficacy and safety of etrolizumab as "
                             "induction and maintenance therapy in patients with "
                             "moderately to severely active UC previously treated "
                             "with TNF inhibitors.",
        "primary_endpoint": "Remission at Week 14 (induction) by Mayo Clinic Score "
                            "(MCS <=2, no individual subscore >1, rectal bleeding "
                            "subscore 0); remission at Week 66 among Week-14 "
                            "responders (maintenance).",
        "inclusion_criteria": [
            "UC diagnosis >=3 months, moderate-to-severe disease per Mayo score",
            "Prior TNF inhibitor exposure (1-2 anti-TNF regimens within past 5 "
            "years) with >=8-week washout",
            "Stable background 5-ASA/corticosteroid/immunomodulator therapy allowed",
        ],
        "exclusion_criteria": [
            "Alternative colitis diagnoses (indeterminate, ischemic, radiation, "
            "microscopic)",
            "Crohn's disease, fistula, abscess, dysplasia, obstruction, or toxic "
            "megacolon",
            "Prior UC surgery/ostomy, prior integrin antagonist or tofacitinib "
            "exposure",
            "Active/latent TB, HIV, hepatitis B/C",
        ],
        "amendment_history": [
            {"version": "Amendment 6", "date": "2014-01-10",
             "patients_at_time": "Pre-enrollment"},
        ],
        "tmf_documents": {
            "Protocol (Final)": {"status": "Complete", "date": "2014-01-10", "version": "Amendment 6"},
            "Investigator Agreement": {"status": "Missing", "date": None, "version": None},
            "Ethics Committee Approval": {"status": "Missing", "date": None, "version": None},
            "IND Approval": {"status": "Missing", "date": None, "version": None},
            "Informed Consent Form": {"status": "Missing", "date": None, "version": None},
            "Monitoring Plan": {"status": "Missing", "date": None, "version": None},
        },
        "risk_level": "High",
        "notes": "184 centers across 24 countries, prior-anti-TNF-exposed population. "
                 "Amendment 6 predates the 2014-05-21 enrollment start by ~4 months — "
                 "a high amendment count this early is unusual and worth a second "
                 "check against the primary protocol history if this becomes a talking "
                 "point in the demo. Sourced from ClinicalTrials.gov (NCT02100696).",
    },
    "MER-2026-005": {
        "tax_id": "MER-2026-005",
        "nct_id": "NCT03105128",
        "eudract": "2016-003123-32",
        "protocol_no": "M16-006",
        "study_number": "ADVANCE",
        "short_name": "ADVANCE",
        "drug": "Risankizumab (Skyrizi)",
        "sponsor": "AbbVie",
        "phase": "Phase 3",
        "condition": "Crohn's Disease",
        "condition_type": ["CD"],
        "design": "Randomized, Double-Blind, Placebo-Controlled, Multicenter "
                  "induction study in two periods (Period 1 randomized dose "
                  "comparison, Period 2 re-treatment for inadequate responders)",
        "duration": "12-week induction only (maintenance assessed separately in the "
                    "companion FORTIFY study)",
        "ind_number": "On file",
        "protocol_date": "2017-03-01",
        "latest_amendment": "Amendment 2",
        "latest_amendment_date": "2017-03-01",
        "countries": ["USA", "Canada", "Germany", "France", "Japan", "China",
                      "South Korea", "Australia", "Brazil"],
        "patients_screened": None,
        "patients_randomized": 931,
        "primary_objective": "To evaluate the efficacy and safety of risankizumab "
                             "versus placebo as induction therapy in patients with "
                             "moderately to severely active Crohn's disease.",
        "primary_endpoint": "Co-primary endpoints at Week 12: clinical remission by "
                            "CDAI (<150, US design) or stool frequency/abdominal "
                            "pain score (global design), and endoscopic response "
                            "(>=50% reduction from baseline in SES-CD).",
        "inclusion_criteria": [
            "Age 16-80, confirmed CD diagnosis >=3 months",
            "Moderate-to-severe disease per CDAI/stool frequency/abdominal pain/SES-CD",
            "Demonstrated intolerance or inadequate response to conventional or "
            "biologic therapy",
        ],
        "exclusion_criteria": [
            "UC or indeterminate colitis diagnosis",
            "Recent biologic use within washout windows (anti-TNF within 8 weeks, "
            "ustekinumab within 12 weeks)",
            "Prior p19 inhibitor exposure",
            "CD complications requiring surgery, ostomy, or ileoanal pouch",
        ],
        "amendment_history": [
            {"version": "Amendment 2", "date": "2017-03-01",
             "patients_at_time": "Pre-enrollment"},
        ],
        "tmf_documents": {
            "Protocol (Final)": {"status": "Complete", "date": "2017-03-01", "version": "Amendment 2"},
            "Investigator Agreement": {"status": "Missing", "date": None, "version": None},
            "Ethics Committee Approval": {"status": "Missing", "date": None, "version": None},
            "IND Approval": {"status": "Missing", "date": None, "version": None},
            "Informed Consent Form": {"status": "Missing", "date": None, "version": None},
        },
        "risk_level": "Medium",
        "notes": "Induction-only registration; maintenance assessed separately in the "
                 "companion FORTIFY study (NCT03105102). Sourced from "
                 "ClinicalTrials.gov (NCT03105128).",
    },

    "MER-2026-007": {
        "tax_id": "MER-2026-007",
        "nct_id": "NCT02574637",
        "eudract": "2015-000609-38",
        "protocol_no": "D5170C00002",
        "study_number": "D5170C00002",
        "short_name": "MER-2026-007",
        "drug": "MEDI2070",
        "sponsor": "MedImmune Limited, a wholly owned subsidiary of AstraZeneca",
        "phase": "Phase 2b",
        "condition": "Crohn's Disease",
        "condition_type": [],
        "design": "See protocol",
        "duration": "See protocol",
        "ind_number": "111773",
        "protocol_date": "2015-08-06",
        "latest_amendment": "Amendment 1",
        "latest_amendment_date": "2015-11-18",
        "countries": ["See protocol"],
        "patients_screened": None,
        "patients_randomized": None,
        "primary_objective": "To evaluate the efficacy of MEDI2070 versus placebo to induce clinical remission based on the CDAI score at Week 8 in subjects with moderate to severe Crohn's disease who have failed or are intolerant to anti-TNFα therapy.",
        "primary_endpoint": "Clinical remission rate as measured by the Crohn's Disease Activity Index (CDAI) at Week 8 compared with placebo.",
        "pdf_filename": "MER-2026-007_MEDI2070-CD_D5170C00002_Protocol_Amendment-1_2015-11-18.pdf",
        "inclusion_criteria": ["See protocol"],
        "exclusion_criteria": ["See protocol"],
        "amendment_history": [{"version": "Amendment 1", "date": "2015-11-18", "patients_at_time": "0"}],
        "tmf_documents": {
            "Protocol (Final)": {"status": "Complete", "date": "2015-11-18", "version": "Amendment 1"},
            "Investigator Agreement": {"status": "Missing", "date": None, "version": None},
            "Ethics Committee Approval": {"status": "Missing", "date": None, "version": None},
            "IND Approval": {"status": "Missing", "date": None, "version": None},
            "Informed Consent Form": {"status": "Missing", "date": None, "version": None},
            "Monitoring Plan": {"status": "Missing", "date": None, "version": None},
        },
        "risk_level": "Medium",
        "notes": "Auto-ingested via TMF Intelligence System.",
    },
}

TMF_ZONES = {
    "Zone 1": "Trial Management",
    "Zone 2": "Subject Information and Consent",
    "Zone 3": "Subject Identification",
    "Zone 4": "Site and Staff Information",
    "Zone 5": "Scientific and Medical Information",
    "Zone 6": "Investigational Medicinal Products",
    "Zone 7": "Regulatory and Ethics",
    "Zone 8": "Investigator Site File",
}

FLAG_RULES = {
    "Missing": {
        "action": "Locate or obtain document and file in TMF within 30 days.",
        "severity": "Critical",
    },
    "Expired": {
        "action": "Renew document and update TMF with current version immediately.",
        "severity": "Critical",
    },
    "Needs Review": {
        "action": "Review document for completeness and accuracy within 14 days.",
        "severity": "Warning",
    },
    "Pending": {
        "action": "Follow up with responsible party to obtain document.",
        "severity": "Warning",
    },
    "Complete": {
        "action": "No action required.",
        "severity": "OK",
    },
}
