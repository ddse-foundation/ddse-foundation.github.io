---
title: "Domain-Focused Starter Packs"
description: "Learn how to create and contribute domain-focused starter packs that transform architectural expertise into reusable, AI-powered blueprints"
layout: default
parent: "Join the DDSE Community"
nav_order: 1
---

# Domain-Focused Starter Packs
## Building the Architectural Wisdom Library

*Transform your hard-won architectural decisions into reusable blueprints that power the next generation of AI-assisted development*

---

## The New Reality: AI Writes Code Faster Than We Can Govern It

Large language model copilots can scaffold a REST service in seconds, yet post-mortems still reveal outages caused by missing rate-limits, unencrypted PII, or silently divergent microservices. What failed wasn't the generator—it was the **decision memory** that never made it into the prompt. Senior architects know the trade-offs, but those nuances live in diagrams, Slack threads, or tribal lore, invisible to AI and new hires alike.

> **The critical question**: *If your carefully argued architecture choice isn't machine-readable, does it even exist in 2025?*

This is where **Domain-Focused Starter Packs** emerge as the solution. They capture architectural wisdom in machine-readable TDRs (Technical Decision Records) that both humans and AI can consume, creating a shared library where expertise compounds rather than remains trapped in individual minds.

---

## What Is a Domain-Focused Starter Pack?

A **Domain-Focused Starter Pack** is a curated collection of TDRs that encodes the architectural decisions for a specific domain or use case. Each pack includes:

### Core Components

**1. TDR Collection**
- Complete decision hierarchy (MDD → ADR → EDR → IDR)
- YAML front-matter with structured metadata
- Rich `ai_context` blocks for code generation
- Clear rationale and consequence documentation

**2. Generator Script**
- Automated code generation from TDR decisions
- Framework-agnostic approach with customizable outputs
- Integration with popular LLMs and development tools
- Validation and testing automation

**3. Domain Expertise**
- Battle-tested patterns from production environments
- Industry-specific compliance and security considerations
- Performance optimization strategies
- Common pitfall avoidance

**4. Community Integration**
- Peer review process for quality assurance
- Version control and semantic versioning
- Documentation and usage examples
- Contribution guidelines and maintenance

### The Community Vision

Think Terraform modules or AWS Marketplace AMIs—except the unit of reuse is **decision intelligence**. The more high-quality packs exist, the easier it becomes for organizations to compose entire platforms by mixing and matching domain blueprints:

- Plug in **E-Commerce Checkout TDRs**
- Wire them to **Tax-Calculation EDRs** 
- Layer on **PCI-Compliance ADRs**
- Let AI stitch the implementation code

Contributors effectively stock the shelves of an open source library where architectural wisdom is shared instead of yet another NPM package.

---

## Why This Matters Now: The Four Critical Drivers

### 1. Audit & Compliance Pressure
Regulated sectors are under increasing pressure to show **why** a design is secure, not merely **that** it is. TDRs provide a searchable, signed decision trail that satisfies auditors and supports compliance frameworks like SOX, GDPR, and HIPAA.

### 2. Onboarding Speed Crisis
New team members traditionally shadow seniors for weeks to understand architectural context. With TDR packs, they can read the decision chain and understand the architecture in 30 minutes instead of 30 days.

### 3. Prompt Grounding Revolution
The same YAML that documents decisions drives your copilot's context window, dramatically reducing hallucinations and ensuring generated code follows established patterns rather than inventing new ones.

### 4. Continuous Architecture Demand
When requirements change, you update a decision file, not dozens of wikis scattered across tools. AI handles the ripple effect in code, keeping implementation aligned with evolving intent.

---

## Priority Domains: Where to Make the Biggest Impact

Based on community feedback and industry trends, three domains promise disproportionate impact for early starter pack contributions:

### 1. AI-Agent Service Pack ⭐ **Highest Priority**

**Why Critical**: Agentic workflows are exploding across industries, but decisions about tool caching, memory management, and guard-rails are being re-discovered by every team.

