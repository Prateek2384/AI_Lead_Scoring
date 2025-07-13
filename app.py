import pandas as pd
import numpy as np
import random

np.random.seed(42)  # For reproducibility

num_rows = 10000  # Number of leads to generate

def random_phone():
    return "+91-" + str(random.randint(7000000000, 9999999999))

# Possible values
lead_sources = ["Website", "Referral", "Cold Call", "Social Media", "Event"]
age_groups = ["18-25", "26-35", "36-50", "51+"]
interaction_freqs = ["Low", "Medium", "High"]

# Helper functions
def get_family_background(age_group):
    if age_group == "18-25":
        return "Single"
    elif age_group == "26-35":
        return random.choice(["Married", "Single"])
    else:
        return random.choice(["Married", "Married with Kids"])

def get_interest_level(source):
    mapping = {
        "Website": "Medium",
        "Referral": "High",
        "Cold Call": "Low",
        "Social Media": "Medium",
        "Event": "High"
    }
    return mapping[source]

def get_time_since_interaction(freq):
    if freq == "High":
        return random.randint(1, 3)
    elif freq == "Medium":
        return random.randint(4, 10)
    else:
        return random.randint(11, 30)

def get_credit_score(income):
    base = 500
    extra = min(income // 100000 * 10, 350)  # Higher income → higher score
    return base + extra

def get_website_visits(income):
    base = min(income // 100000, 10)
    return base + random.randint(0, 3)

# Generate data
data = {
    "Phone Number": [random_phone() for _ in range(num_rows)],
    "Email": [f"user{i}@example.com" for i in range(num_rows)],
    "Age Group": np.random.choice(age_groups, size=num_rows),
    "Income": np.random.randint(100000, 1000001, size=num_rows),  # INR 100k to 10L
    "Lead Source": np.random.choice(lead_sources, size=num_rows),
    "Interaction Frequency": np.random.choice(interaction_freqs, size=num_rows),
}

# Derived fields
data["Family Background"] = [get_family_background(ag) for ag in data["Age Group"]]
data["Product Interest Level"] = [get_interest_level(src) for src in data["Lead Source"]]
data["Time Since Last Interaction"] = [get_time_since_interaction(freq) for freq in data["Interaction Frequency"]]
data["Credit Score"] = [get_credit_score(inc) for inc in data["Income"]]
data["Website Visit Count"] = [get_website_visits(inc) for inc in data["Income"]]

# Optional: Add Intent (binary label for high/low intent)
data["Intent"] = np.random.choice([0, 1], size=num_rows, p=[0.7, 0.3])  # 30% high-intent

# Create DataFrame
df = pd.DataFrame(data)[[
    "Phone Number", "Email", "Credit Score", "Age Group", "Family Background",
    "Income", "Lead Source", "Product Interest Level", "Interaction Frequency",
    "Time Since Last Interaction", "Website Visit Count", "Intent"
]]

# Save to CSV
df.to_csv("data/leads.csv", index=False)
print("✅ Dataset saved to 'leads.csv'")