Main schedule
==========================

The following diagram shows the start of the generic main with the calls in the 
configuration and the logger.

.. mermaid ::
    sequenceDiagram
        main.py->>+configuration.py: Create App configuration
        configuration.py-->>-main.py: return config
        main.py->>+configuration.py: set_configurations(config)
        configuration.py->>+generic_requests.py: init_generic_requests()
        generic_requests.py-->>-configuration.py: None
        configuration.py->>+watcher.py: init_generic_watcher()
        watcher.py-->>-configuration.py: None
        configuration.py-->>-main.py: None
        main.py->>+watcher.py: init_logging
        watcher.py-->>-main.py: None