**Key Decisions to Encode**:
- **Memory Architecture**: Short-term vs long-term storage, privacy boundaries
- **Tool Integration**: Rate limiting, sandboxing, error handling
- **Guard Rails**: Content filtering, cost controls, execution timeouts
- **Monitoring**: Token usage tracking, performance metrics, failure analysis

**Target Demo**: Agent spins up, answers a complex question with multiple tool calls, passes security lint checks, operates within cost budgets.

**Implementation Patterns**:
- LangGraph-based orchestration
- ReAct (Reasoning + Acting) patterns
- Function calling with external APIs
- Streaming responses with real-time updates

### 2. RAG Service Pack ⭐ **High Priority**

**Why Critical**: 70% of GenAI POCs in 2025 are RAG-based, but most fail under load due to poor architectural decisions about chunking, embedding, and query ranking.

**Key Decisions to Encode**:
- **Chunking Strategy**: Document segmentation, overlap policies, metadata preservation
- **Vector Storage**: Database selection, indexing strategies, similarity metrics
- **Retrieval Logic**: Hybrid search, re-ranking, relevance thresholds
- **Response Generation**: Context window management, citation formatting, hallucination detection

**Target Demo**: CLI ingests PDF → API responds with grounded answer, latency < 200ms, proper citations included.

**Implementation Patterns**:
- Vector database integration (Pinecone, Chroma, PGVector)
- Embedding model selection and optimization
- Query preprocessing and expansion
- Response quality validation

### 3. E-Commerce Micro-Stack Pack ⭐ **High Priority**

**Why Critical**: Cart logic, payment orchestration, and inventory management represent well-understood domain problems that every startup re-discovers, often with preventable security and scalability issues.

**Key Decisions to Encode**:
- **Catalog Management**: Product hierarchies, search indexing, pricing strategies
- **Cart Logic**: Session management, reservation timeouts, quantity limits
- **Payment Orchestration**: Provider selection, PCI compliance, retry logic
- **Inventory Tracking**: Consistency models, reservation systems, fraud detection

**Target Demo**: Swagger UI showing product search, add-to-cart workflow, Stripe test charge completion.

**Implementation Patterns**:
- Event-driven architecture for inventory updates
- Saga patterns for distributed transactions
- API gateway for service composition
- Caching strategies for catalog performance

---

## Secondary Domains: Next Wave Opportunities

### Fintech Core Ledger Pack
Double-entry accounting, PCI-compliant token storage, reconciliation batch jobs, regulatory reporting frameworks.

### Healthcare Compliance Pack
HIPAA-ready architectures, clinical workflow patterns, patient data anonymization, audit trail requirements.

### IoT/Edge Computing Pack
Device management, telemetry collection, real-time processing, offline synchronization patterns.

### Enterprise Integration Pack
API gateway patterns, event streaming, legacy system integration, enterprise security models.

---

## Anatomy of a Gold-Standard Starter Pack

Creating a professional-quality starter pack requires attention to several key elements:

### 1. Folder Structure
```
example/<domain>-app-tdr-only/
├── README.md                    # Overview and quick start
├── docs/                        # Detailed documentation
├── tdrs/                        # Decision records
│   ├── mdd/                     # Meta-decisions
│   ├── adr/                     # Architectural decisions
│   ├── edr/                     # Engineering decisions
│   └── idr/                     # Implementation decisions
├── generate.py                  # Code generation script
├── validate.py                  # TDR validation
├── demo/                        # Generated example output
└── media/                       # Screenshots, videos
```

### 2. YAML Discipline
Every TDR must pass the open-source ANTLR validator in CI. This ensures:
- Consistent metadata structure
- Valid YAML syntax
- Required field completion
- Proper decision hierarchy

### 3. Rich AI Context Blocks
The `ai_context` section is crucial for effective code generation:

