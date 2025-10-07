# Agent Development Lifecycle (ADLC) - AgentforceDX Implementation

This folder contains a complete implementation of the Agent Development Lifecycle using **AgentforceDX pro-code tools** - the new suite of developer tools for building AI agents with Salesforce CLI and VS Code.

## Overview

Based on [Salesforce's AgentforceDX announcement](https://developer.salesforce.com/blogs/2025/05/introducing-agentforce-dx-pro-code-tools), this implementation uses:
- **Salesforce CLI `agents` plugin** for building, testing, and previewing agents
- **AgentforceDX extension** for VS Code and Code Builder
- **YAML-based metadata** for human-readable agent configurations
- **Pro-code workflows** integrated into existing development environments

## The Agent Development Lifecycle with AgentforceDX

### Phase 1: Ideation & Design
**Purpose**: Define the agent's purpose, persona, and core capabilities using AgentforceDX interactive specification generation.

**AgentforceDX Features**:
- Interactive `sf agent generate agent-spec` command
- AI-generated topics based on company and role information
- Human-readable YAML specifications in `specs/agentSpec.yaml`
- VS Code integration for real-time editing

**Implementation**:
```bash
# Generate agent specification interactively
sf agent generate agent-spec

# Interactive prompts:
# Type of agent: Customer
# Company Name: Coral Cloud Resorts
# Company Description: [Company details]
# Agent Role: [Role description]
```

**Output**: `specs/agentSpec.yaml` - Complete agent specification with AI-generated topics

### Phase 2: Development
**Purpose**: Build agent using AgentforceDX CLI and VS Code integration.

**AgentforceDX Features**:
- CLI-based agent creation and management
- VS Code integration for real-time development
- YAML-based tool and action definitions
- Pro-code workflows in familiar development environment

**Key Commands**:
```bash
# Create agent from specification
sf agents create --spec specs/agentSpec.yaml --org your-org

# Validate agent configuration
sf agents validate --spec specs/agentSpec.yaml --org your-org

# Preview agent conversation
sf agents preview --agent "Agent Name" --org your-org
```

### Phase 3: Testing & Validation
**Purpose**: Test agent using AgentforceDX testing capabilities and conversation preview.

**AgentforceDX Features**:
- CLI-based agent testing
- Conversation preview with session debug/trace info
- Integrated testing in VS Code
- Apex debugging from conversation preview

**Key Commands**:
```bash
# Run conversation tests
sf agents test conversation --agent "Agent Name" --scenario test-scenarios.yaml --org your-org

# Preview with debug information
sf agents preview --agent "Agent Name" --input "Test input" --debug true --org your-org

# Run performance tests
sf agents test performance --agent "Agent Name" --duration 300 --org your-org
```

### Phase 4: Deployment & Release
**Purpose**: Deploy agent to production using AgentforceDX deployment capabilities.

**AgentforceDX Features**:
- CLI-based agent deployment
- Multi-environment deployment pipeline
- Production environment management
- Deployment validation and rollback

**Key Commands**:
```bash
# Deploy to staging
sf agents deploy --agent "Agent Name" --target staging --validate true

# Deploy to production
sf agents deploy --agent "Agent Name" --target production --validate true --rollback true

# Verify deployment
sf agents status --agent "Agent Name" --target production
```

### Phase 5: Monitoring & Tuning
**Purpose**: Monitor agent performance and optimize using AgentforceDX monitoring capabilities.

**AgentforceDX Features**:
- CLI-based agent monitoring
- Performance analytics and reporting
- Automated optimization recommendations
- Real-time monitoring dashboards

**Key Commands**:
```bash
# Get agent metrics
sf agents monitor metrics --agent "Agent Name" --period 24h --org your-org

# Get performance report
sf agents monitor report --agent "Agent Name" --format json --org your-org

# Get optimization recommendations
sf agents monitor optimize --agent "Agent Name" --org your-org
```

## Project Structure

```
AgentforceDX/
├── ADLC_AgentforceDX.ipynb          # Main implementation notebook
├── README.md                   # This documentation
├── specs/                      # AgentforceDX specifications
│   └── agentSpec.yaml         # Generated agent specification
└── agent_outputs/             # Organized output files by phases
    ├── phase1_ideation/       # Agent specifications and design
    ├── phase2_development/    # Development artifacts and tools
    ├── phase3_testing/        # Test scenarios and execution
    ├── phase4_deployment/     # Deployment packages and metadata
    └── phase5_monitoring/     # Monitoring dashboards and analytics
```

## Quick Start

### Prerequisites
1. **Salesforce CLI** (latest version)
2. **AgentforceDX plugin** (auto-installed with first agent command)
3. **VS Code with AgentforceDX extension** (or Code Builder)
4. **Salesforce org** with Agentforce enabled

### Installation
```bash
# Update Salesforce CLI
sf update

# Install AgentforceDX plugin (auto-triggered with first agent command)
sf agents --help

# Install VS Code extension
# Search for 'AgentforceDX' in VS Code Marketplace
```

### Running the Implementation
1. **Open the Notebook**:
   ```bash
   jupyter notebook ADLC_AgentforceDX.ipynb
   ```

2. **Configure Salesforce Org**:
   - Authenticate with your Salesforce org
   - Ensure Agentforce is enabled

3. **Execute Phases Sequentially**:
   - Run Phase 1: Ideation & Design (Interactive specification generation)
   - Run Phase 2: Development (CLI-based agent creation)
   - Run Phase 3: Testing & Validation (Comprehensive testing)
   - Run Phase 4: Deployment & Release (Multi-environment deployment)
   - Run Phase 5: Monitoring & Tuning (Performance monitoring)

## Key Features

### Resort Manager Agent Capabilities
- Customer complaint resolution
- Employee scheduling management
- Reservation assistance
- Activity coordination
- Process optimization
- Emergency response
- Revenue management

### AgentforceDX Benefits
- **Stay in your flow**: Work with Agentforce metadata without leaving your development environment
- **Move faster**: Generate, modify, and validate agent configurations using YAML
- **Test with confidence**: Preview agent conversations while making changes to underlying Apex classes
- **Automate everything**: Integrate agent testing and evaluation directly into CI/CD pipelines

### Advanced Features
- **Interactive Specification Generation**: AI-powered topic generation based on company context
- **VS Code Integration**: Real-time editing with syntax highlighting and preview
- **CLI-Based Workflows**: Complete agent lifecycle management through command line
- **Multi-Environment Deployment**: Staging and production deployment with validation
- **Comprehensive Monitoring**: Performance analytics and optimization recommendations

## Technical Implementation

### AgentforceDX CLI Integration
- **Authentication**: Uses Salesforce CLI for org authentication
- **Agent Creation**: Uses `sf agents create` for agent development
- **Testing**: Uses `sf agents test` for comprehensive testing
- **Deployment**: Uses `sf agents deploy` for multi-environment deployment
- **Monitoring**: Uses `sf agents monitor` for performance tracking

### YAML-Based Configuration
- **Human-Readable**: YAML format for easy editing and version control
- **AI-Generated Topics**: Automatic topic generation based on company context
- **Structured Metadata**: Organized specification with clear hierarchy
- **Pro-Code Friendly**: Designed for developers who prefer code over clicks

### VS Code Integration
- **Real-Time Editing**: Live preview of agent changes
- **Syntax Highlighting**: YAML syntax support for agent specifications
- **Debug Support**: Apex debugging from conversation preview
- **Integrated Testing**: Run tests directly from VS Code

## Output Files Organization

### Phase 1: Ideation
- `specs/agentSpec.yaml` - Main agent specification
- `agent_outputs/phase1_ideation/` - Phase-specific outputs

### Phase 2: Development
- Development artifacts and tool configurations
- VS Code workspace settings
- CLI command references

### Phase 3: Testing
- Test scenarios and execution scripts
- Testing command references
- Test reports and validation results

### Phase 4: Deployment
- Deployment packages and metadata
- Multi-environment configuration
- Deployment scripts and validation

### Phase 5: Monitoring
- Performance data and analytics
- Monitoring dashboards and reports
- Optimization recommendations

## Security

- No credentials are stored in the repository
- Use Salesforce CLI authentication for org access
- All sensitive data is excluded via .gitignore
- Follow Salesforce security best practices

## Requirements

- Python 3.9+
- Jupyter Notebook
- Salesforce CLI (latest version)
- Salesforce org with Agentforce enabled
- VS Code with AgentforceDX extension (optional but recommended)

## Documentation

- **ADLC_AgentforceDX.ipynb**: Interactive implementation with all 5 phases
- **specs/agentSpec.yaml**: Agent specification template
- **agent_outputs/**: Organized output files by phases

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly using AgentforceDX CLI
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For questions and support:
- Check the [AgentforceDX Developer Guide](https://developer.salesforce.com/docs/agentforce-dx)
- Review the [Agent Commands Reference](https://developer.salesforce.com/docs/agentforce-dx/commands)
- Open an issue for bugs or feature requests

## Repository URL

**https://github.com/akshatasawant9699/Salesforce_ADLC_Whitepaper**

## Changelog

### Latest Updates
- ✅ Complete ADLC implementation with AgentforceDX
- ✅ Interactive agent specification generation
- ✅ AI-powered topic generation
- ✅ CLI-based development workflow
- ✅ VS Code integration for pro-code development
- ✅ Multi-environment deployment pipeline
- ✅ Comprehensive monitoring and optimization
- ✅ Production-ready implementation
- ✅ Professional documentation and examples

## Resources

- [AgentforceDX Developer Guide](https://developer.salesforce.com/docs/agentforce-dx)
- [Agent Commands Reference](https://developer.salesforce.com/docs/agentforce-dx/commands)
- [VS Code Extension](https://marketplace.visualstudio.com/items?itemName=salesforce.agentforce-dx)
- [Salesforce CLI Documentation](https://developer.salesforce.com/tools/sfdxcli)
