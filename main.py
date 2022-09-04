import os
import json
import time
import schedule
from utils.rss_aggregator import RssAggregatorService


if __name__ == "__main__":
    cli = RssAggregatorService()
    cli.update_rss_content()
    schedule.every().hour.do(cli.update_rss_content)
    while True:
        schedule.run_pending()
        time.sleep(1)
