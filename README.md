# gigshield-devtrails2026
AI-Powered Parametric Insurance for Q-Commerce Delivery Partners
# 🛡️ GigShield — AI-Powered Parametric Income Insurance for Grocery & Q-Commerce Delivery Partners

> **Guidewire DEVTrails 2026 | Phase 1 Submission**
> Platform: Web + Mobile | Persona: Grocery / Q-Commerce (Zepto, Blinkit, Swiggy Instamart)

---

## 📌 Table of Contents

1. [Problem Statement](#1-problem-statement)
2. [Our Solution](#2-our-solution)
3. [Persona & Scenarios](#3-persona--scenarios)
4. [Application Workflow](#4-application-workflow)
5. [Weekly Premium Model](#5-weekly-premium-model)
6. [Parametric Triggers](#6-parametric-triggers)
7. [Platform Choice — Web + Mobile](#7-platform-choice--web--mobile)
8. [AI/ML Integration Plan](#8-aiml-integration-plan)
9. [Tech Stack](#9-tech-stack)
10. [Development Plan](#10-development-plan)
11. [Team](#11-team)

---

## 1. Problem Statement

India's Q-Commerce sector (Zepto, Blinkit, Swiggy Instamart) runs on 10-minute delivery promises, placing grocery delivery partners under intense pressure to stay active across all conditions. Unlike food delivery, Q-Commerce workers operate on **hyperlocal, time-critical routes** — meaning even a 2-hour disruption wipes out their entire peak earning window.

External disruptions — extreme heat, flash floods, poor AQI, curfews, or sudden zone closures — can force these workers off the road entirely, causing **20–30% income loss per week** with no safety net of any kind. GigShield exists to fix that.

---

## 2. Our Solution

**GigShield** is an AI-enabled parametric income insurance platform built exclusively for Q-Commerce delivery partners. It automatically monitors external disruption signals and triggers instant, no-claim-needed payouts when a worker's earning capacity is demonstrably impaired by events outside their control.

**What makes it parametric:** Payouts are triggered by objective, verifiable data (weather API readings, AQI levels, traffic zone alerts) — not by the worker filing a manual claim. When the trigger fires, the money moves.

**What GigShield does NOT cover:** health, life, accidents, vehicle repairs, or personal decisions. Coverage is for **lost income from external disruptions only**.

---

## 3. Persona & Scenarios

### Primary Persona: Ravi, Blinkit Delivery Partner — Bengaluru

- Works 9–10 hours/day, ~6 days/week
- Average weekly earnings: ₹4,000–₹6,000
- Operates across 2–3 hyperlocal zones (2–5 km radius per zone)
- Peak hours: 8–11 AM, 6–10 PM — disruptions during these windows hit hardest
- No savings buffer; income is week-to-week

### Scenario A — Flash Flood / Heavy Rain

> Bengaluru receives an IMD red alert. Ravi's zone (Koramangala) sees rainfall >50mm in 3 hours. Roads flood, platform orders drop to near zero. Ravi cannot ride.
>
> **GigShield Response:** Weather API confirms red-alert rainfall threshold crossed in Ravi's registered zone. Parametric trigger fires. ₹350 automatic payout (partial-day loss) credited to Ravi's UPI ID within minutes. No claim filed. No documents uploaded.

### Scenario B — Extreme Heat (AQI / Temperature)

> May afternoon in Delhi NCR. Temperature hits 46°C. Outdoor work becomes medically unsafe (per IMD heat action plan). Zepto partner Amir stops working at 1 PM.
>
> **GigShield Response:** Temperature API confirms >44°C sustained for 2+ hours during Amir's active shift window. Trigger fires. Daily partial payout processed automatically.

### Scenario C — Sudden Zone Closure / Local Strike

> A bandh is called in parts of Pune. Specific delivery zones are locked down by local administration. Swiggy Instamart's own API shows zero active orders in that zone.
>
> **GigShield Response:** Platform activity signal + geo-zone alert confirms zone-level disruption. Trigger fires for all active GigShield-enrolled workers in that zone.

### Scenario D — Severe Pollution (AQI)

> Delhi's AQI hits 400+ (Severe). GRAP Stage IV restrictions are imposed. Outdoor delivery is legally restricted or dangerous.
>
> **GigShield Response:** CPCB/IQAir API confirms AQI ≥ 400 in worker's city zone. Trigger fires for enrolled workers in affected zones.

---

## 4. Application Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                      WORKER JOURNEY                         │
│                                                             │
│  1. ONBOARDING (5 min, mobile-first)                        │
│     → Phone number + OTP login                              │
│     → Platform selection (Zepto / Blinkit / Instamart)     │
│     → Zone registration (GPS-verified)                      │
│     → Income baseline (avg weekly earnings, self-reported)  │
│     → AI risk profile generated                             │
│                                                             │
│  2. POLICY CREATION                                         │
│     → Worker selects weekly coverage tier                   │
│     → AI shows dynamic premium based on risk profile        │
│     → Worker pays weekly premium (UPI / wallet)             │
│     → Policy active for 7 days                              │
│                                                             │
│  3. LIVE MONITORING (Automated, background)                 │
│     → Weather / AQI / traffic APIs polled every 15 min      │
│     → Worker GPS activity cross-checked (fraud prevention)  │
│     → Zone-level disruption score updated in real-time      │
│                                                             │
│  4. TRIGGER & CLAIM (Zero-touch)                            │
│     → Disruption threshold crossed in worker's zone         │
│     → AI fraud check runs (location, activity, duplicates)  │
│     → Payout amount calculated (hours lost × daily rate)    │
│     → UPI transfer initiated — settled within minutes       │
│     → Worker notified via push notification                 │
│                                                             │
│  5. DASHBOARD                                               │
│     → Worker: active policy, earnings protected, payout     │
│       history                                               │
│     → Admin: disruption heat maps, loss ratios, fraud       │
│       flags, predictive next-week risk index                │
└─────────────────────────────────────────────────────────────┘
```

---

## 5. Weekly Premium Model

### Design Philosophy

Q-Commerce workers earn and spend week-to-week. Monthly premiums create a drop-off problem — workers won't pay ₹200 upfront for a month of coverage. A ₹40–60/week premium fits naturally into their income cycle and mirrors how they already think about earnings.

### Premium Tiers

| Tier | Weekly Premium | Max Weekly Payout | Ideal For |
|------|---------------|-------------------|-----------|
| Basic Shield | ₹35 | ₹800 | New workers, low-risk zones |
| Standard Shield | ₹55 | ₹1,500 | Regular full-time workers |
| Pro Shield | ₹85 | ₹2,500 | High-earning, high-risk zone workers |

> ⚠️ Coverage is for **lost income only**. No health, accident, or vehicle payouts under any tier.

### Dynamic Premium Calculation (AI-Adjusted)

The base tier price is adjusted weekly by the AI risk engine based on:

| Factor | Adjustment |
|--------|------------|
| Historical disruption frequency in worker's zone | ±₹5–15 |
| Current week's weather forecast severity | ±₹3–10 |
| Worker's claim history (fraud signal) | +₹5–20 |
| Low-risk zone bonus (historically safe) | −₹2–8 |
| Platform activity consistency (trust score) | −₹2–5 |

**Example:** Ravi (Koramangala, Bengaluru) in July during monsoon peak → Standard Shield base ₹55 + monsoon adjustment +₹12 = **₹67/week**. The app explains every adjustment transparently.

### Payout Formula

```
Daily Payout = (Weekly Earnings Baseline / 6 working days) × disruption_severity_coefficient

disruption_severity_coefficient:
  - Partial disruption (2–4 hrs affected): 0.3
  - Major disruption (4–6 hrs affected):   0.5
  - Full-day disruption (6+ hrs affected): 0.8

Weekly payout is capped at the tier's Max Weekly Payout.
```

---

## 6. Parametric Triggers

These are the objective, API-verified thresholds that automatically initiate a payout. Workers do not need to file a claim.

| # | Trigger Name | Data Source | Threshold | Severity |
|---|-------------|------------|-----------|---------|
| T1 | Heavy Rain / Flood | OpenWeatherMap / IMD | Rainfall ≥ 35mm/3hrs OR IMD Orange/Red alert active in zone | Major / Full-day |
| T2 | Extreme Heat | OpenWeatherMap / IMD | Temperature ≥ 44°C sustained for ≥ 2hrs during 10AM–5PM | Partial / Major |
| T3 | Severe Air Pollution | CPCB AQI API / IQAir | AQI ≥ 400 (Severe) sustained ≥ 3hrs in worker's city zone | Major |
| T4 | Zone Closure / Curfew | Platform API (mock) + Govt alert feed | Zero orders in worker's registered zone for ≥ 2hrs during peak hours | Major / Full-day |
| T5 | Platform Outage | Platform API heartbeat (mock) | Platform app/API unavailable for ≥ 1.5hrs during peak window | Partial |

> **Note:** All triggers are zone-specific. A flood in Indiranagar does not trigger payouts for a worker active in Whitefield. GPS zone matching is mandatory.

---

## 7. Platform Choice — Web + Mobile

### Why Both?

**Mobile App (Flutter)** is the primary worker-facing surface. Q-Commerce partners are mobile-native — they onboard, check policy status, and receive payout notifications entirely on their phones. A Flutter app gives us a single codebase for Android and iOS with native GPS, push notifications, and UPI deep-links.

**Web App (React / Next.js)** serves two purposes:
1. **Admin / Insurer Dashboard** — complex analytics, fraud review queues, and disruption heat maps are better suited to a desktop interface for operations teams.
2. **Worker Web Portal** — for workers who prefer browser access, or for onboarding flows that require document verification on a larger screen.

This dual approach ensures we don't sacrifice UX for either the end-worker or the insurer operations team.

---

## 8. AI/ML Integration Plan

### 8.1 Dynamic Premium Calculation (Risk Scoring Model)

**Approach:** A gradient-boosted regression model (XGBoost / scikit-learn) trained on:
- Historical weather disruption data by city zone (IMD archives)
- Platform order volume fluctuations during past disruption events (mocked for prototype)
- Worker zone, tenure, and claim history

**Output:** A weekly risk score (0–100) per worker, mapped to a premium adjustment multiplier.

**Implementation:** Served via a FastAPI endpoint. Called during policy creation and refreshed every Sunday for the upcoming week's premium.

### 8.2 Fraud Detection Engine

**Approach:** A rule-based anomaly detection layer combined with an isolation forest model:

| Check | Method |
|-------|--------|
| **GPS spoofing detection** | Cross-validate worker's last known GPS coordinates against claimed disruption zone. If worker was 15+ km away from the triggered zone, flag as anomaly. |
| **Activity paradox check** | If worker's platform shows active deliveries during a supposed disruption window, payout is blocked and flagged for review. |
| **Duplicate claim prevention** | Hash-based deduplication on (worker_id, zone_id, trigger_id, date). Identical claim signatures are auto-rejected. |
| **Frequency anomaly** | Isolation forest flags workers claiming significantly more disruption days than zone peers. Sent to manual review queue. |

### 8.3 Predictive Disruption Index (Admin Dashboard)

**Approach:** A lightweight LSTM or ARIMA model forecasting next week's likely disruption probability per city zone, using:
- 3-year IMD rainfall / temperature historical data
- AQI seasonal trends
- Local event calendars (bandh/strike patterns — rule-based)

**Output:** A "Next Week Risk Index" heatmap on the insurer dashboard, helping operations teams pre-position reserves.

### 8.4 Onboarding Income Baseline Estimation

**Approach:** When a worker self-reports income, the AI cross-references it against:
- Platform tier averages for their city/zone (mocked data)
- Working hours declared vs. zone order density

If the declared income is a significant outlier, the system flags it and prompts re-verification — preventing over-insurance fraud at onboarding.

---

## 9. Tech Stack

```
┌─────────────────────────────────────────────────┐
│                   FRONTEND                      │
│  Web (Admin + Worker Portal): React / Next.js   │
│  Mobile (Worker App): Flutter (Android + iOS)   │
│  State Management: Zustand (web), Riverpod (mob)│
└──────────────────────┬──────────────────────────┘
                       │ REST / WebSocket
┌──────────────────────▼──────────────────────────┐
│                   BACKEND                       │
│  API Layer: Python / FastAPI                    │
│  Auth: JWT + OTP (Firebase Auth or custom)      │
│  Task Queue: Celery + Redis (trigger monitoring)│
│  Real-time alerts: WebSocket (FastAPI native)   │
└──────────────────────┬──────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────┐
│                  AI / ML LAYER                  │
│  Framework: scikit-learn, XGBoost               │
│  Anomaly Detection: Isolation Forest            │
│  Model Serving: FastAPI ML endpoints            │
│  Forecasting: statsmodels ARIMA (Phase 3)       │
└──────────────────────┬──────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────┐
│              DATA & INTEGRATIONS                │
│  Database: PostgreSQL (primary)                 │
│  Cache: Redis                                   │
│  Weather API: OpenWeatherMap (free tier)        │
│  AQI API: CPCB / IQAir (free tier)             │
│  Platform API: Mocked (FastAPI mock server)     │
│  Payment: Razorpay Test Mode / UPI Simulator    │
└─────────────────────────────────────────────────┘
```

### Why This Stack?

- **FastAPI** is async-native and perfect for real-time trigger monitoring. Python's ML ecosystem (scikit-learn, XGBoost) integrates naturally without a separate model-serving layer in early phases.
- **React / Next.js** gives us SSR for the admin dashboard (SEO not needed, but fast initial loads matter for data-heavy dashboards) and a clean component model for complex UI.
- **Flutter** avoids maintaining two separate mobile codebases. Single Dart codebase ships to both Android (primary) and iOS.
- **PostgreSQL** handles relational insurance data (policies, claims, payouts) reliably with ACID guarantees.
- **Celery + Redis** handles the background trigger monitoring loop — polling weather APIs every 15 minutes without blocking the main API.

---

## 10. Development Plan

### Phase 1 (Weeks 1–2): Ideation & Foundation
- [x] Persona research and scenario definition
- [x] Premium model design and trigger specification
- [x] Tech stack finalization
- [ ] Repository structure setup
- [ ] Database schema design (workers, policies, claims, payouts, trigger_logs)
- [ ] Basic FastAPI project scaffold
- [ ] Basic Flutter app scaffold (onboarding screens, wireframes)

### Phase 2 (Weeks 3–4): Automation & Protection
- [ ] Worker registration and OTP login (Flutter + FastAPI)
- [ ] Policy creation flow with dynamic premium display
- [ ] Weather + AQI API integration (real data in worker zone)
- [ ] Parametric trigger engine (Celery polling loop, 3–5 triggers live)
- [ ] Fraud detection Layer 1 (GPS zone match, duplicate prevention)
- [ ] Claims management module + mock Razorpay payout
- [ ] Basic worker dashboard (active policy, payout history)

### Phase 3 (Weeks 5–6): Scale & Optimise
- [ ] Advanced fraud detection (isolation forest, activity paradox)
- [ ] Predictive disruption index (ARIMA model, admin dashboard heatmap)
- [ ] Full insurer admin dashboard (loss ratios, fraud queue, analytics)
- [ ] UPI simulator / Razorpay test mode full integration
- [ ] Performance testing and load optimisation
- [ ] Final pitch deck and 5-minute demo video

---

## 11. Team

|         Name         |                           |     Role    |
|------------------|                               |-------------|
| *(Twinkle Das)* |                                |Backend / AI-ML |
| *(Darshan Lathi)* |                              |Frontend / React |
| *(ShuchiShubhra Sahu)* |                         |Mobile / Flutter |
| *(Smita Samal)* |                                |Full-stack / DevOps|
| *(SoumyaRanjan Sethi)* |                         |Product / UI-UX |

---

> *GigShield — Because every delivery matters, and every rupee lost to a rainstorm shouldn't be.*
