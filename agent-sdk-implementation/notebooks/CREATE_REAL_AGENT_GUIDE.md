# Create REAL Agent - Step-by-Step Guide

## Issue
The Salesforce CLI is experiencing technical issues creating agents programmatically. This guide shows you how to create a **REAL agent** (not mock) using the Agentforce Builder UI.

---

## Agent Specification

**Agent Name**: Coral Cloud Resorts Resort Manager  
**Agent Type**: Customer (External-facing)  
**Company**: Coral Cloud Resorts  
**Scope**: Public

---

## Step-by-Step Instructions

### Step 1: Access Agentforce Builder

1. Open your Salesforce org:
   ```
   https://your-org.salesforce.com
   ```

2. Navigate to Setup:
   - Click the gear icon (⚙️) in the top right
   - Select "Setup"

3. Find Agentforce:
   - In the Quick Find box, search for "Agentforce"
   - Click on "Agents" or "Agentforce Agents"

### Step 2: Create New Agent

1. Click the **"New Agent"** or **"Create Agent"** button

2. Enter Basic Information:
   ```
   Name: Coral Cloud Resorts Resort Manager
   Type: Customer
   Description: The resort manager fields customer complaints, manages employee schedules, and generally ensures that all processes are running smoothly for Coral Cloud Resorts
   ```

### Step 3: Configure Company Information

```
Company Name: Coral Cloud Resorts

Company Description: Coral Cloud Resorts provides customers with exceptional destination activities, unforgettable experiences, and reservation services, all backed by a commitment to provide top-notch customer service.
```

### Step 4: Set Agent Personality

```
Role: Resort Operations Manager

Tone: professional and friendly
```

### Step 5: Add Topics

Add these 5 topics to your agent:

#### Topic 1: Customer Complaint Resolution
```
Name: Customer Complaint Resolution
Description: Handle and resolve customer complaints efficiently, providing timely solutions and ensuring guest satisfaction.
```

#### Topic 2: Employee Schedule Management
```
Name: Employee Schedule Management
Description: Optimize and manage employee schedules effectively, ensuring proper coverage and work-life balance.
```

#### Topic 3: Reservation Assistance
```
Name: Reservation Assistance
Description: Support customers with booking and reservation needs, including modifications, cancellations, and special requests.
```

#### Topic 4: Activity Recommendations
```
Name: Activity Recommendations
Description: Provide tailored suggestions for destination activities based on guest preferences, weather, and availability.
```

#### Topic 5: Service Quality Monitoring
```
Name: Service Quality Monitoring
Description: Track and ensure high quality of customer service across all resort operations and touchpoints.
```

### Step 6: Save and Activate

1. Click **"Save"** to create the agent
2. Click **"Activate"** to make the agent live
3. Note the Agent ID for reference

---

## Verification

After creating the agent, verify it exists:

### Using Salesforce CLI:
```bash
sf data query --query "SELECT Id, Name, Type FROM BotDefinition WHERE Name LIKE '%Resort Manager%'" --target-org your_username@example.com
```

### Using Salesforce UI:
1. Go to Setup > Agentforce > Agents
2. You should see "Coral Cloud Resorts Resort Manager" in the list
3. Click on it to view details

---

## Alternative: Use API

If you prefer programmatic creation, use the Salesforce REST API:

```python
import requests
import json

# Authenticate and get access token
# ... authentication code ...

# Create agent via REST API
url = f"{instance_url}/services/data/v60.0/sobjects/BotDefinition"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

agent_data = {
    "Name": "Coral Cloud Resorts Resort Manager",
    "Type": "Customer",
    "Description": "Resort manager for comprehensive operations management",
    # ... additional fields ...
}

response = requests.post(url, headers=headers, json=agent_data)
print(response.json())
```

---

## Troubleshooting

### Issue: "Agentforce not found in Setup"
**Solution**: Agentforce may not be enabled in your org
- Contact Salesforce support to enable Agentforce
- Or use a different org with Agentforce enabled

### Issue: "Permission denied"
**Solution**: You need Agentforce Admin permissions
- Go to Setup > Users > Permission Sets
- Assign "Agentforce Admin" permission set to your user

### Issue: "Cannot create agent"
**Solution**: Check org edition
- Agentforce requires Enterprise Edition or higher
- Developer Edition orgs may have limited Agentforce features

---

## Files Created

The following files contain your agent specification:

1. **agentSpec.yaml** - YAML format for Salesforce CLI
2. **agent_spec.json** - JSON format with all details
3. **sfdx-project.json** - Salesforce project configuration

These files can be used for:
- Version control
- Deployment to other orgs
- Documentation
- Backup and restore

---

## Next Steps After Creating Real Agent

1. **Test the Agent**:
   - Use the Agentforce Builder preview
   - Test with sample conversations
   - Verify all topics work correctly

2. **Add Actions**:
   - Connect to Salesforce objects
   - Add custom Apex actions
   - Integrate with external systems

3. **Configure Knowledge Base**:
   - Add knowledge articles
   - Connect to Salesforce Knowledge
   - Upload documents

4. **Deploy to Production**:
   - Export agent metadata
   - Deploy using Salesforce CLI
   - Test in production org

---

## Summary

**Status**: Agent specification is ready  
**Method**: Use Agentforce Builder UI (recommended)  
**Alternative**: Salesforce REST API  
**Type**: REAL agent (not mock)  

Follow the steps above to create your **REAL** Coral Cloud Resorts Resort Manager agent in Salesforce!

---

## Support

If you encounter issues:
1. Check Salesforce Agentforce documentation
2. Verify org has Agentforce enabled
3. Ensure you have proper permissions
4. Contact Salesforce support if needed

**Documentation**: https://developer.salesforce.com/docs/einstein/genai/guide/agentforce-overview.html
