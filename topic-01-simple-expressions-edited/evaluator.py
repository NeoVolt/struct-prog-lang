import parser, tokenizer

def evaluate(ast):
    if ast["tag"] == "number":
        return ast["value"]
    elif ast["tag"] == "+":
        return evaluate(ast["left"]) + evaluate(ast["right"])
    elif ast["tag"] == "-":
        return evaluate(ast["left"]) - evaluate(ast["right"])
    elif ast["tag"] == "*":
        return evaluate(ast["left"]) * evaluate(ast["right"])
    elif ast["tag"] == "/":
        return evaluate(ast["left"]) / evaluate(ast["right"])
    elif ast["tag"] == "%":
        # default modulus should support negative numbers correctly.
        # apparently there's like 3 different ways to evaluate it anyways, 
        # this one uses the floor method 
        return evaluate(ast["left"]) % evaluate(ast["right"]) 
    else:
        raise ValueError(f"Unknown AST node: {ast}")

def test_evaluate():
    print("test evaluate()")
    ast = {"tag": "number", "value": 3}
    assert evaluate(ast) == 3
    ast = {
        "tag": "+",
        "left": {"tag": "number", "value": 3},
        "right": {"tag": "number", "value": 4},
    }
    assert evaluate(ast) == 7
    ast = {
        "tag": "*",
        "left": {
            "tag": "+",
            "left": {"tag": "number", "value": 3},
            "right": {"tag": "number", "value": 4},
        },
        "right": {"tag": "number", "value": 5},
    }
    assert evaluate(ast) == 35
    tokens = tokenizer.tokenize("3*(4+5)")
    ast, tokens = parser.parse_expression(tokens)
    assert evaluate(ast) == 27

def test_evaluate_modulus():
    print("test evaluate_modulus()")
    ast = {
        "tag": "%",
        "left": {"tag": "number", "value": 6},
        "right": {"tag": "number", "value": 2},
    }
    assert evaluate(ast) == 0
    ast = {
        "tag": "%",
        "left": {"tag": "number", "value": 8},
        "right": {"tag": "number", "value": 3},
    }
    assert evaluate(ast) == 2
    ast = {
        "tag": "%",
        "left": {
            "tag": "-",
            "left": {"tag": "number", "value": 3},
            "right": {"tag": "number", "value": 16},
        },
        "right": {"tag": "number", "value": 3},
    }
    assert evaluate(ast) == 2


if __name__ == "__main__":
    test_evaluate()
    test_evaluate_modulus()
    print("done.")
