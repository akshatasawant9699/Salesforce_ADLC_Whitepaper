# Coral Cloud Resorts Agent - Command Reference

## 🚀 Quick Start Commands

### Prerequisites Check
```bash
# Check Python version
python3 --version

# Check Salesforce CLI
sf --version

# Check org connection
sf org list
```

### Essential Commands
```bash
# 1. Install dependencies
pip3 install pyyaml

# 2. Validate configuration
python3 agent_setup.py

# 3. Run demo
python3 demo_agent.py

# 4. Generate agent spec
./scripts/run_agent_generation.sh
```

### Expected Output
- ✅ Configuration validation passed
- ✅ 6 topics configured
- ✅ 7 demo scenarios tested
- ✅ Salesforce config generated

## 📁 Key Files
- `specs/agentSpec.yaml` - Agent specification
- `agent_setup.py` - Validation script
- `demo_agent.py` - Demo implementation
- `scripts/run_agent_generation.sh` - Helper script

## 🎯 Success Criteria
- All Python commands run without errors
- Configuration validation passes
- Demo shows 7 successful scenarios
- Salesforce CLI commands work
- Configuration files generated

**Ready for Phase 2 Implementation!**
