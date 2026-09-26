# VoltRelay-Hackathon

# VoltRelay Energy — Data Analytics Hackathon

## 📊 Project Overview

VoltRelay Energy is a synthetic battery-swapping network operating across six Indian cities.

This project analyzes millions of operational records to understand:

- Network performance
- Swap failures and service issues
- Station and geographic patterns
- Battery and equipment performance
- Pricing and partner economics
- Rider retention and customer experience

The objective is to transform raw operational data into actionable business insights that can help improve service reliability, operational efficiency, and customer experience.

---

## 🎯 Business Problem

Battery-swapping networks need to maintain high availability while managing stations, batteries, riders, pricing, and operational constraints.

The analysis focuses on answering six key business questions:

1. How is the overall network performing?
2. Where and when are swap failures occurring?
3. Which cities and stations experience higher service issues?
4. Are certain battery or equipment groups associated with poorer performance?
5. How do pricing structures and partner transactions affect economics?
6. What patterns are visible in rider retention and customer experience?

---

## 📁 Project Structure

```text
VoltRelay_Hackathon/
│
├── data/
│   ├── swap_events.csv
│   ├── station_hourly_status.csv
│   ├── riders.csv
│   ├── batteries.csv
│   ├── support_tickets.csv
│   ├── stations.csv
│   ├── city_daily_context.csv
│   └── fleet_partners.csv
│
├── notebooks/
│   └── VoltRelay_Analysis.ipynb
│
├── src/
│   ├── data_cleaning.py
│   ├── metrics.py
│   └── analysis.py
│
├── outputs/
│   ├── charts/
│   └── tables/
│
├── analysis/
│   └── VoltRelay_Analysis_Report.docx
│
├── requirements.txt
│
└── README.md
