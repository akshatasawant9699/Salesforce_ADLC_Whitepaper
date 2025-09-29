# Phase 1: Ideation & Design with Agentforce DX

## Mission Statement
Design a resort manager agent for Coral Cloud Resorts that handles customer complaints, manages employee schedules, and ensures smooth resort operations.

## Design Decisions

### Agent Type
- **Type**: Customer-facing service agent
- **Persona**: Helpful and professional conversational tone
- **Company**: Coral Cloud Resorts

### Core Capabilities
- Customer complaint resolution
- Employee schedule management
- Resort policy knowledge
- Reservation assistance
- Emergency response coordination

## Agentforce DX Implementation

### Step 1: Generate Agent Specification

```bash
# Navigate to your DX project directory
cd agentforcedx

# Generate agent specification interactively
sf agent generate agent-spec
```

**Interactive Prompts:**
```
Type of agent: Customer
Company Name: Coral Cloud Resorts
Company Description: Coral Cloud Resorts provides customers with exceptional destination activities, unforgettable experiences, and reservation services, all backed by a commitment to top-notch customer service.
Role of the agent: The resort manager fields customer complaints, manages employee schedules, and generally makes sure everything is working smoothly.
```

### Step 2: Generated agentSpec.yaml

The command creates an `agentSpec.yaml` file in your DX project's `specs` directory:

```yaml
# specs/agentSpec.yaml
name: "Coral Cloud Resorts Resort Manager"
description: "The resort manager fields customer complaints, manages employee schedules, and generally makes sure everything is working smoothly."
agentType: "Customer"
companyName: "Coral Cloud Resorts"
companyDescription: "Coral Cloud Resorts provides customers with exceptional destination activities, unforgettable experiences, and reservation services, all backed by a commitment to top-notch customer service."
topics:
  - name: "Customer Complaints"
    description: "Handle and resolve customer complaints about services, accommodations, or experiences"
  - name: "Employee Scheduling"
    description: "Manage and update employee work schedules and shift assignments"
  - name: "Reservation Management"
    description: "Assist with booking modifications, cancellations, and special requests"
  - name: "Resort Policies"
    description: "Provide information about resort policies, rules, and procedures"
  - name: "Activity Recommendations"
    description: "Suggest activities and experiences based on guest preferences"
  - name: "Emergency Response"
    description: "Handle urgent situations and coordinate emergency procedures"
  - name: "Room Service"
    description: "Coordinate room service requests and housekeeping needs"
  - name: "Guest Services"
    description: "Provide general assistance and information to guests"
  - name: "Maintenance Issues"
    description: "Report and coordinate resolution of maintenance problems"
  - name: "Special Events"
    description: "Coordinate special events and celebrations for guests"
```

### Step 3: Validate the Specification

```bash
# Validate the agent specification
sf agent validate agent-spec --spec-file specs/agentSpec.yaml
```

## Phase 1 Deliverables

1. **agentSpec.yaml** - Complete agent specification with topics
2. **Design Documentation** - Clear mission, persona, and capabilities
3. **Topic Definitions** - AI-generated topics that define agent capabilities

## Best Practices for Phase 1

- **Be Specific**: Define clear, actionable topics
- **Consider Edge Cases**: Include emergency and maintenance scenarios
- **Align with Business Goals**: Ensure topics support business objectives
- **Review and Iterate**: Refine topics based on stakeholder feedback

## Next Steps

After completing Phase 1, proceed to Phase 2: Development to transform the specification into a functional agent.
