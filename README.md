# 🤖 Directory Clean-Up Agent

An AI-powered agentic filesystem automation system that can **perceive, remember, plan, validate, execute, observe, and iterate** over directory cleanup operations.

The project uses **Python + Google Gemini AI** to generate intelligent cleanup plans while maintaining safety through validation, human confirmation, execution verification, persistent memory, and controlled retries.

---

# 🎯 Project Overview

The Directory Clean-Up Agent is designed to automate repetitive filesystem organization tasks.

Instead of directly modifying files, the agent follows a controlled agentic workflow:

```text
Perceive
    ↓
Remember
    ↓
Plan
    ↓
Validate
    ↓
Human Confirmation
    ↓
Act
    ↓
Observe
    ↓
Update Memory
    ↓
Evaluate
    ↓
Repeat if required
```

The system can:

- Scan directories
- Collect file metadata
- Analyze files using Gemini AI
- Generate cleanup plans
- Validate AI-generated plans
- Move files
- Delete temporary files
- Rename files
- Ignore unknown files
- Verify completed operations
- Remember previous operations
- Avoid unnecessary repeated actions
- Retry temporary failures
- Stop safely after repeated errors
- Maintain structured logs

---

# 🚀 Development Progress

## 📅 Day 1 – Project Setup

### Objectives

- Initialized the Directory Clean-Up Agent project
- Created the project folder structure
- Set up Python virtual environment
- Installed required dependencies
- Initialized Git repository
- Created GitHub repository
- Added `.gitignore`

### Completed

- ✅ Python Virtual Environment
- ✅ Git Repository
- ✅ GitHub Repository
- ✅ Basic Project Structure
- ✅ Dependency Installation
- ✅ Environment/Secret Protection

---

# 📅 Day 2 – Project Architecture

## Objectives

Designed the modular architecture of the agent.

### Initial Structure

```text
DIRECTORY AGENT/
│
├── data/
├── docs/
├── logs/
├── src/
├── tests/
├── tools/
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

### Initial Modules

- Agent
- Perceive
- Planner
- Logger
- Observer
- Executor

The system was designed using separate modules so that each stage of the agent could be independently tested and improved.

---

# 📅 Day 3 – Perceive Stage

## Objectives

Implemented the first stage of the agent loop.

### Features

- Directory scanning
- File metadata collection
- File name detection
- Extension detection
- File size collection
- File path collection
- Logging support

### Workflow

```text
Start
   │
   ▼
Perceive
   │
   ▼
Scan Directory
   │
   ▼
Collect Metadata
   │
   ▼
Log Results
```

### Example Information

```text
Name      : IMG001.jpg
Extension : .jpg
Size      : 0 bytes
```

No files are modified during the Perceive stage.

---

# 📅 Day 4 – Gemini AI Planning

## Objectives

Integrated Google Gemini AI into the planning stage.

### Completed

- Gemini API integration
- Environment variable configuration
- Secure API key handling
- Planner module
- Prompt engineering
- JSON response parsing
- AI-based decision making

### Workflow

```text
Perceive
    ↓
Gemini Planner
    ↓
JSON Cleanup Plan
```

### Example Plan

```json
[
    {
        "file": "photo.jpg",
        "action": "move",
        "destination": "Images",
        "reason": "Image file"
    }
]
```

The Planner only proposes actions. It does not directly modify files.

---

# 📅 Day 5 – Dry Run Execution

## Objectives

Implemented the execution layer in Dry Run mode.

### Tools

```text
tools/
│
├── move_tool.py
├── rename_tool.py
└── delete_tool.py
```

### Supported Actions

- Move
- Rename
- Delete
- Ignore

### Dry Run Example

```text
========== ACT STAGE (DRY RUN) ==========

[DRY RUN]
Move File : image.jpg
Destination : Images

[DRY RUN]
Delete File : temp.tmp

[IGNORE]
notes.pdf
```

Dry Run mode allows the execution system to be tested without changing the filesystem.

---

# 📅 Day 6 – Real File Execution

## Objectives

Implemented real filesystem operations.

### Completed

- Real file movement
- Real file deletion
- Real file renaming
- Destination folder creation
- Execution result tracking
- Success/failure handling
- User confirmation

### Execution Flow

```text
Perceive
    ↓
Plan
    ↓
Validate
    ↓
Confirmation
    ↓
Act
    ↓
Filesystem Operation
```

### Example

```text
========== ACT STAGE ==========

