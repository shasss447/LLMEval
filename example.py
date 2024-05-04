# example.py
from LLMEval.eval import Eval, TestCases, parse_dataset,get_test_cases

def main():
    # Instantiate Eval class
    llm_eval = Eval(endpoint_url="http://llm-endpoint.com")

    # Define test cases to evaluate
    test_cases = [TestCases.Fairness, TestCases.Bias, TestCases.Hallucinations]

    # Load dataset
    dataset_file = "dataset.csv"
    dataset = parse_dataset(dataset_file)
    #Get test cases
    test_cases = get_test_cases()
    # Run evaluations
    evaluation_results = eval.scan(dataset, test_cases)

    # Print results
    for question, results in evaluation_results.items():
        print(f"Question: {question}")
        for test_case, result in results.items():
            print(f"{test_case}: {result}")

if __name__ == "__main__":
    main()
