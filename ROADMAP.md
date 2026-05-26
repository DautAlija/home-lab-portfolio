# Home Lab Portfolio — Project Roadmap

## Overview
A personal cybersecurity home lab simulating real-world attack
scenarios and analyst workflows. Built to develop hands-on skills
in network security, threat detection, incident response, and
security automation.

This roadmap tracks all active and completed work across both
standalone projects and the ongoing home lab build.

---

## Standalone Projects

| # | Project | Priority | Status |
|---|---|---|---|
| 01 | OPNSense Firewall & IDS/IPS Lab | 🔴 High | 🔄 In Progress |
| | ↳ Part 1 — Console Configuration & Network Setup | | ✅ Complete |
| | ↳ Part 2 — Web GUI Configuration | | ✅ Complete |
| | ↳ Part 3 — Firewall Rules & Traffic Control | | 🔄 In Progress |
| | &nbsp;&nbsp;&nbsp;• Default rules review | | ✅ Complete |
| | &nbsp;&nbsp;&nbsp;• Aliases | | ✅ Complete |
| | &nbsp;&nbsp;&nbsp;• Allow/Block HTTP rules | | ✅ Complete |
| | &nbsp;&nbsp;&nbsp;• Firewall log analysis | | ✅ Complete |
| | &nbsp;&nbsp;&nbsp;• Block vs Reject demonstration | | ✅ Complete |
| | &nbsp;&nbsp;&nbsp;• FTP rule | | ✅ Complete |
| | &nbsp;&nbsp;&nbsp;• Telnet rule | | ✅ Complete |
| | &nbsp;&nbsp;&nbsp;• NAT port forwarding | | ⏳ Pending |
| | &nbsp;&nbsp;&nbsp;• Traffic shaping | | ⏳ Pending |
| | ↳ Part 4 — IDS/IPS with Suricata | | ⏳ Pending |
| 02 | HTB CTF — Network Forensics | 🔴 High | ✅ Complete |
| 03 | DVWA — Command Injection & Database Enumeration | 🔴 High | ✅ Complete |
| 04 | Nmap Reconnaissance | 🔴 High | ⏳ Pending |
| 05 | Wireshark HTTP/FTP Analysis | 🔴 High | ⏳ Pending |
| 06 | SQL Injection & Blind SQL Injection | 🟡 Medium | ⏳ Pending |
| 07 | Password Cracking — Hydra | 🟡 Medium | ⏳ Pending |
| 08 | Cryptography — OpenSSL | 🟢 Low | ⏳ Pending |

---

## Home Lab

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

## Tools & Technologies

| Tool | Purpose | Phase |
|---|---|---|
| VMware | Lab virtualization | Phase 0 |
| Kali Linux | Attacker machine | All phases |
| OPNSense | Firewall & IDS/IPS | Phase 0 |
| Wireshark | Network traffic capture | Phase 1, 3 |
| Nmap | Reconnaissance scanning | Phase 1 |
| Splunk | SIEM & log analysis | Phase 1, 2, 3 |
| Hydra | Brute force attacks | Phase 2 |
| Hashcat | Password cracking | Phase 2 |
| Suricata | Intrusion detection | Phase 3 |
| Python | Scripting & automation | Phase 4 |
| Anthropic API | AI automation | Phase 4 |
| GitHub Pages