✔ Moved IMG001.jpg → Images

✔ Deleted old_file.tmp
```

---

# 📅 Day 7 – Observe Stage

## Objectives

Implemented the Observe stage to verify whether requested operations actually succeeded.

### Completed

- Move verification
- Delete verification
- Rename verification
- Ignore handling
- Observation report generation
- Verification status tracking

### Workflow

```text
Perceive
    ↓
Plan
    ↓
Act
    ↓
Observe
    ↓
Verify Results
```

### Example

```text
========== OBSERVE STAGE ==========

✔ Verified: test_image.jpg moved successfully.

✔ Verified: test_temp.tmp deleted successfully.

ℹ Ignored: unknown.xyz
```

### Observation Report

```text
logs/observation_report.json
```

---

# 📅 Day 8 – Agent Loop & Iteration Control

## Objectives

Implemented a continuous agent loop.

### New Module

```text
src/loop_controller.py
```

### Completed

- Iteration tracking
- Maximum iteration limit
- Cleanup completion detection
- Failed action detection
- Continue/stop decisions
- Agent loop integration
- Loop controller tests

### Agent Loop

```text
        ┌──────────────┐
        │   PERCEIVE   │
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │     PLAN     │
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │     ACT      │
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │   OBSERVE    │
        └──────┬───────┘
               ↓
       Cleanup Complete?
          │          │
         Yes         No
          │          │
          ▼          └────→ Next Iteration
       Complete
```

A maximum iteration limit prevents infinite execution.

---

# 📅 Day 9 – Plan Validation & Safety

## Objectives

Implemented a validation layer between AI planning and filesystem execution.

### New Module

```text
src/plan_validator.py
```

### Validation Checks

The validator checks:

- File existence
- Valid actions
- Missing destinations
- Duplicate actions
- Conflicting actions
- Unsafe destinations

### Workflow

```text
Gemini Plan
    ↓
Plan Validator
    ↓
 ┌──┴──┐
 │     │
Valid Invalid
 │     │
 ↓     ↓
Act   Stop
```

### Example

```text
========== VALIDATION STAGE ==========

✅ Plan validation passed.
```

### Invalid Action

```text
{
    "valid": false,
    "errors": [
        "Invalid action 'compress' for 'IMG001.jpg'."
    ]
}
```

### Unsafe Destination

Destinations such as:

```text
../outside_folder
```

are rejected.

### Validation Tests

```text
TEST 1 — VALID PLAN
TEST 2 — INVALID ACTION
TEST 3 — MISSING DESTINATION
TEST 4 — DUPLICATE ACTION
TEST 5 — UNSAFE DESTINATION
```

All validation scenarios were successfully verified.

---

# 📅 Day 10 – Persistent Agent Memory

## Objectives

Implemented persistent memory so the agent can remember previous cleanup operations.

### New Module

```text
src/memory.py
```

### Memory Information

The system stores:

- Timestamp
- Iteration
- File name
- Action
- Status
- Destination
- Message

### Example

```json
{
    "timestamp": "2026-08-08T20:27:26",
    "iteration": 1,
    "file": "first.jpg",
    "action": "move",
    "status": "verified",
    "destination": "Images",
    "message": "✔ Verified: first.jpg moved successfully."
}
```

### Memory Operations

The memory system supports:

- Remember operation
- Get all memory
- Get file history
- Get latest file history
- Clear memory
- Persistent JSON storage

### Storage

```text
logs/memory.json
```

Memory persistence was verified across separate executions.

---

# 📅 Day 11 – Memory-Aware Planning

## Objectives

Connected persistent memory to the Gemini Planner.

The Planner can now consider previous cleanup operations before generating a new plan.

### Memory-Aware Architecture

```text
        ┌──────────────┐
        │   PERCEIVE   │
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │    MEMORY    │
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │ GEMINI PLAN  │
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │   VALIDATE   │
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │     ACT      │
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │   OBSERVE    │
        └──────┬───────┘
               ↓
             MEMORY
```

### Example

If memory contains:

```text
report.pdf
→ move
→ Documents
→ verified
```

The Planner can decide:

```text
report.pdf
→ ignore
→ Already processed successfully
```

New files continue to receive normal decisions:

```text
new_image.jpg
→ move → Images

