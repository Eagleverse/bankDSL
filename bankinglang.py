class Position:
    def __init__(self):
        self.idx = None

    def advance(self, current_char):
        pass


class Lexer:
    def __init__(self, fn, text):
        self.pos = None
        self.fn = fn
        self.text = text
        # self.pos = Position(-1, 0, -1, fn, text)
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None


class Parser:
    def __init__(self, tokens):
        self.current_tok = None
        self.tokens = tokens
        self.tok_idx = -1
        self.advance()

    def advance(self):
        self.tok_idx += 1
        self.update_current_tok()
        return self.current_tok

    def update_current_tok(self):
        pass
