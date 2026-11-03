# Weekly Product Pulse: Customer Sentiment & Feedback Analysis

**Period:** August – October 2026  
**Target Product:** Groww (SBI Mutual Fund Integration)  

---

### Executive Summary & Top Themes
Analysis of recent customer reviews reveals significant user friction centered around redemption fee transparency and operational processing:
1. **Exit Load Misunderstanding on SIPs (45% of complaints):** Primary driver of negative 1-star reviews.
2. **SIP Payment-to-NAV Allocation Latency (30%):** Frustration over $T+2$ day NAV settlement delays.
3. **Tax Statement Generation Errors (25%):** Technical failure in opening password-protected CAS files.

---

### Key Supporting User Quotes
* *"I redeemed after 13 months, but 1% exit load was still deducted. Fix this calculation bug!"*
* *"Nobody explained that each monthly SIP installment has its own 1-year timer."*
* *"App showed zero penalty on main screen, but fee was charged on redemption."*

---

### Core Observation
Users conflate **total portfolio age** with **individual SIP unit age**. When redeeming SIP investments after 12 months, units purchased in months 2–12 are still under 365 days old and trigger a 1% exit load penalty under SEBI/SBI MF guidelines.

---

### Recommended Product Action Ideas
1. **Dynamic Pre-Redemption Breakdown:** Implement a real-time fee preview on the redemption confirmation drawer showing exact exit load per unit batch.
2. **SIP Unit FIFO Visualizer:** Add a visual badge indicating how many units are currently "Exit-Load Free" vs. "Exit-Load Applicable".
3. **Contextual Tooltip Nudge:** Display an inline alert: *"Units purchased via SIP within the last 365 days will incur a 1% exit load."*