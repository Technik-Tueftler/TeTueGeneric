"""
Main function for starting application
"""

import src


def main() -> None:
    """
    Scheduling function for regular call.
    """
    config = src.Configuration()
    print(type(config))
    print(type(config.watcher))
    src.watcher.init_logging(config.watcher)
    src.watcher.logger.info(f"Start application in version: {src.__version__}")
    print(config.gen_req.request_timeout)
    print(config.watcher.log_level)


if __name__ == "__main__":
    main()
