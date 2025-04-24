from scholarly_publications.fetcher import fetch_all_publications

# scholar = ScholarlyPublications()
publications = fetch_all_publications('1jBAOUoAAAAJ')
# _publications('1jBAOUoAAAAJ')

import json
with open('publications.json', 'w') as f:
    json.dump(publications, f)