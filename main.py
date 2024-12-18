"""main
"""
import src


def main():
    """
    temp
    """
    src.watcher.init_logging("ERROR")
    src.watcher.logger.error("Test")
    config = src.Configuration()

    print(config.gen_req.request_timeout)
    print(config.db.ip)

if __name__ == "__main__":
    main()
