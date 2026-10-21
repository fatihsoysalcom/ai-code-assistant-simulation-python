import textwrap

def simulate_ai_assistant(prompt: str, existing_code: str = "") -> str:
    """
    Simulates a basic AI coding assistant based on a given prompt.
    It can generate simple code or suggest refactoring.
    """
    prompt_lower = prompt.lower()
    response = []

    # --- AI-like Code Generation --- 
    # This section demonstrates how an AI assistant might generate code from a natural language request.
    if "generate python function to add two numbers" in prompt_lower:
        response.append("# AI Generated Code: Function to add two numbers")
        response.append(textwrap.dedent("""
            def add_two_numbers(a, b):
                """Adds two numbers and returns the sum."""
                return a + b

            # Example usage:
            # result = add_two_numbers(5, 3)
            # print(f"Sum: {result}") # Output: Sum: 8
        ""))
        return "\n".join(response)

    elif "generate python function to calculate factorial" in prompt_lower:
        response.append("# AI Generated Code: Function to calculate factorial")
        response.append(textwrap.dedent("""
            def factorial(n):
                """Calculates the factorial of a non-negative integer."""
                if not isinstance(n, int) or n < 0:
                    raise ValueError("Input must be a non-negative integer.")
                if n == 0:
                    return 1
                else:
                    return n * factorial(n - 1)

            # Example usage:
            # fact_5 = factorial(5)
            # print(f"Factorial of 5: {fact_5}") # Output: Factorial of 5: 120
        ""))
        return "\n".join(response)

    # --- AI-like Code Refactoring --- 
    # This section simulates an AI suggesting improvements or refactoring for existing code.
    elif "refactor loop to list comprehension" in prompt_lower and existing_code:
        response.append("# AI Suggested Refactoring:")
        response.append("# Original code snippet provided:")
        response.append(textwrap.indent(existing_code, "    "))
        response.append("\n# Refactored using a list comprehension for conciseness and readability:")
        
        # Simple heuristic for refactoring a common loop pattern
        if "for num in numbers:" in existing_code and "squared_numbers.append(num * num)" in existing_code:
            refactored_code = textwrap.dedent("""
                numbers = [1, 2, 3, 4, 5]
                squared_numbers = [num * num for num in numbers]
                # print(f"Squared numbers: {squared_numbers}")
            "")
            response.append(refactored_code)
        elif "for item in my_list:" in existing_code and "new_list.append(item.upper())" in existing_code:
             refactored_code = textwrap.dedent("""
                my_list = ["apple", "banana", "cherry"]
                new_list = [item.upper() for item in my_list]
                # print(f"Uppercase list: {new_list}")
            "")
             response.append(refactored_code)
        else:
            response.append("# (Could not apply specific refactoring based on the provided code snippet.)")
            response.append("# Example of a list comprehension refactoring:")
            response.append(textwrap.dedent("""
                # Original:
                # new_list = []
                # for x in old_list:
                #     if condition(x):
                #         new_list.append(transform(x))
                #
                # Refactored:
                # new_list = [transform(x) for x in old_list if condition(x)]
            ""))
        return "\n".join(response)

    # --- General AI Guidance --- 
    # This demonstrates an AI's ability to provide explanations or answer questions.
    elif "explain list comprehension" in prompt_lower:
        response.append("# AI Explanation:")
        response.append(textwrap.dedent("""
            A list comprehension offers a concise way to create lists.
            It consists of brackets containing an expression followed by a `for` clause,
            then zero or more `for` or `if` clauses.
            The result will be a new list resulting from evaluating the expression
            in the context of the `for` and `if` clauses which follow it.

            Example:
            squares = [x**2 for x in range(10)] # Creates a list of squares from 0 to 9.
            even_numbers = [x for x in range(10) if x % 2 == 0] # Creates a list of even numbers.
        ""))
        return "\n".join(response)

    else:
        response.append("# AI Assistant: I couldn't understand your request fully.")
        response.append("# Try prompts like:")
        response.append("# - 'Generate Python function to add two numbers'")
        response.append("# - 'Generate Python function to calculate factorial'")
        response.append("# - 'Refactor loop to list comprehension' (and provide code)")
        response.append("# - 'Explain list comprehension'")
        return "\n".join(response)

if __name__ == "__main__":
    print("Welcome to the AI Coding Assistant Simulator!")
    print("Type 'exit' to quit.")
    print("-" * 40)

    while True:
        user_prompt = input("\nEnter your request (e.g., 'Generate Python function to add two numbers'):\n> ")
        if user_prompt.lower() == 'exit':
            break

        existing_code_input = ""
        if "refactor" in user_prompt.lower():
            print("\nPlease paste the code you want to refactor (type 'END' on a new line to finish):")
            code_lines = []
            while True:
                line = input()
                if line == 'END':
                    break
                code_lines.append(line)
            existing_code_input = "\n".join(code_lines)

        print("\n" + "=" * 40)
        print("AI Assistant's Response:")
        print("=" * 40)
        ai_response = simulate_ai_assistant(user_prompt, existing_code_input)
        print(ai_response)
        print("=" * 40)

    print("\nThank you for using the AI Coding Assistant Simulator!")
