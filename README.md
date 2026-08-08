# 🤖 Directory Clean-Up Agent

An AI-powered agentic system that intelligently analyzes, plans, validates, executes, observes, and remembers directory cleanup operations.

---

# 🚀 Progress Report

## 📅 Day 1 – Project Setup

### Objectives

- Initialized the Directory Clean-Up Agent project.
- Created the project folder structure.
- Set up a Python virtual environment.
- Installed required dependencies.
- Initialized a Git repository.
- Created the first GitHub repository.
- Added `.gitignore` to ignore virtual environment, logs, and secrets.

### Completed

- ✅ Python Virtual Environment
- ✅ Git Repository
- ✅ GitHub Repository
- ✅ Basic Project Structure
- ✅ Dependency Installation

---

# 📅 Day 2 – Project Architecture

### Objectives

Designed the overall architecture of the agent.

### Completed

Project Structure

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

### Modules Created

- Agent
- Perceive
- Planner
- Logger
- Observer (Skeleton)
- Executor (Skeleton)

---

# 📅 Day 3 – Perceive Stage

### Objectives

Implemented the first phase of the Agent Loop.

### Features

- Directory scanning
- File metadata collection
- Extension detection
- File size collection
- Logging support
- Sample folder for testing

### Agent Flow

```text
Start
   │
   ▼
Perceive
   │
   ▼
Collect File Metadata
   │
   ▼
Log Iteration
```

### Output

The agent successfully scans a directory and gathers information such as:

- File Name
- File Extension
- File Size
- File Path

No file modifications are performed during this stage.

---

# 📅 Day 4 – Planning Stage (Gemini AI)

### Objectives

Integrated Google's Gemini API to generate intelligent cleanup plans.

### Completed

- Gemini API Integration
- Environment Variable Configuration
- Secure API Key Management
- Planner Module
- Prompt Engineering
- JSON Response Parsing
- AI-Based Decision Making

### Workflow

```text
Perceive
     │
     ▼
Gemini Planner
     │
     ▼
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

The planner only proposes actions and does not modify any files.

---

# 📅 Day 5 – Dry Run Execution

### Objectives

Implemented the execution layer in Dry Run mode.

### Modules Created

```text
tools/
│
├── move_tool.py
├── rename_tool.py
└── delete_tool.py
```

### Executor

Created a centralized Executor that dispatches actions to the appropriate tool.

### Supported Actions

- Move
- Rename
- Delete
- Ignore

### Dry Run

No files are actually modified.

Example Output:

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

### Agent Loop

```text
Perceive
      │
      ▼
Plan (Gemini)
      │
      ▼
Act (Dry Run)
      │
      ▼
Logger
```

### Current Capabilities

- ✅ Scan folders
- ✅ Collect metadata
- ✅ Generate AI cleanup plan
- ✅ Parse JSON plan
- ✅ Dispatch actions
- ✅ Simulate execution
- ✅ Log every stage

---

# 📅 Day 6 – Real File Execution

### Objectives

Implemented real filesystem operations after successfully testing the Dry Run execution.

### Completed

- Real file movement
- Real file deletion
- Destination folder creation
- File operation result tracking
- Success and failure handling
- User confirmation before execution

### Real Execution Flow

```text
Perceive
      │
      ▼
Plan
      │
      ▼
Confirmation
      │
      ▼
Act
      │
      ▼
Real File Operation
```

### Example

```text
========== ACT STAGE ==========

✔ Moved IMG001.jpg → Images

✔ Deleted old_file.tmp
```

### Structured Execution Result

The Executor returns structured results such as:

```python
{
    "status": "success",
    "action": "move",
    "file": "IMG001.jpg",
    "destination": "Images",
    "dry_run": False
}
```

---

# 📅 Day 7 – Observe Stage

### Objectives

Implemented the Observe stage to verify whether file operations were actually successful.

### Completed

- Move verification
- Delete verification
- Rename verification
- Ignore handling
- Observation report generation
- Verification status tracking

### Agent Loop

```text
Perceive
      │
      ▼
Plan
      │
      ▼
Act
      │
      ▼
Observe
      │
      ▼
Verify Results
```

### Example Output

```text
========== OBSERVE STAGE ==========

