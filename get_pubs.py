from scholarly_publications import ScholarlyPublications

scholar = ScholarlyPublications()
publications = scholar.get_publications('your_google_scholar_id_here')

import json
with open('publications.json', 'w') as f:
    json.dump(publications, f)