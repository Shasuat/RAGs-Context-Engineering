import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(
    page_title="Review Intelligence & MCP Assistant",
    page_icon="📊",
    layout="wide",
)

# Sidebar Disclaimer
with st.sidebar:
  st.header("⚠️ Disclaimer")
  st.write("Facts-only. No investment advice.")
  st.markdown("---")
  st.info(
      "Simulated MCP Approval Workflow for Groww / SBI Mutual Fund insights."
  )

# Main Title
st.title("📊 AI-Powered Review Intelligence & MCP Workflow")
st.markdown(
    "Transforming raw customer reviews into actionable product updates and"
    " support communication with approval-gated MCP actions."
)

# Tabs for workflow steps
tab1, tab2, tab3 = st.tabs(
    ["1. Review Intelligence", "2. Weekly Pulse & Explainer", "3. MCP Approval"
    " & Actions"]
)

with tab1:
  st.subheader("Cluster Reviews & Theme Detection")
  st.markdown(
      "Analyzing recent user feedback (last 8-12 weeks) for SBI Mutual Fund"
      " schemes on Groww."
  )

  # Sample review metrics / table
  data = {
      "Theme": [
          "Pricing / Fee Confusion",
          "App UI / Navigation",
          "Transaction Delay",
          "KYC / Onboarding",
      ],
      "Mentions": [42, 28, 19, 11],
      "Top Issue": [
          "Unexpected Exit Load charged on redemptions",
          "Dark mode toggle resets",
          "SIP auto-debit confirmation lag",
          "PAN verification error loops",
      ],
  }
  df = pd.DataFrame(data)
  st.table(df)

  st.markdown("### 💬 Extracted User Quotes")
  st.markdown(
      "> *\"I redeemed my SBI Large & Midcap units after 10 months and noticed a"
      " 1% charge deducted. The app didn't show this clearly upfront!\"*"
  )
  st.markdown(
      "> *\"Why is there an exit load when the fund factsheet says long term?"
      " Confusing rules.\"*"
  )
  st.markdown(
      "> *\"Tried canceling a SIP and couldn't find the exit clause easily in"
      " the dashboard.\"*"
  )

with tab2:
  st.subheader("Weekly Product Pulse (Internal Output)")
  st.markdown("""
    * **Summary:** High volume of user tickets regarding unexpected deductions during redemption.
    * **Key Observation:** Users confuse the 1-year exit load window with ELSS lock-in periods or assume equity funds are entirely fee-free on early exit.
    * **Action Ideas:** 
      1. Add a prominent fee preview modal right before a user clicks 'Confirm Redemption'.
      2. Link the KIM exit load table directly inside the holding details screen.
      3. Push a targeted in-app tooltip clarifying exit load timelines.
    """)

  st.subheader("Standardized Fee Explainer (Customer-Facing)")
  st.markdown("""
    * **What is an Exit Load?** A fee charged by the AMC when an investor redeems units within a specific timeframe.
    * **SBI Large & Midcap / Flexicap Rule:** 1% exit load if redeemed within 1 year of allotment; Nil after 1 year.
    * **ELSS Exception:** SBI Long Term Equity Fund has a mandatory 3-year lock-in with 0% exit load post-lockin.
    * **Transparency:** Deducted automatically from redemption proceeds.
    * **Source Link:** [SBI MF Official Charges Disclosure](https://www.sbimf.com/)
    * *Last checked: October 2026*
    """)

with tab3:
  st.subheader("Model Context Protocol (MCP) Actions & Approval Gateway")
  st.markdown(
      "Review the structured payload below before executing internal tool"
      " logging and email drafting."
  )

  # Payload preview box
  payload_preview = f"""
    - **Date:** {date.today()}
    - **Top Themes:** Pricing Confusion, UI Navigation, Transaction Delays
    - **Identified Fee Issue:** Exit load misunderstanding on equity redemptions
    - **Action Status:** Pending Manager Approval
    """
  st.code(payload_preview, language="markdown")

  # Approval Checkbox
  approval = st.checkbox(
      "✅ I approve logging these insights to internal docs and generating the"
      " support email draft."
  )

  if st.button("Execute MCP Actions"):
    if approval:
      st.success(
          "🎉 Approval granted! MCP workflow executed successfully:"
      )
      st.markdown(
          "- 📄 **Appended to Docs:** Successfully logged entry to Notion /"
          " Google Docs workspace."
      )
      st.markdown(
          "- ✉️ **Email Draft Created:** Generated Gmail draft titled *"
          f"Weekly Product Pulse + Customer Clarification — {date.today()}*"
      )
    else:
      st.warning(
          "⚠️ Approval required! Please check the approval box before"
          " executing MCP actions."
      )
