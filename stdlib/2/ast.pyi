# Python 2.7 ast

import typing
from typing import Any, Iterator, Union

from _ast import (
    Add, alias, And, arguments, Assert, Assign, AST, Attribute, AugAssign,
    AugLoad, AugStore, BinOp, BitAnd, BitOr, BitXor, BoolOp, boolop, Break,
    Call, ClassDef, cmpop, Compare, comprehension, Continue, Del, Delete, Dict,
    DictComp, Div, Ellipsis, Eq, ExceptHandler, Exec, Expr, expr, Expression,
    expr_context, ExtSlice, FloorDiv, For, FunctionDef, GeneratorExp, Global,
    Gt, GtE, If, IfExp, Import, ImportFrom, In, Index, Interactive, Invert, Is,
    IsNot, keyword, Lambda, List, ListComp, Load, LShift, Lt, LtE, Mod, mod,
    Module, Mult, Name, Not, NotEq, NotIn, Num, operator, Or, Param, Pass, Pow,
    Print, Raise, Repr, Return, RShift, Set, SetComp, Slice, slice, stmt,
    Store, Str, Sub, Subscript, Suite, TryExcept, TryFinally, Tuple, UAdd,
    UnaryOp, unaryop, USub, While, With, Yield
)

__version__ = ...  # type: str
PyCF_ONLY_AST = ...  # type: int


def parse(source: Union[str, bytes], filename: Union[str, bytes] = ..., mode: str = ...) -> AST: ...
def copy_location(new_node: AST, old_node: AST) -> AST: ...
def dump(node: AST, annotate_fields: bool = ..., include_attributes: bool = ...) -> str: ...
def fix_missing_locations(node: AST) -> AST: ...
def get_docstring(node: AST, clean: bool = ...) -> str: ...
def increment_lineno(node: AST, n: int = ...) -> AST: ...
def iter_child_nodes(node: AST) -> Iterator[AST]: ...
def iter_fields(node: AST) -> Iterator[typing.Tuple[str, Any]]: ...
def literal_eval(node_or_string: Union[str, AST]) -> Any: ...
def walk(node: AST) -> Iterator[AST]: ...

class NodeVisitor():
    def visit(self, node: AST) -> Any: ...
    def generic_visit(self, node: AST) -> None: ...

class NodeTransformer(NodeVisitor):
    def generic_visit(self, node: AST) -> None: ...
