#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from collections import Counter, defaultdict, OrderedDict
import json
import time


curyear = time.localtime()[0]
format_tuple = lambda t: '%s (%s)' % (t[0], t[1])


def count_and_format(authors, n=10):
    return [format_tuple(p) for p in Counter(authors).most_common(n)]

def get_year(year_id):
    if int(year_id) < int(str(curyear)[-2:]):
        return '20%s' % year_id
    else:
        return '19%s' % year_id

def get_authors_by_year(papers):
    d = defaultdict(list)
    for paper in papers:
        d[get_year(paper['id'][1:3])].extend(paper.get('authors', []))
    return d


if __name__=='__main__':

    with open('crawler/items.json', 'r') as f:
        papers = json.load(f)

    d = get_authors_by_year(papers)

    # Get frequent authors by year
    e = dict()
    for k, v in d.items():
        e[k] = [format_tuple(p) for p in Counter(v).most_common(3)]

    # Get globally frequent authors
    all_authors = sum([paper.get('authors', []) for paper in papers], [])
    e['all'] = count_and_format(all_authors)

    # Get recently frequent authors
    nyears = [3, 5, 10, 20]
    for n in nyears:
        years = map(str, range(curyear-n, curyear+1))
        recent_authors = sum([d[year] for year in years], [])
        e['recent_%syrs' % n] = count_and_format(recent_authors)

    # Write to file
    with open('top3.json', 'w') as f:
        json.dump(e, f, indent=2)