temporary.tmp
→ delete
```

### Completed

- Latest file history lookup
- Memory context generation
- Memory-aware planning
- Previous action analysis
- Repeated action prevention
- Planner-memory integration
- Observer-memory integration
- Persistent memory testing

---

# 📅 Day 12 – Integration & Reliability

## Objectives

Integrated the major agent components and verified the complete workflow.

### Final Pipeline

```text
┌──────────────┐
│   PERCEIVE   │
└──────┬───────┘
       ↓
┌──────────────┐
│    MEMORY    │
└──────┬───────┘
       ↓
┌──────────────┐
│ GEMINI PLAN  │
└──────┬───────┘
       ↓
┌──────────────┐
│   VALIDATE   │
└──────┬───────┘
       ↓
┌──────────────┐
│ CONFIRMATION │
└──────┬───────┘
       ↓
┌──────────────┐
│     ACT      │
└──────┬───────┘
       ↓
┌──────────────┐
│   OBSERVE    │
└──────┬───────┘
       ↓
┌──────────────┐
│    MEMORY    │
└──────────────┘
```

### Completed

- Full agent integration
- Real filesystem execution
- Plan validation
- User confirmation
- Observation
- Persistent memory
- Memory-aware planning
- Iteration control
- End-to-end testing

---

# 📅 Day 13 – Reliability, Error Handling & Regression Testing

## Objectives

Strengthened the agent against planner failures, corrupted memory, repeated errors, and invalid plans.

---

## 13.1 Controlled Error Retry

The Agent now has controlled error retries.

### Configuration

```python
self.error_retries = 0
self.max_error_retries = 2
```

### Behavior

```text
Planner/API Error
       ↓
Error 1 → Retry
       ↓
Error 2 → Retry
       ↓
Error 3 → Stop Safely
```

The agent no longer repeatedly attempts the same failed operation indefinitely.

### Example

```text
Error : Simulated Planner failure

Error retry 1/2

Attempting another iteration...
```

After repeated failure:

```text
==================================================
AGENT STOPPED AFTER REPEATED ERRORS
==================================================

RESULT:
[]
```

### Verification

The controlled retry test successfully passed.

---

# 13.2 Planner Error Handling

The Planner was tested against multiple failure conditions.

### Tested Scenarios

```text
TEST 1 — GEMINI API FAILURE
TEST 2 — EMPTY RESPONSE
TEST 3 — INVALID JSON
TEST 4 — MISSING FILE
TEST 5 — VALID RESPONSE
```

All scenarios passed.

### Example

```text
TEST 1 — GEMINI API FAILURE
✅ TEST PASSED
```

The Planner safely converts API and response problems into controlled errors.

---

# 13.3 Memory Error Handling

Persistent memory was tested against:

- Missing memory file
- Valid memory
- Corrupted JSON
- Invalid memory structure
- Recovery after corruption

### Results

```text
TEST 1 — MISSING MEMORY FILE
✅ TEST PASSED

TEST 2 — VALID MEMORY
✅ TEST PASSED

TEST 3 — CORRUPTED JSON
✅ TEST PASSED

TEST 4 — WRONG MEMORY FORMAT
✅ TEST PASSED

TEST 5 — MEMORY RECOVERY
✅ TEST PASSED
```

If `memory.json` contains invalid JSON, the system safely starts with empty memory instead of crashing.

---

# 13.4 Full Regression Testing

The following components were regression tested:

```text
Loop Controller
Plan Validator
Memory
Observer
Memory Persistence
Latest Memory
Memory Planner
Memory-Aware Planner
Planner Error Handling
Agent Error Handling
Memory Error Handling
```

### Final Validation Result

```text
All critical regression tests passed.
```

---

# 🏗️ Current Project Structure

```text
DIRECTORY AGENT/
│
├── data/
│   └── sample_folder/
│
├── docs/
│
├── logs/
│   ├── iterations.json
│   ├── memory.json
│   └── observation_report.json
│
├── src/
│   ├── agent.py
│   ├── config.py
│   ├── executor.py
│   ├── logger.py
│   ├── loop_controller.py
│   ├── memory.py
│   ├── observer.py
│   ├── perceive.py
│   ├── plan_validator.py
│   └── planner.py
│
├── tools/
│   ├── file_tools.py
│   ├── move_tool.py
│   ├── rename_tool.py
│   └── delete_tool.py
│
├── tests/
│   ├── __init__.py
│   ├── test_agent_error_handling.py
│   ├── test_agent_validation.py
│   ├── test_delete.py
│   ├── test_delete_real.py
│   ├── test_executor.py
│   ├── test_executor_real.py
│   ├── test_gemini.py
│   ├── test_latest_memory.py
│   ├── test_logger.py
│   ├── test_loop_controller.py
│   ├── test_memory.py
│   ├── test_memory_agent.py
│   ├── test_memory_agent_run2.py
│   ├── test_memory_aware_planner.py
│   ├── test_memory_error_handling.py
│   ├── test_memory_persistence.py
│   ├── test_memory_planner.py
│   ├── test_move.py
│   ├── test_move_real.py
│   ├── test_observer.py
│   ├── test_observer_memory.py
│   ├── test_perceive.py
│   ├── test_plan_validator.py
│   ├── test_planner.py
│   ├── test_planner_error_handling.py
│   ├── test_real_memory.py
│   ├── test_rename.py
│   ├── test_rename_real.py
│   └── test_scan.py
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🔄 Complete Agent Workflow