✔ Verified: test_image.jpg moved successfully.
✔ Verified: test_temp.tmp deleted successfully.
ℹ Ignored: unknown.xyz
```

### Observation Report

The observation results are stored in:

```text
logs/observation_report.json
```

---

# 📅 Day 8 – Agent Loop & Iteration Control

### Objectives

Implemented an Agent Loop that allows the agent to repeatedly perceive, plan, act, and observe until cleanup is completed or the maximum iteration limit is reached.

### New Module

```text
src/
└── loop_controller.py
```

### Completed

- Iteration tracking
- Maximum iteration limit
- Cleanup completion detection
- Failed action detection
- Continue/stop decision
- Agent loop integration
- Loop controller testing

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
          │           │
         Yes          No
          │           │
          ▼           └──────→ Next Iteration
       Complete
```

### Safety

A maximum iteration limit prevents the agent from running indefinitely.

---

# 📅 Day 9 – Plan Validation & Safety

### Objectives

Implemented a validation layer to verify AI-generated cleanup plans before execution.

### New Module

```text
src/
└── plan_validator.py
```

### Validation Checks

The validator checks:

- File existence
- Valid actions
- Missing destinations
- Duplicate actions
- Conflicting actions
- Unsafe destinations

### Validation Workflow

```text
Gemini Plan
     │
     ▼
Plan Validator
     │
 ┌───┴────┐
 │        │
Valid    Invalid
 │        │
 ▼        ▼
Execute  Stop
```

### Example

```text
========== VALIDATION STAGE ==========

✅ Plan validation passed.
```

### Invalid Plan Example

```python
{
    "valid": False,
    "errors": [
        "Invalid action 'compress' for 'IMG001.jpg'."
    ]
}
```

### Unsafe Destination Protection

The validator prevents unsafe destinations such as:

```text
../outside_folder
```

from being used.

### Testing

The following validation scenarios were tested:

```text
TEST 1 — VALID PLAN
TEST 2 — INVALID ACTION
TEST 3 — MISSING DESTINATION
TEST 4 — DUPLICATE ACTION
TEST 5 — UNSAFE DESTINATION
```

All validation scenarios were successfully verified.

---

# 📅 Day 10 – Agent Memory

### Objectives

Implemented persistent memory so the agent can remember previous cleanup operations.

### New Module

```text
src/
└── memory.py
```

### Memory Stores

The agent memory stores:

- Timestamp
- Iteration
- File name
- Action
- Status
- Destination
- Message

### Example Memory Entry

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

### Memory Persistence

Memory is stored in:

```text
logs/memory.json
```

The persistence tests verified that memory remains available across separate executions.

---

# 📅 Day 11 – Memory-Aware Planning

### Objectives

Connected persistent memory to the planning system so previous cleanup history can influence future decisions.

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

### Completed

- Latest file history lookup
- Memory context generation
- Memory-aware planning
- Previous action analysis
- Repeated action prevention
- Persistent memory integration with Planner
- Persistent memory integration with Observer
- Full memory-aware agent testing

### Example

If memory contains:

```text
report.pdf
→ move
→ Documents
→ verified
```

the planner can make the decision:

```text
report.pdf
→ ignore
→ Already processed successfully
```

At the same time, new files continue to receive normal decisions:

```text
new_image.jpg
→ move → Images

temporary.tmp
→ delete
```

### Day 11 Testing

The following tests were successfully completed:

- ✅ Latest Memory
- ✅ Memory Planner
- ✅ Memory-Aware Planner
- ✅ Full Memory Agent Run 1
- ✅ Full Memory Agent Run 2
- ✅ Memory Persistence

---

# 📅 Day 12 – Final Integration & Reliability

### Objectives

Integrated all agent components and performed final reliability, testing, and end-to-end verification.

### Reliability Improvements

Improved the memory system to safely handle:

- Missing memory files
- Invalid JSON
- Invalid memory structures
- File read errors
- File write errors

Memory failures now generate warnings instead of unnecessarily stopping the entire agent.

### Final Agent Pipeline

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

### Final Testing

The final real-agent test successfully demonstrated:

```text
Total Actions : 7
Successful    : 4
Ignored       : 3
Failed        : 0
```

### Successful Operations

Examples of successful operations included:

