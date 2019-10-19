from poxlang.pox_token import tokenize, WhiteSpace

src = 'if (troo) { return 7 * (1.23 + 32) } else { return "lol" }'
print(repr(src), end='\n'*2)
toks = tokenize(src)
toks = (t for t in toks if not isinstance(t, WhiteSpace))
for i, tok in enumerate(toks):
    print(i, tok)
