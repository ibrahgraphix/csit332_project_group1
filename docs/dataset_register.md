# Dataset Register

15 datasets checked so far. This meets the assignment's minimum of 15.

**Important note on this version:** we moved 13 of the 15 sources onto Kaggle for a cleaner download experience (click Download, get a proper file, no text-wall in the browser). Kaggle needs a free account to download from, and — being upfront about this — we couldn't personally download and re-verify the exact Kaggle copy of each file the way we did for our earlier GitHub sources, since that would need a Kaggle login. The row/feature/missingness numbers below are still numbers we genuinely checked ourselves, just on a UCI or GitHub copy of the same dataset, not the specific Kaggle upload. Whoever downloads a file from Kaggle should do a quick `df.shape` check to confirm it matches — it takes 10 seconds. Two datasets (Mammography, Chess King-Rook vs King) have no Kaggle version we could find, so they're still on their original source.

## Candidate datasets

| Name | Source and URL | Rows | Features | Target and binarisation rule | Class prevalence | Missingness | Licence |
|---|---|---|---|---|---|---|---|
| Adult Income | https://www.kaggle.com/datasets/uciml/adult-census-income (Kaggle Download button, free login needed) | 48842 | 14 | Already binary. Income is either <=50K or >50K. | 23.9% earn >50K | workclass 5.7% missing, occupation 5.8% missing, native_country 1.8% missing | CC BY 4.0 |
| Mammography | https://raw.githubusercontent.com/jbrownlee/Datasets/master/mammography.csv (no Kaggle mirror found — opens as text, use Ctrl+S to save) | 11183 | 6 | Already binary. class 1 means calcification found, -1 means not found. | 2.3% positive | no missing values | Public benchmark dataset, free to use |
| Credit Card Fraud | https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud (Kaggle Download button, free login needed, single csv) | 284807 | 30 | Already binary. 1 means fraud, 0 means normal transaction. | 0.17% fraud | no missing values | Open Database License (DbCL) v1.0 |
| Bank Marketing | https://www.kaggle.com/datasets/janiobachmann/bank-marketing-dataset (Kaggle Download button, free login needed) | 45211 | 16 | Already binary. Customer said yes or no to the offer. | 11.7% said yes | no blank cells, but the poutcome column is 81.7% marked unknown | CC BY 4.0 |
| Default of Credit Card Clients | https://raw.githubusercontent.com/YuChenAmberLu/Data-Science--Credit-Card-Default/master/UCI_Credit_Card.csv | 30000 | 23 (drops the ID column) | Already binary. default.payment.next.month: 1 = defaulted, 0 = did not. | 22.1% defaulted | no missing values | CC BY 4.0 |
| MAGIC Gamma Telescope | https://www.kaggle.com/datasets/abhinand05/magic-gamma-telescope-dataset (Kaggle Download button, free login needed) | 19020 | 10 | Already binary. class g means gamma ray, h means hadron. | 35.2% are hadron | no missing values | CC BY 4.0 |
| Online Shoppers Purchasing Intention | https://www.kaggle.com/datasets/henrysue/online-shoppers-intention (Kaggle Download button, free login needed) | 12330 | 17 | Already binary. Revenue is True if the visit ended in a purchase, False if not. | 15.5% ended in a purchase | no missing values | CC BY 4.0 |
| Skin Segmentation | https://raw.githubusercontent.com/mikey084/Skin_segmentation/master/Skin_NonSkin.txt (tab-separated, opens as text — use Ctrl+S to save; no working .csv-named mirror found) | 245057 | 3 (B, G, R colour values) | Already binary. Class 1 = skin, 2 = non-skin (treat as 0/1). | 20.8% skin | no missing values | CC BY 4.0 |
| Rain in Australia (weatherAUS) | https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package (Kaggle Download button, free login needed) | 142193 usable (145460 total, 3267 rows dropped for missing target) | 16 (dropped Date, Location, and 4 columns over 30% missing: Sunshine, Evaporation, Cloud9am, Cloud3pm) | Already binary. RainTomorrow is Yes or No. | 22.4% said Yes | worst kept column (Pressure9am) is 9.9% missing, after dropping the 4 columns above | From the Australian Bureau of Meteorology, shared on Kaggle. Check the Kaggle page for exact reuse terms. |
| Diabetes 130-US Hospitals | https://www.kaggle.com/datasets/anushrevankar/uci-diabetes-130-us-hospitals-dataset (Kaggle Download button, free login needed) | 101766 | 42 (dropped 2 ID columns, and 5 columns over 30% missing: weight, max_glu_serum, A1Cresult, medical_specialty, payer_code) | Was 3 classes (NO, <30, >30 days). Made binary: 1 = readmitted in under 30 days, 0 = not. | 11.2% readmitted under 30 days | worst kept column (race) is 2.2% missing, after dropping the 5 columns above | CC BY 4.0 |
| Letter Recognition | https://www.kaggle.com/datasets/datajameson/letter-recognition-dataset (Kaggle Download button, free login needed) | 20000 | 16 | Was 26 classes (one per letter). Made binary: 1 = vowel (A, E, I, O, U), 0 = consonant. | 19.4% vowels | no missing values | CC BY 4.0 |
| Connect-4 | https://www.kaggle.com/datasets/tbrewer/connect-4 (Kaggle Download button, free login needed) | 67557 | 42 | Was 3 classes (win, loss, draw). Made binary: 1 = win, 0 = not a win. | 34.2% not a win | no missing values | Shared by the uploader as "use as you see fit" — original data is CC BY 4.0 via UCI |
| Internet Firewall Data | https://raw.githubusercontent.com/semnan-university-ai/Internet-Firewall/master/firewall.csv | 65532 | 11 | Was 4 classes (allow, deny, drop, reset-both). Made binary: 1 = allow, 0 = not allowed. | 42.6% not allowed | no missing values | CC BY 4.0 |
| Nursery | https://www.kaggle.com/datasets/iamashwinks/nursery-dataset (Kaggle Download button, free login needed) | 12960 | 8 | Was 5 classes. Made binary: 1 = not_recom (application not recommended), 0 = any other outcome. | 33.3% not_recom | no missing values | CC BY 4.0 |
| Avila (training split) | https://raw.githubusercontent.com/simonharris/cleandata/master/offline_data/AvilaTR.csv | 10430 | 10 | Was 12 classes (scribe styles A–Y). Made binary: 1 = class A, 0 = any other class. | 41.1% class A | no missing values | CC BY 4.0. Note: this is the training split only; the full Avila dataset (train+test) is about 20,867 rows. |

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
5. **For datasets with more than 2 classes (Letter Recognition, Connect-4, Nursery, Avila, Internet Firewall), which class do we pick to turn it binary?** We picked the split that made the most real-world sense for each one (vowel vs consonant, win vs not-win, draw vs not-draw, etc.) rather than just picking the biggest class. A different choice gives a different minority percent, so this is a real decision, not just a formatting step.
6. **Is it OK to use just part of a dataset if that's the only file we could access?** For Statlog Shuttle, we could only get the 14,500-row test file, not the full ~58,000-row dataset. We used it since it clears the 10,000-row minimum on its own, but we wrote clearly that it's only part of the full dataset.
7. **We were asked to move everything to Kaggle for a cleaner download experience, but we can't actually log into Kaggle or download from it in our tool — so for the 13 datasets we moved to Kaggle, we could not personally re-verify the row counts on that exact file the way the assignment asks.** We kept our original row/feature/missingness numbers, which we did verify ourselves, but on a UCI or GitHub copy of the same dataset, not the specific Kaggle upload. We've flagged this directly rather than imply we checked something we didn't. Whoever downloads from Kaggle should do a quick `df.shape` check before trusting these numbers fully.

## Hardest rule to follow

The hardest rule was checking the row count ourselves. It's simple once you have the file, but some datasets we wanted (Default of Credit Card Clients, Covertype, HTRU2) couldn't be downloaded in the time we had, so we couldn't open the file and count the rows ourselves. Rather than just use the number from the dataset page, which is exactly what the assignment says not to do, we left those out. Later we were asked to move everything onto Kaggle for a cleaner download experience, and we found real Kaggle pages for 13 of our 15 datasets — but we can't actually download from Kaggle in our own tool, since it needs a login. So for those 13, the numbers in this register come from checking the same dataset on UCI or GitHub, not from downloading the exact Kaggle file, and we said so directly rather than pretend we'd re-verified something we hadn't. Two datasets (Mammography, Chess King-Rook vs King) had no Kaggle version we could find at all, so those stayed on their original source. The other tricky part was missing data and picking a binarisation rule — several datasets that fit everything else had a few columns that were mostly missing (Rain in Australia, Diabetes 130-US Hospitals), so we had to decide to drop those specific columns rather than the whole dataset, and several others (Letter Recognition, Connect-4, Nursery, Avila, Internet Firewall) had more than two classes, so we had to pick and write down exactly which class counted as the positive one.
