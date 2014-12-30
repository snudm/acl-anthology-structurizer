# ACL trend survey

## Data crawling

- Configure year and journal in `crawler/crawler/settings.py`.  (Haven't tried crawling other proceedings/journals than ACL though)

        $ cd crawler
        $ scrapy crawl acl -o items.csv -t csv
        $ scrapy crawl acl -o items.json -t json

- Be careful of running the code twice because the json file gets appended, rather than overwritten.

## Calc frequent authors

    $ python count.py
