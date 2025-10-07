#!/bin/bash
# AgentforceDX Testing Script
echo "=== AGENTFORCEDX TESTING ==="

# Validate agent configuration
echo "Validating agent configuration..."
sf agents validate --agent "Coral Cloud Resorts Resort Manager" --org agentforce-dev

# Run conversation tests
echo "Running conversation tests..."
sf agents test conversation --agent "Coral Cloud Resorts Resort Manager" --scenario agent_outputs/phase3_testing/agentforce_test_scenarios.yaml --org agentforce-dev

# Preview agent conversation
echo "Previewing agent conversation..."
sf agents preview --agent "Coral Cloud Resorts Resort Manager" --input "I need help with my reservation" --debug true --org agentforce-dev

echo "=== TESTING COMPLETE ==="
