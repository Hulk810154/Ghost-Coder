import argparse
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_function_name(doc) -> str:
    """
    Extracts a function name from a spaCy doc.
    """
    verb = None
    dobj = None
    for token in doc:
        if token.pos_ == "VERB" and verb is None:
            verb = token
            for child in token.children:
                if child.dep_ == "dobj":
                    dobj = child
                    break  # assume first dobj

    if verb:
        if dobj and dobj.pos_ == "NOUN":
            return f"{verb.lemma_}_{dobj.lemma_}"
        else:
            return verb.lemma_

    return "my_function"

def extract_arguments(doc, function_name) -> list[str]:
    """
    Extracts function arguments from a spaCy doc.
    """
    args = []
    for token in doc:
        # Arguments can be direct objects or objects of prepositions
        if token.dep_ in ["dobj", "pobj"]:
            if token.pos_ in ["NOUN", "PROPN", "PRON"]:
                # Avoid including parts of the function name as arguments
                if token.lemma_ not in function_name:
                    args.append(token.lemma_)
        # Check for conjunctions (e.g., "x and y")
        if token.dep_ == "conj" and token.head.dep_ in ["dobj", "pobj"]:
             if token.lemma_ not in function_name:
                    args.append(token.lemma_)

    # A simple rule for variable names like 'x' or 'y'
    for token in doc:
        if (token.pos_ in ["NOUN", "PROPN", "PRON"]) and token.is_alpha and len(token.text) == 1:
            if token.lemma_ not in args:
                args.append(token.lemma_)

    # Remove duplicates and return
    return list(dict.fromkeys(args))

def generate_body(doc, args: list[str]) -> str:
    """
    Generates the function body based on keywords in the description.
    """
    lemmas = [token.lemma_ for token in doc]
    if "add" in lemmas or "sum" in lemmas:
        if len(args) >= 2:
            return f"    return {args[0]} + {args[1]}"
    if "subtract" in lemmas or "difference" in lemmas:
        if len(args) >= 2:
            return f"    return {args[0]} - {args[1]}"
    if "multiply" in lemmas or "product" in lemmas:
        if len(args) >= 2:
            return f"    return {args[0]} * {args[1]}"
    if "divide" in lemmas or "quotient" in lemmas:
        if len(args) >= 2:
            return f"    return {args[0]} / {args[1]}"
    return "    pass"

def generate_function_from_description(description: str) -> str:
    """
    Generates a Python function from a natural language description.
    """
    doc = nlp(description)
    function_name = extract_function_name(doc)
    arguments = extract_arguments(doc, function_name)
    args_string = ", ".join(arguments)
    body = generate_body(doc, arguments)

    function_template = '''def {function_name}({args_string}):
    """
    {description}
    """
{body}
'''
    return function_template.format(
        function_name=function_name,
        args_string=args_string,
        description=description,
        body=body
    )

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
