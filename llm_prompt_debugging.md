# LLM Prompt Debugging Example

This example shows a simple workflow for diagnosing and improving prompts when working with large language models (LLMs).

## Scenario

A user asks an AI assistant to generate a SQL query.

Prompt:

Write a SQL query to calculate total revenue by department.

The model returns an incorrect query that does not aggregate results correctly.

## Initial Model Output

SELECT department, revenue
FROM transactions;

This query does not calculate totals.

## Investigation

The prompt does not clearly specify that aggregation is required.

The model interpreted the request as simply retrieving data.

## Improved Prompt

Write a SQL query that calculates the total revenue per department using SUM() and GROUP BY.

## Correct Output

SELECT
    department,
    SUM(revenue) AS total_revenue
FROM transactions
GROUP BY department
ORDER BY total_revenue DESC;

## Prompt Debugging Workflow

1. Identify what the user actually needs
2. Examine where the prompt is ambiguous
3. Add clear instructions and constraints
4. Test the prompt again
5. Validate the output

## Key Insight

Many LLM errors are caused by vague prompts rather than model limitations.  
Careful prompt design can significantly improve the quality of results.

## Tools

LLM APIs  
Prompt iteration  
SQL validation
