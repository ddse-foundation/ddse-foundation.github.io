---
layout: default
title: What is DDSE?
parent: Getting Started
nav_order: 1
description: "Decision-Driven Software Engineering methodology that puts human decision-making at the center of AI-assisted development through structured Technical Decision Records (TDRs)"
---

# What is DDSE?

Decision-Driven Software Engineering (DDSE) is a methodology that **puts human decision-making at the center of AI-assisted development**. Instead of letting AI tools generate code without context, DDSE ensures every implementation follows documented human decisions about architecture, patterns, and constraints.

## The Core Philosophy

> **Human Intelligence defines WHAT and WHY.  
> Artificial Intelligence accelerates HOW.**

In traditional development, decisions often remain implicit—in senior developers' heads, scattered across chat logs, or buried in code comments. When AI tools join the team, they lack this crucial context and generate solutions that may work but don't align with human intentions.

DDSE makes these decisions **explicit, structured, and AI-accessible** through Technical Decision Records (TDRs).

---

## Why DDSE Matters Now

### The AI Development Challenge

Modern AI coding assistants are incredibly powerful but fundamentally **context-blind**:

- **GitHub Copilot** generates syntactically correct code but doesn't know your architectural constraints
- **ChatGPT** provides working solutions but can't maintain consistency across sessions
- **Claude** understands individual problems but lacks awareness of your system-wide decisions

Without decision governance, AI-assisted development creates:
- ⚠️ **Technical debt** from inconsistent patterns
- ⚠️ **Architectural drift** as AI tools make different assumptions
- ⚠️ **Lost human authority** over critical technical choices
- ⚠️ **Communication breakdowns** between human decisions and AI implementation

### The DDSE Solution

DDSE provides a structured framework where:

✅ **Humans maintain decision authority** through documented TDRs  
✅ **AI tools receive rich context** for aligned implementation  
✅ **Consistency emerges naturally** across all AI interactions  
✅ **Knowledge persists** beyond individual developers or sessions  

---

## Core DDSE Concepts

### 1. Technical Decision Records (TDRs)

TDRs are structured documents that capture technical decisions with specific sections for AI guidance:

```yaml
---
decision_id: "idr-001"
title: "API Input Validation Strategy"
status: "accepted"
decision_type: "implementation"
---

# Decision Context
We need consistent input validation across all API endpoints...

# Decision Outcome
All API endpoints will use Pydantic models for input validation...

# AI Context
ai_context:
  implementation_priority: |
    Implement validation decorators first, then apply to existing endpoints
  framework_guidance: |
    Use FastAPI's dependency injection for reusable validation logic
  constraint_enforcement: |
    MUST return 422 status codes for validation errors
    NEVER accept unvalidated input in any endpoint
```

### 2. Decision Hierarchy

DDSE organizes decisions into a clear hierarchy:

**MDD (Major Design Decisions)**
: Strategic product and business constraints that guide everything else

**ADR (Architectural Decision Records)**
: System structure, technology choices, and cross-cutting concerns

**EDR (Engineering Decision Records)**
: Implementation approaches that span multiple components

**IDR (Implementation Decision Records)**
: Specific coding patterns, conventions, and detailed implementation rules

**TDM (Technical Decision Memos)**
: Quick tactical decisions and trade-offs

### 3. AI Integration Points

Each TDR includes structured AI context that:
- **Guides implementation priority** (what to build first)
- **Recommends frameworks and patterns** (how to build it)
- **Enforces constraints** (what rules must be followed)
- **Provides examples** (concrete implementation patterns)

---

## DDSE in Practice

### Traditional Development Flow
```
Requirements → Design → Implementation → Review → Deploy
     ↓            ↓            ↓           ↓        ↓
  Ambiguous    Mental     Inconsistent  Late    Technical
   details     models      patterns    catches    debt
```

### DDSE Development Flow
```
Requirements → TDR Creation → AI Implementation → Validation → Deploy
     ↓              ↓             ↓            ↓         ↓
   Clarified    Documented   Context-aware   Early     Aligned
   through      decisions    generation     catches   implementation
   TDR process
```

### Example: Before and After

**Before DDSE:**
```javascript
// Different developers, different AI sessions, different patterns:

// Developer A with Copilot
const user = await db.users.findOne({email: email});

// Developer B with ChatGPT  
const user = await User.findByEmail(email);

// Developer C with Claude
const user = await getUserByEmail(email);
```

**After DDSE with IDR-001 "Data Access Patterns":**
```javascript
// All developers, all AI tools, consistent pattern:

// Repository pattern enforced by TDR
const user = await userRepository.findByEmail(email);
```

---

## Key Benefits

### For Teams
- **Faster onboarding**: New developers understand decisions through TDRs
- **Reduced miscommunication**: Explicit decisions prevent assumptions
- **Better AI outcomes**: Context-aware AI generates aligned code
- **Preserved knowledge**: Decision rationale survives team changes

### For Developers  
- **Clearer implementation**: Know exactly what patterns to follow
- **AI amplification**: Tools become smarter with decision context
- **Less rework**: Fewer "that's not how we do it" conversations
- **Better estimates**: Understanding constraints improves planning

### For Organizations
- **Reduced technical debt**: Consistent patterns prevent drift
- **Faster delivery**: AI acceleration within human-defined guardrails
- **Knowledge retention**: Decisions persist beyond individual contributors
- **Quality consistency**: Automated enforcement of human choices

---

## Getting Started

The beauty of DDSE is you can **start small and grow gradually**:

1. **Pick one recent decision** (e.g., "How should we handle errors?")
2. **Document it in a simple TDR** using our templates
3. **Include AI context** for your preferred implementation approach
4. **Use the TDR with your AI tools** in the next coding session
5. **Experience the difference** in code quality and consistency

[Try the Quick Start →]({% link getting-started/quick-start.md %}){: .btn .btn-primary }

---

## Next Steps

- [🚀 Quick Start]({% link getting-started/quick-start.md %}) - Create your first TDR in 5 minutes
- [🧮 ROI Calculator]({% link getting-started/roi-calculator.md %}) - Quantify the benefits
- [📖 Learn DDSE Fundamentals]({% link learn-ddse/manifesto.md %}) - Deep dive into methodology

**DDSE isn't about perfect documentation—it's about better AI collaboration.** Start where it helps most and expand as you see value.
