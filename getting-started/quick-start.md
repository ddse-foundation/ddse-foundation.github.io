---
layout: default
title: Quick Start
parent: Getting Started
nav_order: 2
description: "Create your first TDR and experience DDSE in 5 minutes"
---

# 🚀 Quick Start Guide

Get hands-on with DDSE in just **5 minutes**. This guide wa- 📖 Learn TDR Hierarchy - Understand MDD, ADR, EDR, IDR relationships
- [🛠️ Explore Templates]({% link implementation/templates/index.md %}) - Get templates for all TDR types
- [📘 View Source Code](https://github.com/ddse-foundation/ddse-foundation) - Access the GitHub repository
- [📚 Learn More]({% link learn-ddse/specification.md %}) - Master the complete DDSE methodologyyou through creating your first Technical Decision Record (TDR) and using it with AI tools.

## What You'll Accomplish

By the end of this guide, you'll have:
- ✅ Created your first TDR with AI context
- ✅ Used it to generate consistent code with AI tools
- ✅ Validated your TDR for compliance
- ✅ Experienced the DDSE difference firsthand

---

## Step 1: Choose Your Decision (1 minute)

Pick a **recent technical decision** you made. Great candidates:

### 🎯 API Design Decisions
- "How should we handle input validation?"
- "What error response format should we use?"
- "How should we structure our endpoints?"

### 🏗️ Code Organization Decisions  
- "How should we organize our database queries?"
- "What naming convention should we use for functions?"
- "How should we handle configuration?"

### 🔧 Tool Configuration Decisions
- "What linting rules should we enforce?"
- "How should we structure our test files?"
- "What CI/CD pipeline should we use?"

**For this example, let's use: "API Input Validation Strategy"**

---

## Step 2: Download Template (30 seconds)

For our example decision, we'll use an **IDR (Implementation Decision Record)** template:

**Option A: Copy from GitHub**
1. Go to [IDR Template](https://github.com/ddse-foundation/ddse-foundation/blob/main/tdr-templates/idr-template.md)
2. Copy the raw markdown content
3. Save as `idr-001-input-validation.md` in your project

**Option B: Use our generator**
1. Visit our [Interactive TDR Builder]({% link implementation/templates/interactive-builder.md %})
2. Select "IDR - Implementation Decision"
3. Download the customized template

---

## Step 3: Fill Your TDR (3 minutes)

Replace the template content with your actual decision:

```yaml
---
decision_id: "idr-001"
title: "API Input Validation Strategy"
status: "accepted"
decision_type: "implementation"
created: "2025-01-27"
author: "Your Name"
---

# Decision Context

We need consistent input validation across all API endpoints. Currently, different endpoints handle validation differently, leading to inconsistent error messages and security gaps.

## Current State
- Some endpoints use manual validation
- Error messages vary between endpoints  
- No standardized validation failure responses

## Decision Drivers
- Security: Prevent invalid data from reaching business logic
- Consistency: Uniform validation patterns across all endpoints
- Developer Experience: Clear error messages for API consumers
- Maintainability: Centralized validation logic

# Decision Outcome

We will use **Pydantic models for all API input validation** with FastAPI's built-in integration.

## Selected Option
**Option 1: Pydantic models with FastAPI dependency injection**

### Implementation Details
- All API endpoints will define Pydantic models for request bodies
- Use FastAPI's automatic validation and error handling
- Return standardized 422 errors for validation failures
- Custom error messages for business-specific validation rules

## Consequences

### Positive
- Automatic request validation with minimal boilerplate
- Type hints improve IDE support and documentation
- Consistent error response format across all endpoints
- Easy to test validation logic in isolation

### Negative  
- Additional dependency on Pydantic
- Learning curve for developers unfamiliar with Pydantic
- Migration effort for existing endpoints

# AI Context

## Implementation Priority
Implement validation decorators first, then migrate existing endpoints in order of business criticality. Start with user registration and authentication endpoints.

## Framework Guidance
- Use FastAPI's dependency injection system for reusable validation logic
- Create base validator classes for common patterns (email, phone, etc.)
- Leverage Pydantic's built-in validators for standard formats
- Use custom validators for business-specific rules

## Constraint Enforcement
- MUST return 422 status code for validation errors
- MUST include field-level error details in response
- NEVER accept unvalidated input in any endpoint handler
- MUST log validation failures for security monitoring

## Pattern Examples
```python
from pydantic import BaseModel, EmailStr, validator
from fastapi import HTTPException

class UserRegistrationRequest(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    
    @validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        return v

@app.post("/users/register")
async def register_user(request: UserRegistrationRequest):
    # Input is automatically validated by FastAPI + Pydantic
    # Business logic here knows input is valid
    pass
```

# Related Decisions
- adr-001-rest-api-architecture.md (REST API choice enables this pattern)
- edr-001-error-handling-strategy.md (Defines error response format)
```

---

## Step 4: Test with AI Tools (1 minute)

Now use your TDR with your favorite AI tool:

### With GitHub Copilot
1. Open your project in VS Code
2. Create a new API endpoint file
3. Add a comment: `// Following idr-001-input-validation.md, create user registration endpoint`
4. Watch Copilot generate code following your TDR patterns

### With ChatGPT/Claude
1. Copy your TDR content
2. Ask: "Following this TDR, implement a user registration endpoint for our FastAPI application"
3. Compare the generated code with your documented patterns

### Expected Result
The AI should generate code that:
- ✅ Uses Pydantic models for validation
- ✅ Returns 422 errors for invalid input
- ✅ Includes proper error handling
- ✅ Follows the exact patterns you documented

---

## Step 5: Validate Your TDR (30 seconds)

Check if your TDR follows DDSE best practices:

**Option A: Online Validator**
1. Use the [GitHub TDR Validator](https://github.com/ddse-foundation/ddse-foundation/blob/main/tools/tdr_validator.py)
2. Paste your TDR content
3. Get instant feedback on compliance

**Option B: Python Validator**
```bash
# Download the validator
curl -O https://raw.githubusercontent.com/ddse-foundation/ddse-foundation/main/tools/tdr_validator.py

# Validate your TDR
python tdr_validator.py idr-001-input-validation.md
```

**Expected Output:**
```
✅ TDR Structure: Valid
✅ Required Sections: Present  
✅ AI Context: Complete
✅ Cross-references: Valid
🎉 TDR passes all validation checks!
```

---

## 🎉 Congratulations!

You've just created your first DDSE TDR and experienced AI-guided development with human decision authority. 

### What You've Learned
- **TDRs provide structure** for technical decisions
- **AI context sections** guide tool behavior effectively  
- **Validation ensures quality** and compliance
- **Consistency improves** when AI tools follow documented patterns

### Immediate Next Steps

1. **Try another decision**: Pick a different technical choice and create another TDR
2. **Share with your team**: Show them the AI-generated code quality difference
3. **Build your TDR library**: Document 3-5 key decisions over the next week

### Expand Your Knowledge

- 📖 Learn TDR Hierarchy - Understand MDD, ADR, EDR, IDR relationships
- [🛠️ Explore Templates]({% link implementation/templates/index.md %}) - Get templates for all TDR types
- [� View Source Code](https://github.com/ddse-foundation/ddse-foundation) - Access the GitHub repository
- [👥 Team Adoption Guide](https://github.com/ddse-foundation/ddse-foundation/blob/main/adoption/README.md) - Roll out DDSE to your team

---

## ❓ Troubleshooting

### "My AI tool isn't following the TDR patterns"
- **Check AI context sections**: Make sure they're specific and actionable
- **Be more explicit**: Add concrete examples and constraint enforcement
- **Try different prompts**: "Following the exact patterns in this TDR..."

### "The TDR feels too formal for my small project"
- **Start lighter**: Use just the Decision Context, Outcome, and AI Context sections
- **Focus on value**: Only document decisions that actually need consistency
- **Grow gradually**: Add more structure as your project and team grows

### "I'm not sure which TDR type to use"
- **IDR for implementation**: Specific coding patterns and conventions
- **EDR for engineering**: Cross-cutting technical approaches  
- **ADR for architecture**: Major structural and technology decisions
- **MDD for strategy**: Business and product-level constraints

[View on GitHub →](https://github.com/ddse-foundation/ddse-foundation){: .btn .btn-outline }

---

**You're now ready to transform your development workflow with DDSE!** 🚀

The next step is expanding this approach to more decisions and sharing the benefits with your team.
