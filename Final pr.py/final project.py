import pandas as pd
import matplotlib.pyplot as plt

class StockAnalyzer:

    def __init__(self):
        self.data = None
        print("==== Stock Market Analysis Program ====")

    def loadData(self):

        print("== Load Dataset ==")

        try:
            path = "AAPL.csv"   
            self.data = pd.read_csv(path)

            self.data["Date"] = pd.to_datetime(self.data["Date"])

            print("Dataset Loaded Successfully!")
            print("File:", path)

        except Exception as e:
            print("Error Loading File:", e)

    def exploreData(self):

        if self.data is None:
            print("Please Load Dataset First!")
            return

        print("== Explore Data ==")
        print("1. First 5 Rows")
        print("2. Last 5 Rows")
        print("3. Column Names")
        print("4. Data Types")
        print("5. Info")
        print("6. Back")

        while True:

            try:
                ch = int(input("Enter Choice: "))

                if ch == 1:
                    print(self.data.head())

                elif ch == 2:
                    print(self.data.tail())

                elif ch == 3:
                    print(self.data.columns)

                elif ch == 4:
                    print(self.data.dtypes)

                elif ch == 5:
                    print(self.data.info())

                elif ch == 6:
                    break

                else:
                    print("Invalid Choice!")

            except:
                print("Enter Valid Number!")

    def stockOperations(self):

        if self.data is None:
            print("Please Load Dataset First!")
            return

        print("=== Stock Operations ===")
        print("1. Highest Price")
        print("2. Lowest Price")
        print("3. Average Close Price")
        print("4. Moving Average (20 Days)")
        print("5. Back")

        while True:

            try:
                ch = int(input("Enter Choice: "))

                if ch == 1:

                    print("Highest Price:")
                    print(self.data["High"].max())

                elif ch == 2:

                    print("Lowest Price:")
                    print(self.data["Low"].min())

                elif ch == 3:

                    avg = self.data["Close"].mean()
                    print("Average Close Price =", avg)

                elif ch == 4:

                    self.data["MA20"] = self.data["Close"].rolling(20).mean()
                    print("20 Days Moving Average Added!")

                elif ch == 5:
                    break

                else:
                    print("Invalid Choice!")

            except:
                print("Enter Valid Number!")

    def handleMissing(self):

        if self.data is None:
            print("Please Load Dataset First!")
            return

        print("=== Handle Missing Data ===")
        print("1. Show Missing Values")
        print("2. Fill with Mean")
        print("3. Delete Missing Rows")
        print("4. Back")

        while True:

            try:
                ch = int(input("Enter Choice: "))

                if ch == 1:

                    print(self.data.isnull().sum())

                elif ch == 2:

                    self.data.fillna(self.data.mean(numeric_only=True), inplace=True)
                    print("Filled with Mean!")

                elif ch == 3:

                    self.data.dropna(inplace=True)
                    print("Missing Rows Deleted!")

                elif ch == 4:
                    break

                else:
                    print("Invalid Choice!")

            except:
                print("Enter Valid Number!")

    def descriptive(self):

        if self.data is None:
            print("Please Load Dataset First!")
            return

        print("=== Descriptive Statistics ===")
        print(self.data.describe())

    def visualization(self):

        if self.data is None:
            print("Please Load Dataset First!")
            return

        print("==== Stock Visualization ====")
        print("1. Closing Price Trend")
        print("2. Volume Chart")
        print("3. High vs Low")
        print("4. Moving Average Chart")
        print("5. Histogram (Close Price)")

        try:
            ch = int(input("Enter Choice: "))

            if ch == 1:

                plt.figure()
                plt.plot(self.data["Date"], self.data["Close"])
                plt.title("Closing Price Trend")
                plt.xlabel("Date")
                plt.ylabel("Close Price")
                plt.show()

            elif ch == 2:

                plt.figure()
                plt.bar(self.data["Date"], self.data["Volume"])
                plt.title("Trading Volume")
                plt.xlabel("Date")
                plt.ylabel("Volume")
                plt.show()

            elif ch == 3:

                plt.figure()
                plt.scatter(self.data["High"], self.data["Low"])
                plt.title("High vs Low Price")
                plt.xlabel("High")
                plt.ylabel("Low")
                plt.show()

            elif ch == 4:

                if "MA20" not in self.data.columns:
                    self.data["MA20"] = self.data["Close"].rolling(20).mean()

                plt.figure()
                plt.plot(self.data["Date"], self.data["Close"], label="Close")
                plt.plot(self.data["Date"], self.data["MA20"], label="MA20")
                plt.legend()
                plt.title("Moving Average Chart")
                plt.show()

            elif ch == 5:

                plt.figure()
                plt.hist(self.data["Close"], bins=15)
                plt.title("Close Price Distribution")
                plt.xlabel("Price")
                plt.ylabel("Frequency")
                plt.show()

            else:
                print("Invalid Choice!")

        except:
            print("Enter Valid Number!")

    def savePlot(self):

        name = input("Enter File Name (ex: plot.png): ")

        try:
            plt.savefig(name)
            print("Plot Saved Successfully!")

        except:
            print("Error Saving File!")

def main():

    obj = StockAnalyzer()

    while True:

        print("\n===== MAIN MENU =====")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Stock Operations")
        print("4. Handle Missing Data")
        print("5. Descriptive Statistics")
        print("6. Visualization")
        print("7. Save Plot")
        print("8. Exit")

        try:
            ch = int(input("Enter Choice: "))

            if ch == 1:
                obj.loadData()

            elif ch == 2:
                obj.exploreData()

            elif ch == 3:
                obj.stockOperations()

            elif ch == 4:
                obj.handleMissing()

            elif ch == 5:
                obj.descriptive()

            elif ch == 6:
                obj.visualization()

            elif ch == 7:
                obj.savePlot()

            elif ch == 8:
                print("Program Closed!")
                break

            else:
                print("Invalid Choice!")

        except:
            print("Enter Valid Number!")

main()