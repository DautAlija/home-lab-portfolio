# Home Lab

## Concept: Build, Break, Detect, Respond, Harden

This lab is built around one full lifecycle instead of five disconnected
exercises. The same environment is used to build real infrastructure,
attack it, detect that attack, automate the response, and then harden
the environment and prove the fix works — mirroring how security work
actually happens in a SOC or a security engineering role, rather than
treating offense and defense as separate projects.

Python is not confined to a single "automation" phase — it's used
throughout: parsing logs, generating detection content, and eventually
driving the incident-response automation in Phase 3. Each phase's
write-up documents where Python is used and why.

## Phases

| Phase | Focus | Status |
|---|---|---|
| [Phase 0 — Environment Setup](./phase-0-environment-setup/) | Network architecture, VM provisioning, Splunk deployment, baseline validation | ✅ Complete |
| Phase 1 — Attack Chain | Full attack chain executed against the lab, mapped to [MITRE ATT&CK](https://attack.mitre.org/) tactics and techniques | ⏳ Planned |
| Phase 2 — Detection Engineering | Detections built in Splunk from Phase 1 telemetry, authored as portable Sigma rules | ⏳ Planned |
| Phase 3 — Security Automation | Python + Anthropic API tooling for automated alert triage and incident response drafting | ⏳ Planned |
| Phase 4 — Hardening & Re-Test | Remediations applied based on Phase 1–3 findings, attack chain re-run to prove the fixes hold | ⏳ Planned |

## Why this structure

Each phase depends on the one before it: there's no attack chain to
detect without a working environment (Phase 0), no detections to
automate around without real attack telemetry (Phase 1 → 2), and no
hardening to validate without something to re-test against (Phase 4
re-runs Phase 1). The goal is a lab that can demonstrate the full
lifecycle of a finding — from "this attack worked" to "here's the
detection, here's the automated response, and here's proof the fix
closes the gap" — rather than a set of isolated tool demos.
