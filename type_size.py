import numpy as np
import pandas as pd
import time


def load_frame(pathname: str, cols: list) -> pd.DataFrame:
    return pd.read_csv(pathname, names=cols)


def get_sizes(df: pd.DataFrame, type_size: dict):
    max_values = {c: df[c].max() for c in df.columns}
    for mv in max_values.keys():
        if mv != "hash":
            k = 8
            while max_values[mv] > type_size[k][1]:
                k = k * 2
            print(f"{mv}: {k}")


if __name__ == "__main__":
    type_size = {
        8: [np.iinfo(np.uint8).min, np.iinfo(np.uint8).max],
        16: [np.iinfo(np.uint16).min, np.iinfo(np.uint16).max],
        32: [np.iinfo(np.uint32).min, np.iinfo(np.uint32).max],
        64: [np.iinfo(np.uint64).min, np.iinfo(np.uint64).max],
    }

    tx_cols = ["timestamp", "blk", "tx", "is_coinbase", "fee"]
    in_cols = ["tx", "prev_tx", "out_pos"]
    out_cols = ["tx", "out_pos", "address", "amount", "script_type"]
    map_cols = ["hash", "address"]

    start = time.time()
    tx_df = load_frame("transactions.csv", tx_cols)
    in_df = load_frame("inputs.csv", in_cols)
    out_df = load_frame("outputs.csv", out_cols)
    map_df = load_frame("mappings.csv", map_cols)
    end = time.time()

    print(f"elapsed time: {end - start} seconds")

    get_sizes(tx_df, type_size)
    get_sizes(in_df, type_size)
    get_sizes(out_df, type_size)
    get_sizes(map_df, type_size)

    print(tx_df.info())
    print(in_df.info())
    print(out_df.info())
    print(map_df.info())
