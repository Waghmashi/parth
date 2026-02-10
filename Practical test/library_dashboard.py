import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')


class LibraryDashboard:

    def __init__(self):
        self.data = None
        print("\n===== E-Library Data Insights Dashboard =====\n")

    def load_data(self, file_path):
        if not os.path.exists(file_path):
            print("Error: File not found!")
            return False

        try:
            self.data = pd.read_csv(file_path)
            self.data.columns = self.data.columns.str.strip()

            column_map = {
                "Book_ID": "Transaction ID",
                "Title": "Book Title",
                "Category": "Genre",
                "Times_Issued": "Borrowing Duration (Days)",
                "Year_Published": "Year_Published",
                "Author": "Author",
                "Copies_Available": "Copies_Available"
            }

            self.data.rename(columns=column_map, inplace=True)

            if "Date" not in self.data.columns:
                self.data["Date"] = pd.date_range("2024-01-01", periods=len(self.data), freq="D")

            if "User ID" not in self.data.columns:
                self.data["User ID"] = range(1001, 1001 + len(self.data))

            required = [
                "Transaction ID",
                "Date",
                "User ID",
                "Book Title",
                "Genre",
                "Borrowing Duration (Days)"
            ]

            if any(col not in self.data.columns for col in required):
                print("Required columns missing!")
                return False

            self.data["Date"] = pd.to_datetime(self.data["Date"], errors="coerce")
            self.data.dropna(inplace=True)

            print("Dataset Loaded Successfully!")
            print("Total Records:", len(self.data))
            return True

        except Exception as e:
            print("Error:", e)
            return False

    def calculate_statistics(self):
        top_books = self.data["Book Title"].value_counts().head(5)
        avg_duration = np.mean(self.data["Borrowing Duration (Days)"])
        std_duration = np.std(self.data["Borrowing Duration (Days)"])
        busiest_day = self.data["Date"].value_counts().idxmax()

        print("\nTop 5 Books:")
        for i, (b, c) in enumerate(top_books.items(), 1):
            print(f"{i}. {b} - {c}")

        print("\nAverage Duration:", round(avg_duration, 2))
        print("Std Deviation:", round(std_duration, 2))
        print("Busiest Day:", busiest_day.date())
        print("Unique Users:", self.data["User ID"].nunique())
        print("Unique Genres:", self.data["Genre"].nunique())

    def filter_transactions(self, genre=None, start=None, end=None):
        df = self.data.copy()

        if genre:
            df = df[df["Genre"].str.contains(genre, case=False)]
        if start:
            df = df[df["Date"] >= pd.to_datetime(start)]
        if end:
            df = df[df["Date"] <= pd.to_datetime(end)]

        print("Filtered Records:", len(df))
        print(df.head())
        return df

    def generate_report(self):
        print("\nTotal Transactions:", len(self.data))
        print("Unique Users:", self.data["User ID"].nunique())
        print("Most Borrowed Book:", self.data["Book Title"].value_counts().idxmax())
        print("Popular Genre:", self.data["Genre"].value_counts().idxmax())
        print("Average Duration:", round(self.data["Borrowing Duration (Days)"].mean(), 2))

    def visualize_data(self):
        fig, axes = plt.subplots(2, 2, figsize=(14, 9))

        self.data["Book Title"].value_counts().head(5).plot(kind="barh", ax=axes[0, 0])
        axes[0, 0].set_title("Top 5 Books")

        self.data["Genre"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=axes[0, 1])

        self.data["Month"] = self.data["Date"].dt.to_period("M").astype(str)
        self.data.groupby("Month").size().plot(ax=axes[1, 0])
        axes[1, 0].tick_params(axis="x", rotation=45)

        self.data.groupby("Genre")["Borrowing Duration (Days)"].mean().plot(kind="bar", ax=axes[1, 1])

        plt.tight_layout()
        plt.show()

        self.data["Day"] = self.data["Date"].dt.day_name()
        table = pd.pivot_table(
            self.data,
            values="Borrowing Duration (Days)",
            index="Day",
            columns="Genre",
            aggfunc=np.mean,
            fill_value=0
        )

        plt.figure(figsize=(12, 6))
        sns.heatmap(table, annot=True, fmt=".1f")
        plt.show()


def main():
    dashboard = LibraryDashboard()
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "E library.csv")

    if not dashboard.load_data(path):
        return

    while True:
        print("\n1. Statistics")
        print("2. Filter")
        print("3. Report")
        print("4. Visualize")
        print("5. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            dashboard.calculate_statistics()
        elif ch == "2":
            g = input("Genre: ")
            s = input("Start Date (YYYY-MM-DD): ")
            e = input("End Date (YYYY-MM-DD): ")
            dashboard.filter_transactions(g or None, s or None, e or None)
        elif ch == "3":
            dashboard.generate_report()
        elif ch == "4":
            dashboard.visualize_data()
        elif ch == "5":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()