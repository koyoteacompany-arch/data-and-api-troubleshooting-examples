# AI-Assisted Data Investigation

This example demonstrates how SQL queries and AI tools can be used together to investigate reporting discrepancies in a dataset.

## Scenario

A reporting dashboard shows a mismatch between transaction totals and departmental summaries.

Goal: Identify where the discrepancy occurs.

## Step 1 – Pull transaction data

SELECT
    department,
    SUM(amount) AS total_spend
FROM transactions
GROUP BY department
ORDER BY total_spend DESC;

## Step 2 – Check for missing joins

SELECT
    t.transaction_id,
    a.account_name
FROM transactions t
LEFT JOIN accounts a
ON t.account_id = a.account_id
WHERE a.account_id IS NULL;

This query identifies transactions that are not mapped to accounts.

## Step 3 – Investigate data anomalies

SELECT
    transaction_id,
    amount
FROM transactions
WHERE amount < 0;

Negative values may indicate refunds or incorrect data entries.

## Workflow

1. Use SQL to isolate the data issue.
2. Use AI tools to summarize patterns and explain anomalies.
3. Validate results with stakeholders before correcting the dataset.

This approach helps combine traditional data analysis with AI-assisted investigation workflows.
