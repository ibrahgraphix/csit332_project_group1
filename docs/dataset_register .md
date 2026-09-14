# Dataset Register

15 datasets checked so far. This meets the assignment's minimum of 15.

## Candidate datasets

| Name | Source and URL | Rows | Features | Target and binarisation rule | Class prevalence | Missingness | Licence |
|---|---|---|---|---|---|---|---|
| Adult Income | UCI, mirror: github.com/jbrownlee/Datasets/blob/master/adult-all.csv | 48842 | 14 | Already binary. Income is either <=50K or >50K. | 23.9% earn >50K | workclass 5.7% missing, occupation 5.8% missing, native-country 1.8% missing | CC BY 4.0 |
| Mammography | UCI/KEEL, mirror: github.com/jbrownlee/Datasets/blob/master/mammography.csv | 11183 | 6 | Already binary. 1 means calcification found, -1 means not found. | 2.3% positive | no missing values | Public benchmark dataset, free to use |
| Credit Card Fraud | kaggle.com/datasets/mlg-ulb/creditcardfraud | 284807 | 30 | Already binary. 1 means fraud, 0 means normal transaction. | 0.17% fraud | no missing values | Open Database License (DbCL) v1.0 |
| Bank Marketing | archive.ics.uci.edu/dataset/222/bank+marketing | 45211 | 16 | Already binary. Customer said yes or no to the offer. | 11.7% said yes | no blank cells, but the poutcome column is 81.7% marked unknown | CC BY 4.0 |
| Give Me Some Credit | kaggle.com/c/GiveMeSomeCredit | 150000 | 10 | Already binary. 1 means serious default within 2 years, 0 means no default. | 6.7% defaulted | MonthlyIncome 19.8% missing, NumberOfDependents 2.6% missing | Kaggle competition data, check competition rules before reuse |
| MAGIC Gamma Telescope | UCI, mirror: github.com/mikeizbicki/datasets/blob/master/csv/uci/magic04.data | 19020 | 10 | Already binary. g means gamma ray, h means hadron. | 35.2% are hadron | no missing values | CC BY 4.0 |
| Online Shoppers Purchasing Intention | UCI, mirror: github.com/sharmaroshan/Online-Shoppers-Purchasing-Intention | 12330 | 17 | Already binary. Revenue is True if the visit ended in a purchase, False if not. | 15.5% ended in a purchase | no missing values | CC BY 4.0 |
| EEG Eye State | UCI, mirror: github.com/Krishh-mishra98/eeg-eye-state-dataset | 14980 | 14 | Already binary. 1 means eyes closed, 2 means eyes open (treated as 0/1). | 44.9% eyes open | no missing values | CC BY 4.0 |
| Rain in Australia (weatherAUS) | Kaggle: kaggle.com/datasets/jsphyg/weather-dataset-rattle-package, mirror: github.com/acakin/weatherAUS | 142193 usable (145460 total, 3267 rows dropped for missing target) | 16 (dropped Date, Location, and 4 columns over 30% missing: Sunshine, Evaporation, Cloud9am, Cloud3pm) | Already binary. RainTomorrow is Yes or No. | 22.4% said Yes | worst kept column (Pressure9am) is 9.9% missing, after dropping the 4 columns above | From the Australian Bureau of Meteorology, shared on Kaggle. Check the Kaggle page for exact reuse terms. |
| Diabetes 130-US Hospitals | UCI, mirror: github.com/swengzju/Predicting-Diabetes-Patient-Readmission | 101766 | 42 (dropped 2 ID columns, and 5 columns over 30% missing: weight, max_glu_serum, A1Cresult, medical_specialty, payer_code) | Was 3 classes (NO, <30, >30 days). Made binary: 1 = readmitted in under 30 days, 0 = not. | 11.2% readmitted under 30 days | worst kept column (race) is 2.2% missing, after dropping the 5 columns above | CC BY 4.0 |
| Letter Recognition | UCI, mirror: github.com/mikeizbicki/datasets/blob/master/csv/uci/letter-recognition.data | 20000 | 16 | Was 26 classes (one per letter). Made binary: 1 = vowel (A, E, I, O, U), 0 = consonant. | 19.4% vowels | no missing values | CC BY 4.0 |
| Connect-4 | UCI, mirror: github.com/ducanng/Decision-Tree-with-scikit-learn/blob/master/connect-4.data | 67557 | 42 | Was 3 classes (win, loss, draw). Made binary: 1 = win, 0 = not a win. | 34.2% not a win | no missing values | CC BY 4.0 |
| Statlog Shuttle (test split) | UCI, mirror: github.com/mikeizbicki/datasets/blob/master/csv/uci/shuttle.tst | 14500 | 9 | Was 7 classes. Made binary: 1 = class 1 "Rad Flow", 0 = any other class. | 20.8% not class 1 | no missing values | CC BY 4.0. Note: this is only the test portion of the full dataset (the full set has about 58,000 rows). We could only get this file, so all numbers here are for this 14,500-row file only. |
| Nursery | UCI, mirror: github.com/mikeizbicki/datasets/blob/master/csv/uci/nursery.data | 12960 | 8 | Was 5 classes. Made binary: 1 = not_recom (application not recommended), 0 = any other outcome. | 33.3% not_recom | no missing values | CC BY 4.0 |
| Chess (King-Rook vs King) | UCI, mirror: github.com/mikeizbicki/datasets/blob/master/csv/uci/krkopt.data | 28056 | 6 | Was 18 classes (draw, or number of moves to win). Made binary: 1 = draw, 0 = White wins in some number of moves. | 10.0% draw | no missing values | CC BY 4.0 |

