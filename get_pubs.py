from scholarly_publications.fetcher import fetch_all_publications

# scholar = ScholarlyPublications()
publications = fetch_all_publications('1jBAOUoAAAAJ')
# _publications('1jBAOUoAAAAJ')

import json
import os
filename = os.path.join('_data','publications.json')
with open(filename, 'w') as f:
    json.dump(publications, f)