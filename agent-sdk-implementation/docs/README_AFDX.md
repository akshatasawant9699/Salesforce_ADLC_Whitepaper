# Agent Development Lifecycle (ADLC) with Agentforce DX

This directory contains the Agentforce DX implementation of the Agent Development Lifecycle, providing a pro-code approach to agent development using Salesforce CLI and modern DevOps practices.

## Overview

Agentforce DX extends Salesforce Developer Experience (DX) tools to work with agents, enabling:
- Version control for agent metadata
- CI/CD integration for agent deployment
- Pro-code development workflows
- Modern DevOps practices

## Directory Structure

```
docs/
├── ADLC_AFDX.md                    # Complete ADLC implementation guide
├── phase1_ideation_design.md       # Phase 1 detailed implementation
├── specs/
│   └── agentSpec.yaml             # Sample agent specification
└── README_AFDX.md                  # This file
```

## Prerequisites

- Salesforce Developer Edition org with Agentforce enabled
- Salesforce CLI (latest version)
- Visual Studio Code with Salesforce Extensions
- Git for version control

## Quick Start

### 1. Set Up Development Environment

```bash
# Install Salesforce CLI
npm install -g @salesforce/cli

# Verify installation
sf --version

# Update to latest version
sf update
```

### 2. Create DX Project

```bash
# Create new DX project
sf project generate --name agentforcedx

# Navigate to project
cd agentforcedx
```

### 3. Authorize Org

```bash
# Authorize your Developer Edition org
sf org login web --alias agentforce
```

### 4. Generate Agent Specification

```bash
# Generate agent specification interactively
sf agent generate agent-spec
```

### 5. Create Agent

```bash
# Create agent from specification
sf agent create --spec-file specs/agentSpec.yaml
```

## Phase Implementation

### Phase 1: Ideation & Design
- Generate agent specification using `sf agent generate agent-spec`
- Define agent topics and capabilities
- Validate specification with `sf agent validate agent-spec`

### Phase 2: Development
- Create agent from specification using `sf agent create`
- Customize agent actions and flows
- Add custom Apex classes for business logic

### Phase 3: Testing & Validation
- Run unit tests with `sf apex run test`
- Test agent functionality with `sf agent test`
- Perform end-to-end testing

### Phase 4: Deployment & Release
- Deploy to scratch org for testing
- Deploy to sandbox for UAT
- Deploy to production with proper validation

### Phase 5: Monitoring & Tuning
- Enable monitoring with `sf agent monitor enable`
- Analyze performance metrics
- Optimize agent based on usage data

## Key Commands

### Agent Management
```bash
# Generate agent specification
sf agent generate agent-spec

# Create agent from specification
sf agent create --spec-file specs/agentSpec.yaml

# List agents
sf agent list

# Test agent
sf agent test --agent-name "Agent Name"
```

### Deployment
```bash
# Deploy to target org
sf project deploy start --target-org org-alias

# Deploy specific agent
sf agent deploy --agent-name "Agent Name" --target-org org-alias
```

### Monitoring
```bash
# Enable monitoring
sf agent monitor enable --agent-name "Agent Name"

# Get metrics
sf agent monitor get-metrics --agent-name "Agent Name"

# Analyze usage
sf agent monitor analyze --agent-name "Agent Name"
```

## Best Practices

### Development
- Use version control for all agent metadata
- Implement comprehensive testing strategies
- Follow Salesforce development best practices
- Document all customizations

### Deployment
- Use CI/CD pipelines for automated deployment
- Implement proper environment management
- Follow security best practices
- Maintain rollback capabilities

### Monitoring
- Set up comprehensive monitoring from day one
- Implement alerting for critical issues
- Regular performance reviews
- Continuous optimization based on data

## Resources

- [Agentforce DX Trailhead Project](https://trailhead.salesforce.com/content/learn/projects/create-an-agent-using-pro-code-tools/get-started-with-agentforce-dx)
- [Salesforce CLI Command Reference](https://developer.salesforce.com/docs/atlas.en-us.sfdx_cli_reference.meta/sfdx_cli_reference/)
- [Agentforce Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.agentforce.meta/agentforce/)
- [Salesforce DX Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/)

## Support

For questions and support:
- Salesforce Developer Community
- Trailhead Community
- Salesforce Partner Portal
