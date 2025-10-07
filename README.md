# The Agent Development Lifecycle (ADLC) - Complete Implementation

This repository contains a comprehensive implementation of **The Agent Development Lifecycle** using two distinct approaches: **Python SDK** and **AgentforceDX**. Both implementations demonstrate all five phases of agent development from ideation to monitoring, providing developers with complete, production-ready solutions.

## Overview

The Agent Development Lifecycle (ADLC) is a structured framework for developing AI agents that encompasses five critical phases. This repository provides two complete implementations:

1. **Agent Python SDK Implementation** - Using Salesforce Python SDK (`agentforce-sdk`)
2. **AgentforceDX Implementation** - Using Salesforce CLI and VS Code pro-code tools

Both implementations follow the same ADLC phases but use different tools and approaches, giving developers flexibility in their development workflow.

## Repository Structure

```
├── Agent Python SDK/                    # Python SDK Implementation
│   ├── agent-sdk-adlc-notebook.ipynb    # Main implementation notebook
│   ├── README.md                        # Python SDK documentation
│   ├── agent_spec.json                  # Agent specification
│   └── agent_outputs/                   # Organized output files by phases
│       ├── phase1_ideation/             # Agent specifications
│       ├── phase2_development/          # Development outputs
│       ├── phase3_testing/              # Test case XML files
│       ├── phase4_deployment/           # Deployment metadata
│       └── phase5_monitoring/           # Dashboards and monitoring
└── AgentforceDX/                       # AgentforceDX Implementation
    ├── ADLC_AgentforceDX.ipynb          # Main implementation notebook
    └── README.md                        # AgentforceDX documentation
```

## The Agent Development Lifecycle

### Phase 1: Ideation & Design

**Purpose**: Define the agent's purpose, persona, and core capabilities through structured ideation.

#### Python SDK Approach
- Interactive agent specification collection
- AI-powered topic generation based on company type
- Complete agent JSON with metadata and topics
- Python SDK compatible specification generation

#### AgentforceDX Approach
- Interactive `sf agent generate agent-spec` command
- AI-generated topics based on company and role information
- Human-readable YAML specifications in `specs/agentSpec.yaml`
- VS Code integration for real-time editing

**Output**: Agent specification files ready for development

### Phase 2: Development

**Purpose**: Build agent with core functionality using development tools.

#### Python SDK Approach
- Salesforce SDK integration with authentication
- Real agent creation in Salesforce org
- Tools and knowledge base implementation using `Action` classes
- Centralized credential management

#### AgentforceDX Approach
- CLI-based agent creation and management
- VS Code integration for real-time development
- YAML-based tool and action definitions
- Pro-code workflows in familiar development environment

**Key Commands (AgentforceDX)**:
```bash
# Create agent from specification
sf agents create --spec specs/agentSpec.yaml --org your-org

# Validate agent configuration
sf agents validate --spec specs/agentSpec.yaml --org your-org

# Preview agent conversation
sf agents preview --agent "Agent Name" --org your-org
```

### Phase 3: Testing & Validation

**Purpose**: Ensure agent quality, security, and performance using comprehensive testing.

#### Python SDK Approach
- **Salesforce Testing API Integration**: Uses `AiEvaluationDefinition` metadata type
- **Comprehensive Test Suites**: Guest Services, Employee Management, Revenue Optimization
- **Multi-Dimensional Testing**: Utterances, context variables, conversation history
- **Quality Metrics**: Accuracy, empathy, relevance, conciseness
- **Connect API Integration**: Test execution and detailed reports

#### AgentforceDX Approach
- CLI-based agent testing
- Conversation preview with session debug/trace info
- Integrated testing in VS Code
- Apex debugging from conversation preview

**Key Commands (AgentforceDX)**:
```bash
# Run conversation tests
sf agents test conversation --agent "Agent Name" --scenario test-scenarios.yaml --org your-org

# Preview with debug information
sf agents preview --agent "Agent Name" --input "Test input" --debug true --org your-org

# Run performance tests
sf agents test performance --agent "Agent Name" --duration 300 --org your-org
```

### Phase 4: Deployment & Release

**Purpose**: Deploy the validated agent to production Salesforce environment.

#### Python SDK Approach
- Automated deployment using `agentforce-sdk`
- Real agent creation in Salesforce org
- Deployment verification
- Builder UI integration

#### AgentforceDX Approach
- CLI-based agent deployment
- Multi-environment deployment pipeline
- Production environment management
- Deployment validation and rollback

