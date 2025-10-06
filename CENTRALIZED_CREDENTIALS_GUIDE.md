# 🔐 Centralized Credentials Guide - ADLC Notebook

## Overview

The ADLC notebook now uses a **centralized credentials approach** where Salesforce credentials are set once in Phase 2 and automatically reused in all subsequent phases (3, 4, and 5).

---

## How It Works

### Phase 2: Global Credential Setup
- **Location**: Cell 6 (Phase 2)
- **Purpose**: Set up global credentials that will be reused across all phases
- **Variables Created**:
  - `SALESFORCE_USERNAME` - Your Salesforce username
  - `SALESFORCE_PASSWORD` - Your Salesforce password  
  - `SALESFORCE_SECURITY_TOKEN` - Your security token (if required)
  - `auth` - Global authentication object
  - `agentforce` - Global Agentforce client

### Phases 3, 4, 5: Automatic Reuse
- **No credential input required** - automatically uses global credentials
- **Automatic validation** - checks if Phase 2 was run first
- **Seamless experience** - no need to re-authenticate

---

## User Experience

### Before (Old Approach)
```
Phase 2: Enter credentials → Authenticate
Phase 3: Enter credentials → Authenticate  
Phase 4: Enter credentials → Authenticate
Phase 5: Enter credentials → Authenticate
```

### After (New Approach)
```
Phase 2: Enter credentials → Authenticate → Store globally
Phase 3: ✅ Use global credentials automatically
Phase 4: ✅ Use global credentials automatically  
Phase 5: ✅ Use global credentials automatically
```

---

## Setup Instructions

### 1. Run Phase 2 First
**IMPORTANT**: Always run Phase 2 before any other phase to set up global credentials.

### 2. Set Your Credentials in Phase 2
In Cell 6 (Phase 2), replace the placeholder values:

```python
# =============================================================================
# 🔐 CENTRALIZED CREDENTIALS - SET ONCE, USE EVERYWHERE
# =============================================================================
SALESFORCE_USERNAME = "your_username@example.com"  # Replace with your username
SALESFORCE_PASSWORD = "your_password"              # Replace with your password  
SALESFORCE_SECURITY_TOKEN = ""                     # Add if required
```

### 3. Run Phases Sequentially
- **Phase 1**: Generate agent specification
- **Phase 2**: Set credentials and create agent
- **Phase 3**: Test agent (uses global credentials)
- **Phase 4**: Deploy agent (uses global credentials)
- **Phase 5**: Monitor agent (uses global credentials)

---

## Error Handling

### If You Skip Phase 2
```
❌ ERROR: Global credentials not found. Please run Phase 2 first.
```

**Solution**: Run Phase 2 first to set up global credentials.

### If Credentials Are Invalid
```
❌ ERROR: Authentication setup failed: [error details]
```

**Solution**: Check your credentials in Phase 2 and try again.

---

## Benefits

### ✅ User Experience
- **Set credentials once** - no repetitive input
- **Automatic reuse** - seamless across phases
- **Clear error messages** - helpful guidance

### ✅ Security
- **Centralized management** - credentials in one place
- **No duplication** - reduces credential exposure
- **Easy updates** - change once, applies everywhere

### ✅ Reliability
- **Consistent authentication** - same credentials across phases
- **Automatic validation** - ensures Phase 2 was run
- **Error prevention** - catches missing setup early

---

## Technical Details

### Global Variables Created in Phase 2
```python
# Credentials
SALESFORCE_USERNAME = "your_username@example.com"
SALESFORCE_PASSWORD = "your_password"  
SALESFORCE_SECURITY_TOKEN = ""

# Authentication objects
auth = BasicAuth(username=SALESFORCE_USERNAME, password=SALESFORCE_PASSWORD, security_token=SALESFORCE_SECURITY_TOKEN)
agentforce = Agentforce(auth=auth)
```

### Validation in Each Phase
```python
# Check for Global Credentials from Phase 2
if 'SALESFORCE_USERNAME' not in globals():
    raise Exception("Global credentials not found. Please run Phase 2 first.")

print(f"✅ Using global credentials for: {SALESFORCE_USERNAME}")
print("✅ Global authentication and Agentforce client available")
```

---

## Migration from Old Approach

### If You Have Existing Notebook
1. **Clear all outputs**: Kernel → Restart & Clear Output
2. **Run Phase 1**: Generate agent specification
3. **Run Phase 2**: Set up global credentials
4. **Run Phases 3-5**: They will automatically use global credentials

### If You Get Errors
1. **Check Phase 2 was run**: Look for "Global authentication configured" message
2. **Verify credentials**: Make sure they're correct in Phase 2
3. **Restart kernel**: If needed, restart and run phases sequentially

---

## Best Practices

### 🔐 Security
- **Never commit credentials** to git
- **Use environment variables** for production
- **Rotate credentials** regularly

### 📝 Usage
- **Always run Phase 2 first**
- **Set credentials once** in Phase 2
- **Run phases sequentially** for best results

### 🐛 Troubleshooting
- **Clear outputs** if you see old credential errors
- **Restart kernel** if global variables are missing
- **Check Phase 2** if other phases fail

---

## Summary

The centralized credentials approach provides:
- **Better user experience** - set once, use everywhere
- **Improved security** - credentials in one place
- **Enhanced reliability** - consistent authentication
- **Clear error handling** - helpful guidance

**Remember**: Always run Phase 2 first to set up global credentials, then all other phases will automatically reuse them!

---

**Date**: 2025-10-06  
**Status**: Implemented  
**Next**: Use the notebook with centralized credentials
