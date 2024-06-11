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
