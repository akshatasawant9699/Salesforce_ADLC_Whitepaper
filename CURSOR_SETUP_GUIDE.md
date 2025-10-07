# How to Run AgentforceDX in Cursor/VS Code

This guide shows you **4 different approaches** to run the AgentforceDX implementation in Cursor (VS Code) for the best development experience.

## Prerequisites

### 1. Install Required Tools
```bash
# Install Salesforce CLI (if not already installed)
npm install -g @salesforce/cli

# Install AgentforceDX plugin
sf plugins install @salesforce/plugin-agents

# Verify installation
sf --version
sf agents --help
```

### 2. Authenticate with Salesforce
```bash
# Login to your Salesforce org
sf org login web --alias agentforce-dev

# Verify authentication
sf org list
```

## Approach 1: CLI Script (Easiest) 🚀

**Best for**: Quick execution, notebook-like experience

### Steps:
1. **Open Cursor/VS Code** in your project directory
2. **Open Integrated Terminal**: `Ctrl+`` (backtick) or `View → Terminal`
3. **Run the script** (choose one option):

   **Option A: Interactive Mode (with prompts)**
   ```bash
   ./AgentforceDX/run_agentforce_dx.sh
   ```

   **Option B: Non-Interactive Mode (with defaults)**
   ```bash
   ./AgentforceDX/run_agentforce_dx.sh --non-interactive
   ```

### What it does:
- **Interactive Mode**: Prompts for user input with defaults
- **Non-Interactive Mode**: Uses default values automatically
- Runs all 5 ADLC phases sequentially
- Colored output and status messages
- Pauses between steps for review (interactive mode)
- Error handling and validation

### Example Output:
```
AGENTFORCEDX CLI SCRIPT - COMPLETE ADLC IMPLEMENTATION
This script provides a notebook-like experience using CLI commands

[INFO] Checking Salesforce CLI installation...
[SUCCESS] Salesforce CLI: @salesforce/cli/2.15.0
[SUCCESS] AgentforceDX plugin: Available

=== PHASE 1: IDEATION & DESIGN ===
[INFO] Generating agent specification using interactive CLI command
[INFO] Command: sf agent generate agent-spec
Press Enter to continue to the next step...
```

## Approach 2: VS Code Tasks (Recommended) 🎯

**Best for**: Professional development, individual control

### Steps:
1. **Open Command Palette**: `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
2. **Type**: `Tasks: Run Task`
3. **Select from available tasks**:
   - `AgentforceDX: Generate Agent Spec`
   - `AgentforceDX: Create Agent`
   - `AgentforceDX: Preview Agent`
   - `AgentforceDX: Deploy Agent`
   - `AgentforceDX: Monitor Agent`
   - `AgentforceDX: Complete ADLC Script`
   - `AgentforceDX: Complete ADLC Script (Non-Interactive)`

### Available Tasks:
- **Individual Commands**: Run specific phases as needed
- **Complete Script**: Run all phases sequentially
- **Keyboard Shortcuts**: Quick access to commands
- **Integrated Terminal**: All output in VS Code

### Customize Tasks:
Edit `.vscode/tasks.json` to add your own tasks:
```json
{
    "label": "My Custom Task",
    "type": "shell",
    "command": "sf",
    "args": ["agents", "list"],
    "group": "build"
}
```

## Approach 3: Jupyter Notebook (Interactive) 📓

**Best for**: Interactive development, step-by-step execution

### Steps:
1. **Install Jupyter** (if not already installed):
   ```bash
   pip install jupyter
   ```

2. **Open the notebook**:
   ```bash
   jupyter notebook AgentforceDX/ADLC_AgentforceDX.ipynb
   ```

3. **Run cells sequentially**:
   - Click on each cell
   - Press `Shift+Enter` to execute
   - Follow the interactive prompts

### Notebook Features:
- **Interactive Execution**: Run cells one by one
- **Rich Output**: Visualizations and formatted output
- **Step-by-Step**: Perfect for learning and debugging
- **Save Progress**: Your work is automatically saved

## Approach 4: Individual Commands (Advanced) ⚡

**Best for**: Advanced users, custom workflows

### Phase 1: Ideation & Design
```bash
# Generate agent specification
sf agent generate agent-spec

# This will prompt you for:
# - Type of agent (e.g., Customer, Employee, Partner)
# - Company Name
# - Company Description  
# - Agent Role
```

