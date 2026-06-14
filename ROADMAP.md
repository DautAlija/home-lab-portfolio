# Home Lab Portfolio — Project Roadmap

## Overview
A personal cybersecurity portfolio spanning standalone projects,
an on-prem home lab, and a cloud security lab. Built to develop
hands-on skills in network security, threat detection, incident
response, cloud identity, and security automation.

This roadmap tracks all active and completed work across
standalone projects, the on-prem home lab, the cloud security
lab, and ongoing certifications/challenges.

---

## Standalone Projects

| # | Project | Priority | Status |
|---|---|---|---|
| 01 | OPNSense Firewall & IDS/IPS Lab | 🔴 High | 🔄 In Progress |
| | ↳ Part 1 — Console Configuration & Network Setup | | ✅ Complete |
| | ↳ Part 2 — Web GUI Configuration | | ✅ Complete |
| | ↳ Part 3 — Firewall Rules & Traffic Control | | 🔄 In Progress — NAT & traffic shaping remaining |
| | ↳ Part 4 — IDS/IPS with Suricata | | ⏳ Pending |
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

### Phase 0 — Environment Setup
> Status: 🔄 In Progress

- [ ] Configure VMware network (attacker, victim, monitoring VMs)
- [ ] Set up Kali Linux as attacker machine
- [ ] Set up Windows 10/11 VM as victim machine
- [ ] Install and configure Splunk on Ubuntu VM
- [ ] Install Suricata as IDS on OPNSense
- [ ] Configure Wireshark on monitoring machine
- [x] Initialize GitHub repo and establish commit workflow

---

### Phase 1 — Reconnaissance
> Status: ⏳ Not Started

- [ ] Run Nmap scans from Kali against Windows VM
- [ ] Capture traffic in Wireshark
- [ ] Ingest logs into Splunk
- [ ] Analyze and document findings
- [ ] Write Case File 1

---

### Phase 2 — Brute Force Attack
> Status: ⏳ Not Started

- [ ] Simulate brute force login using Hydra
- [ ] Capture failed login events
- [ ] Build Splunk detection rule for brute force pattern
- [ ] Use Hashcat to crack captured hashes
- [ ] Analyze and document findings
- [ ] Write Case File 2

---

### Phase 3 — Data Exfiltration
> Status: ⏳ Not Started

- [ ] Simulate data exfiltration over the network
- [ ] Detect at network level with Wireshark and Suricata
- [ ] Correlate events in Splunk
- [ ] Analyze and document findings
- [ ] Write Case File 3

---

### Phase 4 — AI Automation Layer
> Status: ⏳ Not Started

- [ ] Build Python script to read Splunk alerts
- [ ] Integrate Anthropic API for automated log analysis
- [ ] Auto-generate triage recommendations
- [ ] Auto-generate incident report drafts
- [ ] Document automation workflow

---

### Phase 5 — Portfolio Website
> Status: ⏳ Not Started

- [ ] Build professional site on GitHub Pages
- [ ] Present all case files
- [ ] Document tools, methodology, and findings
- [ ] Add to LinkedIn, resume, Handshake, Indeed

---

## Cloud Security Lab

### Phase 1 — M365 Dev Tenant & Entra ID Setup
> Status: ⏳ Not Started

- [ ] Take Cribl University training and earn Cribl certification
- [ ] Set up free Microsoft 365 Developer sandbox tenant
- [ ] Populate tenant with 10-20 dummy users/groups
- [ ] Configure Conditional Access policies (geo-block, MFA)
- [ ] Document tenant setup and policy configuration

---

### Phase 2 — Cribl.Cloud Pipeline Configuration
> Status: ⏳ Not Started

- [ ] Register app in Entra ID for API access
- [ ] Configure Cribl.Cloud source to ingest Entra ID audit/sign-in logs
- [ ] Build Cribl pipeline — mask PII, drop noisy events
- [ ] Route clean telemetry to a destination (Elastic/Grafana)
- [ ] Document data flow and pipeline configuration

---

### Phase 3 — SOC Simulation & Dashboard
> Status: ⏳ Not Started

- [ ] Trigger Conditional Access violation (VPN, simulated foreign login)
- [ ] Verify event captured and processed through Cribl pipeline
- [ ] Build SOC dashboard from clean telemetry
- [ ] Write up findings as a case file

---

## Certs & Challenges

| Item | Status |
|---|---|
| Timus SASE Certified Specialist | ✅ Complete |
| Cribl Certification | ⏳ Planned (before Cloud Security Lab Phase 2) |
| TryHackMe Rooms | ⏳ Ongoing — alongside other projects |
| BTLO Investigations | ⏳ Ongoing — alongside other projects |

---

## Tools & Technologies

| Tool | Purpose | Area |
|---|---|---|
| VMware | Lab virtualization | Home Lab |
| Kali Linux | Attacker machine | Home Lab |
| OPNSense | Firewall & IDS/IPS | Home Lab |
| Wireshark | Network traffic capture | Home Lab |
| Nmap | Reconnaissance scanning | Home Lab |
| Splunk | SIEM & log analysis | Home Lab |
| Hydra | Brute force attacks | Home Lab |
| Hashcat | Password cracking | Home Lab |
| Suricata | Intrusion detection | Home Lab |
| Python | Scripting & automation | Home Lab |
| Anthropic API | AI automation | Home Lab |
| GitHub Pages | Portfolio website | Home Lab |
| Microsoft Entra ID | Cloud identity & access | Cloud Security Lab |
| Microsoft Graph API | Identity log/data access | Cloud Security Lab |
| Cribl.Cloud | Log pipeline & transformation | Cloud Security Lab |
| M365 Developer Tenant | Sandbox environment | Cloud Security Lab |

---

## Notes
*This roadmap is a living document — updated as the project
evolves. Priority and status updated with every significant push.*