# ADLC Implementation - Python SDK & Agentforce DX

This repository contains the complete Agent Development Lifecycle (ADLC) implementation using both the Salesforce Python SDK and Agentforce DX for creating, testing, and deploying AI agents.

## Project Structure

```
agent-sdk-implementation/
├── notebooks/
│   ├── ADLC_PythonSDK.ipynb    # Complete notebook with all 5 phases
│   ├── agent_spec.json         # Generated agent specification
│   └── deploy_agent.py         # Standalone deployment script
├── docs/
│   ├── ADLC_AFDX.md            # Complete AFDX implementation guide
│   ├── specs/
│   │   └── agentSpec.yaml      # Sample agent specification
│   └── README_AFDX.md          # AFDX documentation
├── requirements.txt            # Python dependencies
├── .gitignore                 # Git ignore rules
├── WHITEPAPER.md              # Project documentation
└── README.md                  # This file
```

## Features

### Implementation Approaches

#### Python SDK Implementation
- **Jupyter Notebook**: Complete interactive implementation
- **Python SDK**: Uses `agentforce-sdk` for agent creation
- **Data Cloud Integration**: Performance monitoring and analytics

#### Agentforce DX Implementation
- **Pro-Code Development**: CLI-based agent development
- **Version Control**: Git integration for agent metadata
- **CI/CD Integration**: Automated deployment pipelines
- **Modern DevOps**: Industry-standard development practices

### Phase 1: Ideation & Design
- Interactive agent specification generation
- Company and role-based topic generation
- JSON specification creation compatible with agentforce-sdk
- YAML specification for Agentforce DX

### Phase 2: Development
- Agent creation using Salesforce Python SDK
- Enhanced resort manager capabilities
- Advanced features including:
  - Weather-based activity recommendations
  - Revenue optimization
  - Guest satisfaction analytics
  - Reservation management
  - Employee scheduling
  - Complaint handling

### Phase 3: Testing & Validation
- Comprehensive testing suite with:
  - Unit testing for individual functions
  - End-to-end conversation simulation
  - Adversarial testing for security
  - Performance and load testing
- All tests validated and working

### Phase 4: Deployment & Release
- Deploy agent to Salesforce using Agentforce DX
- Open agent in Agentforce Builder UI
- Manage agent metadata and version control
- Production readiness checklist

### Phase 5: Monitoring & Tuning
- Monitor agent performance using Data Cloud Python Connector
- Track key metrics: response time, success rate, user satisfaction, cost
- Generate performance analytics and visualizations
- Provide optimization recommendations
- Export performance data for analysis
- Configure monitoring dashboards

## Quick Start

### Python SDK Implementation

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Notebook**
   ```bash
   jupyter notebook notebooks/ADLC_PythonSDK.ipynb
   ```

3. **Configure Credentials**
   - Replace placeholder credentials in the notebook with your Salesforce credentials
   - Ensure you have agentforce-sdk access

### Agentforce DX Implementation

1. **Install Salesforce CLI**
   ```bash
   npm install -g @salesforce/cli
   sf update
   ```

2. **Create DX Project**
   ```bash
   sf project generate --name agentforcedx
   cd agentforcedx
   ```

3. **Authorize Org**
   ```bash
   sf org login web --alias agentforce
   ```

4. **Generate Agent Specification**
   ```bash
   sf agent generate agent-spec
   ```

5. **Create Agent**
   ```bash
   sf agent create --spec-file specs/agentSpec.yaml
   ```

## Requirements

### Python SDK Implementation
- Python 3.9+
- Jupyter Notebook
- Salesforce org with Agentforce enabled
- agentforce-sdk package

### Agentforce DX Implementation
- Salesforce CLI (latest version)
- Visual Studio Code with Salesforce Extensions
- Salesforce Developer Edition org with Agentforce enabled
- Git for version control

## Usage

### Python SDK Implementation

The notebook provides a complete implementation of the Agent Development Lifecycle:

1. **Phase 1**: Collect agent requirements and generate specification
2. **Phase 2**: Create agent with enhanced capabilities and tools
3. **Phase 3**: Comprehensive testing and validation
4. **Phase 4**: Deploy agent to production Salesforce org
5. **Phase 5**: Monitor agent performance and provide analytics

#### Running All Phases

Execute the notebook cells in sequence to complete the full ADLC:

1. **Phase 1**: Generates `agent_spec.json` with agent specification
2. **Phase 2**: Creates agent with advanced resort management capabilities
3. **Phase 3**: Runs comprehensive tests (unit, E2E, adversarial, performance)
4. **Phase 4**: Deploys agent to your Salesforce org using agentforce-sdk
5. **Phase 5**: Monitors agent performance using Data Cloud analytics

#### Standalone Deployment

For quick deployment without running the full notebook:

```bash
cd notebooks
python deploy_agent.py
```

**Note**: Update credentials in the script before running.

### Agentforce DX Implementation

Follow the comprehensive guide in `docs/ADLC_AFDX.md` for the complete Agentforce DX implementation:

1. **Phase 1**: Generate agent specification using `sf agent generate agent-spec`
2. **Phase 2**: Create agent from specification using `sf agent create`
3. **Phase 3**: Test agent functionality using `sf agent test`
4. **Phase 4**: Deploy agent using `sf project deploy start`
5. **Phase 5**: Monitor agent using `sf agent monitor` commands

#### Key Commands

```bash
# Generate agent specification
sf agent generate agent-spec

# Create agent from specification
sf agent create --spec-file specs/agentSpec.yaml

# Test agent
sf agent test --agent-name "Agent Name"

# Deploy agent
sf project deploy start --target-org org-alias

# Monitor agent
sf agent monitor enable --agent-name "Agent Name"
```

## Advanced Features

- **Weather Integration**: Context-aware activity recommendations
- **Revenue Optimization**: Dynamic pricing based on demand
- **Analytics**: Guest satisfaction analysis and insights
- **Knowledge Base**: Resort policies and procedures
- **Tools**: Comprehensive resort management functions

## Security

- No credentials are stored in the repository
- Use environment variables or secure credential management
- All sensitive data is excluded via .gitignore

## Documentation

- **WHITEPAPER.md**: Detailed implementation documentation
- **docs/ADLC_AFDX.md**: Complete Agentforce DX implementation guide with all 5 phases
- **docs/README_AFDX.md**: Agentforce DX quick start guide

## License

This project is for demonstration purposes of the Salesforce Agent Development Lifecycle.