import ply.lex as lex
from lex import TOKEN

tokens = (
    "Number",
    "Name",
    "String",
    "Eq",
    "Leq",
    "Req",
)

reserved = {
    "for" : "FOR",
    "in"  : "IN",
    "if"  : "IF",
    "else" : "ELSE",
    "while" : "WHILE",
    "func" : "FUNC",
    "break" : "BREAK",
    "continue" : "CONTINUE",
    "return" : "RETURN",
    "and" : "AND",
    "or" : "OR",
    "not" : "NOT",
    "nil" : "NIL",
    "ture" : "TRUE",
    "false" : "FALSE",
    "local" : "LOCAL",
}

tokens += list(reserved.values())

# ignore spaces and tab
t_ignore = " \t"

# define comment
def t_COMMENT(t):
    r"#.*"
    
# define newline
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

def t_Number(t):
    r"(\d+\.\d+|\d+\.?|\.\d+)(e[+-]?\d+)?"
    t.value = eval(t.value)
    return t

def t_Name(t):
    r"[a-zA-z_]+\w*"
    # a key word?
    t.type = reserved.get(t.value,\
                          "NAME")
    return t

# define string rule
escape_char = r"\\."
normal_char = r"."
String = r'"(escape_char|normal_char)*"'
@TOKEN(String)
def t_String(t):
    print("a literal string: " + t.value)
    return t

def t_Eq(t):
    r"=="
    return t

def t_Leq(t):
    r"<="
    return t

def t_Req(t):
    r">="
    return t

# literals
literals = ["+", "-", "*", "/", "%", ">",
            "<", "=", ":", ";", "{", "}"
            , "(", ")", "[", "]"]

# error handling rule
def t_error(t):
    print("Illegal character '%s'"
          % t.value[0])
    t.lexer.skip(1)

# EOF handling rule
def t_eof(t):
    # Get more input (Example)
    more = raw_input('... ')
    if more:
        self.lexer.input(more)
        return self.lexer.token()
    return None
