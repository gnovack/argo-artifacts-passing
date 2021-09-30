import numpy as np
import pandas as pd


def main():
    data = np.random.rand(100, 2)
    df = pd.DataFrame(data, columns=["value-1", "value-2"])
    df.to_csv("/tmp/output.csv", index=False)

if __name__ == '__main__':
    main()