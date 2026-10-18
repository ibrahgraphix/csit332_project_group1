# CSIT332 ML Course Project — Component A, Group 1

## Members
- Ibrahim Shelukindo
- Abhinav N
- Nakul Shyamkumar

## Assigned task

Component A — The Engine. We supply the datasets the project runs on.

- **Week 1:** build a candidate dataset register. Find real datasets that fit the project's rules (tabular, binary or binarisable target, at least 10,000 rows, no more than 30% missing in any kept column, clear licence). Check the numbers ourselves instead of trusting the dataset page, and write down which datasets we rejected and why.
- **Week 2:** turn five datasets from the register into clean files the project can run on, and freeze a 30% test split for each.

## What's in this repo

### Week 1: the register
- `candidate_dataset_register.xlsx` — the 15-dataset register with the eight required columns (name, source and URL, rows, features, target and binarisation rule, class prevalence, missingness, licence). It also has sheets for the rejected datasets, the ambiguity list and the hardest criterion.
- `docs/dataset_register.md` — the same register as a page you can read on GitHub.

### Week 2: prepared datasets and frozen splits
- `scripts/` — one preparation script per dataset. Each downloads its data and writes one clean file: numeric columns `f1, f2, ...`, a target `y` with only 0 and 1, no missing values, every feature standardised to mean 0 and standard deviation 1.
  - `prepare_adult.py`
  - `prepare_bank_marketing.py`
  - `prepare_online_shoppers.py`
  - `prepare_credit_default.py`
  - `prepare_magic_gamma.py`
- `splits/` — the frozen split for each of the five datasets: `row_index` and `split` (`pool` or `test`). 30% of the rows are the permanent test set, stratified on `y`. The other 70% is the study pool.
- `profile_table.md` — final rows, final features, class prevalence and split seed for each dataset.
- `cleaning_decisions.md` — what we did to each dataset: how the target was made binary, missing values, categorical columns, dropped columns, and the final counts.

**Split seed: 332** (all five datasets).

## How to reproduce the Week 2 files

```
pip install pandas scikit-learn
python scripts/prepare_adult.py out
python scripts/prepare_bank_marketing.py out
python scripts/prepare_online_shoppers.py out
python scripts/prepare_credit_default.py out
python scripts/prepare_magic_gamma.py out
```

Each script downloads its data into `out/raw`, writes the clean file to `out/prepared`, the split to `out/splits` and a log of the cleaning counts to `out/logs`. The datasets themselves are not stored in this repo. The split files in `splits/` should match `out/splits/` exactly.

## Status

- **Week 1:** 15 datasets in the register. We downloaded and counted 14 of them ourselves. Credit Card Fraud links to Kaggle and its rows were counted on a mirror of the same file.
- **Week 2:** five datasets prepared (Adult, Bank Marketing, Online Shoppers, Default of Credit Card Clients, MAGIC Gamma Telescope), each with a frozen 70/30 split.
