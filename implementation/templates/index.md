---
layout: default
title: Templates & Tools
parent: Implementation
nav_order: 1
description: "TDR templates, validation tools, and creation utilities"
seo_title: "DDSE Templates: Technical Decision Record Tools"
---

# 📋 Templates & Tools

Ready-to-use TDR templates and powerful tools to streamline your DDSE implementation.

## Quick Access

### 🚀 [Interactive TDR Builder]({% link implementation/templates/interactive-builder.md %})
**Create TDRs with guided prompts and real-time validation**

Step-by-step wizard that guides you through creating any type of TDR with contextual help, examples, and automatic validation.

[Build TDR →]({% link implementation/templates/interactive-builder.md %}){: .btn .btn-primary }

---

## TDR Template Library

### 📋 **Complete Template Set**
Production-ready templates for all TDR types with AI context sections:

| Template | Purpose | Complexity | Time to Complete |
|----------|---------|------------|------------------|
| **[MDD Template]({% link implementation/templates/mdd.md %})** | Major Design Decisions | High | 1-2 hours |
| **[ADR Template]({% link implementation/templates/adr.md %})** | Architectural Decisions | Medium | 30-60 minutes |
| **[CDR Template]({% link implementation/templates/cdr.md %})** | Contract Specifications | Medium | 45-90 minutes |
| **[EDR Template]({% link implementation/templates/edr.md %})** | Engineering Decisions | Medium | 20-40 minutes |
| **[IDR Template]({% link implementation/templates/idr.md %})** | Implementation Decisions | Low | 10-20 minutes |
| **[TDM Template]({% link implementation/templates/tdm.md %})** | Technical Decision Memos | Low | 5-10 minutes |

### 🎯 **Template Features**
Every DDSE template includes:

- **YAML Frontmatter**: Structured metadata for tool processing
- **Standard Sections**: Decision context, outcome, and consequences
- **AI Context Block**: Specific guidance for AI tools
- **Cross-Reference Support**: Link to related decisions
- **Validation Ready**: Compatible with DDSE validation tools
- **Examples**: Real-world implementation examples

---

## Validation & Quality Tools

### 🔍 **TDR Validator**
Ensure your TDRs meet DDSE standards:

**Online Validator**
- Instant validation in your browser
- No installation required
- Detailed error reporting
- Improvement suggestions

**CLI Validator** 
- Integrate into development workflow
- Batch validation for multiple TDRs
- CI/CD pipeline integration
- Custom validation rules

[Use GitHub Validator →](https://github.com/ddse-foundation/ddse-foundation/blob/main/tools/tdr_validator.py){: .btn .btn-outline }

### 📊 **Quality Metrics**
Track your TDR quality over time:

- **Completeness Score**: Percentage of required sections filled
- **AI Context Quality**: Effectiveness of AI guidance sections
- **Cross-Reference Coverage**: Decision linkage completeness
- **Validation Compliance**: Adherence to DDSE standards

---

## Template Customization

### 🏢 **Organization Templates**
Create branded templates for your team:

- **Custom Headers**: Add organization branding and standards
- **Required Fields**: Define mandatory sections for your context
- **Approval Workflows**: Add review and approval processes
- **Integration Points**: Connect with existing tools and processes

### 🎨 **Template Builder**
Create custom TDR templates:

1. **Select Base Template**: Start with standard MDD/ADR/EDR/IDR/TDM
2. **Customize Sections**: Add, remove, or modify template sections
3. **Configure AI Context**: Tailor AI guidance for your technology stack
4. **Add Examples**: Include organization-specific examples
5. **Export & Share**: Download for team use or contribute to community templates

---

## Implementation Guidance

### Rapid Implementation (5 minutes)
1. Identify a recent technical decision requiring documentation
2. Select appropriate template (IDR recommended for implementation decisions)
3. Complete required sections using template structure
4. Include AI context specifications for tool integration
5. Validate format and integrate into project repository

### Systematic Implementation (30 minutes)
1. Evaluate organizational decision documentation needs
2. Download relevant template types for common decision categories
3. Customize templates for organizational requirements and terminology
4. Establish validation and review processes
5. Integrate decision documentation into standard development workflows

### Organizational Adoption (2+ hours)
1. Assess current decision documentation practices and gaps
2. Map organizational decision types to appropriate TDR template categories
3. Develop organization-specific template customizations and governance processes
4. Create training materials and establish adoption support processes
5. Implement systematic rollout with measurement and feedback mechanisms

---

## Template Application Examples

### Practical Decision Documentation
Reference implementations demonstrating DDSE template usage:

- **API Architecture Decisions** - RESTful service design and integration patterns
- **Data Management Decisions** - Database technology selection and schema design approaches  
- **Security Implementation Decisions** - Authentication mechanisms and authorization frameworks
- **Development Process Decisions** - Project organization patterns and coding conventions

### Template Evolution and Community Contribution
Templates undergo continuous improvement through community feedback:

- **Version Control**: Systematic tracking of template modifications and improvements
- **Community Input**: Template refinement based on real-world application experience
- **Best Practice Integration**: Incorporation of proven decision documentation patterns
- **Tool Compatibility**: Updates ensuring compatibility with emerging AI development tools

---

**Implementation Resources:**

Begin with [AI Collaboration Methods]({% link implementation/templates/interactive-builder.md %}) for systematic TDR creation guidance, or access [specific template formats]({% link implementation/templates/adr.md %}) for immediate application.

[Access TDR Templates →]({% link implementation/templates/interactive-builder.md %}){: .btn .btn-outline }
