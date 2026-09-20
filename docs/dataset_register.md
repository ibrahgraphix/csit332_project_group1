# Dataset Register

15 datasets checked so far. This meets the assignment's minimum of 15.

Every link is a single file you download directly — no zip to extract. 12 of the 15 are real `.csv` files. Two (Credit Card Fraud, Give Me Some Credit) are on Kaggle — click the Download button on the page (needs a free Kaggle login, but since each is a single-file dataset it downloads as one csv, not a zip). Three (Connect-4, Statlog Shuttle, Chess King-Rook vs King) don't have a working `.csv` mirror we could find, so those stay as `.data`/`.tst` files — still a single plain-text file, just an older extension, and they open fine in Excel or pandas. A couple of links (Mammography, Connect-4, Statlog Shuttle, Chess) open as a wall of text in the browser rather than auto-downloading — use Ctrl+S or right-click > Save Link As to save them.

## Candidate datasets

| Name | Source and URL | Rows | Features | Target and binarisation rule | Class prevalence | Missingness | Licence |
|---|---|---|---|---|---|---|---|
| Adult Income | https://raw.githubusercontent.com/jbrownlee/Datasets/master/adult-all.csv | 48842 | 14 | Already binary. Income is either <=50K or >50K. | 23.9% earn >50K | workclass 5.7% missing, occupation 5.8% missing, native_country 1.8% missing | CC BY 4.0 |
| Mammography | https://raw.githubusercontent.com/jbrownlee/Datasets/master/mammography.csv (opens as text — use Ctrl+S to save) | 11183 | 6 | Already binary. class 1 means calcification found, -1 means not found. | 2.3% positive | no missing values | Public benchmark dataset, free to use |
| Credit Card Fraud | https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud (Download button, needs free Kaggle login, single csv) | 284807 | 30 | Already binary. 1 means fraud, 0 means normal transaction. | 0.17% fraud | no missing values | Open Database License (DbCL) v1.0 |
| Bank Marketing | https://raw.githubusercontent.com/khatrideepti/Bank-Marketing-Data-Analysis/master/bank-full.csv | 45211 | 16 | Already binary. Customer said yes or no to the offer. | 11.7% said yes | no blank cells, but the poutcome column is 81.7% marked unknown | CC BY 4.0 |
| Give Me Some Credit | https://www.kaggle.com/c/GiveMeSomeCredit/data (Download button, needs free Kaggle login, single csv) | 150000 | 10 | Already binary. 1 means serious default within 2 years, 0 means no default. | 6.7% defaulted | MonthlyIncome 19.8% missing, NumberOfDependents 2.6% missing | Kaggle competition data, check competition rules before reuse |
| MAGIC Gamma Telescope | https://raw.githubusercontent.com/EpistasisLab/tpot/master/tutorials/MAGIC%20Gamma%20Telescope/MAGIC%20Gamma%20Telescope%20Data.csv | 19020 | 10 | Already binary. class g means gamma ray, h means hadron. | 35.2% are hadron | no missing values | CC BY 4.0 |
| Online Shoppers Purchasing Intention | https://raw.githubusercontent.com/sharmaroshan/Online-Shoppers-Purchasing-Intention/master/online_shoppers_intention.csv | 12330 | 17 | Already binary. Revenue is True if the visit ended in a purchase, False if not. | 15.5% ended in a purchase | no missing values | CC BY 4.0 |
| EEG Eye State | https://raw.githubusercontent.com/Krishh-mishra98/eeg-eye-state-dataset/master/eeg.csv | 14980 | 14 | Already binary. 1 means eyes closed, 2 means eyes open (treated as 0/1). | 44.9% eyes open | no missing values | CC BY 4.0 |
| Rain in Australia (weatherAUS) | https://raw.githubusercontent.com/acakin/weatherAUS/master/weatherAUS.csv | 142193 usable (145460 total, 3267 rows dropped for missing target) | 16 (dropped Date, Location, and 4 columns over 30% missing: Sunshine, Evaporation, Cloud9am, Cloud3pm) | Already binary. RainTomorrow is Yes or No. | 22.4% said Yes | worst kept column (Pressure9am) is 9.9% missing, after dropping the 4 columns above | From the Australian Bureau of Meteorology, shared on Kaggle. Check the Kaggle page for exact reuse terms. |
| Diabetes 130-US Hospitals | https://raw.githubusercontent.com/swengzju/Predicting-Diabetes-Patient-Readmission/master/diabetic_data.csv | 101766 | 42 (dropped 2 ID columns, and 5 columns over 30% missing: weight, max_glu_serum, A1Cresult, medical_specialty, payer_code) | Was 3 classes (NO, <30, >30 days). Made binary: 1 = readmitted in under 30 days, 0 = not. | 11.2% readmitted under 30 days | worst kept column (race) is 2.2% missing, after dropping the 5 columns above | CC BY 4.0 |
| Letter Recognition | https://raw.githubusercontent.com/aiez/klassif/main/letter.csv | 20000 | 16 | Was 26 classes (one per letter). Made binary: 1 = vowel (A, E, I, O, U), 0 = consonant. | 19.4% vowels | no missing values | CC BY 4.0 (original UCI data); this csv copy is shared under MIT by the repo maintainer |
| Connect-4 | https://raw.githubusercontent.com/ducanng/Decision-Tree-with-scikit-learn/master/connect-4.data (opens as text — use Ctrl+S to save) | 67557 | 42 | Was 3 classes (win, loss, draw). Made binary: 1 = win, 0 = not a win. | 34.2% not a win | no missing values | CC BY 4.0. Note: no working .csv mirror found — this is a .data file, same single comma-separated file, just an older extension. |
| Statlog Shuttle (test split) | https://raw.githubusercontent.com/mikeizbicki/datasets/master/csv/uci/shuttle.tst (opens as text — use Ctrl+S to save) | 14500 | 9 | Was 7 classes. Made binary: 1 = class 1 "Rad Flow", 0 = any other class. | 20.8% not class 1 | no missing values | CC BY 4.0. Note: this is only the test portion of the full dataset (full set is about 58,000 rows). No working .csv mirror found — this is a .tst file, same single space-separated file, just an older extension. |
| Nursery | https://raw.githubusercontent.com/aiez/klassif/main/nursery.csv | 12960 | 8 | Was 5 classes. Made binary: 1 = not_recom (application not recommended), 0 = any other outcome. | 33.3% not_recom | no missing values | CC BY 4.0 (original UCI data); this csv copy is shared under MIT by the repo maintainer |
| Chess (King-Rook vs King) | https://raw.githubusercontent.com/mikeizbicki/datasets/master/csv/uci/krkopt.data (opens as text — use Ctrl+S to save) | 28056 | 6 | Was 18 classes (draw, or number of moves to win). Made binary: 1 = draw, 0 = White wins in some number of moves. | 10.0% draw | no missing values | CC BY 4.0. Note: no working .csv mirror found — there's a similarly-named "King-Rook vs King-Pawn" dataset out there but it's a different, smaller dataset, so we didn't substitute it. This is a .data file, same single comma-separated file, just an older extension. |

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
7. **We wanted every dataset to be a single .csv file with no zip to extract, but a few (Connect-4, Statlog Shuttle, Chess King-Rook vs King) only exist as older .data/.tst files with no working .csv mirror we could find.** We swapped in real .csv versions wherever we found one that matched the exact same dataset (MAGIC, Letter Recognition, and Nursery all got upgraded this way). For the 3 we couldn't find a .csv for, we kept the .data/.tst file rather than substitute a different, smaller dataset with a similar name (there's a "King-Rook vs King-Pawn" dataset that sounds similar to our Chess dataset but is a completely different, smaller dataset — we didn't want to quietly swap in the wrong data just to get a .csv extension).

## Hardest rule to follow

The hardest rule was checking the row count ourselves. It's simple once you have the file, but some datasets we wanted (Default of Credit Card Clients, Covertype, HTRU2) couldn't be downloaded in the time we had, so we couldn't open the file and count the rows ourselves. Rather than just use the number from the dataset page, which is exactly what the assignment says not to do, we left those out. We also went through two rounds of link problems: first, some links pointed at a repo instead of a file, or opened as a wall of text instead of downloading; then, once we fixed that, we still wanted single .csv files with no zip to extract, so we went back and found real .csv mirrors for three more datasets (MAGIC, Letter Recognition, Nursery). Three others (Connect-4, Statlog Shuttle, Chess King-Rook vs King) still don't have a .csv version we could find, so those stay as .data/.tst files — still a single file, just an older extension. The other tricky part was missing data and picking a binarisation rule — several datasets that fit everything else had a few columns that were mostly missing (Rain in Australia, Diabetes 130-US Hospitals), so we had to decide to drop those specific columns rather than the whole dataset, and several others (Letter Recognition, Connect-4, Nursery, Chess, Shuttle) had more than two classes, so we had to pick and write down exactly which class counted as the positive one.
