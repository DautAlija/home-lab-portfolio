# Home Lab Portfolio — Project Roadmap

## Overview
A personal cybersecurity home lab simulating real-world attack
scenarios and analyst workflows. Built to develop hands-on skills
in network security, threat detection, incident response, and
security automation.

**Tools:** VMware · Kali Linux · Splunk · Wireshark · Nmap ·
Hydra · Snort/Suricata · Velociraptor · Python · GitHub

---

## Phase 0 — Environment Setup
> Status: 🔄 In Progress

- [ ] Configure VMware network (attacker, victim, monitoring VMs)
- [ ] Set up Kali Linux as attacker machine
- [ ] Set up Windows 10/11 VM as victim machine
- [ ] Install and configure Splunk on Ubuntu VM
- [ ] Install Suricata as IDS on OPNSense
- [ ] Configure Wireshark on monitoring machine
- [ ] Initialize GitHub repo and establish commit workflow ✅

---

## Phase 1 — Reconnaissance
> Status: ⏳ Not Started

- [ ] Run Nmap scans from Kali against Windows VM
- [ ] Capture traffic in Wireshark
- [ ] Ingest logs into Splunk
- [ ] Analyze and document findings
- [ ] Write Case File 4

---

## Phase 2 — Brute Force Attack
> Status: ⏳ Not Started

- [ ] Simulate brute force login using Hydra
- [ ] Capture failed login events
- [ ] Build Splunk detection rule for brute force pattern
- [ ] Analyze and document findings
- [ ] Write Case File 5

---

## Phase 3 — Data Exfiltration
> Status: ⏳ Not Started

- [ ] Simulate data exfiltration over the network
- [ ] Detect at network level with Wireshark and Suricata
- [ ] Correlate events in Splunk
- [ ] Analyze and document findings
- [ ] Write Case File 6

---

## Phase 4 — AI Automation Layer
> Status: ⏳ Not Started

- [ ] Build Python script to read Splunk alerts
- [ ] Integrate Anthropic API for automated log analysis
- [ ] Auto-generate triage recommendations
- [ ] Auto-generate incident report drafts
- [ ] Document automation workflow

---

## Phase 5 — Portfolio Website
> Status: ⏳ Not Started

- [ ] Build professional site on GitHub Pages
- [ ] Present all case files
- [ ] Document tools, methodology, and findings
- [ ] Add to LinkedIn, resume, Handshake, Indeed

---

## Existing Case Files
| # | Title | Status |
|---|---|---|
| 01 | OPNSense IDS/IPS Lab | 🔄 In Progress |
| 02 | HTB CTF — Network Forensics | 🔄 In Progress |
| 03 | DVWA — Command Injection | 🔄 In Progress |

---

## Notes
*This roadmap is a living document — updated as the project evolves.*