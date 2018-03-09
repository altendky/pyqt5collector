import attr

import scrapy.linkextractors
import scrapy.spiders


result = None


@attr.s(frozen=True)
class Condition:
    archive_type = attr.ib(default=None)
    release_type = attr.ib(default=None)

    def matches(self, url):
        return all((x is None) or (x in url) for x in
                   (self.archive_type, self.release_type))


class ArchiveLink(scrapy.Item):
    archive_type = scrapy.Field()
    release_type = scrapy.Field()
    url = scrapy.Field()


conditions = (
    Condition(archive_type='tar.gz', release_type='dev'),
    Condition(archive_type='zip', release_type='dev'),
    Condition(release_type='ChangeLog'),
)


class Spider(scrapy.spiders.CrawlSpider):
    name = 'pyqt5'
    start_urls = ['https://www.riverbankcomputing.com/software/pyqt/download5']
    rules = (
        scrapy.spiders.Rule(
            scrapy.linkextractors.LinkExtractor(
                allow=tuple(c.archive_type for c in conditions if
                            c.archive_type is not None),
                deny_extensions=[],
            ),
            process_links='handle',
        ),
    )

    def handle(self, links):
        urls = [link.url for link in links]

        archives = {}

        for condition in conditions:
            matches = (
                url
                for url in urls
                if condition.matches(url)
            )
            try:
                archives[condition], = matches
            except ValueError:
                pass

        global result
        result = archives

        return []
