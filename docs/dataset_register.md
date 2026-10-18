# Dataset Register

15 datasets, each checked by downloading the file and counting rows, features, missing values and class balance with pandas. The one exception is Credit Card Fraud, which we counted on a mirror of the same file, because we could not download from Kaggle ourselves. `y = 1` / the 'minority class' in the prevalence column is always the smaller class.

## Candidate datasets

| Name | Source and URL | Rows | Features | Target and binarisation rule | Class prevalence | Missingness | Licence |
|---|---|---|---|---|---|---|---|
| Adult (Census Income) | https://raw.githubusercontent.com/jbrownlee/Datasets/master/adult-all.csv — (origin: UCI) | 48842 | 14 | Already binary. income: >50K = 1, <=50K = 0. | 23.9% | 3 columns: workclass 5.7%, occupation 5.8%, native-country 1.8% (coded '?') | CC BY 4.0 (UCI) |
| Mammography | https://raw.githubusercontent.com/jbrownlee/Datasets/master/mammography.csv — (origin: OpenML/KEEL) | 11183 | 6 | Already binary. class: '1' (calcification) = 1, '-1' = 0. | 2.3% | 0%, 0 columns | No explicit licence found; widely mirrored benchmark. Check before redistributing. |
| Credit Card Fraud (ULB) | https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud — (Kaggle page; we counted the rows on a mirror of the same file, not on the Kaggle download) | 284807 | 30 | Already binary. Class: 1 = fraud, 0 = genuine. | 0.17% | 0%, 0 columns | DbCL v1.0 (Kaggle page) |
| Bank Marketing | https://raw.githubusercontent.com/khatrideepti/Bank-Marketing-Data-Analysis/master/bank-full.csv — (origin: UCI, semicolon-separated) | 45211 | 16 | Already binary. y: yes = 1, no = 0. | 11.7% | 0% null. 'unknown' is used as a category: poutcome 81.7%, contact 28.8%, education 4.1%, job 0.6% | CC BY 4.0 (UCI) |
| Default of Credit Card Clients | https://raw.githubusercontent.com/YuChenAmberLu/Data-Science--Credit-Card-Default/master/UCI_Credit_Card.csv — (origin: UCI) | 30000 | 23 | Already binary. default.payment.next.month: 1 = default, 0 = no default. ID column excluded from the feature count. | 22.1% | 0%, 0 columns | CC BY 4.0 (UCI) |
| MAGIC Gamma Telescope | https://raw.githubusercontent.com/EpistasisLab/tpot/master/tutorials/MAGIC%20Gamma%20Telescope/MAGIC%20Gamma%20Telescope%20Data.csv — (origin: UCI) | 19020 | 10 | Already binary. Class: h (hadron) = 1, g (gamma) = 0. | 35.2% | 0%, 0 columns | CC BY 4.0 (UCI) |
| Online Shoppers Purchasing Intention | https://raw.githubusercontent.com/sharmaroshan/Online-Shoppers-Purchasing-Intention/master/online_shoppers_intention.csv — (origin: UCI) | 12330 | 17 | Already binary. Revenue: True = 1, False = 0. | 15.5% | 0%, 0 columns | CC BY 4.0 (UCI) |
| Rain in Australia (weatherAUS) | https://raw.githubusercontent.com/acakin/weatherAUS/master/weatherAUS.csv — (origin: Kaggle, Bureau of Meteorology data) | 142193 | 16 | Already binary. RainTomorrow: Yes = 1, No = 0. 3,267 of 145,460 rows dropped for a missing target. Date and Location excluded. | 22.4% | 4 columns over 30% (Sunshine 47.7%, Evaporation 42.8%, Cloud3pm 40.2%, Cloud9am 37.7%), to be dropped. Worst kept column: Pressure9am 9.9%. (Percentages are out of the 142,193 rows with a target.) | Bureau of Meteorology data via Kaggle; reuse terms on the Kaggle page |
| Diabetes 130-US Hospitals | https://raw.githubusercontent.com/swengzju/Predicting-Diabetes-Patient-Readmission/master/diabetic_data.csv — (origin: UCI) | 101766 | 42 | 3 classes (NO, >30, <30). Binarised: readmitted '<30' = 1, all others = 0. | 11.2% | 5 columns over 30% (weight 96.9%, max_glu_serum 94.7%, A1Cresult 83.3%, medical_specialty 49.1%, payer_code 39.6%), to be dropped. Worst kept column: race 2.2%. | CC BY 4.0 (UCI) |
| Letter Recognition | https://raw.githubusercontent.com/aiez/klassif/main/letter.csv — (origin: UCI) | 20000 | 16 | 26 classes (letters). Binarised: vowel (A, E, I, O, U) = 1, consonant = 0. | 19.4% | 0%, 0 columns | CC BY 4.0 (UCI original); this copy is a third-party mirror |
| Connect-4 | https://raw.githubusercontent.com/ducanng/Decision-Tree-with-scikit-learn/master/connect-4.data — (origin: UCI; .data extension, comma-separated) | 67557 | 42 | 3 classes (win, loss, draw). Binarised: not-win (loss or draw) = 1, win = 0, so that the minority class is 1. | 34.2% | 0%, 0 columns | CC BY 4.0 (UCI) |
| Nursery | https://raw.githubusercontent.com/aiez/klassif/main/nursery.csv — (origin: UCI) | 12960 | 8 | 5 classes. Binarised: not_recom = 1, all others = 0. | 33.3% | 0%, 0 columns | CC BY 4.0 (UCI original); this copy is a third-party mirror |
| Skin Segmentation | https://raw.githubusercontent.com/mikey084/Skin_segmentation/master/Skin_NonSkin.txt — (origin: UCI; .txt extension, tab-separated, no header) | 245057 | 3 | Already binary. Fourth column: 1 = skin, 2 = non-skin. Skin recoded to 1, non-skin to 0. | 20.8% | 0%, 0 columns | CC BY 4.0 (UCI) |
| Internet Firewall Data | https://raw.githubusercontent.com/semnan-university-ai/Internet-Firewall/master/firewall.csv — (origin: UCI) | 65532 | 11 | 4 classes in Action (allow, deny, drop, reset-both). Binarised: not-allow (deny, drop, reset-both) = 1, allow = 0. | 42.6% | 0%, 0 columns | CC BY 4.0 (UCI) |
| Avila (training split) | https://raw.githubusercontent.com/simonharris/cleandata/master/offline_data/AvilaTR.csv — (origin: UCI; no header) | 10430 | 10 | 12 classes (scribe styles). Binarised: class A = 1, all others = 0. Training split only (full dataset is about 20,867 rows). | 41.1% | 0%, 0 columns | CC BY 4.0 (UCI) |

