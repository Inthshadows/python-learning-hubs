%%writefile streamlit_app.py

import streamlit as st
import pandas as pd
from datetime import datetime

# Page Config
st.set_page_config(page_title="Python Learning Hub", page_icon="🐍", layout="wide")

# Title
st.title("🐍 Python Fundamentals Learning Hub")
st.markdown("### Day 3 Training - Interactive Learning")

# Sidebar Navigation
topic = st.sidebar.radio("Select Topic:", [
    "🏠 Home",
    "⚙️ Virtual Environment",
    "🔧 Functions",
    "📊 Data Structures",
    "📁 File Handling",
    "✅ Compliance Project"
])

# ==================== HOME ====================
if topic == "🏠 Home":
    st.markdown("""
    ## Welcome to Python Training! 👋
    
    **What you'll learn:**
    - ⚙️ Virtual Environment Setup
    - 🔧 Functions & Reusable Code
    - 📊 Data Structures (Lists, Dicts, DataFrames)
    - 📁 File Handling & CSV
    - ✅ Real-World Compliance Project
    
    **Select a topic from the sidebar to begin!**
    """)

# ==================== VIRTUAL ENVIRONMENT ====================
elif topic == "⚙️ Virtual Environment":
    st.header("⚙️ Virtual Environment Setup")
    
    st.markdown("""
    ## What is a Virtual Environment?
    
    A **virtual environment** is an isolated Python workspace where each project has its own packages.
    """)
    
    st.warning("**Problem:** Project A needs pandas 2.0, Project B needs pandas 1.5 → Conflict!")
    st.success("**Solution:** Each project gets its own virtual environment → No conflicts!")
    
    st.subheader("Step-by-Step Setup")
    
    st.markdown("**Step 1: Create Virtual Environment**")
    st.code("python -m venv venv", language="bash")
    
    st.markdown("**Step 2: Activate**")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("Windows:")
        st.code("venv\\Scripts\\activate", language="bash")
    with col2:
        st.markdown("Mac/Linux:")
        st.code("source venv/bin/activate", language="bash")
    
    st.markdown("**Step 3: Install Packages**")
    st.code("pip install pandas numpy", language="bash")
    
    st.markdown("**Step 4: Deactivate**")
    st.code("deactivate", language="bash")
    
    st.info("✅ **Best Practice:** Always use virtual environments for projects!")

# ==================== FUNCTIONS ====================
elif topic == "🔧 Functions":
    st.header("🔧 Functions - Reusable Code")
    
    st.markdown("""
    ## What is a Function?
    
    A **function** is a named block of code that performs a specific task.
    Write once, use many times!
    """)
    
    st.subheader("Example 1: Simple Function")
    st.code('''
def greet_user(name):
    """Welcome a user"""
    print(f"Hello, {name}!")
    print("Welcome to Python training")

# Call the function
greet_user("Amit")
greet_user("Team")
    ''', language="python")
    
    st.subheader("Example 2: Function with Return")
    st.code('''
def calculate_compliance_score(total, completed):
    """Calculate compliance percentage"""
    if total == 0:
        return 0
    return (completed / total) * 100

# Use the function
score = calculate_compliance_score(8, 6)
print(f"Compliance: {score}%")  # Output: 75.0%
    ''', language="python")
    
    st.subheader("Example 3: Decision Function")
    st.code('''
def evaluate_status(status, due_date, today):
    """Determine compliance state"""
    if status == "Completed":
        return "Compliant"
    elif due_date < today:
        return "Overdue"
    else:
        return "Due Soon"
    ''', language="python")
    
    st.info("""
    **Key Points:**
    - `def` → defines a function
    - Parameters → inputs inside parentheses
    - `return` → sends result back
    - Call with `function_name()`
    """)

# ==================== DATA STRUCTURES ====================
elif topic == "📊 Data Structures":
    st.header("📊 Data Structures")
    
    st.markdown("## 1️⃣ Lists - Ordered Collection")
    st.code('''
employees = ["Amit", "Ravi", "Neha"]
employees.append("Sharma")  # Add item
print(employees[0])  # Access: "Amit"
    ''', language="python")
    
    st.markdown("## 2️⃣ Dictionaries - Key-Value Pairs")
    st.code('''
employee = {
    "id": 101,
    "name": "Amit",
    "department": "IT",
    "status": "Active"
}
print(employee["name"])  # Access: "Amit"
    ''', language="python")
    
    st.markdown("## 3️⃣ DataFrames - Tables (Pandas)")
    st.code('''
import pandas as pd

data = {
    "control_id": ["C001", "C002", "C003"],
    "status": ["Completed", "Pending", "Completed"],
    "due_days": [90, 30, 7]
}
df = pd.DataFrame(data)
print(df)
    ''', language="python")
    
    # Show live DataFrame
    st.markdown("**Live Example:**")
    df = pd.DataFrame({
        "control_id": ["C001", "C002", "C003"],
        "status": ["Completed", "Pending", "Completed"],
        "due_days": [90, 30, 7]
    })
    st.dataframe(df, use_container_width=True)
    
    st.markdown("## Comparison Table")
    comparison = pd.DataFrame({
        "Structure": ["List", "Dictionary", "DataFrame"],
        "Ordered": ["Yes", "No", "Yes"],
        "Use Case": ["Multiple items", "Key-value data", "Tables"]
    })
    st.table(comparison)

