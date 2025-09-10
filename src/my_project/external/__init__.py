"""
Package for dependant backends, backends, repositories and collections, that the application uses.

It'd be better to declare the interface of every dependant,
that returns implementation-agnostic objects (usually Pydantic models or dataclass structures). And then,
implement the interface in the backend-specific modules.
Lately, the interface could be re-implemented for tests.
"""