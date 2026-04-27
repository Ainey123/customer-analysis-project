import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def run_visual_analysis(file_path):
    # 1. Load Data
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return
    
    df = pd.read_csv(file_path)
    print("Dataset Loaded Successfully!")
    print(df.head()) # Shows first 5 rows in terminal

    # Set style for professional look
    sns.set_theme(style="whitegrid")

    # --- Plot 1: Age Distribution ---
    plt.figure(figsize=(10, 5))
    sns.histplot(df['Age'], bins=20, kde=True, color='royalblue')
    plt.title('Customer Age Distribution')
    plt.savefig('age_plot.png') # Backup save
    plt.show() # This opens the diagram in VS Code

    # --- Plot 2: Category Popularity ---
    plt.figure(figsize=(10, 5))
    sns.countplot(data=df, x='Category', palette='viridis', hue='Category', legend=False)
    plt.title('Most Purchased Categories')
    plt.xticks(rotation=45)
    plt.savefig('category_plot.png') # Backup save
    plt.show()

    # --- Plot 3: Ratings by Category ---
    plt.figure(figsize=(10, 5))
    sns.barplot(data=df, x='Category', y='Review Rate', palette='magma', hue='Category', legend=False)
    plt.title('Average Satisfaction Rating per Category')
    plt.savefig('ratings_plot.png') # Backup save
    plt.show()

    # --- Print Results Summary ---
    print("\n" + "="*30)
    print("QUICK RESULTS SUMMARY")
    print("="*30)
    print(f"Total Records: {len(df)}")
    print(f"Average Customer Age: {df['Age'].mean():.1f} years")
    print(f"Top Category: {df['Category'].value_counts().idxmax()}")
    print(f"Average Review Rating: {df['Review Rate'].mean():.2f}/5")
    print("="*30)

if __name__ == "__main__":
    # Ensure your CSV is named exactly this and is in the same folder
    FILENAME = 'customer_records_1000.csv'
    run_visual_analysis(FILENAME)
