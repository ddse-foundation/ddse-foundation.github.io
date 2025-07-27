---
layout: default
title: Specification
parent: Learn DDSE
nav_order: 2
description: "Complete technical specification for implementing Decision-Driven Software Engineering"
---

# 📋 DDSE Specification v1.0
{: .no_toc }

## Complete Technical Standards for Decision-Driven Software Engineering

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Document Information

**Document Status**: Final  
**Version**: 1.0  
**Date**: July 26, 2025  
**Maintainer**: DDSE Foundation  
**License**: MIT  

---

## Executive Summary

This specification defines the standards, practices, and organizational structures for implementing Decision-Driven Software Engineering (DDSE) methodology in software projects. DDSE establishes Technical Decision Records (TDRs) as first-class artifacts in the software development lifecycle, ensuring technical decisions are captured, maintained, and enforced throughout the development process.

---

## Core Principles

### Decision-First Development

Every codebase implementing DDSE:
- **MUST** maintain TDRs as primary governance artifacts
- **MUST** link all user stories and tasks to relevant TDRs
- **SHOULD** create TDRs before implementation begins
- **MUST** update TDRs when decisions change

### Single Source of Truth

- TDRs **MUST** reside within the codebase repository
- External tools (Jira, boards) **MUST** reference TDRs via links
- Narrative discussions **MAY** occur in external tools but **MUST** be preserved in structured TDR format

### AI and Human Readable

- All TDRs **MUST** use Markdown format (.md extension)
- Templates **MUST** support automated parsing by AI tools
- Content **MUST** be structured for both human comprehension and machine processing

---

## TDR Framework

### Decision Hierarchy

The DDSE framework defines five types of Technical Decision Records, organized hierarchically:

```
MDD (Major Design Decision)
├── ADR (Architectural Decision Record)
│   ├── EDR (Engineering Decision Record)
│   └── IDR (Implementation Decision Record)
└── TDM (Trade-off Decision Matrix)
```

### TDR Type Definitions

#### Major Design Decision (MDD)
- **Scope**: System-wide strategic decisions
- **Level**: Portfolio/Product level
- **Examples**: Cloud vs On-premise, Buy vs Build, Technology stack selection
- **Authority**: Product owners, CTOs, Enterprise architects
- **Lifecycle**: Long-term (years)

#### Architectural Decision Record (ADR)
- **Scope**: System architecture and cross-cutting concerns
- **Level**: Application/Service level
- **Examples**: Microservices vs Monolith, Database selection, Integration patterns
- **Authority**: Solution architects, Technical leads
- **Lifecycle**: Medium-term (months to years)

#### Engineering Decision Record (EDR)
- **Scope**: Development practices and tooling
- **Level**: Team/Project level
- **Examples**: CI/CD pipeline, Testing strategy, Code standards
- **Authority**: Technical leads, Senior engineers
- **Lifecycle**: Medium-term (sprints to months)

#### Implementation Decision Record (IDR)
- **Scope**: Component-specific implementation choices
- **Level**: Component/Feature level
- **Examples**: Algorithm selection, Library choices, Design patterns
- **Authority**: Feature owners, Developers
- **Lifecycle**: Short-term (sprints to months)

#### Trade-off Decision Matrix (TDM)
- **Scope**: Supporting analysis for any TDR type
- **Level**: Any level
- **Examples**: Framework comparison, Performance analysis, Cost-benefit analysis
- **Authority**: Decision owner or designated analyst
- **Lifecycle**: Point-in-time analysis

---

## Organization Structure

### Recommended: Distributed TDR Structure
```
project-root/
├── tdr/
│   ├── mdd/
│   │   └── mdd-001-cloud-deployment.md
│   └── adr/
│       └── adr-001-microservices-architecture.md
├── src/
│   ├── user-service/
│   │   ├── tdr/
│   │   │   ├── edr-001-user-auth-strategy.md
│   │   │   └── idr-001-password-hashing.md
│   │   └── code/
│   └── payment-service/
│       ├── tdr/
│       │   ├── edr-001-payment-gateway.md
│       │   └── idr-001-transaction-logging.md
│       └── code/
```

### File Naming Convention
- **Format**: `{type}-{sequence}-{title}.md`
- **Examples**: 
  - `mdd-001-cloud-deployment.md`
  - `adr-005-event-driven-architecture.md`
  - `edr-003-ci-cd-pipeline.md`
  - `idr-012-user-validation.md`

---

## Template Standards

### Common Template Structure

All TDR types **MUST** include the following sections for automated parsing:

```yaml
metadata:
  status: [Proposed|Accepted|Superseded|Deprecated]
  date: YYYY-MM-DD
  type: [MDD|ADR|EDR|IDR|TDM]
  decision_owner: string
  reviewers: [list]
  
content:
  title: string
  context: structured_text
  decision: structured_text
  alternatives: [list]
  rationale: structured_text
  consequences: structured_text
  
automation:
  ai_context: structured_summary
  compliance_rules: [list]
  verification_methods: [list]
  
references:
  supersedes: [tdr_ids]
  superseded_by: [tdr_ids]
  related: [tdr_ids]
  depends_on: [tdr_ids]
```

### AI Assistant Integration

Every TDR **MUST** include an AI Assistant Context section:

```markdown
## AI Assistant Context
**Decision Summary**: [One sentence decision summary]
**Key Constraints**: [Comma-separated constraints]
**Required Patterns**: [Patterns to follow]
**Anti-patterns**: [Patterns to avoid]
**Verification Commands**: [Automated checks]
```

---

## Compliance and Governance

### Decision Authority Matrix

| TDR Type | Decision Authority | Approval Required | Review Frequency |
|----------|-------------------|-------------------|-------------------|
| MDD | CTO, Product Owner | Architecture Board | Quarterly |
| ADR | Solution Architect | Tech Lead | Monthly |
| EDR | Tech Lead | Senior Developer | Sprint |
| IDR | Feature Owner | Peer Review | As Needed |

### Automated Compliance

- Implementation **MUST** follow TDR guidelines
- Deviations **MUST** be flagged in CI/CD
- AI agents **SHOULD** monitor architectural drift

---

## Implementation Guidelines

### Adoption Strategy

1. **Phase 1**: Implement ADRs for major architectural decisions
2. **Phase 2**: Add EDRs for engineering practices
3. **Phase 3**: Introduce IDRs for implementation decisions
4. **Phase 4**: Full automation and AI integration

### Quality Metrics

- Completeness score (all sections filled)
- Clarity score (readability analysis)
- Currency score (recency of updates)
- Usage score (reference frequency)

---

## Version Management

### Status Transitions
```
Proposed → Accepted → [Superseded|Deprecated]
```

### Historical Preservation
- Superseded TDRs **MUST** be preserved
- Decision evolution **MUST** be traceable
- Archive policies **SHOULD** be defined

---

## Next Steps

### 🔥 **Understand the Philosophy**
Learn the core principles behind this specification.

[Read the Manifesto →]({% link learn-ddse/manifesto.md %}){: .btn .btn-outline }

### 🧠 **Explore the History**
Understand how decision records evolved in the industry.

[Learn Decision Memory →]({% link learn-ddse/decision-memory.md %}){: .btn .btn-green }

### 🚀 **Start Implementation**
Begin implementing DDSE using this specification.

[Get Started →]({% link implementation/index.md %}){: .btn .btn-primary }

---

*DDSE Specification v1.0 - Building the Foundation for Decision-Driven Development*
