# AgentforceDX - VS Code Notebook-Like Experience

This guide shows you how to get a notebook-like experience with AgentforceDX using VS Code and the AgentforceDX extension.

## Prerequisites

1. **VS Code** with Salesforce Extensions
2. **Salesforce CLI** (latest version)
3. **AgentforceDX Extension** for VS Code
4. **Salesforce Developer Edition** org with Agentforce enabled

## Setup Instructions

### Step 1: Install VS Code Extensions

1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search for and install:
   - **Salesforce Extension Pack**
   - **AgentforceDX Extension** (when available)

### Step 2: Create Salesforce DX Project

1. Open VS Code
2. Press `Ctrl+Shift+P` (Command Palette)
3. Type: `SFDX: Create Project`
4. Choose: `Standard`
5. Project name: `agentforce-dx-project`
6. Click `Create Project`

### Step 3: Authorize Your Org

1. Press `Ctrl+Shift+P`
2. Type: `SFDX: Authorize an Org`
3. Choose: `Project Default`
4. Alias: `agentforce-dev`
5. Sign in to your Developer Edition org
6. Click `Allow`

### Step 4: Install AgentforceDX Plugin

```bash
# In VS Code integrated terminal
sf plugins install @salesforce/plugin-agents
```

## Notebook-Like Experience

### Method 1: VS Code Integrated Terminal + Script

1. **Open Integrated Terminal**: `Ctrl+`` (backtick)
2. **Run the Script**:
   ```bash
   ./run_agentforce_dx.sh
   ```
3. **Follow Interactive Prompts**: The script will guide you through each phase

### Method 2: VS Code Tasks (Recommended)

Create `.vscode/tasks.json`:

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "AgentforceDX: Generate Agent Spec",
            "type": "shell",
            "command": "sf",
            "args": ["agent", "generate", "agent-spec"],
            "group": "build",
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "new"
            },
            "problemMatcher": []
        },
        {
            "label": "AgentforceDX: Create Agent",
            "type": "shell",
            "command": "sf",
            "args": ["agent", "create", "--spec", "specs/agentSpec.yaml"],
            "group": "build",
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "new"
            },
            "problemMatcher": []
        },
        {
            "label": "AgentforceDX: Preview Agent",
            "type": "shell",
            "command": "sf",
            "args": ["agent", "preview", "--agent", "Coral Cloud Resorts Customer Agent"],
            "group": "build",
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "new"
            },
            "problemMatcher": []
        },
        {
            "label": "AgentforceDX: Deploy Agent",
            "type": "shell",
            "command": "sf",
            "args": ["agent", "deploy", "--agent", "Coral Cloud Resorts Customer Agent"],
            "group": "build",
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "new"
            },
            "problemMatcher": []
        },
        {
            "label": "AgentforceDX: Monitor Agent",
            "type": "shell",
            "command": "sf",
            "args": ["agent", "monitor", "--agent", "Coral Cloud Resorts Customer Agent"],
            "group": "build",
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "new"
            },
            "problemMatcher": []
        }
    ]
}
```

### Method 3: VS Code Launch Configuration

Create `.vscode/launch.json`:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "AgentforceDX: Complete ADLC",
            "type": "node",
            "request": "launch",
            "program": "${workspaceFolder}/run_agentforce_dx.sh",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}"
        }
    ]
}
```

## Usage Instructions

### Option 1: Run Script (Easiest)

1. Open VS Code in your project directory
2. Open integrated terminal: `Ctrl+``
3. Run: `./run_agentforce_dx.sh`
4. Follow the interactive prompts

### Option 2: Use VS Code Tasks

1. Press `Ctrl+Shift+P`
2. Type: `Tasks: Run Task`
3. Select the task you want to run:
   - `AgentforceDX: Generate Agent Spec`
   - `AgentforceDX: Create Agent`
   - `AgentforceDX: Preview Agent`
   - `AgentforceDX: Deploy Agent`
   - `AgentforceDX: Monitor Agent`

### Option 3: Use Launch Configuration

1. Press `F5` or go to Run and Debug
2. Select `AgentforceDX: Complete ADLC`
3. Click the play button

## Benefits of This Approach

### ✅ Notebook-Like Experience
- **Sequential Execution**: Run commands one by one
- **Interactive Prompts**: Just like a notebook
- **Visual Feedback**: Colored output and status messages
- **Pause Between Steps**: Review results before continuing

### ✅ VS Code Integration
- **Integrated Terminal**: Run commands directly in VS Code
- **Task Runner**: Execute commands with keyboard shortcuts
- **Debug Support**: Step through the process
- **File Management**: All files in one place

### ✅ Professional Workflow
- **Version Control**: Git integration
- **Team Collaboration**: Share the same setup
- **CI/CD Ready**: Scripts can be automated
- **Documentation**: Everything in one place

## Advanced Features

### Custom Commands
You can add custom commands to the script:

```bash
# Add to run_agentforce_dx.sh
custom_command() {
    print_info "Running custom command..."
    sf agent validate --spec specs/agentSpec.yaml
}
```

### Error Handling
The script includes error handling and will stop if a command fails.

### Logging
All commands are logged with timestamps and results.

## Troubleshooting

### Common Issues

1. **CLI Not Found**: Install Salesforce CLI
2. **Plugin Not Found**: Install AgentforceDX plugin
3. **Org Not Authorized**: Run `sf org login web`
4. **Permission Denied**: Make script executable with `chmod +x`

### Debug Mode

Run with debug output:
```bash
bash -x ./run_agentforce_dx.sh
```

## Next Steps

1. **Run the Script**: Start with `./run_agentforce_dx.sh`
2. **Customize Commands**: Modify the script for your needs
3. **Add to CI/CD**: Use the script in your deployment pipeline
4. **Share with Team**: Commit the script to your repository

This approach gives you the best of both worlds: the power of CLI commands with the convenience of a notebook-like experience!
