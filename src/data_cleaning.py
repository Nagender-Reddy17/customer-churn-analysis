import pandas as pd


# -------------------------------
# Load Data
# -------------------------------
def load_data(path):
    df = pd.read_csv(path)
    return df


# -------------------------------
# Clean Data
# -------------------------------
def clean_data(df):
    # ✅ Step 1: Standardize column names
    df.columns = df.columns.str.strip().str.replace(" ", "_")
    print("Columns after cleaning:", df.columns.tolist())

    # ✅ Step 2: Handle TotalCharges safely
    if 'TotalCharges' in df.columns:
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    elif 'Total_Charges' in df.columns:
        df['Total_Charges'] = pd.to_numeric(df['Total_Charges'], errors='coerce')

    # ✅ Step 3: Handle missing values
    print("\nMissing values before cleaning:\n", df.isnull().sum())
    df = df.dropna()

    # ✅ Step 4: Convert Churn column
    if 'Churn' in df.columns:
        df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    # ✅ Step 5: Convert SeniorCitizen if needed
    if 'SeniorCitizen' in df.columns:
        df['SeniorCitizen'] = df['SeniorCitizen'].astype(int)

    # ✅ Step 6: Drop unnecessary columns
    if 'customerID' in df.columns:
        df = df.drop('customerID', axis=1)

    print("\nData cleaned successfully!\n")
    return df


# -------------------------------
# Save Data
# -------------------------------
def save_data(df, path):
    df.to_csv(path, index=False)


# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":
    input_path = "data/raw/Telco_Churn_dataset.csv"
    output_path = "data/processed/cleaned_churn.csv"

    df = load_data(input_path)
    df = clean_data(df)
    save_data(df, output_path)

    print("✅ Cleaned data saved at:", output_path)