# ==================== FILE HANDLING ====================
elif topic == "📁 File Handling":
    st.header("📁 File Handling & CSV")
    
    st.markdown("## Writing to a File")
    st.code('''
with open("log.txt", "w") as file:
    file.write("Python file handling started")
    file.write("This is line 2")
# File closes automatically!
    ''', language="python")
    
    st.markdown("## Reading a File")
    st.code('''
with open("log.txt", "r") as file:
    content = file.read()
    print(content)
    ''', language="python")
    
    st.markdown("## Reading CSV with Pandas (EASIEST)")
    st.code('''
import pandas as pd

# Read CSV
df = pd.read_csv("data.csv")

# View data
print(df.head())

# Filter
completed = df[df["status"] == "Completed"]

# Write to CSV
df.to_csv("output.csv", index=False)
    ''', language="python")
    
    st.info("""
    **Key Points:**
    - Use `with` statement (auto-closes files)
    - Use Pandas for CSV (simplest!)
    - "r" = read, "w" = write, "a" = append
    """)

# ==================== COMPLIANCE PROJECT ====================
elif topic == "✅ Compliance Project":
    st.header("✅ Compliance Checklist Automator")
    
    st.markdown("""
    ## The Business Problem
    
    Organizations must track compliance controls across departments.
    Manual tracking = missed deadlines, audit failures!
    
    **Solution:** Automate with Python!
    """)
    
    st.subheader("Input Data")
    
    # Master data
    master = pd.DataFrame({
        "control_id": ["C001", "C002", "C003"],
        "control_name": ["Password Review", "Access Review", "Backup Check"],
        "frequency": ["Quarterly", "Monthly", "Weekly"],
        "due_days": [90, 30, 7]
    })
    st.markdown("**Compliance Master:**")
    st.dataframe(master, use_container_width=True)
    
    # Execution data
    execution = pd.DataFrame({
        "control_id": ["C001", "C002", "C003"],
        "department": ["IT", "IT", "IT"],
        "status": ["Completed", "Pending", "Pending"]
    })
    st.markdown("**Execution Status:**")
    st.dataframe(execution, use_container_width=True)
    
    st.subheader("Core Logic")
    st.code('''
def evaluate_status(row):
    """Classify compliance state"""
    if row["status"] == "Completed":
        return "Compliant"
    elif row["due_date"] < today:
        return "Overdue"
    else:
        return "Due Soon"

# Apply to all rows
df["compliance_state"] = df.apply(evaluate_status, axis=1)
    ''', language="python")
    
    st.subheader("Complete Code")
    with st.expander("📝 View Full Code"):
        st.code('''
import pandas as pd
from datetime import datetime

# Load data
master = pd.read_csv("compliance_master.csv")
execution = pd.read_csv("compliance_execution.csv")

# Merge
df = execution.merge(master, on="control_id", how="left")

# Calculate due dates
df["last_checked"] = pd.to_datetime(df["last_checked"])
df["due_date"] = df["last_checked"] + pd.to_timedelta(df["due_days"], unit="D")

# Evaluate status
def evaluate_status(row):
    today = datetime.now().date()
    if row["status"] == "Completed":
        return "Compliant"
    elif row["due_date"].date() < today:
        return "Overdue"
    else:
        return "Due Soon"

df["compliance_state"] = df.apply(evaluate_status, axis=1)

# Generate report
summary = df.groupby("department").agg({
    "control_id": "count",
    "status": lambda x: (x == "Completed").sum()
}).reset_index()

# Save
summary.to_csv("compliance_report.csv", index=False)
print("✅ Report generated!")
        ''', language="python")
    
    st.success("This is how Python solves real business problems!")

# Footer
st.markdown("---")
st.markdown("*Python Fundamentals Learning Hub | Day 3 Training*")


