# Phase 1: Ideation & Design with Agentforce DX

## Prerequisites

### Create DX Project

```bash
# Create a new Salesforce DX project
sf project generate --name agentforcedx

# Navigate to the project directory
cd agentforcedx
```

### Authorize Salesforce Org

```bash
# Authorize your Salesforce org
sf org login web --alias agentforce

# Set as default org
sf config set target-org agentforce
```

## Generate Agent Specification

```bash
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

## Generated agentSpec.yaml

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

---

# Phase 2: Development

## Create Agent from Specification

```bash
# Create the agent using the spec file
sf agent create --spec specs/agentSpec.yaml --name "Coral Cloud Resort Manager"
```

When prompted, you can accept the default API name, Coral_Cloud_Resort_Manager. The command parses the spec, creates the agent, and retrieves the metadata. This metadata includes a Bot, BotVersion, and a GenAiPlannerBundle, which is the "glue" that adds AI intelligence and references the agent's topics and actions.

## Preview Agent Creation

```bash
# Preview the agent creation
sf agent create --spec specs/agentSpec.yaml --name "Coral Cloud Resort Manager" --preview
```

This generates a local JSON file detailing the agent that the LLM will create, including suggested actions.

## Troubleshooting

If you encounter duplicate username errors, use a unique API name:

```bash
# Create agent with unique API name
sf agent create --spec specs/agentSpec.yaml --name "Coral Cloud Resort Manager" --api-name Coral_Cloud_Resort_Manager_$(date +%Y%m%d_%H%M%S)
```

## Open Agent in Builder UI

```bash
# Open the agent in Agentforce Builder UI
sf org open agent --api-name Coral_Cloud_Resort_Manager
```

