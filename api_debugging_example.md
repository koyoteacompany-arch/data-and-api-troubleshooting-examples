# API Debugging Example

This example shows a common troubleshooting scenario when working with API requests in SaaS platforms.

## Scenario

A POST request to an API endpoint returns an error when triggered from a workflow automation tool.

Endpoint:
POST /api/users

Headers:
Content-Type: application/json

Request body:

{
  "userId": 12345,
  "domain": "acme.com,
  "includeInactive": true,
}

The request returns a generic error.

## Investigation

Step 1: Validate JSON structure

Issues identified:
- Missing quote in the domain field
- Trailing comma after the final property

Incorrect JSON:

{
  "userId": 12345,
  "domain": "acme.com,
  "includeInactive": true,
}

Correct JSON:

{
  "userId": 12345,
  "domain": "acme.com",
  "includeInactive": true
}

## Troubleshooting Workflow

1. Check request format
2. Validate JSON structure
3. Confirm required headers
4. Review API documentation
5. Test the request using Postman or curl
6. Verify response codes and logs

## Outcome

After correcting the JSON formatting issues, the API request returns a successful response (200 OK) and the workflow executes as expected.
