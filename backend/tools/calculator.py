def calculate(expression: str):
    """
    Safely evaluate basic mathematical expressions.
    """

    allowed_characters = "0123456789+-*/(). "

    if not all(
        character in allowed_characters
        for character in expression
    ):
        return "Invalid mathematical expression."

    try:
        result = eval(expression, {"__builtins__": {}})

        return str(result)

    except Exception:
        return "Could not calculate the expression." 