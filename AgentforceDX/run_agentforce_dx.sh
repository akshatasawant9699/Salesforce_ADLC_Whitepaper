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
    echo -e "${GREEN}[SUCCESS] $1${NC}"
}

print_info() {
    echo -e "${BLUE}[INFO] $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}[WARNING] $1${NC}"
}

print_error() {
    echo -e "${RED}[ERROR] $1${NC}"
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

# Authenticate with Salesforce
authenticate_salesforce() {
    echo ""
    echo "=== SALESFORCE AUTHENTICATION ==="
    print_info "Authenticating with Salesforce Developer Edition"
    echo ""
    
    # Set credentials
    SALESFORCE_USERNAME="akshatasawant2010824@agentforce.com"
    SALESFORCE_PASSWORD="Ambadnya@9699"
    ORG_ALIAS="agentforce-dev"
    
    print_info "Using Developer Edition credentials"
    print_info "Username: $SALESFORCE_USERNAME"
    print_info "Org Alias: $ORG_ALIAS"
    echo ""
    
    # Check if already authenticated
    if sf org list | grep -q "$ORG_ALIAS"; then
        print_status "Already authenticated with $ORG_ALIAS"
        sf org display --target-org $ORG_ALIAS
        return 0
    fi
    
    # Login to Salesforce using web authentication
    print_info "Logging into Salesforce..."
    echo "Please complete the web authentication in your browser..."
    sf org login web --alias $ORG_ALIAS --instance-url https://login.salesforce.com --set-default
    
    if [ $? -eq 0 ]; then
        print_status "Successfully authenticated with Salesforce"
        print_info "Org alias: $ORG_ALIAS"
        print_info "Instance URL: https://login.salesforce.com"
        
        # Display org info
        sf org display --target-org $ORG_ALIAS
    else
        print_error "Failed to authenticate with Salesforce"
        print_info "Please check your credentials and try again"
        print_info "You can also run: sf org login web --alias $ORG_ALIAS"
        return 1
    fi
}

# Verify authentication before running agent commands
verify_authentication() {
    print_info "Verifying Salesforce authentication..."
    
    # Check if we have an authenticated org
    if ! sf org list | grep -q "agentforce-dev"; then
        print_error "Not authenticated with Salesforce"
        print_info "Please run: sf org login web --alias agentforce-dev"
        return 1
    fi
    
    # Check if org is accessible
    if ! sf org display --target-org agentforce-dev &> /dev/null; then
        print_error "Cannot access authenticated org"
        print_info "Please re-authenticate: sf org login web --alias agentforce-dev"
        return 1
    fi
    
    print_status "Authentication verified"
    return 0
}

# Phase 1: Ideation & Design
phase1_ideation() {
    echo ""
    echo "=== PHASE 1: IDEATION & DESIGN ==="
    print_info "Creating comprehensive agent specification with all necessary details"
    echo ""
    
    # Reference the Agent Python SDK agent_spec.json structure
    print_info "Referencing Agent Python SDK agent_spec.json for specification structure"
    echo ""
    
    # Prompt for specific details as mentioned in the requirements
    echo "Please provide the following details for your agent:"
    echo ""
    
    # Type of agent
    read -p "Type of agent (Customer/Employee/Partner/External): " AGENT_TYPE
    
    # Company Name
    read -p "Company Name: " COMPANY_NAME
    
    # Company Description
    read -p "Company Description: " COMPANY_DESC
    
    # Agent Role
    read -p "Agent Role: " AGENT_ROLE
    
    # Auto-generate agent name from company name
    AGENT_NAME="${COMPANY_NAME} Customer Agent"
    
    # Use company description as agent description
    AGENT_DESC="$COMPANY_DESC"
    
    # Tone
    read -p "Tone (casual/professional/friendly): " TONE
    
    echo ""
    print_info "Using the following configuration:"
    echo "  - Agent Name: $AGENT_NAME"
    echo "  - Agent Description: $AGENT_DESC"
    echo "  - Type of agent: $AGENT_TYPE"
    echo "  - Company Name: $COMPANY_NAME"
    echo "  - Company Description: $COMPANY_DESC"
    echo "  - Agent Role: $AGENT_ROLE"
    echo "  - Tone: $TONE"
    echo ""
    
    # Create specs directory if it doesn't exist
    mkdir -p specs
    
    # Create comprehensive agentSpec.yaml with all details
    cat > specs/agentSpec.yaml << EOF
# Required top-level properties for AgentforceDX CLI
agentType: $(echo "$AGENT_TYPE" | tr '[:upper:]' '[:lower:]')
role: $AGENT_ROLE
companyName: $COMPANY_NAME
companyDescription: $COMPANY_DESC

agent:
  company:
    description: $COMPANY_DESC
    name: $COMPANY_NAME
  name: $COMPANY_NAME Customer Agent
  persona: Professional, helpful, and knowledgeable customer agent who ensures smooth operations and exceptional experiences
  role: $AGENT_ROLE
  type: $AGENT_TYPE
metadata:
  command: sf agent generate agent-spec
  created: '$(date -u +%Y-%m-%dT%H:%M:%S.%3NZ)'
  framework: AgentforceDX
  generated_by: AgentforceDX CLI
  version: '1.0'
topics:
  - name: "Reservation Management"
    description: "Handle guest reservations, modifications, and cancellations"
tools:
  - name: "ReservationSystem"
    description: "Access and manage guest reservations"
    type: "API"
    endpoint: "/api/reservations"
  - name: "GuestServices"
    description: "Provide information about resort services"
    type: "KnowledgeBase"
    source: "resort_services_kb"
  - name: "CustomerSupport"
    description: "Handle guest complaints and issues"
    type: "Workflow"
    process: "complaint_resolution"
  - name: "ActivityPlanner"
    description: "Recommend and book activities for guests"
    type: "API"
    endpoint: "/api/activities"
  - name: "EmergencyResponse"
    description: "Handle urgent situations and emergencies"
    type: "Workflow"
    process: "emergency_protocol"
knowledge_bases:
  - name: "Resort Policies"
    description: "Information about resort policies and procedures"
    source: "policies_kb"
  - name: "Local Attractions"
    description: "Information about nearby attractions and activities"
    source: "attractions_kb"
  - name: "Dining Options"
    description: "Information about restaurants and dining options"
    source: "dining_kb"
  - name: "Amenities Guide"
    description: "Information about resort amenities and facilities"
    source: "amenities_kb"
workflows:
  - name: "Reservation Process"
    description: "Complete workflow for handling reservations"
    steps:
      - "Validate guest information"
      - "Check room availability"
      - "Process payment"
      - "Send confirmation"
  - name: "Complaint Resolution"
    description: "Process for handling guest complaints"
    steps:
      - "Listen to guest concern"
      - "Assess the situation"
      - "Propose solution"
      - "Follow up on resolution"
  - name: "Activity Booking"
    description: "Process for booking activities and experiences"
    steps:
      - "Understand guest preferences"
      - "Check availability"
      - "Provide recommendations"
      - "Process booking"
settings:
  language: "en-US"
  timezone: "UTC"
  response_timeout: 30
  max_conversation_turns: 10
  escalation_threshold: 3
EOF
    
    if [ $? -eq 0 ]; then
        print_status "Comprehensive agent specification generated successfully"
        print_info "File created: specs/agentSpec.yaml"
        print_info "This file contains all necessary details for agent creation including:"
        echo "  - Agent configuration and persona"
        echo "  - 5 comprehensive topics with examples"
        echo "  - 5 tools for different functions"
        echo "  - 4 knowledge bases for information"
        echo "  - 3 workflows for common processes"
        echo "  - Settings for language and behavior"
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
    
    # Check if we're in a Salesforce project
    if [ ! -f "sfdx-project.json" ]; then
        print_info "Creating Salesforce DX project structure..."
        
        # Create sfdx-project.json
        cat > sfdx-project.json << EOF
{
  "packageDirectories": [
    {
      "path": "force-app",
      "default": true
    }
  ],
  "name": "agentforce-dx-project",
  "namespace": "",
  "sfdcLoginUrl": "https://login.salesforce.com",
  "sourceApiVersion": "60.0",
  "packageAliases": {}
}
EOF
        
        # Create force-app directory structure
        mkdir -p force-app/main/default
        
        print_status "Salesforce DX project structure created"
    fi
    
    # Verify authentication before creating agent
    if ! verify_authentication; then
        print_error "Authentication failed. Cannot create agent."
        return 1
    fi
    
    print_info "Command: sf agent create"
    print_info "This will create the agent in your Salesforce org"
    echo ""
    
    # Ask if user wants to preview first
    read -p "Do you want to preview the agent structure before creating? (y/n): " PREVIEW_CHOICE
    if [ "$PREVIEW_CHOICE" = "y" ] || [ "$PREVIEW_CHOICE" = "Y" ]; then
        print_info "Running: sf agent create --preview"
        sf agent create --spec specs/agentSpec.yaml --name "$AGENT_NAME" --preview
        
        if [ $? -eq 0 ]; then
            print_status "Agent preview completed"
            print_info "Preview JSON file generated locally"
            echo ""
        else
            print_error "Failed to preview agent"
            return 1
        fi
    fi
    
    wait_for_user
    
    print_info "Running: sf agent create"
    sf agent create --spec specs/agentSpec.yaml --name "$AGENT_NAME"
    
    if [ $? -eq 0 ]; then
        print_status "Agent created successfully"
        print_info "Agent is now available in your Salesforce org"
    else
        print_error "Failed to create agent"
        print_info "Make sure you are authenticated with Salesforce CLI"
        print_info "Run: sf org login web --alias agentforce-dev"
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
    sf agent preview --agent "$AGENT_NAME"
    
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
    sf agent deploy --agent "$AGENT_NAME"
    
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
    sf agent monitor --agent "$AGENT_NAME"
    
    if [ $? -eq 0 ]; then
        print_status "Agent monitoring completed"
        print_info "You can view performance metrics and optimization recommendations"
    else
        print_error "Failed to monitor agent"
        return 1
    fi
}

# Non-interactive mode function
non_interactive_mode() {
    echo ""
    echo "=== NON-INTERACTIVE MODE ==="
    print_info "Using default values for all inputs"
    echo ""
    
    # Set default values
    AGENT_TYPE="Customer"
    COMPANY_NAME="Coral Cloud Resorts"
    COMPANY_DESC="Luxury resort providing exceptional guest experiences"
    AGENT_ROLE="Customer service agent for resort guests"
    AGENT_NAME="${COMPANY_NAME} Customer Agent"
    AGENT_DESC="$COMPANY_DESC"
    TONE="casual"
    
    print_info "Using the following default inputs:"
    echo "  - Agent Name: $AGENT_NAME (auto-generated from company name)"
    echo "  - Agent Description: $AGENT_DESC (same as company description)"
    echo "  - Type of agent: $AGENT_TYPE"
    echo "  - Company Name: $COMPANY_NAME"
    echo "  - Company Description: $COMPANY_DESC"
    echo "  - Agent Role: $AGENT_ROLE"
    echo "  - Tone: $TONE"
    echo ""
    
    # Create specs directory if it doesn't exist
    mkdir -p specs
    
    # Create comprehensive agentSpec.yaml with all details
    cat > specs/agentSpec.yaml << EOF
# Required top-level properties for AgentforceDX CLI
agentType: $(echo "$AGENT_TYPE" | tr '[:upper:]' '[:lower:]')
role: $AGENT_ROLE
companyName: $COMPANY_NAME
companyDescription: $COMPANY_DESC

agent:
  company:
    description: $COMPANY_DESC
    name: $COMPANY_NAME
  name: $COMPANY_NAME Customer Agent
  persona: Professional, helpful, and knowledgeable customer agent who ensures smooth operations and exceptional experiences
  role: $AGENT_ROLE
  type: $AGENT_TYPE
metadata:
  command: sf agent generate agent-spec
  created: '$(date -u +%Y-%m-%dT%H:%M:%S.%3NZ)'
  framework: AgentforceDX
  generated_by: AgentforceDX CLI
  version: '1.0'
topics:
  - name: "Reservation Management"
    description: "Handle guest reservations, modifications, and cancellations"
tools:
  - name: "ReservationSystem"
    description: "Access and manage guest reservations"
    type: "API"
    endpoint: "/api/reservations"
  - name: "GuestServices"
    description: "Provide information about resort services"
    type: "KnowledgeBase"
    source: "resort_services_kb"
  - name: "CustomerSupport"
    description: "Handle guest complaints and issues"
    type: "Workflow"
    process: "complaint_resolution"
  - name: "ActivityPlanner"
    description: "Recommend and book activities for guests"
    type: "API"
    endpoint: "/api/activities"
  - name: "EmergencyResponse"
    description: "Handle urgent situations and emergencies"
    type: "Workflow"
    process: "emergency_protocol"
knowledge_bases:
  - name: "Resort Policies"
    description: "Information about resort policies and procedures"
    source: "policies_kb"
  - name: "Local Attractions"
    description: "Information about nearby attractions and activities"
    source: "attractions_kb"
  - name: "Dining Options"
    description: "Information about restaurants and dining options"
    source: "dining_kb"
  - name: "Amenities Guide"
    description: "Information about resort amenities and facilities"
    source: "amenities_kb"
workflows:
  - name: "Reservation Process"
    description: "Complete workflow for handling reservations"
    steps:
      - "Validate guest information"
      - "Check room availability"
      - "Process payment"
      - "Send confirmation"
  - name: "Complaint Resolution"
    description: "Process for handling guest complaints"
    steps:
      - "Listen to guest concern"
      - "Assess the situation"
      - "Propose solution"
      - "Follow up on resolution"
  - name: "Activity Booking"
    description: "Process for booking activities and experiences"
    steps:
      - "Understand guest preferences"
      - "Check availability"
      - "Provide recommendations"
      - "Process booking"
settings:
  language: "en-US"
  timezone: "UTC"
  response_timeout: 30
  max_conversation_turns: 10
  escalation_threshold: 3
EOF
    
    if [ $? -eq 0 ]; then
        print_status "Comprehensive agent specification generated successfully"
        print_info "File created: specs/agentSpec.yaml"
        print_info "This file contains all necessary details for agent creation including:"
        echo "  - Agent configuration and persona"
        echo "  - 5 comprehensive topics with examples"
        echo "  - 5 tools for different functions"
        echo "  - 4 knowledge bases for information"
        echo "  - 3 workflows for common processes"
        echo "  - Settings for language and behavior"
    else
        print_error "Failed to generate agent specification"
        return 1
    fi
}

# Help function
show_help() {
    echo "AGENTFORCEDX CLI SCRIPT - COMPLETE ADLC IMPLEMENTATION"
    echo ""
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --non-interactive, -n    Run in non-interactive mode with default values"
    echo "  --help, -h              Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0                      # Interactive mode (prompts for input)"
    echo "  $0 --non-interactive    # Non-interactive mode (uses defaults)"
    echo "  $0 -n                   # Short form of non-interactive mode"
    echo ""
    echo "Interactive Mode:"
    echo "  - Prompts for agent type, company name, description, and role"
    echo "  - Allows customization of all inputs"
    echo "  - Pauses between steps for review"
    echo ""
    echo "Non-Interactive Mode:"
    echo "  - Uses default values: Customer agent for Coral Cloud Resorts"
    echo "  - No user input required"
    echo "  - Runs all phases automatically"
    echo ""
    echo "Default Values:"
    echo "  - Agent Type: Customer"
    echo "  - Company Name: Coral Cloud Resorts"
    echo "  - Company Description: Luxury resort providing exceptional guest experiences"
    echo "  - Agent Role: Customer service agent for resort guests"
    echo ""
}

# Main execution
main() {
    # Check for help option
    if [ "$1" = "--help" ] || [ "$1" = "-h" ]; then
        show_help
        exit 0
    fi
    
    echo "AGENTFORCEDX CLI SCRIPT - COMPLETE ADLC IMPLEMENTATION"
    echo "This script provides a notebook-like experience using CLI commands"
    echo ""
    
    # Check for non-interactive mode
    if [ "$1" = "--non-interactive" ] || [ "$1" = "-n" ]; then
        print_info "Running in non-interactive mode"
        echo ""
        
        # Check prerequisites
        check_cli
        
        # Authenticate with Salesforce
        authenticate_salesforce
        
        echo ""
        print_info "Starting AgentforceDX ADLC implementation..."
        echo ""
        
        # Run all phases with non-interactive mode
        non_interactive_mode
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
    else
    # Check prerequisites
    check_cli
    
    # Authenticate with Salesforce
    authenticate_salesforce
    
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
    fi
}

# Run main function
main "$@"
