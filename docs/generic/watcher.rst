watcher
==========================

.. automodule:: src.tetue_generic.watcher
    :members:
    :exclude-members: WatcherConfiguration


Initialization function
=======================
The initialization process is performed by the :func:`src.tetue_generic.watcher.init` function. This function performs the following tasks:

Procedure for the initialization process
----------------------------------------

   1. Removes existing loggers
   2. Defines a custom log level "EXTDEBUG"
   3. Adds a method for the new log level
   4. Configures file output with rotation
   5. Configures console output with color

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

The log level "EXTDEBUG" is used to display additional information that is not displayed with the "DEBUG" log level.

