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

## Preview Agent Creation

Before creating the agent, preview what it will look like in your org:

```bash
# Preview the agent creation (generates JSON file with agent details)
sf agent create --spec specs/agentSpec.yaml --name "Resort Manager" --preview
```

This command generates a JSON file named `Resort_Manager_Preview_<timestamp>.json` that describes the agent the LLM will create, including suggested actions for each topic, instructions, and sample utterances.

## Create Agent from Specification

Once you're satisfied with the preview, create the agent in your org:

```bash
# Create the agent using the spec file
sf agent create --spec specs/agentSpec.yaml --name "Resort Manager"
```

The command prompts you for the API name of the agent (we recommend accepting the default `Resort_Manager`). The command then:
- Parses the agent spec file
- Creates the agent in your development org
- Retrieves the metadata back to your local DX project

This metadata includes a Bot, BotVersion, and a GenAiPlannerBundle, which adds AI intelligence and references the agent's topics and actions.

## Troubleshooting

### Permission Set Assignment

If you encounter permission set assignment errors, manually assign the required permission sets:

```bash
# Check available Agentforce permission sets
sf data query --query "SELECT Id, Name, Label FROM PermissionSet WHERE Name LIKE '%Agent%'"

# Assign required permission sets to the agent user
sf data create record --sobject PermissionSetAssignment --values "AssigneeId=USER_ID PermissionSetId=0PSHs000006QPkqOAG"
sf data create record --sobject PermissionSetAssignment --values "AssigneeId=USER_ID PermissionSetId=0PSHs000007RFQROA4"
```

### Duplicate Username Errors

If you encounter duplicate username errors, use a unique API name:

```bash
# Create agent with unique API name
sf agent create --spec specs/agentSpec.yaml --name "Coral Cloud Resort Manager" --api-name Coral_Cloud_Resort_Manager_$(date +%Y%m%d_%H%M%S)_$(uuidgen | cut -c1-8)
```

### Deleting Previously Created Agents

**Option 1: Use Salesforce Setup UI (Recommended)**
1. Go to **Setup** → **Object Manager** → **Bot Definition**
2. Find your agent (Coral Cloud Resorts Resort Manager)
3. Click on the agent name to open it
4. Click **"Delete"** button and confirm

**Option 2: Use CLI with Admin Permissions**
```bash
# Check existing agents
sf data query --query "SELECT Id, DeveloperName, MasterLabel FROM BotDefinition WHERE MasterLabel LIKE '%Coral%' OR MasterLabel LIKE '%Resort%'"

# Delete agent (requires admin permissions)
sf data delete record --sobject BotDefinition --record-id AGENT_ID

# Check and delete agent users
sf data query --query "SELECT Id, Username, Name FROM User WHERE Username LIKE '%Coral%' OR Username LIKE '%Resort%'"
sf data delete record --sobject User --record-id USER_ID
```

**Option 3: Use Unique Names (No Deletion Required)**
```bash
# Create agent with unique API name to avoid conflicts
sf agent create --spec specs/agentSpec.yaml --name "Coral Cloud Resort Manager" --api-name Coral_Cloud_Resort_Manager_$(date +%Y%m%d_%H%M%S)_$(uuidgen | cut -c1-8)
```

**Note**: If you encounter "insufficient access rights" errors, use the Setup UI or create agents with unique names instead of deleting existing ones.



## Open Agent in Builder UI

After creating the agent, open it in the Agentforce Builder UI:

```bash
# Open the agent in Agentforce Builder UI
sf org open agent --api-name Resort_Manager
```

**Note**: The `--api-name` flag uses the API name of the agent. To find an agent's API name, go to Setup in your org and navigate to the agent's details page.

Now that you've created a basic agent, it's time to customize it and implement the details of what it can do.