**Key Commands (AgentforceDX)**:
```bash
# Deploy to staging
sf agents deploy --agent "Agent Name" --target staging --validate true

# Deploy to production
sf agents deploy --agent "Agent Name" --target production --validate true --rollback true

# Verify deployment
sf agents status --agent "Agent Name" --target production
```

### Phase 5: Monitoring & Tuning

**Purpose**: Monitor agent performance and continuously optimize through data-driven insights.

#### Python SDK Approach
- **Enhanced Observability**: Comprehensive monitoring class
- **Multi-Dimensional Metrics**: Response time, success rate, user satisfaction
- **Performance Dashboards**: Matplotlib and Plotly visualizations
- **Trace Management**: Execution traces with severity levels
- **Interactive Visualizations**: Radar charts, heatmaps, gauge charts
- **Comprehensive Reporting**: Detailed observability reports

#### AgentforceDX Approach
- CLI-based agent monitoring
- Performance analytics and reporting
- Automated optimization recommendations
- Real-time monitoring dashboards

**Key Commands (AgentforceDX)**:
```bash
# Get agent metrics
sf agents monitor metrics --agent "Agent Name" --period 24h --org your-org

# Get performance report
sf agents monitor report --agent "Agent Name" --format json --org your-org

# Get optimization recommendations
sf agents monitor optimize --agent "Agent Name" --org your-org
```

## Quick Start

### Prerequisites

#### For Python SDK Implementation
- Python 3.9+
- Salesforce Developer Edition org with Agentforce enabled
- Jupyter Notebook
- Required packages: `agentforce-sdk`, `pandas`, `matplotlib`, `seaborn`, `plotly`, `numpy`

#### For AgentforceDX Implementation
- Salesforce CLI (latest version)
- AgentforceDX plugin (auto-installed with first agent command)
- VS Code with AgentforceDX extension (or Code Builder)
- Salesforce org with Agentforce enabled

### Installation

#### Python SDK
```bash
pip install agentforce-sdk pandas matplotlib seaborn plotly numpy jupyter
```

#### AgentforceDX
```bash
# Update Salesforce CLI
sf update

# Install AgentforceDX plugin (auto-triggered with first agent command)
sf agents --help

# Install VS Code extension
# Search for 'AgentforceDX' in VS Code Marketplace
```

### Running the Implementations

#### Python SDK Implementation
1. **Open the Notebook**:
   ```bash
   jupyter notebook "Agent Python SDK/agent-sdk-adlc-notebook.ipynb"
   ```

2. **Configure Credentials**:
   - Update Salesforce credentials in Phase 2
   - Ensure you have agentforce-sdk access

3. **Execute Phases Sequentially**:
   - Run Phase 1: Ideation & Design
   - Run Phase 2: Development
   - Run Phase 3: Testing & Validation
   - Run Phase 4: Deployment & Release
   - Run Phase 5: Monitoring & Tuning

