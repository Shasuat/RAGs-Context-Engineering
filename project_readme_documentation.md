# AI-Powered Review Intelligence & MCP Approval Workflow

**Product Context:** Groww (SBI Mutual Fund Integration)  
**Milestone:** NextLeap PM Fellowship — AI System Design & Workflow Orchestration  

---

## 📌 Project Overview

This system transforms raw customer reviews into actionable product insights and customer-facing support documentation. By processing unstructured app store and platform feedback, the intelligence layer detects top themes, highlights recurring user confusion around **Exit Load charges on early redemptions**, and automatically generates:

1. **Weekly Internal Product Pulse** ($\le 250$ words) for product managers and engineering leads.
2. **Standardized Fee Explainer** ($\le 6$ concise bullet points) for support teams to resolve user queries.
3. **Approval-Gated MCP Tool Actions** that log these artifacts into an internal knowledge base (Google Docs / Notion) and prepare a Gmail draft without auto-sending.

---

## 🔍 Step 1: Review Intelligence Layer Findings

**Dataset:** 25 recent user reviews collected over the past 8–12 weeks regarding Groww's SBI Mutual Fund journey.

### Identified Clusters & Top Themes:
1. **Fee & Charge Confusion (Exit Load):** Users feel "cheated" or surprised when a 1% exit load is deducted upon withdrawing funds within 365 days of investment.
2. **SIP Processing & NAV Allocation Delays:** Complaints regarding payment deduction happening on Day $T$, but NAV allocation taking up to $T+2$ business days.
3. **Statement & Tax Document Downloads:** Friction surrounding capital gains statement generation and password protection on PDF files.

### Identified Fee/Charge Issue:
* **Core Pain Point:** Misunderstanding of how **Exit Load duration is calculated** (per-tranche/per-SIP installment vs. lump-sum investment date).
* **Representative User Quote:** *"I withdrew my SBI Flexicap money after 1 year of starting SIP, but Groww still deducted 1% exit load! Why are they stealing my money without warning?"*

---

## ⚙️ Model Context Protocol (MCP) & Approval Gating Architecture

```
┌─────────────────────────┐
│ Raw Reviews (CSV Data)  │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Review Intelligence     │
│ (Clustering & Extraction│
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Artifact Generation     │
│ (Product Pulse &        │
│ Fee Explainer)          │
└───────────┬─────────────┘
            │
            ▼
┌────────────────────────────────────────────────────────┐
│               HUMAN APPROVAL STEP (GATE)              │
│ Prompt: "Approve logging to Notion & Drafting Email?"  │
└───────────┬────────────────────────────────┬───────────┘
            │ APPROVED                       │ REJECTED
            ▼                                ▼
┌─────────────────────────┐      ┌───────────────────────┐
│ MCP Action Executed:    │      │ Action Terminated &   │
│ 1. Append to Doc/Notes  │      │ Logs Maintained       │
│ 2. Create Gmail Draft   │      └───────────────────────┘
└─────────────────────────┘
```

### Where Approval Happens:
Before executing external side effects via MCP tools (e.g., updating databases or creating email drafts), the system pauses and presents a summary preview to the Product Manager. The system requires an explicit user confirmation (`APPROVE` button or command line trigger) before making API calls.

---

## 🚀 How to Run the Prototype

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Shasuat/mf-facts-assistant.git
   cd mf-facts-assistant
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Workflow Application:**
   ```bash
   streamlit run app.py
   ```

4. **Trigger MCP Workflow:**
   * Navigate to the **Review Intelligence** tab.
   * Click **Process Feedback**.
   * Review generated outputs in the preview panel.
   * Click **"Approve & Execute MCP Pipeline"** to trigger document appending and email draft creation.

---

## 🔒 Privacy & Compliance
* **Zero PII:** Dataset contains no user email addresses, phone numbers, PAN, or account details.
* **Facts-Only Guardrail:** All fee explanations are grounded strictly in SEBI guidelines and SBI Mutual Fund KIM disclosures.