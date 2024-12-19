Adding a module
==========================
This site explains how to create a new module, both for the generic part and for the application.

The following illustration shows the structure of the project:

.. code-block:: rst

   Application
    ├── src
    ├   ├── __init__.py
    ├   ├── db.py
    ├   ├── configuration.py
    ├   └── tetue_generic
    ├       ├── __init__.py
    ├       └── watcher.py
    ├── default.env
    └── main.py

Generic
-------
The watcher module with new functions should be added to the generic folder.

Structure
~~~~~~~~~~

1. Add new file *watcher.py* in **tetue_generic** directory
2. Add import for watcher in *__init__.py* in **src** directory

.. code-block:: python

    from .tetue_generic.watcher import *

3. Now the functions in *watcher.py* are available in *main.py*

Configuration
~~~~~~~~~~
If a configuration is required for the new generic parts, the following must be created.

1. Create a configuration class

.. code-block:: python

    from pydantic import BaseModel, FilePath

    class WatcherConfiguration(BaseModel):
        log_level: str = ""
        log_file_path: FilePath = None

2. Declaring a local configuration and the initialization function

.. code-block:: python

    watcher_settings = WatcherConfiguration()

    def init_generic_watcher(log_file_path: FilePath) -> None:
        watcher_settings.log_file_path = log_file_path

3. 

Application
-------
lala lup