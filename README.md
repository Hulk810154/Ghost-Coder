# Code Generator

This project is a CLI tool that uses Natural Language Processing (NLP) to generate Python functions from natural language descriptions.

## Features

*   **Intelligent Function Name Extraction**: Automatically generates a meaningful function name from the description.
*   **Argument Extraction**: Identifies function arguments from the description.
*   **Basic Body Generation**: Generates the function body for simple arithmetic operations.

## Installation

To install the tool, clone the repository and then install it using pip:

```bash
git clone https://github.com/example/code-generator.git
cd code-generator
pip install -r requirements.txt
python3 -m spacy download en_core_web_sm
pip install .
```

## Usage

To use the tool, run it from the command line with a description of the function you want to create.

### Example 1: Add two numbers

```bash
codegenerator "a function to calculate the sum of x and y"
```

Output:
```python
def calculate_sum(x, y):
    """
    a function to calculate the sum of x and y
    """
    return x + y
```

### Example 2: Find the difference

```bash
codegenerator "a function to find the difference between a and b"
```

Output:
```python
def find_difference(a, b):
    """
    a function to find the difference between a and b
    """
    return a - b
```
