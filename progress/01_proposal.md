# Project Proposal: Evaluating Financial Data

## AI Usage
### AI Generated Ideas:
1. Stock Return Direction Classifier
Can financial inicators detect whether a stock will be up or down in n days?
2. Detecting Anomalies in the Market
Can abnormal market behavior be detected during stress periods?
3. Portfolio Risk and Diversification Analysis
How do correlations between assets shift during market stress?


### AI Influence on Deciscion Making
Using AI, I transformed very general, non-specific project ideas into a project idea that was both specific and realistic. 
I also very quickly got an estimate of how realistic each project is, what tools I would need, and how long it might take 
to complete this project. Based on several prompts with AI, I elected to go with idea 2. I will apply supervised machine learning
methods to predict whether the market is at risk of crisis or whether its behavior is normal.

### AI Excerpt
Prompt: This project needs to have a practical application and also still be realistic with the resources I have available.
Response: "The durable, unsexy uses — fraud detection, credit risk, volatility modeling, compliance — are where ML creates the most consistent value, and where a well-executed project is most credible.
This is part of why anomaly detection or volatility forecasting makes for a stronger project than return prediction — you're solving problems the industry actually relies on ML for. Want to lock in a direction and start building?"

### Project Specs
### Research Question
Using market data provided on yfinance and labeling the market as either being in crisis (1), or behaving normally (0) in the last 20 years, can machine learning methods reliably predict whether the market is experiencing an anomoly?

### Target Variable
Market Volatility, with labels: Crisis = 1, and Normal = 0

### Dataset
**Primary Dataset:** yfinance
**Secondary/Backup Data:** Federal Reserve Economic Data

### Feasibility
**Time:** I expect this project to range from 15-25 hours in total. This should be manageable with about 4-7 hours of work each week.
**Compute:** Compute needs for this project will certainly be met. I will using Random Forest, Logistic Regression and Gradient Boosting.
**Scope:** I will use one dataset (maybe two), 3 supervised ML methods, an additional ML method, feature importance and SHAP will be used to explain model behavior, the project will be reproducible, and a demo will be done in a jupiter noteboook.

### Ethical/Legal Considerations
YFinance is a publicly available dataset, intended for personal use. Since I am not using the data in a commercial framework, I am not an any violation of their terms. The only ethical consideration is ensuring that the data is handled properly and that the labels are created to my best ability and not in a way that will intentionally manipulate my results.

### ML Methods
**Main ML Methods:**
1. Logistic Regression
2. Random Forest
3. Gradient Boosting

**Additional ML Method:**
Isolation Forest