## Rejected datasets

| Name | Rows found | Why rejected |
|---|---|---|
| Phoneme | 5,404 | Under 10,000 rows |
| Oil Spill | 937 | Under 10,000 rows |
| Sonar | 208 | Under 10,000 rows |
| Pima Indians Diabetes | 768 | Under 10,000 rows |
| German Credit | 1,000 | Under 10,000 rows |
| Telco Customer Churn | 7,043 | Under 10,000 rows |
| IBM HR Attrition | 1,470 | Under 10,000 rows |
| Covertype | not verified | No downloadable file we could load and count. It would also need a binarisation rule (7 classes). |
| HTRU2 (Pulsar) | not verified | No working download link found, so the row count could not be checked. |
| Give Me Some Credit | not verified | The Kaggle download did not work for the group, so the file could not be loaded and counted. |
| EEG Eye State | 14,980 in the UCI copy we checked; about 4,900 in the copy the group downloaded | The two copies disagree, and we could not settle which is right. Dropped rather than guess. |
| Statlog Shuttle | 14,500 (test file only) | Only a .tst test-split file was reachable, not a single csv with all rows. |
| Chess (King-Rook vs King) | 28,056 | Only available as a .data file with no csv version found. |

- We examined 28 datasets in total. 15 are in the register and 13 were rejected.
- Most common reason: under 10,000 rows (7 of 13).
- Second most common: no downloadable csv we could load and count (5 of 13: Covertype, HTRU2, Give Me Some Credit, Statlog Shuttle, Chess).
- Third: two copies of the same dataset disagreed on row count (1 of 13: EEG Eye State).

## Ambiguity list

1. **Is 'unknown' in Bank Marketing missing data?** Counted as a category, not as missing. poutcome is 81.7% 'unknown', which would fail the 30% rule if counted as missing. A stricter reading would drop that column.
2. **What counts as an identifier column?** Dropped pure row numbers and IDs (e.g. ID in Default of Credit Card Clients). The brief gives no rule for near-unique columns.
3. **Does the 30% rule apply per column or per dataset?** Read as per column, as written. Columns over 30% are dropped, not the whole dataset (Rain in Australia, Diabetes 130).
4. **How to binarise a many-class target?** Chose a split that makes sense for each dataset (vowel/consonant, win/not-win, class A/other). A different choice would change prevalence and difficulty, so it is a research decision.
5. **Can a dataset be used if only part of it is available?** Avila is the training split only (10,430 rows, close to the 10,000 limit). Statlog Shuttle was dropped for this reason.
6. **Which copy of a dataset is the real one?** Row counts were checked on one copy of each file. EEG Eye State showed that two copies can disagree, so the count has to be re-checked on the exact file used.
7. **Do .data and .txt files count as csv?** Connect-4 (.data) and Skin Segmentation (.txt) are plain delimited text, but not named .csv. Kept and flagged.

## Hardest criterion to apply, and why

The hardest rule was checking the row count ourselves. Loading a file and counting is easy once you have the file. The problem was getting a file we could trust. Several datasets (Covertype, HTRU2, Give Me Some Credit) could not be downloaded in a form we could load, so we could not count them and left them out instead of copying a number from a dataset page. EEG Eye State was the clearest example of why the rule exists: one copy had 14,980 rows and another had about 4,900, so a published count alone would have been wrong for one of them. The next hardest was missing data, because 'unknown' in Bank Marketing is not a null but would break the 30% rule if counted as one. Binarising many-class targets (Letter Recognition, Connect-4, Nursery, Avila, Firewall) was also a real choice, since each split gives a different prevalence.
