# Salesforce CLI Agent Generation Guide

## Step-by-Step Instructions

### 1. Prerequisites Check
First, verify your Salesforce CLI is working and you have connected orgs:

```bash
sf --version
sf org list
```

### 2. Run the Agent Generation Command

In your VS Code integrated terminal, run:

```bash
sf agent generate agent-spec --target-org resorts-demo
```

**Note**: Using the new "resorts-demo" org connection with the provided credentials.

### 3. Interactive Prompts

The command will prompt you for the following information. Here are the exact answers to provide:

#### Prompt 1: Type of agent
```
? Type of agent: Customer
```

#### Prompt 2: Company Name
```
? Company Name: Coral Cloud Resorts
```

#### Prompt 3: Company Description
```
? Company Description: Coral Cloud Resorts provides customers with exceptional destination activities, unforgettable experiences, and reservation services, all backed by a commitment to top-notch customer service.
```

#### Prompt 4: Role of the agent
```
? Role of the agent: The resort manager fields customer complaints, manages employee schedules, and generally makes sure everything is working smoothly.
```

#### Prompt 5: Confirm overwrite (if file exists)
```
? Confirm overwrite of spec file /Users/akshata.sawant/SF_ADLC_Whitepaper/specs/agentSpec.yaml? (y/N) y
```

#### Prompt 6: Path for generated file (optional)
```
? Path for the generated YAML agent spec file; can be an absolute or relative path: specs/agentSpec.yaml
```

### 4. Expected Output

After providing all the information, the command will:
- Generate an `agentSpec.yaml` file in your `specs/` directory
- Create AI-generated topics based on your inputs
- Display a summary of the generated agent specification

### 5. Review the Generated File

After the command completes, you can review the generated file:

```bash
cat specs/agentSpec.yaml
```

### 6. Compare with Our Implementation

You can compare the Salesforce CLI generated file with our manually created one:

```bash
diff specs/agentSpec.yaml specs/agentSpec.yaml.backup
```

## Troubleshooting

### If you get "No default environment found" error:
```bash
sf org list
# Use one of the listed orgs with --target-org flag
sf agent generate agent-spec --target-org <org-alias>
```

### If the command gets stuck:
- Press `Ctrl+C` to cancel
- Try running the command again
- Make sure you're in the correct directory

### If you want to start fresh:
```bash
rm specs/agentSpec.yaml
sf agent generate agent-spec --target-org resume-demo
```

## What the Command Does

The `sf agent generate agent-spec` command:

1. **Analyzes your inputs** using AI to understand the business context
2. **Generates relevant topics** that the agent can handle
3. **Creates conversation flows** appropriate for the role
4. **Sets up integration points** for external systems
5. **Defines success metrics** for the agent

## Expected Topics Generated

Based on your inputs, the Salesforce CLI should generate topics like:
- Customer service and complaints
- Reservation management
- Employee scheduling
- Resort operations
- Policy information
- Emergency response

## Next Steps After Generation

1. **Review the generated topics** in `agentSpec.yaml`
2. **Edit and refine** any topics that need adjustment
3. **Add specific examples** for your use case
4. **Test the configuration** using our validation script
5. **Move to Phase 2** implementation

## Manual Alternative

If the interactive command doesn't work, you can use our pre-generated `agentSpec.yaml` file, which contains all the necessary configuration for Coral Cloud Resorts.
