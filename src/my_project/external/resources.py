"""
Module for handling external open-closed or acquirable resources: clients, connections, descriptors or files.

Resources usually implement the context manager protocol (i.e., define __enter__ and __exit__ methods) to ensure proper acquisition and release of the resource.
The singleton instance of the resource could be stored in a private global variable within the module.
"""


_DB_SESSION = ...

def get_db_session():
    global _DB_SESSION
    if _DB_SESSION is None:
        _DB_SESSION = ...
    return _DB_SESSION
