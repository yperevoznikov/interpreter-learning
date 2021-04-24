from main import Tokenizer, Token


def test_math_example():
    text = Tokenizer("5-1")
    tokens = list(text)
    assert len(tokens) == 4
    assert tokens[0].kind == Token.INTEGER
    assert tokens[0].value == "5"
    assert tokens[1].kind == Token.MATH_OPERATOR
    assert tokens[1].value == "-"
    assert tokens[2].kind == Token.INTEGER
    assert tokens[2].value == "1"
    assert tokens[3].kind == Token.EOF