```text
                         START
                           │
                           ▼
                  ┌────────────────┐
                  │    PERCEIVE     │
                  └───────┬────────┘
                          │
                          ▼
                  ┌────────────────┐
                  │     MEMORY      │
                  └───────┬────────┘
                          │
                          ▼
                  ┌────────────────┐
                  │      PLAN       │
                  │   Gemini AI     │
                  └───────┬────────┘
                          │
                          ▼
                  ┌────────────────┐
                  │    VALIDATE     │
                  └───────┬────────┘
                          │
                    ┌─────┴─────┐
                    │           │
                 INVALID       VALID
                    │           │
                    ▼           ▼
                   STOP    CONFIRMATION
                                │
                          ┌─────┴─────┐
                          │           │
                         NO          YES
                          │           │
                          ▼           ▼
                         STOP         ACT
                                      │
                                      ▼
                                ┌────────────┐
                                │  OBSERVE   │
                                └─────┬──────┘
                                      │
                                      ▼
                                ┌────────────┐
                                │   MEMORY   │
                                └─────┬──────┘
                                      │
                                      ▼
                              Cleanup Complete?
                                 │          │
                                YES         NO
                                 │          │
                                 ▼          ▼
                              COMPLETE  NEXT ITERATION
```

---

# 🧠 Agentic Capabilities

The project demonstrates the major components of an agentic system.

## 1. Perception

The agent observes the current filesystem state.

```text
Directory
   ↓
Files
   ↓
Metadata
```

---

## 2. Memory

The agent remembers previous cleanup operations.

```text
File
 ↓
Action
 ↓
Status
 ↓
Destination
 ↓
Timestamp
```

---

## 3. Reasoning

Gemini AI analyzes the current files and previous memory context.

---

## 4. Planning

The Planner produces structured JSON actions.

---

## 5. Validation

The AI-generated plan is checked before execution.

---

## 6. Human Approval

The user must approve the plan before real filesystem modifications.

---

## 7. Action

The Executor performs the requested filesystem operation.

---

## 8. Observation

The Observer verifies whether the operation succeeded.

---

## 9. Learning Through Memory

Successful operations are stored and used during future planning.

---

## 10. Iteration

The agent can repeat the workflow when cleanup is incomplete.

---

## 11. Error Recovery

The agent can retry temporary failures and stop safely after repeated failures.

---

# 🛡️ Safety Features

The project contains multiple safety mechanisms.

### User Safety

- ✅ User confirmation before execution
- ✅ No automatic execution without approval

### Plan Safety

- ✅ File existence validation
- ✅ Valid action validation
- ✅ Destination validation
- ✅ Missing destination detection
- ✅ Duplicate action detection
- ✅ Conflicting action detection
- ✅ Unsafe path detection

### Execution Safety

- ✅ Real execution only after confirmation
- ✅ Structured execution results
- ✅ Post-execution verification

### Agent Safety

- ✅ Maximum iteration limit
- ✅ Controlled error retry
- ✅ Safe stop after repeated errors

### Memory Safety

- ✅ Missing memory file handling
- ✅ Invalid JSON handling
- ✅ Invalid memory structure handling
- ✅ Memory read error handling
- ✅ Memory write error handling

---

# 🧪 Testing

Tests can be executed individually using:

```powershell
python -m tests.test_loop_controller
python -m tests.test_plan_validator
python -m tests.test_memory
python -m tests.test_observer_memory
python -m tests.test_memory_persistence
python -m tests.test_latest_memory
python -m tests.test_memory_planner
python -m tests.test_memory_aware_planner
python -m tests.test_memory_agent
python -m tests.test_memory_agent_run2
python -m tests.test_planner_error_handling
python -m tests.test_agent_error_handling
python -m tests.test_memory_error_handling
```

