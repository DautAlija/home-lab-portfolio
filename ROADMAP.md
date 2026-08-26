# Home Lab Portfolio — Project Roadmap

## Overview
A personal cybersecurity portfolio spanning standalone projects,
an on-prem home lab, and a cloud security lab. Built to develop
hands-on skills in network security, threat detection, incident
response, cloud identity, and security automation.

---

## Certifications & Challenges

| Item | Status |
|---|---|
| Timus SASE Certified Specialist | ✅ Complete |
| Cribl Certified User (CC User) | ✅ Complete |
| TryHackMe Rooms | ⏳ Planned |
| BTLO Investigations | ⏳ Planned |

---

## Standalone Projects

| # | Project | Priority | Status |
|---|---|---|---|
| 01 | OPNSense Firewall Lab | 🔴 High | ✅ Complete |
| | ↳ Part 1 — Console Configuration & Network Setup | | ✅ Complete |
| | ↳ Part 2 — Web GUI Configuration | | ✅ Complete |
| | ↳ Part 3 — Firewall Rules & Traffic Control | | ✅ Complete |
| 02 | HTB CTF — Network Forensics | 🔴 High | ✅ Complete |
| 03 | DVWA — Command Injection & Database Enumeration | 🔴 High | ✅ Complete |
| 04 | Nmap Reconnaissance | 🔴 High | ⏳ Pending |
| 05 | Wireshark HTTP/FTP Analysis | 🔴 High | ⏳ Pending |
| 06 | SQL Injection & Blind SQL Injection | 🟡 Medium | ⏳ Pending |
| 07 | Password Cracking — Hydra | 🟡 Medium | ⏳ Pending |
| 08 | Cryptography — OpenSSL | 🟢 Low | ⏳ Pending |
| 09 | Active Directory Lab — PowerView, Kerberos, Delegation | 🟢 Low | ⏳ Future |

---

## Home Lab (On-Prem)

Built around one concept: Build, Break, Detect, Respond, Harden. Python
is used throughout every phase below, not just Phase 3.

### Phase 0 — Environment Setup
> Status: ✅ Complete

- [x] Design segmented network (OPNSense gateway + isolated VMnet2 LAN)
- [x] Deploy and configure OPNSense as firewall/router
- [x] Deploy Kali Linux attacker VM
- [x] Deploy Windows 11 victim VM
- [x] Deploy Ubuntu Server monitoring VM
- [x] Install and configure Splunk Enterprise
- [x] Assign static IPs and verify full connectivity
- [x] Take clean baseline snapshots of all four VMs
- [x] Initialize GitHub repo and establish commit workflow

→ [Full write-up](./home-lab/phase-0-environment-setup/)

---

### Phase 1 — Full Attack Chain (MITRE ATT&CK)
> Status: ⏳ Not Started

- [ ] Map planned attack chain to MITRE ATT&CK tactics and techniques
- [ ] Execute reconnaissance against the Windows VM from Kali
- [ ] Achieve initial access / exploitation
- [ ] Demonstrate privilege escalation and/or lateral movement
- [ ] Simulate data exfiltration
- [ ] Document each stage against its ATT&CK technique ID

---

### Phase 2 — Detection Engineering
> Status: ⏳ Not Started

- [ ] Ingest Phase 1 attack telemetry into Splunk
- [ ] Write Sigma rules for each attack stage
- [ ] Convert Sigma rules to Splunk SPL detections
- [ ] Validate detections fire correctly against Phase 1 traffic
- [ ] Document detection coverage against MITRE ATT&CK

---

### Phase 3 — Security Automation
> Status: ⏳ Not Started

- [ ] Build Python tooling to pull alerts from Splunk
- [ ] Integrate the Anthropic API for automated alert triage
- [ ] Auto-generate incident report drafts
- [ ] Auto-generate remediation recommendations
- [ ] Document automation architecture and workflow

---

### Phase 4 — Hardening & Re-Test
> Status: ⏳ Not Started

- [ ] Apply remediations based on Phase 1–3 findings
- [ ] Re-run the Phase 1 attack chain against the hardened environment
- [ ] Confirm detections still fire and/or attacks are blocked
- [ ] Document before/after security posture

---

## Cloud Security Lab

### Phase 1 — M365 Dev Tenant & Entra ID Setup
> Status: 🔄 In Progress

- [x] Complete Cribl University training and earn CC User certification
- [ ] Set up free Microsoft 365 Developer sandbox tenant
- [ ] Populate tenant with 10-20 dummy users and groups
- [ ] Configure Conditional Access policies (geo-block, MFA)
- [ ] Document tenant setup and policy configuration

---

### Phase 2 — Cribl.Cloud Pipeline Configuration
> Status: ⏳ Not Started

- [ ] Register app in Entra ID for API access
- [ ] Configure Cribl.Cloud source to ingest Entra ID audit/sign-in logs
- [ ] Build Cribl pipeline — mask PII, drop noisy events
- [ ] Route clean telemetry to destination
- [ ] Document data flow and pipeline configuration

---

### Phase 3 — SOC Simulation & Dashboard
> Status: ⏳ Not Started

- [ ] Trigger Conditional Access violation via VPN
- [ ] Verify event captured and processed through Cribl pipeline
- [ ] Build SOC dashboard from clean telemetry
- [ ] Write up findings as a professional case file

---

## Notes
*This roadmap is a living document — updated as the project
evolves. Priority and status updated with every significant push.*