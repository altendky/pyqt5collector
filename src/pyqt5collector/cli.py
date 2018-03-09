import click
import scrapy.crawler
import twisted.internet.reactor

import pyqt5collector.scrape


@click.command()
def cli():
    runner = scrapy.crawler.CrawlerRunner()
    d = runner.crawl(pyqt5collector.scrape.Spider)
    d.addBoth(lambda _: twisted.internet.reactor.stop())
    twisted.internet.reactor.run()

    print('~~~~')
    print('\n'.join(str(r) for r in pyqt5collector.scrape.result.items()))
