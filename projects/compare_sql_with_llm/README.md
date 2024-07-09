# SQL Query Comparison Using OpenAI's GPT-3.5-turbo

This project demonstrates how to use OpenAI's GPT-3.5-turbo model to compare SQL queries. 
The results are stored back into an Excel file. 
This approach is useful for automated SQL validation and other text comparison tasks.

## Prerequisites

To run this project, you need:

- Python 3.x
- The `openai` and `pandas` libraries

You can install the required libraries using pip:

pip install openai pandas


Setup
Clone the repository or download the script.
Replace "your-openai-api-key" in the script with your actual OpenAI API key. Make sure to keep your API key secure.


Usage
Prepare your Excel file with the test cases. The file should have three columns: CaseID, ExpectedSQL, and ActualSQL.
Specify the path to your Excel file in the script.
Run the script.