```text
final_test.jpg
→ Images
→ verified

test_image.jpg
→ Images
→ verified

final_test.tmp
→ deleted
→ verified

test_temp.tmp
→ deleted
→ verified
```

Unknown file types were safely ignored.

### Final Verification

The agent successfully demonstrated:

- ✅ Real filesystem operations
- ✅ Plan validation
- ✅ User confirmation
- ✅ Execution
- ✅ Observation
- ✅ Persistent memory
- ✅ Memory-aware planning
- ✅ Iteration control
- ✅ Error handling
- ✅ End-to-end execution
- ✅ Zero failed actions in the final test

---

# 🏗 Current Project Structure

```text
DIRECTORY AGENT/
│
├── data/
│   ├── sample_folder/
│   └── memory_test_folder/
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
│   ├── test_loop_controller.py
│   ├── test_plan_validator.py
│   ├── test_memory.py
│   ├── test_observer_memory.py
│   ├── test_memory_persistence.py
│   ├── test_latest_memory.py
│   ├── test_memory_planner.py
│   ├── test_memory_aware_planner.py
│   ├── test_memory_agent.py
│   └── test_memory_agent_run2.py
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🔄 Complete Agent Workflow

The complete system now follows:

```text
                    START
                      │
                      ▼
              ┌──────────────┐
              │   PERCEIVE   │
              └──────┬───────┘
                     │
                     ▼
              ┌──────────────┐
              │    MEMORY    │
              └──────┬───────┘
                     │
                     ▼
              ┌──────────────┐
              │     PLAN     │
              │   Gemini AI  │
              └──────┬───────┘
                     │
                     ▼
              ┌──────────────┐
              │   VALIDATE   │
              └──────┬───────┘
                     │
              ┌──────┴──────┐
              │             │
           INVALID         VALID
              │             │
              ▼             ▼
             STOP      CONFIRMATION
                            │
                       ┌────┴────┐
                       │         │
                      NO        YES
                       │         │
                       ▼         ▼
                     STOP       ACT
                                 │
                                 ▼
                           ┌──────────────┐
                           │   OBSERVE    │
                           └──────┬───────┘
                                  │
                                  ▼
                           ┌──────────────┐
                           │    MEMORY    │
                           └──────┬───────┘
                                  │
                                  ▼
                         Cleanup Complete?
                            │          │
                           YES         NO
                            │          │
                            ▼          ▼
                         COMPLETE   NEXT ITERATION
```

---

# 🧠 Agentic Capabilities

The Directory Clean-Up Agent now demonstrates the major components of an agentic workflow:

### 1. Perception

The agent observes the current state of the filesystem.

### 2. Reasoning

Gemini AI analyzes the files and determines suitable cleanup actions.

### 3. Planning

The AI creates a structured cleanup plan before any modification occurs.

### 4. Validation

The generated plan is checked for safety and correctness.

### 5. Action

The Executor performs the approved filesystem operations.

### 6. Observation

The agent verifies whether the requested operations succeeded.

### 7. Memory

The agent stores successful operations for future decision making.

### 8. Iteration

The agent can repeat the process when cleanup is not complete.

### 9. Safety

The agent includes confirmation, validation, destination safety checks, and maximum iteration limits.

---

# 🛡️ Safety Features

The project includes multiple safety mechanisms:

- ✅ User confirmation before execution
- ✅ Plan validation
- ✅ File existence validation
- ✅ Valid action validation
- ✅ Destination validation
- ✅ Unsafe path detection
- ✅ Duplicate/conflicting action detection
- ✅ Execution verification
- ✅ Persistent operation history
- ✅ Maximum iteration limit
- ✅ Memory error handling

---

# 🧪 Testing

Individual tests can be executed using:

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
```

### Test Categories

```text
Loop Control
     ↓
Plan Validation
     ↓
Memory
     ↓
Observer
     ↓
Memory Persistence
     ↓
Memory-Aware Planning
     ↓
Full Agent
     ↓
End-to-End Testing
```

---

# ⚙️ Requirements

- Python 3.10+
- Google Gemini API
- Python Virtual Environment
- Required Python dependencies from `requirements.txt`

Install dependencies:

```powershell
pip install -r requirements.txt
```

---

# 🔐 Configuration

The Gemini API key should be configured securely through the project's configuration system.

Never commit API keys, passwords, tokens, or other secrets to GitHub.

