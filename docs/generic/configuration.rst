Adding a configuration
==========================
This site explains how to create a new configuration, both for the generic part and for the application.

The following illustration shows the structure of the project:

.. code-block:: rst

   Application
    ├── src
    │   ├── __init__.py
    │   ├── db.py
    │   ├── configuration.py
    │   └── tetue_generic
    │       ├── __init__.py
    │       └── watcher.py
    ├── default.env
    └── main.py

Generic
-------
The watcher module with new functions should be added to the generic folder.
If a configuration is required for the new generic parts, the following must be created.

1. Create a configuration class in *watcher.py*

.. code-block:: python

    from pydantic import BaseModel, FilePath

    class WatcherConfiguration(BaseModel):
        log_level: str = ""
        log_file_path: FilePath = None

2. Declaring a local configuration and the initialization function in *watcher.py*

.. code-block:: python

    watcher_settings = WatcherConfiguration()

    def init_generic_watcher(log_file_path: FilePath) -> None:
        watcher_settings.log_file_path = log_file_path

3. Add new configuration variables to *default.env* with nested delimiter

.. code-block:: rst

    TT_WATCHER__LOG_FILE_PATH=files/app.log
    TT_WATCHER__log_level=INFO

4. Add new init function in *watcher.py* to *set_configurations()* in *configuration.py* in **src**

.. code-block:: python

    def set_configurations(configuration: Configuration) -> None:
        init_generic_watcher(configuration.watcher.log_file_path)

Application
-----------

.. note::

   Still being created