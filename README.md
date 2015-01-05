# ACL trend survey

## Requirements

- Python 2.7
- Install [scrapy](http://scrapy.org)

    $pip install scrapy

## Run
### Data crawling

- Configure year and journal in `crawler/crawler/settings.py`.  (Haven't tried crawling other proceedings/journals than ACL though)

        $ cd crawler
        $ scrapy crawl acl -o items.csv -t csv
        $ scrapy crawl acl -o items.json -t json

- Be careful of running the code twice because the json file gets appended, rather than overwritten.

### Calculate frequent authors

    $ python count.py

## Author

- [Lucy Park](http://github.com/e9t)

## License

- [Apache v2.0](http://www.apache.org/licenses/LICENSE-2.0)