```yaml
ai_context:
  implementation_priorities:
    - "Prioritize security over performance for authentication"
    - "Use async patterns for all external API calls"
  
  framework_hints:
    python: "Use FastAPI with Pydantic models"
    javascript: "Use Express.js with TypeScript"
  
  security_constraints:
    - "All passwords must use bcrypt with salt rounds >= 12"
    - "API keys must be stored in environment variables"
  
  performance_requirements:
    - "Authentication response time < 100ms"
    - "Support 1000 concurrent users"
```

### 4. Generator Script Excellence
The generator script should be:
- **Single Command**: `python generate.py` or `make generate`
- **Framework Flexible**: Support multiple output targets
- **Well Documented**: Clear usage instructions and examples
- **Error Handled**: Graceful failure with helpful messages

### 5. Demo Documentation
Create clear demonstration materials showing:
1. Pack overview and key TDR files
2. Generator command usage
3. Generated code structure walkthrough
4. Application functionality demonstration

> **📹 Looking for Contributors**: We're seeking community members to create video tutorials and interactive demos for starter packs. If you're interested in contributing educational content, please join (https://github.com/ddse-foundation/ddse-foundation).

### 6. Licensing & Attribution
- **MIT License**: Ensures broad adoption and remixing
- **Clear Attribution**: Author credit in metadata and README
- **Contribution Guidelines**: How others can improve the pack
- **Version History**: Semantic versioning for decision evolution

---

## Step-by-Step Creation Guide

### Phase 1: Planning and Research 

**1. Domain Selection**
- Choose a domain you know deeply from production experience
- Verify there's genuine demand (check community discussions)
- Ensure the scope is manageable but non-trivial

**2. Decision Inventory**
- List the 10-20 most critical decisions in your domain
- Group them by TDR type (MDD, ADR, EDR, IDR)
- Identify dependencies between decisions

**3. Reference Architecture**
- Sketch the high-level system architecture
- Identify major components and their interactions
- Document key quality attributes and constraints

### Phase 2: TDR Creation 

**1. Start with Meta-Decisions (MDD)**
```yaml
---
id: MDD-001
title: "Domain Scope and Boundaries"
status: "accepted"
date: "2025-01-15"
authors: ["jane.architect@company.com"]
category: "scope"

ai_context:
  domain_boundaries: "E-commerce checkout and payment processing"
  excluded_concerns: "Inventory management, shipping, tax calculation"
  target_scale: "10,000 orders per day, sub-second response times"
---

# Context
This pack focuses specifically on the checkout and payment flow...

# Decision
We will include cart management, payment orchestration, and order confirmation...

# Consequences
Teams using this pack will need separate solutions for inventory and shipping...
```

**2. Define Architecture (ADR)**
Focus on the fundamental structural decisions:
- Service boundaries and communication patterns
- Data storage and consistency models
- Security and authentication approaches
- Scalability and performance strategies

**3. Specify Engineering Standards (EDR)**
Document the engineering practices:
- Testing strategies and coverage requirements
- Deployment and CI/CD patterns
- Monitoring and observability approaches
- Error handling and resilience patterns

**4. Detail Implementation Choices (IDR)**
Cover the specific technical decisions:
- Framework and library selections
- Configuration management approaches
- Third-party service integrations
- Code organization and structure

### Phase 3: Generator Development 

**1. Choose Your Generation Strategy**
```python
# Simple LLM-based generation
def generate_code(tdr_context, target_framework):
    prompt = build_prompt(tdr_context, target_framework)
    response = llm_client.complete(prompt)
    return parse_and_validate(response)

# Template-based generation with AI enhancement
def generate_code(tdr_context, target_framework):
    base_template = load_template(target_framework)
    enhanced_template = enhance_with_ai(base_template, tdr_context)
    return render_template(enhanced_template, tdr_context)
```

**2. Implement Core Generation Logic**
- Parse TDR files and extract decision context
- Build comprehensive prompts with architectural constraints
- Generate code for multiple target frameworks
- Validate generated code for syntax and basic functionality

**3. Add Validation and Testing**
- Verify generated code compiles/runs successfully
- Check adherence to documented decisions
- Validate security and performance characteristics
- Ensure test coverage meets specified requirements

### 4. Documentation and Demo 

**1. Comprehensive README**

- Clear value proposition and use cases
- Quick start guide with minimal steps
- Detailed decision rationale and trade-offs
- Customization and extension instructions

**2. Demonstration Materials**

- Written walkthrough of pack usage
- Generated code examples and explanations
- Usage instructions and common patterns
- Clear documentation of expected outcomes

> **📹 Looking for Contributors**: We're seeking community members to create video tutorials and interactive demos for starter packs. If you're interested in contributing educational content, please join our [community](https://github.com/ddse-foundation/ddse-foundation).

**3. Example Deployments**

- Include generated code examples
- Provide Docker containers for easy testing
- Document deployment to common platforms
- Include performance benchmarks where relevant

---

## Contribution Workflow: From Idea to Community Asset

### Step 1: Community Engagement
**Before writing any code**, engage with the community:

1. **Join the Community**: Visit [GitHub](https://github.com/ddse-foundation/ddse-foundation) and introduce your pack idea
2. **Validate Demand**: Get feedback from potential users and domain experts
3. **Check for Overlap**: Ensure you're not duplicating existing efforts
4. **Find Collaborators**: Connect with others interested in your domain

### Step 2: Repository Setup
```bash
# Fork and clone the main repository
git clone https://github.com/your-username/ddse-foundation.git
cd ddse-foundation

# Create your pack directory
mkdir -p example/my-domain-app-tdr-only
cd example/my-domain-app-tdr-only

# Initialize pack structure
cp -r ../task-app-tdr-only/* .  # Use task-app as template
```

### Step 3: Development Process
1. **Iterative TDR Development**: Start with core decisions, expand gradually
2. **Early Validation**: Test generator with minimal TDR set
3. **Community Feedback**: Share work-in-progress for early input
4. **Quality Assurance**: Run validation tools and peer review

### Step 4: Pull Request Submission
Your PR should include:
- Complete TDR set with validation passing
- Working generator with clear documentation
- Demo video showing end-to-end workflow
- Comprehensive README with usage instructions

### Step 5: Community Review
Expect feedback on:
- **Decision Quality**: Are the architectural choices sound?
- **Completeness**: Does the pack cover the essential domain concerns?
- **Usability**: Can others successfully use and extend the pack?
- **Documentation**: Is everything clearly explained and demonstrated?

---

## Learning from the Task-App Example

The [Task-App example](https://github.com/ddse-foundation/ddse-foundation/tree/main/example/task-app-tdr-only) serves as the canonical reference for pack structure. Study it to understand:

### Key Success Patterns
1. **Clear Decision Hierarchy**: MDD defines scope, ADRs define architecture, EDRs define standards, IDRs define implementation
2. **Rich AI Context**: Each TDR includes specific guidance for code generation
3. **Framework Flexibility**: Generator supports multiple output targets
4. **Comprehensive Testing**: Generated code includes unit tests and validation

### Generator Architecture
```python
# Key components of task-app generator
def main():
    # 1. Parse all TDRs and build context
    context = parse_tdrs("tdrs/")
    
    # 2. Generate code based on target framework
    framework = get_target_framework()
    code = generate_application(context, framework)
    
    # 3. Write files and validate
    write_generated_files(code)
    validate_generated_code()
    
    # 4. Run tests to ensure functionality
    run_integration_tests()
```

### Decision Documentation Style
```yaml
# Example from task-app showing effective ai_context
ai_context:
  implementation_notes:
    - "Use FastAPI for high-performance async API"
    - "Implement JWT tokens with 1-hour expiration"
    - "Store tasks in SQLite for simplicity, PostgreSQL for production"
  
  security_requirements:
    - "All endpoints except /health require authentication"
    - "Input validation using Pydantic models"
    - "SQL injection protection via ORM"
  
  testing_strategy:
    - "Unit tests for business logic"
    - "Integration tests for API endpoints"
    - "Test coverage minimum 80%"
```

---

## Advanced Patterns: Composable Pack Architecture

### Pack Layering Strategy
As the ecosystem matures, packs can be composed like building blocks:

**Base Layer**: Foundational patterns
- `web-service-base-pack`: HTTP server, logging, health checks
- `data-service-base-pack`: Database integration, migration management
- `auth-service-base-pack`: Authentication, authorization, session management

**Domain Layer**: Specialized functionality
- `ecommerce-checkout-pack`: Cart, payment, order processing
- `content-management-pack`: CMS functionality, publishing workflow
- `analytics-tracking-pack`: Event collection, metric aggregation

**Integration Layer**: Cross-cutting concerns
- `monitoring-observability-pack`: Logging, metrics, tracing
- `security-compliance-pack`: Encryption, audit trails, access controls
- `performance-optimization-pack`: Caching, CDN, load balancing

### Dependency Management
```yaml
# Example pack dependencies in pack metadata
dependencies:
  base_packs:
    - "web-service-base-pack@^1.2.0"
    - "auth-service-base-pack@^2.1.0"
  
  optional_packs:
    - "monitoring-observability-pack@^1.0.0"
    - "security-compliance-pack@^3.2.0"
  
  conflicts:
    - "legacy-auth-pack"  # Incompatible authentication approach
```

### Cross-Pack Decision Coordination
```yaml
# Shared decisions across multiple packs
shared_decisions:
  authentication_strategy: "jwt_with_refresh_tokens"
  database_migration_tool: "alembic"
  logging_format: "structured_json"
  api_versioning: "url_path_based"
```

---

## Open Source Foundation: Built by the Community, for the Community

### Pure Open Source Model

- **All Packs**: MIT licensed, freely available to everyone
- **Community Driven**: Maintained and improved by contributors worldwide
- **No Commercial Barriers**: No premium tiers, subscriptions, or paid features
- **Attribution Based**: Clear contributor recognition and portfolio building

### Sustainable Through Community

- **Collaborative Development**: Shared ownership and responsibility
- **Peer Recognition**: Contributors build reputation through quality contributions
- **Knowledge Sharing**: Best practices spread freely across the community
- **Collective Impact**: Better software architecture for everyone

### Ways to Support the Project

- **Contribute Packs**: Share your domain expertise with the community
- **Improve Documentation**: Help make the project more accessible
- **Provide Feedback**: Test packs and report issues or suggestions
- **Spread the Word**: Help others discover DDSE methodology

> **🌟 Pure Open Source**: This project believes that architectural wisdom should be freely shared. All contributions are made available under the MIT license for maximum reuse and impact.

---

## Quality Assurance: Building Trust in the Marketplace

### Automated Validation Pipeline
Every pack contribution goes through:

1. **TDR Validation**: YAML syntax, required fields, decision hierarchy
2. **Generator Testing**: Code generation success, compilation checks
3. **Security Scanning**: Common vulnerability patterns, dependency analysis
4. **Performance Baseline**: Generated code performance characteristics
5. **Documentation Review**: README completeness, demo video quality

### Community Review Process
- **Domain Expert Review**: Technical accuracy, best practice adherence
- **Usability Testing**: Can newcomers successfully use the pack?
- **Integration Testing**: Does it work well with other popular packs?
- **Long-term Maintenance**: Is the contributor committed to updates?

### Trust Signals for Users
```yaml
# Pack quality indicators
quality_metrics:
  validation_status: "passing"
  security_scan: "clean"
  community_rating: "4.8/5.0"
  usage_count: "1,247 downloads"
  maintenance_score: "active"  # Based on update frequency
  
certifications:
  - "DDSE Foundation Verified"
  - "Security Best Practices"
  - "Production Ready"
```

---

## Getting Started: Your First Contribution

### Week 1: Choose Your Domain
**Action Items**:
- [ ] Identify a domain where you have 2+ years of production experience
- [ ] Research existing packs to avoid duplication
- [ ] Join the community discussion for your chosen domain
- [ ] Study the task-app example thoroughly

**Success Criteria**: Clear domain scope with community validation

### Week 2: Map Your Decisions
**Action Items**:
- [ ] List 15-20 critical decisions you've made in this domain
- [ ] Categorize decisions by TDR type (MDD/ADR/EDR/IDR)
- [ ] Research industry best practices and alternatives
- [ ] Document the decision dependencies and relationships

**Success Criteria**: Complete decision inventory with rationale

### Week 3: Build Your Pack
**Action Items**:
- [ ] Write TDRs following the DDSE specification
- [ ] Create generator script with basic functionality
- [ ] Test generation with multiple target frameworks
- [ ] Validate all TDRs pass automated checks

**Success Criteria**: Working generator that produces runnable code

### Week 4: Polish and Ship
**Action Items**:
- [ ] Write comprehensive documentation
- [ ] Record 2-minute unedited demo video
- [ ] Test pack with fresh eyes (ideally another person)
- [ ] Submit pull request with complete package

**Success Criteria**: Professional-quality pack ready for community use

---

## Community Support: You're Not Alone

### Mentorship Program
**Expert Mentors**: Paired with experienced pack contributors
**Regular Check-ins**: Weekly progress reviews and guidance
**Technical Support**: Help with TDR writing, generator development
**Community Introduction**: Connect with potential collaborators

### Resources and Tools
**TDR Templates**: Starting points for common decision types
**Generator Examples**: Reference implementations for different approaches
**Validation Tools**: Automated checking for quality and compliance
**Testing Frameworks**: Validate generated code quality

### Communication Channels
**Discord Community**: Real-time chat and pair programming *(coming soon)*
**Contributor Newsletter**: Updates, spotlights, and learning resources


---

## Call to Action: The Future Needs Your Expertise

The software industry stands at an inflection point. AI can generate code faster than ever, but the bottleneck has shifted to **decision clarity**. Your hard-won architectural knowledge—tested in production, refined through failure, validated by success—can become the foundation for thousands of future projects.

### Choose Your Contribution Level

**🚀 Pioneer**: Create a high-impact pack in AI/ML, RAG, or E-commerce
- **Time Investment**: 3-4 weeks
- **Impact**: Potentially thousands of users, community recognition
- **Rewards**: Technical leadership, skill development, open source portfolio

**🛠 Builder**: Contribute to tooling, templates, or educational content
- **Time Investment**: 1-2 weeks
- **Impact**: Enable other contributors, improve ecosystem quality
- **Rewards**: Technical recognition, skill development, network building

**📚 Educator**: Create tutorials, case studies, or migration guides
- **Time Investment**: 1-2 weeks
- **Impact**: Accelerate community adoption and best practices
- **Rewards**: Teaching opportunities, content portfolio, community building

### Start Today

1. **[Fork the Repository](https://github.com/ddse-foundation/ddse-foundation)** - Get the code
2. **[Study the Examples](https://github.com/ddse-foundation/ddse-foundation/tree/main/example)** - Learn the patterns
3. **[Start Building](https://github.com/ddse-foundation/ddse-foundation/blob/main/CONTRIBUTING.md)** - Create your pack

The best time to contribute was yesterday. The second best time is now.

Your expertise can shape the future of software development. The question isn't whether AI will change how we build software—it's whether your architectural wisdom will be part of that transformation.

**Ready to turn your expertise into lasting community impact?**

[**Start Your First Domain Pack Today →**](https://github.com/ddse-foundation/ddse-foundation)

---

*This article is licensed under CC-BY. Feel free to fork, remix, and share with attribution to help spread the DDSE methodology.*

**Connect with the community**:
- 🔗 [GitHub Repository](https://github.com/ddse-foundation/ddse-foundation)
