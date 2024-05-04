import csv
import requests
from enum import Enum

class Eval:
    #constructor to initialize the endpoint url
    def __init__(self, endpoint_url):
        self.endpoint_url = endpoint_url
        """
        Initialize Eval object with the specified LLM endpoint URL.
        
        Args:
        - endpoint_url (str): The URL of the LLM endpoint.
        """
    #function to scan the dataset and return hardcoded results
    def scan(self, dataset, test_cases):
        """
        Perform evaluations on the provided dataset based on the specified test cases.
        
        Args:
        - dataset (list of dicts): The dataset containing questions, answers, and contexts.
        - test_cases (list of TestCases): The list of test cases to evaluate.
        
        Returns:
        - results (dict): A dictionary containing evaluation results for each question.
        """
        results = {} #dictionary to store results
        for case in dataset:
            question = case['question']
            response = self.send_request(question) #send request to the endpoint
            if response:
                parsed_data = self.parse_response(response, test_cases)
                results[question] = parsed_data
            else:
                results[question] = "Failed to get response from the endpoint"
        return results
    
    #function to send request to the endpoint
    def send_request(self, question):
        """
        Send a request to the LLM endpoint with the given question.
        
        Args:
        - question (str): The question to send to the endpoint.
        
        Returns:
        - response (dict or None): The response from the endpoint as a dictionary, or None if the request fails.
        """
        try:
            response = requests.post(self.endpoint_url, json={"question": question})
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except Exception as e:
            print(f"Error sending request: {e}")
            return None
    
    #function to parse the response and return hardcoded parsed data
    def parse_response(self, response, test_cases):
        """
        Parse the response from the LLM endpoint based on the specified test cases.
        
        Args:
        - response (dict): The response from the LLM endpoint.
        - test_cases (list of TestCases): The list of test cases to parse.
        
        Returns:
        - parsed_data (dict): A dictionary containing parsed evaluation results based on the test cases.
        """
        parsed_data = {} #dictionary to store parsed data
        for test_case in test_cases:
            if test_case == TestCases.Fairness:
                parsed_data['Fairness'] = "Fairness evaluation result:value" #hardcoded fairness value
            elif test_case == TestCases.Bias:
                parsed_data['Bias'] = "Bias evaluation result:value" #hardcoded bias value
            elif test_case == TestCases.Hallucinations:
                parsed_data['Hallucinations'] = "Hallucinations evaluation result:value" #hardcoded hallucinations value
        return parsed_data

# Enum class to define test cases
class TestCases(Enum):
    Fairness = 1
    Bias = 2
    Hallucinations = 3

#function to parse the dataset
def parse_dataset(dataset_file):
    """
    Parse the dataset from a CSV file.
    
    Args:
    - dataset_file (str): The path to the CSV file containing the dataset.
    
    Returns:
    - dataset (list of dicts): The parsed dataset containing questions, answers, and contexts.
    """
    dataset = [] #list to store dataset
    with open(dataset_file, 'r', newline='', encoding='utf-8') as csvfile: #open the dataset file 
        reader = csv.DictReader(csvfile) #create a csv reader
        for row in reader:
            dataset.append(row)
    return dataset 

#function to get test cases from the user
def get_test_cases():
    """
    Get test cases from user input.
    
    Returns:
    - test_cases (list of TestCases): The list of test cases selected by the user.
    """
    test_cases = [] #list to store test cases
    while True:
        print("Enter test case (1: Fairness, 2: Bias, 3: Hallucinations), or enter 'done' to finish:")
        choice = input().strip()
        if choice == '1':
            test_cases.append(TestCases.Fairness)
        elif choice == '2':
            test_cases.append(TestCases.Bias)
        elif choice == '3':
            test_cases.append(TestCases.Hallucinations)
        elif not choice.strip():
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 'done'.")
    return test_cases #return test cases