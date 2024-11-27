import pandas as pd
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="mistral-nemo", num_ctx=32000)

file_path = 'RISK_DATA_ONLY_RISK.xlsx'
riskdata = pd.read_excel(file_path, sheet_name="Risks (2)")
mitigationdata = pd.read_excel(file_path, sheet_name="Mitigations")

# Filter risks that have successful cost, probability, and criticality
riskdata = riskdata[(riskdata['Cost_Success'] == 1) &
                    (riskdata['Probability_Success'] == 1) &
                    (riskdata['Criticality_Success'] == 1)]

# Rename columns for better understanding
riskdata.rename(columns={'Risk_ID': 'Risk_ID_Risk'}, inplace=True)
mitigationdata.rename(columns={'Risk_ID': 'Risk_ID_Mit'}, inplace=True)

# Join mitigation data with risk data based on Risk_ID
riskdata['Mit_Action_Description'] = riskdata.apply(lambda row: mitigationdata[mitigationdata['Risk_ID_Mit'] == row['Risk_ID_Risk']]['Mit_Action_Description'].values[0] if (row['Project_ID'], row['Risk_ID_Risk']) in list(mitigationdata.set_index(['Project_ID', 'Risk_ID_Mit']).index) else None, axis=1)

# Extract relevant columns for mitigation actions
comments = riskdata[['Project_ID', 'Risk_ID_Risk', 'Mit_Action_Description']]

# Create a list of unique mitigation actions
comments_list = []
for index, row in comments.iterrows():
    if row['Mit_Action_Description'] is not None:
        if row['Mit_Action_Description'] not in comments_list:
            comments_list.append(row['Mit_Action_Description'])

# Join mitigation actions into a single string with newline characters
s = "\n".join(comments_list)

# Define the query to ask Ollama for insights on successful mitigation actions
query = f"""
For the following mitigation actions of successful projects, please provide some insight into why these could be successful, is there a common theme?

Here are the mitigation actions:
{s}
"""

# Invoke Ollama with the query and print the response
print(llm.invoke(query))