Example:

```text
GEMINI_API_KEY=your_api_key_here
```

The actual API key must never be placed directly inside source code or committed to the repository.

---

# ▶️ Running the Agent

### 1. Activate the virtual environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 2. Run the agent

```powershell
python main.py
```

### 3. Review the generated results

Observation report:

```text
logs/observation_report.json
```

Iteration logs:

```text
logs/iterations.json
```

Persistent memory:

```text
logs/memory.json
```

---

# 📊 Example Agent Execution

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

# 📈 Development Progress

```text
Day 1  → Project Setup              ✅
Day 2  → Architecture               ✅
Day 3  → Perceive Stage             ✅
Day 4  → Gemini AI Planning         ✅
Day 5  → Dry Run Execution          ✅
Day 6  → Real File Execution        ✅
Day 7  → Observe Stage              ✅
Day 8  → Agent Loop                 ✅
Day 9  → Plan Validation            ✅
Day 10 → Agent Memory               ✅
Day 11 → Memory-Aware Planning      ✅
Day 12 → Final Integration          ✅
```

---

# ✅ Features Completed

## Core System

- ✅ Project Setup
- ✅ Virtual Environment
- ✅ Git Repository
- ✅ GitHub Repository
- ✅ Agent Architecture
- ✅ Perceive Stage
- ✅ Gemini AI Integration
- ✅ AI Planning
- ✅ JSON Parsing
- ✅ Dry Run Execution
- ✅ Real File Execution
- ✅ Modular Tool System
- ✅ Executor
- ✅ Logging System

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
- ✅ End-to-End Agent Loop

## Testing

- ✅ Loop Controller Testing
- ✅ Plan Validator Testing
- ✅ Observer Testing
- ✅ Memory Testing
- ✅ Memory Persistence Testing
- ✅ Latest Memory Testing
- ✅ Memory Planner Testing
- ✅ Memory-Aware Planner Testing
- ✅ Full Agent Testing
- ✅ Final End-to-End Testing

---

# 🚧 Future Improvements

Possible future improvements include:

- GUI interface
- Scheduled cleanup
- Undo/recovery functionality
- File duplicate detection
- More file categories
- Configurable cleanup rules
- Detailed dashboard
- Cloud storage integration
- Automatic backup before deletion
- Advanced agent reasoning
- More sophisticated memory retrieval
- Human approval levels
- Cleanup history dashboard
- Custom user-defined cleanup policies

---

# 🎯 Project Status

## Development Status

```text
                 DIRECTORY
                CLEAN-UP AGENT
                      │
                      ▼
              ┌──────────────┐
              │   PERCEIVE   │
              └──────┬───────┘
                     ▼
              ┌──────────────┐
              │    MEMORY    │
              └──────┬───────┘
                     ▼
              ┌──────────────┐
              │     PLAN     │
              │   Gemini AI  │
              └──────┬───────┘
                     ▼
              ┌──────────────┐
              │   VALIDATE   │
              └──────┬───────┘
                     ▼
              ┌──────────────┐
              │ CONFIRMATION │
              └──────┬───────┘
                     ▼
              ┌──────────────┐
              │     ACT      │
              └──────┬───────┘
                     ▼
              ┌──────────────┐
              │   OBSERVE    │
              └──────┬───────┘
                     ▼
              ┌──────────────┐
              │    MEMORY    │
              └──────┬───────┘
                     │
                     ▼
                NEXT DECISION
```

# 🏆 Final Status

**Directory Clean-Up Agent — Core Development Complete**

The project successfully demonstrates an end-to-end agentic filesystem automation workflow:

```text
Perception
    ↓
Memory
    ↓
AI Reasoning
    ↓
Planning
    ↓
Validation
    ↓
Human Confirmation
    ↓
Action
    ↓
Observation
    ↓
Memory
    ↓
Iteration
```

The system is capable of analyzing a directory, generating an AI-based cleanup plan, validating that plan for safety, executing approved filesystem operations, verifying the results, and remembering previous operations for future decisions.

---

# 👨‍💻 Project

## Directory Clean-Up Agent

**AI-powered agentic filesystem automation using Python and Gemini AI.**

---

## ⭐ Core Concept

> **Perceive → Remember → Plan → Validate → Act → Observe → Learn → Repeat**