# Dataset Register

5 datasets checked so far. Still working toward the 15+ the assignment asks for.

## Candidate datasets

| Name | Source and URL | Rows | Features | Target and binarisation rule | Class prevalence | Missingness | Licence |
|---|---|---|---|---|---|---|---|
| Adult Income | UCI, mirror: github.com/jbrownlee/Datasets/blob/master/adult-all.csv | 48842 | 14 | Already binary. Income is either <=50K or >50K. | 23.9% earn >50K | workclass 5.7% missing, occupation 5.8% missing, native-country 1.8% missing | CC BY 4.0 |
| Mammography | UCI/KEEL, mirror: github.com/jbrownlee/Datasets/blob/master/mammography.csv | 11183 | 6 | Already binary. 1 means calcification found, -1 means not found. | 2.3% positive | no missing values | Public benchmark dataset, free to use |
| Credit Card Fraud | kaggle.com/datasets/mlg-ulb/creditcardfraud | 284807 | 30 | Already binary. 1 means fraud, 0 means normal transaction. | 0.17% fraud | no missing values | Open Database License (DbCL) v1.0 |
| Bank Marketing | archive.ics.uci.edu/dataset/222/bank+marketing | 45211 | 16 | Already binary. Customer said yes or no to the offer. | 11.7% said yes | no blank cells, but the poutcome column is 81.7% marked unknown | CC BY 4.0 |
| Give Me Some Credit | kaggle.com/c/GiveMeSomeCredit | 150000 | 10 | Already binary. 1 means serious default within 2 years, 0 means no default. | 6.7% defaulted | MonthlyIncome 19.8% missing, NumberOfDependents 2.6% missing | Kaggle competition data, check competition rules before reuse |

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

We looked at 13 datasets total. 5 made it in, 8 didn't.
Main reason for rejecting: too few rows (6 out of 8).
Other reason: couldn't download the file ourselves to check the numbers (2 out of 8).

## Ambiguity list

1. **Bank Marketing has a column that's 81.7% marked "unknown."** Is that missing data or just a normal answer? We counted it as a normal answer (it means "no past contact"), not missing data. Someone else might count it differently.
2. **What counts as a feature vs. an ID column?** We dropped any column that was just a row number or ID, since it has no predictive use.
3. **What to do when the published row count looks right but we can't download the file ourselves?** We left those datasets out instead of trusting the number, since the assignment says to check it ourselves.
4. **Is Kaggle competition data licensed the same way as a normal Kaggle dataset?** We kept Give Me Some Credit in for now but flagged that competition rules are stricter and should be double-checked.

## Hardest rule to follow

The hardest rule was checking the row count ourselves. It's simple once you have the file, but two datasets we wanted (Default of Credit Card Clients and Covertype) couldn't be downloaded in the time we had, so we couldn't open the file and count the rows ourselves. Rather than just use the number from the dataset page, which is exactly what the assignment says not to do, we left both out. The other tricky part was missing data — Bank Marketing has a column that's mostly filled with the word "unknown," and it wasn't obvious if that should count as missing or not.
