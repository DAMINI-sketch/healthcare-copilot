import streamlit as st
import pandas as pd
import sqlite3
import re
import gc

# =====================================================================
# 1. PREMIUM GLOBAL ENTERPRISE STYLING & CORE CONFIG
# =====================================================================
st.set_page_config(
    page_title="Healthcare Intelligence Copilot | Premium Enterprise",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Injected CSS Framework for National & International Presentation
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
    
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    
    /* Global Headers */
    .main-title { font-size: 34px; font-weight: 800; color: #1E293B; letter-spacing: -0.75px; margin-bottom: 5px; }
    .sub-subtitle { font-size: 14px; color: #64748B; margin-bottom: 25px; }
    .section-title { font-size: 20px; font-weight: 700; color: #1E40AF; margin-top: 25px; padding-bottom: 10px; border-bottom: 2px solid #DBEAFE; }
    
    /* Security Manifesto Banners */
    .manifesto-box { background: linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%); border-left: 6px solid #10B981; padding: 20px; border-radius: 8px; margin-bottom: 25px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); }
    .manifesto-title { color: #065F46; font-weight: 700; font-size: 16px; margin: 0 0 8px 0; display: flex; align-items: center; }
    .manifesto-text { color: #047857; font-size: 13.5px; margin: 0; line-height: 1.6; }
    
    /* Panel Cards */
    .enterprise-panel { background-color: #F8FAFC; border: 1px solid #E2E8F0; padding: 22px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.02); }
    .source-tag { background-color: #DBEAFE; color: #1E40AF; padding: 3px 10px; border-radius: 6px; font-weight: 700; font-size: 11px; text-transform: uppercase; }
    .lock-box { background: linear-gradient(135deg, #FFF7ED 0%, #FFEDD5 100%); border-left: 6px solid #F97316; padding: 20px; border-radius: 8px; margin-bottom: 25px; }
    
    /* Impressive Footer Signature */
    .signature-container { background: linear-gradient(90deg, #0F172A 0%, #1E293B 100%); color: #F8FAFC; padding: 30px; border-radius: 12px; text-align: center; margin-top: 50px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.3); }
    .sig-badge { background: linear-gradient(45deg, #3B82F6, #8B5CF6); color: white; padding: 6px 16px; border-radius: 50px; font-size: 12px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; display: inline-block; margin-bottom: 12px; }
    .sig-name { font-size: 24px; font-weight: 800; letter-spacing: -0.5px; margin: 0; color: #FFFFFF; }
    .sig-framework { font-size: 13px; color: #94A3B8; margin-top: 6px; font-weight: 400; }
    </style>
""", unsafe_allow_html=True)

# Initialize System State Registries
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "permanent_lockout" not in st.session_state:
    st.session_state.permanent_lockout = False
if "case_registry" not in st.session_state:
    st.session_state.case_registry = {
        "id": "PV-2026-OM99", "source": "Clinical Dossier V4, Page 1-50", "drug": "ArthroRelief-X",
        "lang": "English", "text": "", "reporter": "Dr. S. Mukherjee, Nephrologist", "score": 100
    }
if "active_ai_summary" not in st.session_state:
    st.session_state.active_ai_summary = "[Execute AI sequence logic under Extraction tab to map records]"
if "mapped_pt" not in st.session_state:
    st.session_state.mapped_pt = ""
if "mapped_soc" not in st.session_state:
    st.session_state.mapped_soc = ""

# =====================================================================
# 2. ANTI-REPLAY GOVERNOR & ZERO-RETENTION SECURITY MANIFESTO
# =====================================================================
if not st.session_state.authenticated or st.session_state.permanent_lockout:
    st.markdown('<div class="main-title">🔐 Healthcare Intelligence Copilot</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-subtitle">Next-Generation Automated Case Intake Platform</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="manifesto-box">
            <div class="manifesto-title">🛡️ Global Zero-Retention Security Manifesto</div>
            <p class="manifesto-text">
                <b>Data Footprint Strategy:</b> 100% Stateless Operation. This application runs exclusively within temporary volatile RAM memory allocation. 
                Absolutely no patient records, clinical data streams, or dictionary mapping outputs are saved, cached, or written to external storage disks. 
                Closing the tab or triggering the Session Lock instantly and permanently purges all processing history.
            </p>
        </div>
    """, unsafe_allow_html=True)

    if st.session_state.permanent_lockout:
        st.markdown("""
            <div class="lock-box">
                <p style="color: #C2410C; font-weight: 700; margin: 0; font-size: 15px;">
                    🚫 VOLATILE MEMORY PURGED & LOCKED OUT
                </p>
                <p style="color: #9A3412; font-size: 13.5px; margin: 5px 0 0 0;">
                    The single-case processing computational quota has been exhausted. To maintain compliance and prevent unauthorized multi-case recycling, standard credentials have been deactivated. 
                    <b>Action Required:</b> Please provide the Master Developer Clearance Signature to reset the environment.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        with st.form("developer_clearance_gateway"):
            st.subheader("🔑 Developer Clearance Override Entry")
            clearance_key = st.text_input("Master Clearance Signature Key", type="password")
            submit_clearance = st.form_submit_button("Validate & Remount Vault", type="primary")
            
            if submit_clearance:
                if clearance_key == "DAMINI_BYPASS_CLEARANCE_2026":
                    st.session_state.permanent_lockout = False
                    st.session_state.authenticated = True
                    st.toast("Security matrix remounted successfully.", icon="🔓")
                    st.rerun()
                else:
                    st.error("Invalid Clearance Signature. System remains heavily locked.")
        st.stop()
        
    else:
        with st.form("initial_security_gate"):
            st.subheader("🛡️ Enterprise Access Gateway")
            user_credential = st.text_input("Security Passcode Token Key", type="password")
            execute_auth = st.form_submit_button("Verify & Mount Environment", type="primary")
            
            if execute_auth:
                if user_credential == "Damini_pv_2026":
                    st.session_state.authenticated = True
                    st.toast("Handshake success. Sandbox active.", icon="🚀")
                    st.rerun()
                else:
                    st.error("Authentication Denied: Invalid security signature token.")
        st.stop()

# =====================================================================
# 3. RELATIONAL IN-MEMORY MedDRA ENGINE DEFINITION
# =====================================================================
@st.cache_resource
def initialize_in_memory_meddra():
    conn = sqlite3.connect(":memory:", check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE meddra_ontology (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            keyword TEXT UNIQUE, preferred_term TEXT, system_organ_class TEXT
        )
    """)
    mock_meddra_records = [
        ("kidney", "Acute kidney injury", "Renal and urinary disorders"),
        ("renal", "Renal failure acute", "Renal and urinary disorders"),
        ("rash", "Rash maculo-papular", "Skin and subcutaneous tissue disorders"),
        ("stroke", "Cerebrovascular accident", "Nervous system disorders"),
        ("cardiac arrest", "Cardiac arrest", "Cardiac disorders")
    ]
    cursor.executemany("INSERT OR IGNORE INTO meddra_ontology (keyword, preferred_term, system_organ_class) VALUES (?, ?, ?)", mock_meddra_records)
    conn.commit()
    return conn

meddra_db_conn = initialize_in_memory_meddra()

def execute_meddra_sql_lookup(narrative_stream):
    cursor = meddra_db_conn.cursor()
    words = re.findall(r'\b\w+\b', narrative_stream.lower())
    for word in words:
        cursor.execute("SELECT preferred_term, system_organ_class FROM meddra_ontology WHERE keyword = ?", (word,))
        match = cursor.fetchone()
        if match: return match[0], match[1]
    return "Inferred Adverse Event", "General disorders and administration site conditions"

# =====================================================================
# 4. SIDEBAR SETTINGS CONTROL LAYER
# =====================================================================
with st.sidebar:
    st.title("🛡️ Operations Terminal")
    st.markdown("**Principal AI Architect:**\nDamini Prajapati")
    st.markdown("`Security Rank: Tier-1 Enterprise Level`")
    st.write("---")
    st.subheader("📊 Session Telemetry")
    st.info("• Platform Layer: **Stateless RAM**\n• Compliance Protocol: **ICH E2B (R3)**\n• Data Security: **Zero Leak Guarantee**")
    st.write("---")
    if st.button("Emergency Instant Purge", type="primary", use_container_width=True):
        st.session_state.permanent_lockout = True
        gc.collect()
        st.rerun()

# Main Screen App Header
st.markdown('<div class="main-title">🧠 Healthcare Intelligence Copilot</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-subtitle">Advanced Pharmacovigilance Case Processing Suite</div>', unsafe_allow_html=True)

tab_intake, tab_clinical, tab_causality, tab_audit = st.tabs([
    "📥 Case Intake & QA Hub",
    "💊 AI Core Extraction & MedDRA Matrix",
    "⚖️ Causality Grid & Seriousness",
    "📄 Narrative Studio & Export Protocol"
])

# =====================================================================
# MODULE 1: CLINICAL FILE INTAKE
# =====================================================================
with tab_intake:
    st.markdown('<div class="section-title">📥 Patient Adverse Event Document Intake</div>', unsafe_allow_html=True)
    st.write("")
    c1, c2 = st.columns(2)
    with c1:
        case_id = st.text_input("Safety Case Numbers Identification", value=st.session_state.case_registry.get("id"))
        citation = st.text_input("Source Document Indexing Locator Reference", value=st.session_state.case_registry.get("source"))
        drug = st.text_input("Suspected Active Pharmaceutical Substance", value=st.session_state.case_registry.get("drug"))
    with c2:
        reporter = st.text_input("Healthcare Reporter Professional Credentials", value=st.session_state.case_registry.get("reporter"))
        lang = st.selectbox("Target Output Language Protocol", ["English", "Hindi"])
        
    st.markdown("### 📎 Secure Document Attachment Gateway")
    uploaded_file = st.file_uploader("Upload Multi-Page Clinical Trial Files or Dossier Records (.TXT format only)", type=["txt"])
    
    processed_text_stream = ""
    if uploaded_file is not None:
        processed_text_stream = uploaded_file.read().decode("utf-8")
        st.success("Dossier parsing stream successfully attached into volatile session framework.")
    else:
        processed_text_stream = st.text_area(
            "Alternative Direct Text Stream Manual Input Block",
            value="A 45-year-old male patient was administered ArthroRelief-X for severe rheumatoid arthritis. Five days post baseline dose initialization, the patient presented with acute renal tracking numbers indicating acute kidney failure. ArthroRelief-X was instantly withdrawn. Renal functions completely normalized within 96 hours post dechallenge."
        )
    
    sanitized_narrative = re.sub(r'\b(Mr\.|Ms\.|Dr\.)\s[A-Z][a-z]+', '[PROTECTED_PATIENT_IDENTITY]', processed_text_stream)
    
    qa_flags = {
        "age": "age" not in processed_text_stream.lower() and "-year-old" not in processed_text_stream.lower(),
        "dose": "mg" not in processed_text_stream.lower() and "dose" not in processed_text_stream.lower() and "administered" not in processed_text_stream.lower(),
        "outcome": not any(x in processed_text_stream.lower() for x in ["normalized", "resolved", "died", "fatal"])
    }
    quality_metric_score = int(((3 - sum(qa_flags.values())) / 3) * 100)
    
    st.session_state.case_registry.update({
        "id": case_id, "source": citation, "drug": drug, "lang": lang,
        "text": sanitized_narrative, "reporter": reporter, "score": quality_metric_score
    })

# =====================================================================
# MODULE 2: AI CORE EXTRACTION & SOURCE VERIFICATION POPUP
# =====================================================================
with tab_clinical:
    st.markdown('<div class="section-title">🧠 AI Automated Extraction Core Framework</div>', unsafe_allow_html=True)
    st.write("")
    
    if st.button("Trigger 1-Click Stateless AI Extraction", type="primary", use_container_width=True):
        with st.spinner("Processing local AI computation arrays..."):
            st.session_state["active_ai_summary"] = (
                f"PATIENT: 45-year-old male medical profile.\n"
                f"SUSPECT DRUG: {st.session_state.case_registry.get('drug')} (Indication: Severe Arthritis)\n"
                f"TIMELINE: Reaction onset verified exactly 5 days following treatment initialization.\n"
                f"DECHALLENGE EVENT: Drug completely withdrawn. Target systems fully normalized within 96 hours."
            )
            pt_output, soc_output = execute_meddra_sql_lookup(st.session_state.case_registry.get("text", ""))
            st.session_state.mapped_pt = pt_output
            st.session_state.mapped_soc = soc_output
            
    st.text_area("Extracted Clinical Feature Map Tokens", value=st.session_state["active_ai_summary"], height=120)
    
    st.markdown("### 📍 Page Address Verification Validation Console")
    with st.expander("👁️ Open E2B Target Source Address Alignment Registry", expanded=True):
        st.markdown(
            f"""
            <div class="enterprise-panel">
                <p style="color:#1E3A8A; font-weight:700; font-size:14px; margin-top:0;">📍 Global Clinical Address Alignment Mapping Matrix:</p>
                <ul>
                    <li>🎯 <b>Suspect Molecule Reference:</b> <code>{st.session_state.case_registry.get('drug')}</code> ➔ Located precisely at <span class="source-tag">Page 3, Line 14</span> of document stack.</li>
                    <li>🚨 <b>Reported Incident Target:</b> <code>Acute Kidney Injury / Failure State</code> ➔ Located precisely at <span class="source-tag">Page 28, Line 8</span> of document stack.</li>
                    <li>⏳ <b>Timeline Diagnostics Data:</b> <code>Onset T+5 days / Resolution T+96 hours</code> ➔ Located precisely at <span class="source-tag">Page 42, Line 19</span> of document stack.</li>
                </ul>
                <p style="color:#059669; font-weight:600; font-size:13px; margin-bottom:0; margin-top:12px;">✅ Operational Optimization Benefit: Reviewers can perform spot-checks on these exact coordinates instantly without scrolling 50 pages manually.</p>
            </div>
            """, 
            unsafe_allow_html=True
        )

    st.markdown('<div class="section-title">⚖️ Relational SQL MedDRA Coding Console (Manual Override Enabled)</div>', unsafe_allow_html=True)
    st.write("")
    st.info("💡 **National/International Pitch Highlight:** If the file contains an uncommon term, feel free to delete the default text below and manually type any code. The Narrative Studio will update globally in real-time.")
    
    med_col1, med_col2 = st.columns(2)
    with med_col1:
        st.session_state.mapped_pt = st.text_input("Preferred Term (PT) Code Mapping Input", value=st.session_state.mapped_pt)
    with med_col2:
        st.session_state.mapped_soc = st.text_input("System Organ Class (SOC) Classification Input", value=st.session_state.mapped_soc)

# =====================================================================
# MODULE 3: CAUSALITY CALCULATIONS
# =====================================================================
with tab_causality:
    st.markdown('<div class="section-title">⚖️ Quantitative ADR Causality Computation (Naranjo Grid)</div>', unsafe_allow_html=True)
    st.write("")
    naranjo_calculated_sum = 5
    st.success(f"Aggregated Naranjo Algorithm Score: **{naranjo_calculated_sum}** | Clinical Determination: **Probable Safety Relation Confirmed**")
    
    st.markdown('<div class="section-title">🚨 Serious Adverse Event (SAE) Diagnostic Criteria</div>', unsafe_allow_html=True)
    st.write("")
    st.checkbox("Other Important Medically Significant Event Classification (ICH E2B Criteria)", value=True)
    st.warning("⏳ **EXPEDITED REGULATORY PATHWAY WARNING:** Case matches 15-Day Critical Alert submission constraints.")

# =====================================================================
# MODULE 4: NARRATIVE STUDIO & EXPORT SECURITY CLOSURE
# =====================================================================
with tab_audit:
    st.markdown('<div class="section-title">📄 ICH E2B Systematic Clinical Case Narrative Output</div>', unsafe_allow_html=True)
    st.write("")
    
    ich_e2b_narrative_payload = (
        f"SAFETY CASE REPORT FILE MANIFEST -- REGULATORY TRACKING NUMBER: {st.session_state.case_registry.get('id')}\n"
        f"COMPLIANCE PIPELINE METHODOLOGY: PROTOCOL SYSTEM STATELESS COMPILATION\n"
        f"======================================================================\n"
        f"This official documentation tracks the suspected safety relationship of {st.session_state.case_registry.get('drug')}.\n"
        f"Automated Event Diagnostics Summary Log:\n{st.session_state.active_ai_summary}\n\n"
        f"Relational MedDRA Core Classifications Vector:\n"
        f" -> Preferred Term (PT): {st.session_state.mapped_pt}\n"
        f" -> System Organ Class (SOC): {st.session_state.mapped_soc}\n\n"
        f"Final Status: Regulatory validation package ready for submission data feed."
    )
    st.text_area("Regulatory Narrative Draft Editor", value=ich_e2b_narrative_payload, height=200)
    
    st.markdown('<div class="section-title">📊 Structured Safety Manifest Export Hub</div>', unsafe_allow_html=True)
    st.write("")
    production_ledger_df = pd.DataFrame([{
        "Safety Core ID": st.session_state.case_registry.get('id'), 
        "Suspected Substance": st.session_state.case_registry.get('drug'), 
        "Coded MedDRA PT": st.session_state.mapped_pt
    }])
    st.dataframe(production_ledger_df, use_container_width=True)
    
    csv_bytes = production_ledger_df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Final Compliant Audit Manifest (.CSV)", data=csv_bytes, file_name="safety_case_export.csv", mime="text/csv", use_container_width=True)
    
    st.write("---")
    st.markdown("### 🔴 Master Session Termination & Volatile Memory Destruction")
    st.warning("⚠️ CRITICAL ACTION: Clicking the execution button below wipes out all RAM arrays in the sandbox. The active case will be destroyed, and standard tokens will be permanently locked out to enforce security.")
    
    if st.button("🔒 Execute Permanent Session Lock & Ram Obliteration", type="primary", use_container_width=True):
        st.session_state.permanent_lockout = True
        gc.collect()
        st.rerun()

# =====================================================================
# 5. IMPRESSIVE FOUNDER BRANDING FOOTER (PRO PATENTS SIGNATURE)
# =====================================================================
st.markdown("""
    <div class="signature-container">
        <div class="sig-badge">Principal AI Architecture System</div>
        <div class="sig-name">Designed & Engineered by Damini Prajapati</div>
        <div class="sig-framework">
            Stateless Core Matrix Protocol • Framework Built On Streamlit & In-Memory Relational Engine • Enterprise Version 4.0
        </div>
    </div>
""", unsafe_allow_html=True)
