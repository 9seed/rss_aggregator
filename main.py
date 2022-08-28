import time
import schedule
from moduls.rss_aggregator import RssAggregatorService

ras = RssAggregatorService()
ras.check_init()
schedule.every().hour.do(ras.update_from_src)

while True:
    schedule.run_pending()
    time.sleep(1)