---

# 🧪 Testing Categories

```text
                 TESTING
                    │
       ┌────────────┼────────────┐
       │            │            │
       ▼            ▼            ▼
   Core Tests   Safety Tests  Memory Tests
       │            │            │
       ▼            ▼            ▼
   Executor      Validator    Persistence
   Perceive      Agent        History
   Planner       Retry        Memory Planner
   Observer
       │            │            │
       └────────────┼────────────┘
                    ▼
             Integration Tests
                    │
                    ▼
             End-to-End Tests
```

---

# ⚙️ Requirements

- Python 3.10+
- Google Gemini API
- Python virtual environment
- Internet connection for Gemini API calls
- Dependencies listed in `requirements.txt`

Install dependencies:

```powershell
pip install -r requirements.txt
```

---

# 🔐 Configuration

The Gemini API key should be stored securely.

Example `.env` configuration:

```text
GEMINI_API_KEY=your_api_key_here
```

Never place the actual API key directly inside source code.

Never commit:

- API keys
- Passwords
- Tokens
- Credentials
- `.env` files

The `.gitignore` protects environment files and runtime logs.

---

# ▶️ Running the Project

## 1. Activate the Virtual Environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## 2. Run the Agent

```powershell
python main.py
```

---

## 3. Confirm the Cleanup Plan

The agent displays the generated plan:

```text
Apply these changes? (yes/no):
```

Enter:

```text
yes
```

to execute the approved operations.

Enter:

```text
no
```

to cancel.

---

# 📊 Example Execution

```text
============================================================
        DIRECTORY CLEAN-UP AGENT
============================================================

========== PERCEIVE STAGE ==========

Scanning folder: data/sample_folder

Found 4 file(s).

========== PLAN STAGE ==========

Cleanup Plan

-----------------------------------
File        : test_image.jpg
Action      : move
Destination : Images
Reason      : Image file

-----------------------------------
File        : test_temp.tmp
Action      : delete
Destination :
Reason      : Temporary file

========== VALIDATION STAGE ==========

✅ Plan validation passed.

==================================================
CONFIRMATION
==================================================

Apply these changes? (yes/no): yes

Executing cleanup...

========== ACT STAGE ==========

✔ Moved test_image.jpg → Images

✔ Deleted test_temp.tmp

========== OBSERVE STAGE ==========

✔ Verified: test_image.jpg moved successfully.

✔ Verified: test_temp.tmp deleted successfully.

==================================================
FINAL REPORT
==================================================

Total Actions : 4
Successful    : 2
Ignored       : 2
Failed        : 0
```

---

# 📁 Runtime Logs

The agent generates structured runtime information.

## Iteration Log

```text
logs/iterations.json
```

Stores information about agent iterations and stages.

## Memory

```text
logs/memory.json
```

Stores persistent cleanup history.

## Observation Report

```text
logs/observation_report.json
```

Stores post-execution verification results.

---

# 📈 Development Progress

```text
Day 1  → Project Setup                    ✅
Day 2  → Architecture                     ✅
Day 3  → Perceive Stage                   ✅
Day 4  → Gemini AI Planning               ✅
Day 5  → Dry Run Execution                ✅
Day 6  → Real File Execution              ✅
Day 7  → Observe Stage                    ✅
Day 8  → Agent Loop                      ✅
Day 9  → Plan Validation & Safety         ✅
Day 10 → Persistent Agent Memory         ✅
Day 11 → Memory-Aware Planning            ✅
Day 12 → Integration & Reliability        ✅
Day 13 → Error Handling & Regression      ✅
```

---

# ✅ Features Completed

## Core System

- ✅ Project Setup
- ✅ Python Virtual Environment
- ✅ Git Repository
- ✅ GitHub Repository
- ✅ Modular Architecture
- ✅ Perceive Stage
- ✅ Gemini AI Integration
- ✅ AI Planning
- ✅ JSON Parsing
- ✅ Dry Run Execution
- ✅ Real File Execution
- ✅ Move Tool
- ✅ Rename Tool
- ✅ Delete Tool
- ✅ Ignore Action
- ✅ Executor
- ✅ Logger

## Agentic Features