#### AgentforceDX Implementation
1. **Open the Notebook**:
   ```bash
   jupyter notebook "AgentforceDX/ADLC_AgentforceDX.ipynb"
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
- Resort policy knowledge
- Emergency response coordination
- Activity recommendations
- Guest services
- Maintenance coordination
- Special events management

### Advanced Features

#### Python SDK Implementation
- **Performance Monitoring**: Response time, success rate, user satisfaction
- **Trace Management**: Execution traces with severity levels
- **Interactive Dashboards**: Matplotlib and Plotly visualizations
- **Comprehensive Reporting**: Detailed analytics and recommendations
- **Salesforce Testing API**: AiEvaluationDefinition integration
- **Quality Metrics**: Accuracy, empathy, relevance, conciseness

#### AgentforceDX Implementation
- **Interactive Specification**: AI-powered topic generation based on company context
- **VS Code Integration**: Real-time editing with syntax highlighting and preview
- **CLI-Based Workflows**: Complete agent lifecycle management through command line
- **Multi-Environment Deployment**: Staging and production deployment with validation
- **Comprehensive Monitoring**: Performance analytics and optimization recommendations

## Technical Implementation

### Python SDK Integration
- **Authentication**: Uses `BasicAuth` for Salesforce authentication
- **Agent Creation**: Uses `Agentforce` and `AgentUtils` classes
- **Tools**: Implements `Action` classes for agent tools
- **Testing**: Integrates with Salesforce Testing API
- **Monitoring**: Advanced observability and performance tracking

### AgentforceDX Integration
- **Authentication**: Uses Salesforce CLI for org authentication
- **Agent Creation**: Uses `sf agents create` for agent development
- **Testing**: Uses `sf agents test` for comprehensive testing
- **Deployment**: Uses `sf agents deploy` for multi-environment deployment
- **Monitoring**: Uses `sf agents monitor` for performance tracking

### YAML-Based Configuration (AgentforceDX)
- **Human-Readable**: YAML format for easy editing and version control
- **AI-Generated Topics**: Automatic topic generation based on company context
- **Structured Metadata**: Organized specification with clear hierarchy
- **Pro-Code Friendly**: Designed for developers who prefer code over clicks

### VS Code Integration (AgentforceDX)
- **Real-Time Editing**: Live preview of agent changes
- **Syntax Highlighting**: YAML syntax support for agent specifications
- **Debug Support**: Apex debugging from conversation preview
- **Integrated Testing**: Run tests directly from VS Code

## Output Files Organization

### Python SDK Implementation
- **Phase 1**: Agent specifications and design documents
- **Phase 2**: Development artifacts and configurations
- **Phase 3**: All test files (6 comprehensive test suites)
- **Phase 4**: Deployment packages and metadata
- **Phase 5**: Performance data, analytics, and monitoring dashboards

### AgentforceDX Implementation
- **Phase 1**: `specs/agentSpec.yaml` (main specification)
- **Phase 2**: Development artifacts and tool configurations
- **Phase 3**: Test scenarios and execution scripts
- **Phase 4**: Deployment packages and metadata
- **Phase 5**: Performance data and analytics

## Security

- No credentials are stored in the repository
- Use environment variables or secure credential management
- All sensitive data is excluded via .gitignore
- Follow Salesforce security best practices

## Requirements

### Python SDK Implementation
- Python 3.9+
- Jupyter Notebook
- Salesforce org with Agentforce enabled
- agentforce-sdk package
- Additional packages: plotly, numpy, matplotlib, seaborn, pandas

### AgentforceDX Implementation
- Salesforce CLI (latest version)
- AgentforceDX plugin
- VS Code with AgentforceDX extension (optional but recommended)
- Salesforce org with Agentforce enabled

## Documentation

- **Agent Python SDK/agent-sdk-adlc-notebook.ipynb**: Interactive implementation with all 5 phases
- **AgentforceDX/ADLC_AgentforceDX.ipynb**: Interactive implementation with all 5 phases
- **Agent Python SDK/README.md**: Python SDK specific documentation
- **AgentforceDX/README.md**: AgentforceDX specific documentation

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly using both implementations
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For questions and support:
- Check the documentation in the respective notebooks
- Review the troubleshooting sections
- Open an issue for bugs or feature requests

## Repository URL

**https://github.com/akshatasawant9699/Salesforce_ADLC_Whitepaper**

## Changelog

### Latest Updates
- ✅ Complete ADLC implementation with both Python SDK and AgentforceDX
- ✅ Interactive agent specification generation for both approaches
- ✅ AI-powered topic generation and YAML-based configurations
- ✅ CLI-based development workflow with VS Code integration
- ✅ Multi-environment deployment pipeline
- ✅ Comprehensive monitoring and optimization
- ✅ Production-ready implementations
- ✅ Professional documentation and examples
- ✅ Clean repository structure with organized output files
- ✅ No emojis, professional presentation
- ✅ Aligned with "The Agent Development Lifecycle" paper

## Resources

### Python SDK
- [Salesforce Python SDK Documentation](https://developer.salesforce.com/docs/agentforce-sdk)
- [Agentforce SDK GitHub](https://github.com/salesforce/agentforce-sdk)

### AgentforceDX
- [AgentforceDX Developer Guide](https://developer.salesforce.com/docs/agentforce-dx)
- [Agent Commands Reference](https://developer.salesforce.com/docs/agentforce-dx/commands)
- [VS Code Extension](https://marketplace.visualstudio.com/items?itemName=salesforce.agentforce-dx)
- [Salesforce CLI Documentation](https://developer.salesforce.com/tools/sfdxcli)

### General
- [Salesforce Agentforce Documentation](https://developer.salesforce.com/docs/agentforce)
- [The Agent Development Lifecycle Paper](https://developer.salesforce.com/docs/agentforce-lifecycle)
