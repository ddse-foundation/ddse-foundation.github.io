---
layout: default
title: CDR Template
parent: Templates & Tools
grand_parent: Implementation
nav_order: 3
description: "Contract Decision Record template for API specifications"
seo_title: "Contract Decision Record Template - DDSE"
---

# CDR Template

Template for Contract Decision Records (CDR) - API contracts, service interfaces, and integration specifications.

## Template Structure

### YAML Frontmatter
```yaml
---
id: CDR-000
title: "Contract Decision Record Template"
status: "template"
date: "2025-08-03"
authors: ["architect@example.com"]
reviewers: ["tech-lead@example.com"]
category: "api-contract"
related_decisions:
  - "ADR-XXX: Related architectural decision"
  - "EDR-XXX: Related engineering decision"
ai_context:
  contract_type: "REST API"
  implementation_priorities:
    - "OpenAPI 3.0 specification compliance"
    - "Backward compatibility during evolution"
    - "Clear error handling and status codes"
  validation_rules:
    - "All endpoints must have proper HTTP status codes"
    - "Request/response schemas must be validated"
    - "API versioning strategy must be followed"
  framework_hints:
    backend: "Express.js with TypeScript"
    frontend: "React with TypeScript"
    testing: "Jest with supertest for API testing"
---
```

### Template Sections

- **Summary**: Brief contract description and system role
- **Context**: System integration point, related decisions, and business requirements
- **Contract Specification**: Complete OpenAPI specification with endpoints, schemas, and error handling
- **Implementation Requirements**: Backend and frontend implementation guidelines
- **Evolution Strategy**: Versioning approach and breaking change process
- **Risks and Mitigations**: Technical and operational risk assessment
- **Success Metrics**: Performance, quality, and adoption metrics
- **Implementation Plan**: Phased rollout with concrete deliverables
- **AI Context Section**: Specific guidance for AI-assisted development

## Key Features

### ✅ **Complete API Specifications**
- Full OpenAPI 3.0 contract definitions
- Request/response schemas with validation
- Authentication and authorization patterns
- Error handling and HTTP status codes

### ✅ **Implementation Guidance**
- Backend framework requirements
- Frontend integration patterns
- Testing strategies and tools
- Performance and scalability considerations

### ✅ **Evolution Support**
- API versioning strategies
- Backward compatibility guidelines
- Breaking change processes
- Migration documentation requirements

### ✅ **AI Integration**
- Contract binding for AI agents
- Implementation constraints and patterns
- Validation rules for generated code
- Framework-specific hints and preferences

## Download Template

Ready-to-use CDR template for immediate implementation of API contracts.

### Full Template Download

```markdown
---
id: CDR-000
title: "Contract Decision Record Template"
status: "template"
date: "2025-08-03"
authors: ["architect@example.com"]
reviewers: ["tech-lead@example.com"]
category: "api-contract"
related_decisions:
  - "ADR-XXX: Related architectural decision"
  - "EDR-XXX: Related engineering decision"
ai_context:
  contract_type: "REST API"
  implementation_priorities:
    - "OpenAPI 3.0 specification compliance"
    - "Backward compatibility during evolution"
    - "Clear error handling and status codes"
  validation_rules:
    - "All endpoints must have proper HTTP status codes"
    - "Request/response schemas must be validated"
    - "API versioning strategy must be followed"
  framework_hints:
    backend: "Express.js with TypeScript"
    frontend: "React with TypeScript"
    testing: "Jest with supertest for API testing"
---

# CDR-000: [Contract Title]

## Summary

Brief description of the contract being defined and its role in the system architecture.

## Context

### System Integration Point
Describe where this contract fits in the overall system architecture and what services/components it connects.

### Related Decisions
Reference the architectural and engineering decisions that inform this contract specification.

### Business Requirements
Outline the business needs that drive the contract requirements.

## Contract Specification

### API Endpoints

#### Endpoint 1: [Operation Name]
```yaml
endpoint: GET /api/v1/resource/{id}
description: Retrieve a specific resource by ID
parameters:
  - name: id
    in: path
    required: true
    schema:
      type: string
      format: uuid
responses:
  200:
    description: Resource retrieved successfully
    content:
      application/json:
        schema:
          $ref: '#/components/schemas/Resource'
  404:
    description: Resource not found
    content:
      application/json:
        schema:
          $ref: '#/components/schemas/Error'
  500:
    description: Internal server error
    content:
      application/json:
        schema:
          $ref: '#/components/schemas/Error'