- ✅ Observe Stage
- ✅ Plan Validation
- ✅ Safety Validation
- ✅ User Confirmation
- ✅ Iteration Control
- ✅ Cleanup Completion Detection
- ✅ Persistent Memory
- ✅ File History
- ✅ Latest Memory Retrieval
- ✅ Memory-Aware Planning
- ✅ Repeated Action Prevention
- ✅ Error Handling
- ✅ Controlled Retry
- ✅ Memory Recovery
- ✅ End-to-End Agent Loop

## Testing

- ✅ Loop Controller Testing
- ✅ Plan Validator Testing
- ✅ Executor Testing
- ✅ Perceive Testing
- ✅ Observer Testing
- ✅ Memory Testing
- ✅ Memory Persistence Testing
- ✅ Latest Memory Testing
- ✅ Memory Planner Testing
- ✅ Memory-Aware Planner Testing
- ✅ Planner Error Handling
- ✅ Agent Error Handling
- ✅ Memory Error Handling
- ✅ Regression Testing

---

# 🚧 Future Improvements

Possible future enhancements include:

- GUI interface
- Web dashboard
- Scheduled cleanup
- Undo/recovery functionality
- Automatic backup before deletion
- Duplicate file detection
- More file categories
- Configurable cleanup rules
- Custom user-defined cleanup policies
- Advanced memory retrieval
- File similarity detection
- Cleanup history dashboard
- Cloud storage integration
- Multi-directory support
- Advanced Gemini reasoning
- Human approval levels
- Configurable retry policies
- Automatic recovery strategies

---

# 🏆 Project Status

```text
┌─────────────────────────────────────────┐
│       DIRECTORY CLEAN-UP AGENT          │
│                                         │
│  Perceive                               │
│      ↓                                  │
│  Remember                               │
│      ↓                                  │
│  Gemini AI Planning                    │
│      ↓                                  │
│  Plan Validation                        │
│      ↓                                  │
│  Human Confirmation                     │
│      ↓                                  │
│  Execute                                │
│      ↓                                  │
│  Observe                                │
│      ↓                                  │
│  Update Memory                          │
│      ↓                                  │
│  Evaluate                               │
│      ↓                                  │
│  Retry / Iterate / Complete             │
│                                         │
└─────────────────────────────────────────┘
```

## Current Status

**Core Development Complete**

The project successfully demonstrates an end-to-end agentic filesystem automation workflow.

The system can:

1. Perceive a directory
2. Collect file metadata
3. Retrieve previous memory
4. Generate an AI-based cleanup plan
5. Validate the plan
6. Ask for human confirmation
7. Execute filesystem operations
8. Observe and verify results
9. Store operation history
10. Use memory during future planning
11. Retry controlled failures
12. Recover from memory errors
13. Stop safely when repeated errors occur

---

# 🎯 Core Concept

```text
┌───────────┐
│ PERCEIVE  │
└─────┬─────┘
      ↓
┌───────────┐
│  REMEMBER │
└─────┬─────┘
      ↓
┌───────────┐
│   PLAN    │
└─────┬─────┘
      ↓
┌───────────┐
│ VALIDATE  │
└─────┬─────┘
      ↓
┌───────────┐
│   ACT     │
└─────┬─────┘
      ↓
┌───────────┐
│  OBSERVE  │
└─────┬─────┘
      ↓
┌───────────┐
│  MEMORY   │
└─────┬─────┘
      ↓
┌───────────┐
│  ITERATE  │
└───────────┘
```

> **Perceive → Remember → Plan → Validate → Act → Observe → Learn → Repeat**

---

# 👨‍💻 Project

## Directory Clean-Up Agent

**AI-powered agentic filesystem automation using Python and Google Gemini AI.**

The project combines AI planning with deterministic filesystem tools, safety validation, human approval, observation, persistent memory, and controlled iteration.

---

# ⭐ Final Development Status

```text
PROJECT SETUP             ✅
AGENT ARCHITECTURE        ✅
PERCEPTION                ✅
GEMINI PLANNING           ✅
DRY RUN                   ✅
REAL EXECUTION            ✅
OBSERVATION               ✅
ITERATION CONTROL         ✅
PLAN VALIDATION           ✅
PERSISTENT MEMORY         ✅
MEMORY-AWARE PLANNING     ✅
ERROR HANDLING            ✅
CONTROLLED RETRY          ✅
MEMORY RECOVERY           ✅
REGRESSION TESTING        ✅

             CORE DEVELOPMENT COMPLETE
```

---