### Phase 2: Development
```bash
# Create agent from specification
sf agents create --spec specs/agentSpec.yaml --org your-org

# Validate agent configuration
sf agents validate --spec specs/agentSpec.yaml --org your-org
```

### Phase 3: Testing & Validation
```bash
# Preview agent conversation
sf agents preview --agent "Agent Name" --org your-org

# Run conversation tests
sf agents test conversation --agent "Agent Name" --scenario test-scenarios.yaml --org your-org

# Run performance tests
sf agents test performance --agent "Agent Name" --duration 300 --org your-org
```

### Phase 4: Deployment & Release
```bash
# Deploy to staging
sf agents deploy --agent "Agent Name" --target staging --validate true

# Deploy to production
sf agents deploy --agent "Agent Name" --target production --validate true --rollback true

# Verify deployment
sf agents status --agent "Agent Name" --target production
```

### Phase 5: Monitoring & Tuning
```bash
# Get agent metrics
sf agents monitor metrics --agent "Agent Name" --period 24h --org your-org

# Get performance report
sf agents monitor report --agent "Agent Name" --format json --org your-org

# Get optimization recommendations
sf agents monitor optimize --agent "Agent Name" --org your-org
```

## Quick Start (Recommended) 🎯

### For Beginners:
1. **Use Approach 1 (CLI Script)**:
   ```bash
   ./AgentforceDX/run_agentforce_dx.sh
   ```

### For Developers:
1. **Use Approach 2 (VS Code Tasks)**:
   - Press `Ctrl+Shift+P`
   - Type `Tasks: Run Task`
   - Select `AgentforceDX: Complete ADLC Script`

### For Interactive Learning:
1. **Use Approach 3 (Jupyter Notebook)**:
   ```bash
   jupyter notebook AgentforceDX/ADLC_AgentforceDX.ipynb
   ```

## Troubleshooting

### Common Issues:

#### 1. CLI Not Found
```bash
# Install Salesforce CLI
npm install -g @salesforce/cli

# Verify installation
sf --version
```

#### 2. Plugin Not Found
```bash
# Install AgentforceDX plugin
sf plugins install @salesforce/plugin-agents

# Verify plugin
sf agents --help
```

#### 3. Org Not Authorized
```bash
# Login to your org
sf org login web --alias agentforce-dev

# Verify authentication
sf org list
```

#### 4. Permission Denied (Script)
```bash
# Make script executable
chmod +x AgentforceDX/run_agentforce_dx.sh

# Run script
./AgentforceDX/run_agentforce_dx.sh
```

#### 5. Jupyter Not Found
```bash
# Install Jupyter
pip install jupyter

# Or use conda
conda install jupyter
```

### Debug Mode:
```bash
# Run script with debug output
bash -x ./AgentforceDX/run_agentforce_dx.sh

# Run individual commands with debug
sf agents --debug create --spec specs/agentSpec.yaml
```

## Best Practices

### 1. Use VS Code Tasks for Development
- **Professional workflow**: Integrated with VS Code
- **Keyboard shortcuts**: Quick access to commands
- **Individual control**: Run specific phases as needed

### 2. Use CLI Script for Quick Execution
- **Notebook-like experience**: Sequential execution with prompts
- **Complete workflow**: All phases in one command
- **Error handling**: Stops on errors with clear messages

### 3. Use Jupyter Notebook for Learning
- **Interactive execution**: Run cells one by one
- **Rich output**: Visualizations and formatted output
- **Step-by-step**: Perfect for understanding the process

### 4. Use Individual Commands for Customization
- **Advanced control**: Run specific commands as needed
- **Custom workflows**: Build your own automation
- **Debugging**: Isolate specific issues

## Next Steps

1. **Choose your approach** based on your needs
2. **Follow the steps** for your chosen approach
3. **Run the implementation** and see the results
4. **Customize** the workflow for your specific needs
5. **Share** your experience with the team

## Repository URL

**https://github.com/akshatasawant9699/Salesforce_ADLC_Whitepaper**

## Support

- **Documentation**: Check the README.md file
- **Issues**: Open an issue on GitHub
- **Questions**: Check the troubleshooting section above

Happy coding with AgentforceDX! 🚀
