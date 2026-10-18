# Component A, Week 2: cleaning decisions

Group 1 (CSIT332). Members: Ibrahim Shelukindo, Abhinav N, Nakul Shyamkumar.

## Rules that apply to all five datasets

- **Output shape.** One file per dataset with columns `f1, f2, ... fk` and `y`. All numbers, no missing values, no text, no ID columns.
- **Which class is 1.** In every dataset `y = 1` is the minority class. That way "prevalence" always means the share of 1s.
- **Categorical columns.** Converted with one-hot encoding, dropping the first level of each column so the new columns are not exact copies of each other. Each section below says how many new columns this made.
- **Standardising.** Every feature has mean 0 and standard deviation 1 (population standard deviation, the same as sklearn's StandardScaler). We did this on the whole dataset, as the instructions say, so the test rows were included when the mean and standard deviation were worked out. If this is a problem for the later steps, the means and standard deviations will need to be worked out on the study pool only.
- **Constant columns.** None of the five datasets had a column that was the same in every row after cleaning.
- **The split.** 30% of the rows are the frozen test set, stratified on `y`, with seed **332** (`sklearn.model_selection.train_test_split`, `test_size=0.30`, `stratify=y`, `shuffle=True`). The 70% that is left is the study pool. The split file for each dataset has two columns: `row_index` and `split` (`pool` or `test`). `row_index` is the position of the row in the prepared file, counting from 0, after any rows were dropped. We ran every script twice and got identical split files both times.
- **Not uploaded.** The scripts download the data themselves. The prepared files are not part of the submission.

## 1. Adult (Census Income) — `prepare_adult.py`

- **Target.** Already binary. `income` of `>50K` is 1 and `<=50K` is 0.
- **Missing values.** Three columns had missing values (written as `?`): workclass (2,799 rows), occupation (2,809) and native_country (857). We dropped every row with a missing value. That removed **3,620 rows** (7.4% of 48,842). No columns were dropped for missing values.
- **Categorical columns.** 7 columns (workclass, marital_status, occupation, relationship, race, sex, native_country) became **75 new columns**.
- **Columns dropped.** `education`, because `education_num` is the same information as a number. `fnlwgt`, because it is a survey sampling weight and says nothing about the person.
- **Final.** 45,222 rows, 80 features, prevalence 24.78%. (The register says 23.9% because it counts all 48,842 rows. Dropping rows with missing values moves it to 24.78%.)

## 2. Bank Marketing — `prepare_bank_marketing.py`

- **Target.** Already binary. `y` of `yes` is 1 and `no` is 0.
- **Missing values.** There are no empty cells. Four columns use the word `unknown`: poutcome (36,959 rows), contact (13,020), education (1,857) and job (288). We kept `unknown` as its own category instead of treating it as missing, so **no rows or columns were dropped**. This is a judgement call: poutcome is 81.7% `unknown`, so under a stricter reading it would break the 30% rule.
- **Categorical columns.** 9 columns (job, marital, education, default, housing, loan, contact, month, poutcome) became **35 new columns**.
- **Columns dropped.** `duration`, because the length of a call is only known after the call has happened, so it cannot be used to predict the result. The UCI notes say to drop it for a realistic model.
- **Final.** 45,211 rows, 41 features, prevalence 11.70%.

## 3. Online Shoppers Purchasing Intention — `prepare_online_shoppers.py`

- **Target.** Already binary. `Revenue` of True is 1 and False is 0.
- **Missing values.** None. No rows or columns dropped.
- **Categorical columns.** Month and VisitorType became **11 new columns**. `Weekend` (True/False) was changed to 1/0. OperatingSystems, Browser, Region and TrafficType are code numbers for categories, but we left them as numbers, because one-hot encoding them would add about 50 mostly empty columns. This is a judgement call.
- **Columns dropped.** None.
- **Final.** 12,330 rows, 26 features, prevalence 15.47%.

## 4. Default of Credit Card Clients — `prepare_credit_default.py`

- **Target.** Already binary. `default.payment.next.month` of 1 means the client defaulted.
- **Missing values.** None. No rows or columns dropped.
- **Categorical columns.** SEX, EDUCATION and MARRIAGE became **10 new columns**. EDUCATION has the codes 0, 5 and 6, which the dataset description does not explain. We kept them as their own levels. The PAY_ columns are repayment status values in order, so they stay as numbers.
- **Columns dropped.** `ID`, because it is a row identifier.
- **Final.** 30,000 rows, 30 features, prevalence 22.12%.

## 5. MAGIC Gamma Telescope — `prepare_magic_gamma.py`

- **Target.** Already binary. `Class` of `h` (hadron) is 1 and `g` (gamma) is 0. Hadron is the smaller class.
- **Missing values.** None. No rows or columns dropped.
- **Categorical columns.** None. All 10 features were already numbers.
- **Columns dropped.** None.
- **Final.** 19,020 rows, 10 features, prevalence 35.16%.

## How to reproduce

```
pip install pandas scikit-learn
python prepare_adult.py out
python prepare_bank_marketing.py out
python prepare_online_shoppers.py out
python prepare_credit_default.py out
python prepare_magic_gamma.py out
```

Each script downloads its data into `out/raw`, writes the clean file to `out/prepared`, the split to `out/splits` and a log of the counts above to `out/logs`.
