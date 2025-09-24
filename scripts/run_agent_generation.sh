#!/bin/bash

echo "🏝️  Coral Cloud Resorts Agent Generation"
echo "========================================"
echo ""
echo "This script will help you run the Salesforce CLI agent generation command."
echo "Follow the prompts and provide the following answers:"
echo ""
echo "📝 PREPARE YOUR ANSWERS:"
echo "1. Type of agent: Customer"
echo "2. Company Name: Coral Cloud Resorts"
echo "3. Company Description: Coral Cloud Resorts provides customers with exceptional destination activities, unforgettable experiences, and reservation services, all backed by a commitment to top-notch customer service."
echo "4. Role of the agent: The resort manager fields customer complaints, manages employee schedules, and generally makes sure everything is working smoothly."
echo ""
echo "Press Enter to start the agent generation..."
read

echo "🚀 Starting agent generation..."
echo "Command: sf agent generate agent-spec --target-org resorts-demo"
echo "Note: Using 'resorts-demo' alias (new org connection)"
echo ""

sf agent generate agent-spec --target-org resorts-demo

echo ""
echo "✅ Agent generation completed!"
echo "📁 Check the generated file: specs/agentSpec.yaml"
echo ""
echo "🔍 To review the generated file:"
echo "cat specs/agentSpec.yaml"
echo ""
echo "📊 To compare with our implementation:"
echo "diff specs/agentSpec.yaml specs/agentSpec.yaml.backup"