```

### Data Schemas

#### Core Resource Schema
```yaml
components:
  schemas:
    Resource:
      type: object
      required:
        - id
        - name
        - createdAt
        - updatedAt
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the resource
        name:
          type: string
          minLength: 1
          maxLength: 255
          description: Human-readable name of the resource
```

### Authentication & Authorization
```yaml
security:
  - bearerAuth: []

components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
```

## Implementation Requirements

### Backend Implementation
- **Framework**: Express.js with TypeScript
- **Validation**: Use Joi or Yup for request validation
- **Error Handling**: Consistent error response format across all endpoints
- **Logging**: Log all API requests with correlation IDs
- **Testing**: Unit tests for business logic, integration tests for API endpoints

### Frontend Integration
- **HTTP Client**: Axios with TypeScript types generated from OpenAPI spec
- **Error Handling**: Consistent error handling and user feedback
- **Caching**: Implement appropriate caching strategy for GET endpoints
- **Loading States**: Proper loading and error states for all API calls

## Evolution Strategy

### Versioning Approach
- **URL Versioning**: `/api/v1/`, `/api/v2/` for major changes
- **Header Versioning**: `Accept: application/vnd.api+json;version=1` for minor changes
- **Backward Compatibility**: Maintain compatibility for at least 2 major versions

### Breaking Change Process
1. **Announcement**: 90-day notice for breaking changes
2. **Parallel Support**: Run old and new versions simultaneously
3. **Migration Guide**: Provide detailed migration documentation
4. **Deprecation**: Clear deprecation timeline and sunset dates

## Success Metrics

### Performance Metrics
- **Response Time**: 95th percentile < 200ms for GET endpoints
- **Throughput**: Support 1000 RPS per endpoint
- **Availability**: 99.9% uptime SLA

### Quality Metrics
- **Error Rate**: < 1% for 4xx errors, < 0.1% for 5xx errors
- **Test Coverage**: > 90% for contract-related code
- **Documentation**: 100% of endpoints documented with examples

## Implementation Plan

### Phase 1: Contract Definition
- [ ] Complete OpenAPI specification
- [ ] Define data schemas and validation rules
- [ ] Create mock API for frontend development
- [ ] Set up contract testing framework

### Phase 2: Backend Implementation
- [ ] Implement API endpoints according to contract
- [ ] Add request/response validation
- [ ] Implement error handling and logging
- [ ] Add comprehensive test suite

### Phase 3: Frontend Integration
- [ ] Generate TypeScript types from OpenAPI spec
- [ ] Implement API client with proper error handling
- [ ] Add loading states and user feedback
- [ ] Implement caching and optimization

### Phase 4: Production Deployment
- [ ] Deploy to staging environment
- [ ] Conduct integration testing
- [ ] Perform security and performance testing
- [ ] Deploy to production with monitoring

## Related Documentation

- **OpenAPI Specification**: [Link to full OpenAPI spec file]
- **Implementation Guide**: [Link to detailed implementation documentation]
- **Client SDK**: [Link to generated client libraries]
- **Testing Guide**: [Link to contract testing documentation]

---

*This Contract Decision Record follows the DDSE v1.1 specification. For questions or clarifications, contact the architecture owner.*
```

## Usage Examples

### Basic API Contract
Perfect for REST APIs with standard CRUD operations:
- User management endpoints
- Product catalog APIs
- Authentication services
- File upload/download contracts

### Microservice Integration
Ideal for service-to-service communication:
- Inter-service API contracts
- Message queue specifications
- Event streaming contracts
- Database integration patterns

### Frontend-Backend Contracts
Essential for coordinated development:
- Parallel frontend/backend development
- Mobile app API specifications
- Single Page Application (SPA) contracts
- Progressive Web App (PWA) integrations

## Best Practices

### ✅ **Do's**
- Include complete OpenAPI specifications
- Define comprehensive error handling
- Specify authentication requirements
- Add AI context for code generation
- Plan for contract evolution

### ❌ **Don'ts**
- Don't create contracts without implementation guidance
- Don't ignore versioning and backward compatibility
- Don't skip testing strategy definition
- Don't omit performance requirements
- Don't forget to link to related architectural decisions

---

## Related Templates

- **[ADR Template]({% link implementation/templates/adr.md %})**: Architectural decisions that inform contracts
- **[EDR Template]({% link implementation/templates/edr.md %})**: Engineering practices for contract implementation
- **[IDR Template]({% link implementation/templates/idr.md %})**: Implementation patterns for contract details

**Next**: Learn about [contract-driven development workflows]({% link learn-ddse/sdlc-contracts.md %}) in the DDSE methodology.
