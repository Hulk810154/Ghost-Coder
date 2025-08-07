import argparse

def generate_function_from_description(description: str) -> str:
    """
    Generates a Python function from a natural language description.
    """
    function_template = '''def my_function():
    """
    {description}
    """
    pass
'''
    return function_template.format(description=description)

def main():
    """
    The main entry point for the CLI tool.
    """
    parser = argparse.ArgumentParser(
        description="Generate a Python function from a description."
    )
    parser.add_argument(
        "description",
        type=str,
        help="The natural language description of the function.",
    )
    args = parser.parse_args()

    generated_code = generate_function_from_description(args.description)
    print(generated_code)

if __name__ == "__main__":
    main()
