watcher
==========================

.. automodule:: src.tetue_generic.watcher
    :members:
    :exclude-members: model_config


Initialization function
=======================
The initialization process is performed by the :func:`src.tetue_generic.watcher.init_logging` function. This function performs the following tasks:

Procedure for the initialization process
----------------------------------------

    1. Removes any existing log handlers.  
    2. Adds a custom log level 'EXTDEBUG'.  
    3. Configures file logging with rotation.  
    4. Sets up console logging with color output

Log levels
----------
The following log levels are available:

   * TRACE
   * EXTDEBUG
   * DEBUG
   * INFO
   * SUCCESS
   * WARNING
   * ERROR
   * CRITICAL

Two Debug Levels for Optimized Logging Granularity

Our system employs two distinct debug levels:

1. DEBUG: For general debugging information.
2. EXTDEBUG: For more detailed, cyclically queried information.

The EXTDEBUG level is used for high-frequency logging events such as repeated API requests. This prevents the standard DEBUG log from being flooded with repetitive information while still allowing for deeper insight into system behavior when needed.

Example: While DEBUG logs general process steps, EXTDEBUG records every single API request with details. This enables precise troubleshooting without compromising the readability of standard logs.

