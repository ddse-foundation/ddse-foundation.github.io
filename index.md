---
layout: default
title: Home
nav_order: 1
description: "Decision-Driven Software Engineering for the AI Era"
seo_title: "DDSE: Decision-Driven Software Engineering for Human-AI Collaboration"
permalink: /
---

# Decision-Driven Software Engineering
{: .fs-9 }
A Methodology for Human-AI Collaboration in Software Development
{: .fs-6 .fw-300 }

[Get Started Now]({% link learn-ddse/index.md %}){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[View on GitHub](https://github.com/ddse-foundation/ddse-foundation){: .btn .fs-5 .mb-4 .mb-md-0 }

---

## 🎯 What is DDSE?

**Decision-Driven Software Engineering (DDSE)** is a methodology that integrates structured decision-making into every phase of the software development lifecycle. At its core, DDSE recognizes that **software engineering is fundamentally about making good decisions under uncertainty**—and that these decisions should be captured, reasoned about, and used to guide both human and AI collaboration.

### DDSE in the Software Development Lifecycle

DDSE enhances traditional SDLC phases by embedding decision governance at each stage:

<div class="code-example" markdown="1">

```
Requirements → TDR Creation → Implementation → CI/CD → Maintenance
     ↓              ↓             ↓          ↓         ↓
   AI helps    AI drafts TDRs  AI generates  AI validates  AI suggests
   clarify     Human approves   code with     compliance   updates
   ambiguity   & owns decision  TDR context
```

**📋 Requirements Phase**
- AI assists in clarifying ambiguous requirements and identifying decision points
- Teams create Major Design Decisions (MDDs) for strategic choices
- Business constraints and user needs become structured decision context

**🏗️ Design & Architecture Phase**  
- AI drafts initial Technical Decision Records (TDRs) based on requirements
- **Humans maintain authority** by reviewing, approving, and owning all decisions
- Architectural Decision Records (ADRs) capture system structure and technology choices

**⚙️ Implementation Phase**
- AI generates code using TDR context for consistent, aligned implementation
- Implementation Decision Records (IDRs) guide specific coding patterns
- Decision-driven development ensures AI follows human-defined constraints

**🚀 CI/CD & Testing Phase**
- AI validates code compliance against documented decision criteria
- Automated checks ensure implementation matches decision requirements
- TDRs provide context for automated testing and deployment strategies

**🔧 Maintenance & Evolution Phase**
- AI suggests updates based on changing requirements and decision outcomes
- Decision history provides context for evaluating change impact
- Technical Decision Memos (TDMs) capture incremental decisions and trade-offs

</div>

### DDSE in Agile Development

DDSE seamlessly integrates with Agile methodologies while addressing a critical gap: **decision governance in iterative development**.

**🔄 Sprint Planning**
- User stories include decision context and AI guidance sections
- Teams identify which decisions need TDRs vs. quick TDMs
- Decision backlogs track architectural and technical choice dependencies

**📅 Daily Standups**
- Teams discuss decision blockers alongside traditional impediments  
- AI-generated code reviewed against documented decision criteria
- Decision conflicts identified and escalated for human resolution

**📊 Sprint Reviews & Retrospectives**
- Decision outcomes evaluated alongside feature delivery
- TDR effectiveness measured through implementation consistency
- Team learning captured in updated decision templates and patterns

**🎯 Continuous Improvement**
- Decision quality metrics inform process refinement
- AI collaboration patterns evolve based on TDR usage effectiveness
- Cross-sprint decision context prevents repeated architectural debates

### Core DDSE Principles

1. **Human Authority**: AI accelerates, humans decide
2. **Decision Transparency**: All significant choices documented and reasoned
3. **Context Preservation**: Decision rationale survives beyond the original team
4. **AI Collaboration**: TDRs provide structured context for AI tools
5. **Incremental Adoption**: Start small, scale based on value demonstrated

---

## 🛠️ Contribute with Ready-Made Templates

**DDSE grows stronger with community contributions!** You can help expand the ecosystem by creating base TDR templates for common project types:

### 🌐 **Web Development Templates**
- **Jekyll Static Sites**: Blog-focused MDDs and content strategy ADRs
- **React Applications**: Component architecture and state management decisions  
- **WordPress Sites**: Theme customization and plugin integration patterns
- **Next.js Projects**: SSR/SSG choices and deployment configuration decisions

### 📱 **Mobile Development Templates**
- **React Native Apps**: Cross-platform vs. native decision frameworks
- **Flutter Projects**: Widget architecture and platform-specific adaptations
- **iOS/Android Native**: Platform-specific design pattern decisions

### 🏢 **Enterprise Application Templates**
- **Microservices Architecture**: Service boundary and communication decisions
- **API Gateway Patterns**: Authentication, rate limiting, and routing choices
- **Database Design**: Schema evolution and migration strategy decisions
- **DevOps Integration**: Container orchestration and monitoring decisions

### 🎥 **Check out the Video: How a Task App in Python can be created with TDR templates in minutes**

<div class="video-container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/0IzQgqFSdvo" 
        title="Creating a Python Task App with TDR Templates" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        allowfullscreen>
</iframe>
</div>

### 🤝 **How to Contribute Templates**
1. **Identify a common project type** that needs decision guidance
2. **Create TDR templates** for typical decisions in that domain
3. **Include AI context sections** for tool integration
4. **Submit via GitHub** with examples and usage documentation
5. **Join our community** for collaborative template refinement

[Start Contributing Templates →](https://github.com/ddse-foundation/ddse-foundation){: .btn .btn-purple }

---

## 🚀 Why DDSE Now?

> "In the AI era, human value lies not in being the exclusive generator of solutions, but in being the authoritative decision-maker who guides generation toward human-aligned outcomes."

**AI can generate code faster than humans—but it can't make intelligent decisions about what should be built or why.** Without decision governance, AI-assisted development creates a dangerous gap: rapid implementation without human authority over architectural direction.

### The Problem: AI Speed Without Human Direction
{: .text-red-200}

- ⚠️ **AI generates code without architectural context**
- ⚠️ **Inconsistent patterns across different AI interactions** 
- ⚠️ **No institutional memory of technical decisions**
- ⚠️ **Rapid technical debt accumulation**
- ⚠️ **Lost human oversight in critical technical choices**

### The Solution: Decision-Driven Development
{: .text-green-200}

- ✅ **Technical Decision Records (TDRs) provide AI context**
- ✅ **Consistent implementation patterns across all AI tools**
- ✅ **Preserved decision rationale and trade-offs**
- ✅ **Human authority maintained over architectural direction**
- ✅ **AI accelerates implementation within human-defined constraints**

---

## 🎯 Core DDSE Concepts

<div class="code-example" markdown="1">

### TDR Hierarchy: Structured Decision Authority

**MDD** (Major Design Decisions)
: Strategic product and business constraint decisions

**ADR** (Architectural Decision Records)  
: System structure and technology choices

**EDR** (Engineering Decision Records)
: Cross-cutting implementation approaches

**IDR** (Implementation Decision Records)
: Specific coding patterns and conventions

**TDM** (Technical Decision Memos)
: Quick tactical decisions and trade-offs

</div>

## 🤖 AI Integration in Practice

DDSE transforms AI from an unguided code generator into an intelligent implementation partner:

```yaml
# Example: TDR AI Context Section
ai_context:
  implementation_priority: |
    Focus on user authentication flow first, then task CRUD operations.
    Prioritize security over performance in authentication components.
  
  framework_guidance: |
    Use FastAPI with SQLAlchemy ORM for clean separation of concerns.
    Follow repository pattern for data access abstraction.
  
  constraint_enforcement: |
    MUST validate all inputs using Pydantic models.
    MUST use JWT tokens with 24-hour expiration.
    NEVER store plaintext passwords.
```

When AI tools read this context, they generate code that:
- **Follows your documented patterns** consistently
- **Respects your architectural constraints** automatically  
- **Implements your business rules** correctly
- **Maintains your quality standards** without extra prompting

---

## 🏁 Quick Start Journey

<div class="code-example" markdown="1">

### 5-Minute Setup

1. **Choose your first decision** to document (start small!)
2. **Download a TDR template** for the decision type
3. **Fill in the decision context** including AI guidance
4. **Use the TDR with your AI tools** for aligned implementation
5. **Validate with our compliance checker** for quality assurance

[Start Your DDSE Journey →]({% link learn-ddse/index.md %}){: .btn .btn-green }

</div>

---

## 🌟 Community & Open Source

The DDSE Foundation is a **100% open source initiative** driven by community collaboration. We operate through transparent governance with multiple ways for anyone to participate and contribute to the evolution of decision-driven software engineering.

### 🌟 Open Community Values

- 📖 **Transparent Development**: All decisions, discussions, and development happen in public
- 🤝 **Inclusive Participation**: Everyone can contribute regardless of background or experience level  
- 🎯 **Merit-Based Leadership**: Governance roles earned through community contribution and expertise
- 🔓 **Open Source Everything**: All code, documentation, and research freely available under MIT license

[Join Our Community →](https://github.com/ddse-foundation/ddse-foundation){: .btn .btn-outline }

---

## 🎯 Ready to Start?

<div class="code-example" markdown="1">

**New to DDSE?** → [Learn DDSE Foundations]({% link learn-ddse/index.md %})

**Want to implement?** → [Implementation Guide]({% link implementation/index.md %})

**Need templates?** → [TDR Templates]({% link implementation/templates/index.md %})

</div>

---

*DDSE Foundation: Advancing decision-aware software development for the AI era.*
