# Dataset Register

15 datasets checked so far. This meets the assignment's minimum of 15.

Every link below is a real, working download, not just a link to a repo page. For datasets hosted on UCI, we use UCI's own official "Download" button link, which saves a `.zip` file straight to your computer when you click it. For the two Kaggle datasets, use the Download button on the Kaggle page (needs a free Kaggle login). Mammography is the one exception — it doesn't have an official zip anywhere, so you'll need to use Ctrl+S (or right-click > Save Link As) to save it, since clicking it just shows the text in your browser.

## Candidate datasets

| Name | Source and URL | Rows | Features | Target and binarisation rule | Class prevalence | Missingness | Licence |
|---|---|---|---|---|---|---|---|
| Adult Income | https://archive.ics.uci.edu/static/public/2/adult.zip (click to download directly) | 48842 | 14 | Already binary. Income is either <=50K or >50K. | 23.9% earn >50K | workclass 5.7% missing, occupation 5.8% missing, native_country 1.8% missing | CC BY 4.0 |
| Mammography | https://raw.githubusercontent.com/jbrownlee/Datasets/master/mammography.csv (opens as text in browser — use Ctrl+S / Save Page As to save it, or right-click the link and choose Save Link As) | 11183 | 6 | Already binary. class 1 means calcification found, -1 means not found. | 2.3% positive | no missing values | Public benchmark dataset, free to use |
| Credit Card Fraud | https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud (click the Download button on the page — needs a free Kaggle account) | 284807 | 30 | Already binary. 1 means fraud, 0 means normal transaction. | 0.17% fraud | no missing values | Open Database License (DbCL) v1.0 |
| Bank Marketing | https://archive.ics.uci.edu/static/public/222/bank+marketing.zip (click to download directly) | 45211 | 16 | Already binary. Customer said yes or no to the offer. | 11.7% said yes | no blank cells, but the poutcome column is 81.7% marked unknown | CC BY 4.0 |
| Give Me Some Credit | https://www.kaggle.com/c/GiveMeSomeCredit/data (click the Download button on the page — needs a free Kaggle account) | 150000 | 10 | Already binary. 1 means serious default within 2 years, 0 means no default. | 6.7% defaulted | MonthlyIncome 19.8% missing, NumberOfDependents 2.6% missing | Kaggle competition data, check competition rules before reuse |
| MAGIC Gamma Telescope | https://archive.ics.uci.edu/static/public/159/magic+gamma+telescope.zip (click to download directly) | 19020 | 10 | Already binary. class g means gamma ray, h means hadron. | 35.2% are hadron | no missing values | CC BY 4.0 |
| Online Shoppers Purchasing Intention | https://archive.ics.uci.edu/static/public/468/online+shoppers+purchasing+intention+dataset.zip (click to download directly) | 12330 | 17 | Already binary. Revenue is True if the visit ended in a purchase, False if not. | 15.5% ended in a purchase | no missing values | CC BY 4.0 |
| EEG Eye State | https://archive.ics.uci.edu/static/public/264/eeg+eye+state.zip (click to download directly) | 14980 | 14 | Already binary. 1 means eyes closed, 2 means eyes open (treated as 0/1). | 44.9% eyes open | no missing values | CC BY 4.0 |
| Rain in Australia (weatherAUS) | https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package (click the Download button on the page — needs a free Kaggle account) | 142193 usable (145460 total, 3267 rows dropped for missing target) | 16 (dropped Date, Location, and 4 columns over 30% missing: Sunshine, Evaporation, Cloud9am, Cloud3pm) | Already binary. RainTomorrow is Yes or No. | 22.4% said Yes | worst kept column (Pressure9am) is 9.9% missing, after dropping the 4 columns above | From the Australian Bureau of Meteorology, shared on Kaggle. Check the Kaggle page for exact reuse terms. |
| Diabetes 130-US Hospitals | https://archive.ics.uci.edu/static/public/296/diabetes+130-us+hospitals+for+years+1999-2008.zip (click to download directly) | 101766 | 42 (dropped 2 ID columns, and 5 columns over 30% missing: weight, max_glu_serum, A1Cresult, medical_specialty, payer_code) | Was 3 classes (NO, <30, >30 days). Made binary: 1 = readmitted in under 30 days, 0 = not. | 11.2% readmitted under 30 days | worst kept column (race) is 2.2% missing, after dropping the 5 columns above | CC BY 4.0 |
| Letter Recognition | https://archive.ics.uci.edu/static/public/59/letter+recognition.zip (click to download directly) | 20000 | 16 | Was 26 classes (one per letter). Made binary: 1 = vowel (A, E, I, O, U), 0 = consonant. | 19.4% vowels | no missing values | CC BY 4.0 |
| Connect-4 | https://archive.ics.uci.edu/static/public/26/connect+4.zip (click to download directly) | 67557 | 42 | Was 3 classes (win, loss, draw). Made binary: 1 = win, 0 = not a win. | 34.2% not a win | no missing values | CC BY 4.0 |
| Statlog Shuttle (test split) | https://archive.ics.uci.edu/static/public/148/statlog+shuttle.zip (click to download directly — zip has both train and test files, we only checked the test file) | 14500 | 9 | Was 7 classes. Made binary: 1 = class 1 "Rad Flow", 0 = any other class. | 20.8% not class 1 | no missing values | CC BY 4.0. Note: we only checked the numbers for the 14,500-row test file inside the zip, not the full ~58,000-row training file. |
| Nursery | https://archive.ics.uci.edu/static/public/76/nursery.zip (click to download directly) | 12960 | 8 | Was 5 classes. Made binary: 1 = not_recom (application not recommended), 0 = any other outcome. | 33.3% not_recom | no missing values | CC BY 4.0 |
| Chess (King-Rook vs King) | https://archive.ics.uci.edu/static/public/22/chess+king+rook+vs+king.zip (click to download directly) | 28056 | 6 | Was 18 classes (draw, or number of moves to win). Made binary: 1 = draw, 0 = White wins in some number of moves. | 10.0% draw | no missing values | CC BY 4.0 |

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
7. **Our GitHub raw links pointed at the right file, but clicking them just opens a wall of text in the browser instead of downloading anything — that's how GitHub serves raw files, not a broken link.** For every dataset that lives on UCI, we switched to UCI's own official Download button link (a .zip file that actually downloads when clicked). For the two that only exist on Kaggle, we pointed to the page's Download button (needs a free Kaggle login, but that's a real download, not a text dump). Mammography doesn't have an official zip anywhere, so we kept the GitHub link but wrote in the register that you need to use Ctrl+S or Save Link As to save it, since simply clicking it just displays the text.

## Hardest rule to follow

The hardest rule was checking the row count ourselves. It's simple once you have the file, but some datasets we wanted (Default of Credit Card Clients, Covertype, HTRU2) couldn't be downloaded in the time we had, so we couldn't open the file and count the rows ourselves. Rather than just use the number from the dataset page, which is exactly what the assignment says not to do, we left those out. We also had a link problem partway through: several of our links technically worked but just opened as a wall of text in the browser instead of downloading anything, since that's how GitHub serves raw files. We fixed this by switching every UCI-hosted dataset to UCI's own official Download button link, which actually saves a file, and by pointing the two Kaggle datasets at their page's Download button instead. The other tricky part was missing data and picking a binarisation rule — several datasets that fit everything else had a few columns that were mostly missing (Rain in Australia, Diabetes 130-US Hospitals), so we had to decide to drop those specific columns rather than the whole dataset, and several others (Letter Recognition, Connect-4, Nursery, Chess, Shuttle) had more than two classes, so we had to pick and write down exactly which class counted as the positive one.
