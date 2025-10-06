# Agent Development Lifecycle (ADLC) - Python SDK Implementation

This folder contains the complete implementation of the Agent Development Lifecycle using Salesforce Python SDK and Agentforce DX.

## Contents

- **`ADLC_PythonSDK.ipynb`** - Main Jupyter notebook implementing all 5 phases of ADLC
- **`ADLC_AFDX.md`** - Agentforce DX implementation guide
- **`agent_spec.json`** - Agent specification template
- **`agent_outputs/`** - Organized output files by phases

## Quick Start

1. **Python SDK Approach**: Run `ADLC_PythonSDK.ipynb` notebook
2. **Agentforce DX Approach**: Follow `ADLC_AFDX.md` guide

## Requirements

- Python 3.9+
- Salesforce Developer Edition
- Required packages: pandas, matplotlib, seaborn, plotly, numpy

## Phase Structure

```
agent_outputs/
├── phase1_ideation/          # Agent specification
├── phase2_development/       # Development outputs
├── phase3_testing/          # Test case XML files
├── phase4_deployment/       # Deployment metadata
└── phase5_monitoring/       # Dashboards and monitoring
```

## Usage

1. **Phase 1**: Generate agent specification
2. **Phase 2**: Create agent with tools and knowledge base
3. **Phase 3**: Test agent with Salesforce Testing API
4. **Phase 4**: Deploy agent to Salesforce
5. **Phase 5**: Monitor agent performance

## Features

- **Centralized credentials** - Set once in Phase 2, used in all phases
- **Real agent creation** - Not mock, actual Salesforce agents
- **Comprehensive testing** - Salesforce Testing API integration
- **Organized outputs** - Files sorted by phases
- **Clean interface** - No emojis, professional appearance

## Documentation

- **Notebook**: Complete implementation with all 5 phases
- **Agentforce DX**: CLI-based implementation guide
- **Outputs**: Organized by phases with clear structure