Row counts, missing value counts, and class counts above were checked by downloading each file and running it through pandas ourselves, not copied from the dataset page.

## Rejected datasets

| Name | Rows found | Why rejected |
|---|---|---|
| Phoneme | 5404 | Too few rows, needs at least 10,000 |
| Oil Spill | 937 | Too few rows |
| Sonar | 208 | Too few rows |
| Pima Indians Diabetes | 768 | Too few rows |
| German Credit | 1000 | Too few rows |
| Telco Customer Churn | 7043 | Too few rows |
| IBM HR Attrition | 1470 | Too few rows |
| Default of Credit Card Clients | 30000 | Row count looks fine but we couldn't download the file ourselves to check it, so we left it out |
| Covertype | 581012 | Row count looks fine but we couldn't download the file, and it also needs a binarisation rule since it has 7 classes |
| HTRU2 (Pulsar Detection) | 17898 | Row count looks fine but we couldn't find a working download link to check it ourselves, so we left it out |

We looked at 24 datasets in total across all rounds. 15 made it in, 9 did not.
Main reason for rejecting: too few rows (6 out of 9).
Other reason: couldn't find a working download link to check the numbers ourselves (3 out of 9: Default of Credit Card Clients, Covertype, HTRU2).

## Ambiguity list

1. **Bank Marketing has a column that's 81.7% marked "unknown."** Is that missing data or just a normal answer? We counted it as a normal answer (it means "no past contact"), not missing data. Someone else might count it differently.
2. **What counts as a feature vs. an ID column?** We dropped any column that was just a row number or ID, since it has no predictive use.
3. **What to do when the published row count looks right but we can't download the file ourselves?** We left those datasets out instead of trusting the number, since the assignment says to check it ourselves.
4. **Is Kaggle competition data licensed the same way as a normal Kaggle dataset?** We kept Give Me Some Credit in for now but flagged that competition rules are stricter and should be double-checked.
5. **For datasets with more than 2 classes (Letter Recognition, Connect-4, Nursery, Chess, Shuttle), which class do we pick to turn it binary?** We picked the split that made the most real-world sense for each one (vowel vs consonant, win vs not-win, draw vs not-draw, etc.) rather than just picking the biggest class. A different choice gives a different minority percent, so this is a real decision, not just a formatting step.
6. **Is it OK to use just part of a dataset if that's the only file we could access?** For Statlog Shuttle, we could only get the 14,500-row test file, not the full ~58,000-row dataset. We used it since it clears the 10,000-row minimum on its own, but we wrote clearly that it's only part of the full dataset.

## Hardest rule to follow

The hardest rule was checking the row count ourselves. It's simple once you have the file, but some datasets we wanted (Default of Credit Card Clients, Covertype, HTRU2) couldn't be downloaded in the time we had, so we couldn't open the file and count the rows ourselves. Rather than just use the number from the dataset page, which is exactly what the assignment says not to do, we left those out. The other tricky part was missing data and picking a binarisation rule — several datasets that fit everything else had a few columns that were mostly missing (Rain in Australia, Diabetes 130-US Hospitals), so we had to decide to drop those specific columns rather than the whole dataset, and several others (Letter Recognition, Connect-4, Nursery, Chess, Shuttle) had more than two classes, so we had to pick and write down exactly which class counted as the "positive" one.
