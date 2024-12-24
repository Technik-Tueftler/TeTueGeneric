"""
Main function for starting application
"""

import src


def main() -> None:
    """
    Scheduling function for regular call.
    """
    config = src.Configuration()
    src.set_configurations(config)
    src.watcher.init_logging(config.watcher.log_level)
    src.watcher.logger.info(f"Start application in version: {src.__version__}")


if __name__ == "__main__":
    main()
