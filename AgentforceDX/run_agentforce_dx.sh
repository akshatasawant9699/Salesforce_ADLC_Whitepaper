#!/bin/bash

# AgentforceDX CLI Script - Complete ADLC Implementation
# This script runs all AgentforceDX commands sequentially for a notebook-like experience

echo "=== AGENTFORCEDX CLI SCRIPT - COMPLETE ADLC IMPLEMENTATION ==="
echo "This script provides a notebook-like experience using CLI commands"
echo ""

# Colors for better output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Function to wait for user input
wait_for_user() {
    echo ""
    read -p "Press Enter to continue to the next step..."
    echo ""
}

# Check if Salesforce CLI is installed
check_cli() {
    print_info "Checking Salesforce CLI installation..."
    if ! command -v sf &> /dev/null; then
        print_error "Salesforce CLI is not installed. Please install it first."
        echo "Run: npm install -g @salesforce/cli"
        exit 1
    fi
    
    # Check CLI version
    sf_version=$(sf --version)
    print_status "Salesforce CLI: $sf_version"
    
    # Check if agents plugin is available
    if ! sf agents --help &> /dev/null; then
        print_warning "AgentforceDX plugin not found. Installing..."
        sf plugins install @salesforce/plugin-agents
    fi
    
    print_status "AgentforceDX plugin: Available"
}

# Phase 1: Ideation & Design
phase1_ideation() {
    echo ""
    echo "=== PHASE 1: IDEATION & DESIGN ==="
    print_info "Generating agent specification using interactive CLI command"
    echo ""
    
    print_info "Command: sf agent generate agent-spec"
    print_info "This will prompt you for:"
    echo "  - Type of agent (e.g., Customer, Employee, Partner)"
    echo "  - Company Name"
    echo "  - Company Description"
    echo "  - Agent Role"
    echo ""
    
    print_warning "You will need to provide the information interactively"
    print_info "Example inputs:"
    echo "  - Type of agent: Customer"
    echo "  - Company Name: Coral Cloud Resorts"
    echo "  - Company Description: [Your company description]"
    echo "  - Agent Role: [Your agent role]"
    echo ""
    
    wait_for_user
    
    print_info "Running: sf agent generate agent-spec"
    sf agent generate agent-spec
    
    if [ $? -eq 0 ]; then
        print_status "Agent specification generated successfully"
        print_info "File created: specs/agentSpec.yaml"
        print_info "This file contains AI-generated topics based on your input"
    else
        print_error "Failed to generate agent specification"
        return 1
    fi
}

# Phase 2: Development
phase2_development() {
    echo ""
    echo "=== PHASE 2: DEVELOPMENT ==="
    print_info "Creating agent from specification"
    echo ""
    
    print_info "Command: sf agent create"
    print_info "This will create the agent in your Salesforce org"
    echo ""
    
    wait_for_user
    
    print_info "Running: sf agent create"
    sf agent create --spec specs/agentSpec.yaml
    
    if [ $? -eq 0 ]; then
        print_status "Agent created successfully"
        print_info "Agent is now available in your Salesforce org"
    else
        print_error "Failed to create agent"
        return 1
    fi
}

# Phase 3: Testing & Validation
phase3_testing() {
    echo ""
    echo "=== PHASE 3: TESTING & VALIDATION ==="
    print_info "Testing agent with conversation preview"
    echo ""
    
    print_info "Command: sf agent preview"
    print_info "This will open a conversation preview to test your agent"
    echo ""
    
    wait_for_user
    
    print_info "Running: sf agent preview"
    sf agent preview --agent "Coral Cloud Resorts Customer Agent"
    
    if [ $? -eq 0 ]; then
        print_status "Agent preview completed"
        print_info "You can test conversations with your agent"
    else
        print_error "Failed to preview agent"
        return 1
    fi
}

# Phase 4: Deployment & Release
phase4_deployment() {
    echo ""
    echo "=== PHASE 4: DEPLOYMENT & RELEASE ==="
    print_info "Deploying agent to production"
    echo ""
    
    print_info "Command: sf agent deploy"
    print_info "This will deploy the agent to your target org"
    echo ""
    
    wait_for_user
    
    print_info "Running: sf agent deploy"
    sf agent deploy --agent "Coral Cloud Resorts Customer Agent"
    
    if [ $? -eq 0 ]; then
        print_status "Agent deployed successfully"
        print_info "Agent is now live in your production org"
    else
        print_error "Failed to deploy agent"
        return 1
    fi
}

# Phase 5: Monitoring & Tuning
phase5_monitoring() {
    echo ""
    echo "=== PHASE 5: MONITORING & TUNING ==="
    print_info "Monitoring agent performance"
    echo ""
    
    print_info "Command: sf agent monitor"
    print_info "This will show agent performance metrics"
    echo ""
    
    wait_for_user
    
    print_info "Running: sf agent monitor"
    sf agent monitor --agent "Coral Cloud Resorts Customer Agent"
    
    if [ $? -eq 0 ]; then
        print_status "Agent monitoring completed"
        print_info "You can view performance metrics and optimization recommendations"
    else
        print_error "Failed to monitor agent"
        return 1
    fi
}

# Main execution
main() {
    echo "🚀 AGENTFORCEDX CLI SCRIPT - COMPLETE ADLC IMPLEMENTATION"
    echo "This script provides a notebook-like experience using CLI commands"
    echo ""
    
    # Check prerequisites
    check_cli
    
    echo ""
    print_info "Starting AgentforceDX ADLC implementation..."
    echo ""
    
    # Run all phases
    phase1_ideation
    phase2_development
    phase3_testing
    phase4_deployment
    phase5_monitoring
    
    echo ""
    echo "=== ADLC IMPLEMENTATION COMPLETE ==="
    print_status "All phases completed successfully"
    print_info "Your agent is now fully implemented using AgentforceDX"
    echo ""
    print_info "Next steps:"
    echo "  - Review the generated agentSpec.yaml file"
    echo "  - Test your agent in the Salesforce org"
    echo "  - Monitor performance and optimize as needed"
    echo ""
    print_status "AgentforceDX ADLC implementation complete!"
}

# Run main function
main "$@"
