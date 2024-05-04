# LLMEval

LLMEval is a Python library for interacting with a given Large Language Model (LLM) endpoint to perform predefined evaluations for fairness, bias, and hallucinations. This library provides easy-to-use functionalities for testing these aspects using a provided dataset.

## Installation
you can clone this repository:
```bash
git clone https://github.com/shasss447/LLMEval.git
```
-------------

## Documentation
### Eval Class

The `Eval` class handles the interaction with the LM endpoint. It includes the following methods:

*   `__init__(self, endpoint_url)`: Initializes the Eval object with the specified LLM endpoint URL.
*   `scan(self, dataset, test_cases)`: Performs evaluations on the provided dataset based on the specified test cases.
*   `send_request(self, question)`: Sends a request to the LLM endpoint with the given question.
*   `parse_response(self, response, test_cases)`: Parses the response from the LLM endpoint based on the specified test cases.

### TestCases Enumeration

The `TestCases` enumeration defines the types of evaluations available: Fairness, Bias, and Hallucinations.

### parse_dataset Function

The `parse_dataset` function parses the dataset from a CSV file with columns for 'question', 'answer', and 'context'.

### get_test_cases Function

The `get_test_cases` function allows users to input test cases interactively.
