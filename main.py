import string


class Token:
    INTEGER = 'INTEGER'
    MATH_OPERATOR = 'MATH_OPERATOR'
    UNDEFINED = 'UNDEFINED'
    EOF = 'EOF'

    def __init__(self, kind, value=None):
        self.kind = kind
        self.value = value

    def __str__(self):
        return f"TOKEN(type={self.kind}, value={self.value})"

    def __repr__(self):
        return self.__str__()


class Tokenizer:
    def __init__(self, text):
        self._text = text

    def __iter__(self):
        self._is_eof_sent = False
        self._position = 0
        self._token_text = ""
        self._token_kind = None
        return self

    def __next__(self):
        if self._is_eof_sent:
            raise StopIteration
        if self._position >= len(self._text):
            self._is_eof_sent = True
            return Token(Token.EOF)
        for position in range(self._position, len(self._text)):
            char = self._text[position]
            if self._token_text == "":
                self._token_kind = self._get_token_kind_by_first_char(char)
            elif self._is_token_end(self._token_kind, char):
                break
            self._token_text += char
            self._position = position + 1  # start next time
        token = Token(self._token_kind, self._token_text)
        self._token_kind = None
        self._token_text = ""
        return token

    def _get_token_kind_by_first_char(self, char):
        if char in string.digits:
            return Token.INTEGER
        if char in "*+-/":
            return Token.MATH_OPERATOR
        return Token.UNDEFINED

    def _is_token_end(self, kind, char):
        if kind == Token.INTEGER and char not in string.digits:
            return True
        if kind == Token.MATH_OPERATOR and char not in "*":
            return True
        return False


class MathTokensConveyor:
    def process(self, tokens):
        result = None
        waiting_math_operator = None

        for token in tokens:
            # # process first token
            # if result is None:
            #     if token.kind != Token.INTEGER:
            #         raise Exception("Number must be first")
            #     result = int(token.value)
            #     continue

            # Handle operations
            if token.kind == Token.MATH_OPERATOR:
                waiting_math_operator = token
                continue

            # Handle numbers
            if token.kind == Token.INTEGER:
                if waiting_math_operator is None and result is not None:
                    raise Exception("Number without preceding operation")
                result = self.apply_operation(
                    waiting_math_operator,
                    result,
                    token
                )

        return result

    def apply_operation(self, operation, left_operand, right_operand):
        if operation is None:
            # simple assignment
            return right_operand

        result_value = None
        if operation.value == "+":
            result_value = float(left_operand.value) + float(right_operand.value)
        elif operation.value == "-":
            result_value = float(left_operand.value) - float(right_operand.value)
        elif operation.value == "/":
            result_value = float(left_operand.value) / float(right_operand.value)
        elif operation.value == "*":
            result_value = float(left_operand.value) * float(right_operand.value)

        if result_value is None:
            raise Exception(f"Not supported operation '{operation}'")

        return Token(Token.INTEGER, str(result_value))


def main(expression):
    text = Tokenizer(expression)
    print(f"Tokens for expression '{expression}':")
    for token in text:
        print(token)

    conveyor = MathTokensConveyor()
    result = conveyor.process(text)
    print("\nResult:")
    print(result)


if __name__ == '__main__':
    main("5*2")
