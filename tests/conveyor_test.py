from main import Token, MathTokensConveyor


def test_complex_example():
    conveyor = MathTokensConveyor()
    result_token = conveyor.process([
        Token(Token.MATH_OPERATOR, "-"),
        Token(Token.INTEGER, "5"),
        Token(Token.MATH_OPERATOR, "+"),
        Token(Token.INTEGER, "4"),
        Token(Token.MATH_OPERATOR, "-"),
        Token(Token.INTEGER, "1"),
        Token(Token.MATH_OPERATOR, "/"),
        Token(Token.INTEGER, "2"),
        Token(Token.MATH_OPERATOR, "*"),
        Token(Token.INTEGER, "4"),
    ])
    assert result_token.value == "-4.0"

