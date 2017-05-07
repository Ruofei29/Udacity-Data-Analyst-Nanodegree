# P4: Explortary Analysis Prosper Loan Data

## Project Overview
This project analyzed the loan data from Prosper. This data set contains 113,937 loans with 81 variables on each loan, including loan amount, borrower rate (or interest rate), current loan status, borrower income, borrower employment status, borrower credit history, and the latest payment information.

## Report
I used R (mainly ggplot2) to do the explortary analysis for Prosper loan data.
If you want to see R code, please go to [Prosper Loan Data.Rmd](https://github.com/Ruofei29/Udacity-Data-Analyst-Nanodegree/blob/master/P4%20Explortary%20Analysis%20Prosper/Prosper%20Loan%20Data.Rmd)
If you want to see complete report, please go to [Prosper_Loan_Data.html](https://github.com/Ruofei29/Udacity-Data-Analyst-Nanodegree/blob/master/P4%20Explortary%20Analysis%20Prosper/Prosper_Loan_Data.html)

## Reflection
This Prosper Loan Data Analysis is quite challenging since there are more than 80000 rows with 81 variables. My difficulties throughout the analysis includes feature selection, plot selection and data cleaning. I feel very happy to find 17 variables that interest me and their relationship with each other through different kinds of exploration. For example, I found the unusual spike of loan amount, the distribution of listing category and so on and so forth. I also noticed the possible correlation between income range, debt to income ratio, credit score, total inquiries, delinquencies, loan status and Prosper rating. However, this analysis still have a lot of limitations. First, I only consider the loans that listed after July 2009. Second, I only select 17 variables out of 81. There are still a lot to do with other variables. Third, I ignored the NAs during the analysis, which might result in some bias. Moving forward, I will suggest to do the following things:

Include the loan before July 2009 and get a complete view of the dataset
Explore more variables especially those describe the borrowers' characteristics since that will give us more info about how prosper decide an interest rate
Try to figure out why the NA exists and how to deal with them in a more apporiate way
Add more statistics step into the explortary data analysis, it will bring more insights to the dataset.
I really apprecaite this opportunity to explore the Prosper Loan Data and provide my own insights with a variety of plots. Enjoy and keep learning!
