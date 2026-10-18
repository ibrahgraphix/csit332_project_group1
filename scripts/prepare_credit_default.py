"""Default of Credit Card Clients. Target: default next month = 1."""
NAME = "credit_default"
URL = "https://raw.githubusercontent.com/YuChenAmberLu/Data-Science--Credit-Card-Default/master/UCI_Credit_Card.csv"

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


df = pd.read_csv(download(URL, "UCI_Credit_Card.csv"))
log = {"rows_raw": int(len(df)), "columns_raw": int(df.shape[1])}

y = df["default.payment.next.month"].astype(int)
log["target_rule"] = "default.payment.next.month: 1 = default, 0 = no default (already binary)"
df = df.drop(columns=["default.payment.next.month"])

log["null_values"] = int(df.isna().sum().sum())
log["rows_dropped_missing"] = 0

df = df.drop(columns=["ID"])
log["dropped_columns"] = {"ID": "row identifier"}

# SEX, EDUCATION, MARRIAGE are category codes -> one-hot. PAY_* are ordered repayment
# status values and stay numeric. EDUCATION has undocumented codes (0, 5, 6): kept as levels.
cat = ["SEX", "EDUCATION", "MARRIAGE"]
for c in cat:
    df[c] = df[c].astype(str)
X = pd.get_dummies(df, columns=cat, drop_first=True, dtype=float)
log["categorical_columns"] = cat
log["new_columns_from_categorical"] = int(X.shape[1] - (df.shape[1] - len(cat)))
finish(NAME, X, y, log)
