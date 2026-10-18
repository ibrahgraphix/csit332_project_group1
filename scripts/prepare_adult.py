"""Adult (Census Income). Target: income > 50K = 1."""
NAME = "adult"
URL = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/adult-all.csv"

# ---- shared steps: identical in all five scripts ----
import json, os, sys, urllib.request
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

SEED = 332            # fixed random seed for the frozen split
TEST_FRACTION = 0.30  # 30% frozen test set, stratified on y
OUT = sys.argv[1] if len(sys.argv) > 1 else "out"   # where outputs are written


def download(url, filename):
    """Download once into OUT/raw and return the local path."""
    os.makedirs(os.path.join(OUT, "raw"), exist_ok=True)
    path = os.path.join(OUT, "raw", filename)
    if not os.path.exists(path):
        urllib.request.urlretrieve(url, path)
    return path


def finish(name, X, y, log):
    """X: numeric DataFrame of features. y: Series of 0/1. Standardise, check, save, split."""
    X = X.astype(float).reset_index(drop=True)
    y = pd.Series(y).astype(int).reset_index(drop=True)
    log["features_before_cleanup"] = int(X.shape[1])

    # drop constant columns (they cannot be standardised)
    const = [c for c in X.columns if X[c].nunique() < 2]
    if const:
        X = X.drop(columns=const)
    log["constant_columns_dropped"] = const

    # rename to f1..fk
    log["feature_names_original"] = list(X.columns)
    X.columns = [f"f{i}" for i in range(1, X.shape[1] + 1)]

    # standardise: mean 0, standard deviation 1 (population sd, as in sklearn StandardScaler)
    X = pd.DataFrame(StandardScaler().fit_transform(X), columns=X.columns)

    # final checks
    assert set(y.unique()) <= {0, 1}, "y must contain only 0 and 1"
    assert not X.isna().any().any() and not y.isna().any(), "no missing values allowed"
    assert all(np.issubdtype(t, np.number) for t in X.dtypes), "numeric features only"
    assert np.allclose(X.mean(), 0, atol=1e-8) and np.allclose(X.std(ddof=0), 1, atol=1e-8)

    data = X.copy()
    data["y"] = y
    os.makedirs(os.path.join(OUT, "prepared"), exist_ok=True)
    data.to_csv(os.path.join(OUT, "prepared", f"{name}.csv"), index=False)

    # frozen split: row positions in the prepared file (0 = first data row)
    idx = np.arange(len(data))
    pool_idx, test_idx = train_test_split(
        idx, test_size=TEST_FRACTION, stratify=y, random_state=SEED, shuffle=True)
    split = pd.DataFrame({"row_index": idx, "split": "pool"})
    split.loc[test_idx, "split"] = "test"
    os.makedirs(os.path.join(OUT, "splits"), exist_ok=True)
    split.to_csv(os.path.join(OUT, "splits", f"{name}_split.csv"), index=False)

    log.update({
        "dataset": name,
        "final_rows": int(len(data)),
        "final_features": int(X.shape[1]),
        "prevalence_y1": float(y.mean()),
        "n_y1": int(y.sum()), "n_y0": int((1 - y).sum()),
        "split_seed": SEED, "test_fraction": TEST_FRACTION,
        "pool_rows": int(len(pool_idx)), "test_rows": int(len(test_idx)),
        "test_prevalence": float(y.iloc[test_idx].mean()),
        "pool_prevalence": float(y.iloc[pool_idx].mean()),
    })
    os.makedirs(os.path.join(OUT, "logs"), exist_ok=True)
    with open(os.path.join(OUT, "logs", f"{name}_log.json"), "w") as f:
        json.dump(log, f, indent=2)
    print(f"{name}: rows={log['final_rows']} features={log['final_features']} "
          f"prevalence={log['prevalence_y1']:.4f} seed={SEED}")


cols = ["age", "workclass", "fnlwgt", "education", "education_num", "marital_status",
        "occupation", "relationship", "race", "sex", "capital_gain", "capital_loss",
        "hours_per_week", "native_country", "income"]
df = pd.read_csv(download(URL, "adult-all.csv"), header=None, names=cols,
                 na_values="?", skipinitialspace=True)
log = {"rows_raw": int(len(df)), "columns_raw": int(df.shape[1])}

# target: >50K = 1, everything else 0 (already binary)
y = df["income"].str.strip().str.rstrip(".").eq(">50K").astype(int)
log["target_rule"] = "income '>50K' = 1, '<=50K' = 0 (already binary)"
df = df.drop(columns=["income"])

# missing values: drop any row with a missing value
miss_cols = df.columns[df.isna().any()].tolist()
log["missing_columns"] = {c: int(df[c].isna().sum()) for c in miss_cols}
keep = ~df.isna().any(axis=1)
log["rows_dropped_missing"] = int((~keep).sum())
df, y = df[keep], y[keep]

# dropped columns
df = df.drop(columns=["education", "fnlwgt"])
log["dropped_columns"] = {
    "education": "same information as education_num (a text version of the same number)",
    "fnlwgt": "survey sampling weight, not a property of the person"}

# categorical -> one-hot (first level dropped)
cat = ["workclass", "marital_status", "occupation", "relationship", "race", "sex", "native_country"]
X = pd.get_dummies(df, columns=cat, drop_first=True, dtype=float)
log["categorical_columns"] = cat
log["new_columns_from_categorical"] = int(X.shape[1] - (df.shape[1] - len(cat)))
finish(NAME, X, y, log)
