from math_expr import calc

def test_calculator():
    test_cases = [
        ("2 + 3", 5),
        ("10 - 7", 3),
        ("4 * 5", 20),
        ("20 / 4", 5),
        ("-5", -5),
        ("--5", 5),
        ("-5 + 3", -2),
        ("2 + 3 * 4", 14),
        ("(2 + 3) * 4", 20),
        ("2 * (3 + 4) / 7", 2),
        ("-(5 + 3) * (2 - (3 * 2))", 32),
        ("4 + 5 * (7 - 3)", 24),
        ("10 / (2 + 3) * 2", 4),
    ]
    
    for expression, expected in test_cases:
        result = calc(expression)
        assert result == expected, f"Test failed for {expression}. Expected {expected}, got {result}"
    print("All tests passed!")

test_calculator()

