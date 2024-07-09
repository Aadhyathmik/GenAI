import pandas as pd
import openai
import json

def compare_sql_with_llm(caseid: str, expected_sql: str, actual_sql: str) -> str:
    sql_compare_system_prompt = 'Compare the two SQLs and determine whether the SQLs are the same or not. If the SQLs are the same the result should be PASS. If the SQLs are not same the result should be FAIL. Also provide a description on how the SQLs differ. The output format should be in well-defined JSON. It has 3 key value pairs. Result: PASS/FAIL. Description : DESCRIPTION ON HOW the SQLs DIFFER. RunTime : Time it took to compare in milliseconds.'
    sql_compare_user_prompt = 'Compare and Evaluate the SQLs. First SQL is: '

    # OpenAI API Key - Add your OpenAI API Key
    openai_api_key = "your open_api_key"
    
    # Call LLM and ask it to compare and give a pass/fail grade
    sql_compare_user_prompt += expected_sql
    sql_compare_user_prompt += ' The next SQL is: ' + actual_sql

    client = openai.Client(api_key=openai_api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": sql_compare_user_prompt},
            {"role": "system", "content": sql_compare_system_prompt},
        ],
        temperature=1,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    #msg = response.choices[0].message['content']
    msg = response.choices[0].message.content
    #return msg
    result_json = json.loads(msg)
    print(result_json)
    return result_json


def main():

# Specify the path to your Excel file
    file_path = '/path/to/your/sql_test_cases.xlsx'

    # Read the Excel file
    df = pd.read_excel(file_path)

    # Verify the content by displaying the first few rows
    print("First few rows of the DataFrame:")
    print(df.head())

    column1 = df.iloc[:, 0]  # First column
    column2 = df.iloc[:, 1]  # Second column
    column3 = df.iloc[:, 2]  # Third column
    df['LLM_Result'] = ""
    df['LLM_Description'] = ""
    df['LLM_Runtime'] = ""

    # Print values from all 3 columns in a loop and update the DataFrame
    print("\nValues from all three columns and LLM results:")
    for i, (val1, val2, val3) in enumerate(zip(column1, column2, column3)):
        llm_result = compare_sql_with_llm(val1, val2, val3)
        df.at[i, 'LLM_Result'] = llm_result.get('Result', 'N/A')
        df.at[i, 'LLM_Description'] = llm_result.get('Description', 'N/A')
        df.at[i, 'LLM_Runtime'] = llm_result.get('RunTime', 'N/A')
        print(f"Runtime for case {val1}: {df.at[i, 'LLM_Runtime']} seconds")
        print(f"Column1: {val1}, Column2: {val2}, Column3: {val3}, LLM_Result: {df.at[i, 'LLM_Result']}, LLM_Description: {df.at[i, 'LLM_Description']}, Runtime: {df.at[i, 'LLM_Runtime']}")

    # Save the updated DataFrame back to the Excel file
    df.to_excel(file_path, index=False)

if __name__ == "__main__":
    main()
