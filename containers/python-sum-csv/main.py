import pandas as pd

def main():
    df = pd.read_csv("/tmp/input.csv")
    df["result"] = df["value-1"] + df["value-2"]
    df[["result"]].to_csv("/tmp/output.csv", index=False)

if __name__ == '__main__':
    main()