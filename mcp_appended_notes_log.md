# Internal Product Knowledge Base — Appended Entry

**Log Timestamp:** 2026-11-03 20:45:00 IST  
**Logged By:** Product Intelligence Automation Pipeline (MCP Tool)  
**Approval Status:** Approved by PM (`Shasuat`)  

---

```json
{
  "date": "2026-11-03",
  "product_context": "Groww / SBI Mutual Fund",
  "top_themes": [
    "Exit Load Misunderstanding on SIP Redemptions",
    "SIP Payment to NAV Allocation Delay",
    "Capital Gains Statement Download Friction"
  ],
  "weekly_pulse_summary": "High user confusion regarding 1% exit load on SIP redemptions beyond 12 months. Users mistake initial SIP start date for unit maturity date.",
  "identified_fee_issue": "Exit Load calculation misunderstanding on individual SIP installments under 365 days.",
  "action_items": [
    "Build pre-redemption fee calculation preview drawer",
    "Add FIFO unit maturity indicator in holdings tab",
    "Deploy standardized support snippet to help desk tools"
  ],
  "explanation_bullets": [
    "Exit load is 1% if redeemed within 365 days of allotment.",
    "No fee applies to units held for longer than 365 days.",
    "Redemptions follow First-In, First-Out (FIFO) ordering.",
    "Each SIP installment carries its own separate 365-day holding timer.",
    "Exit load fees are credited back to the scheme fund per SEBI rules."
  ],
  "source_links": [
    "https://www.sbimf.com/en-us/equity-schemes/sbi-flexicap-fund",
    "https://www.amfiindia.com/investor-corner/knowledge-center/sip.html"
  ]
}
```