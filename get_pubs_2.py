from scholarly import scholarly
import json
import os

def fetch_publications_by_scholar(author_name, limit=20):
    author = scholarly.search_author_id(author_name)  
    
    if not author:
        print("Author not found on Google Scholar.")
        return []

    author_filled = scholarly.fill(author, sections=['publications'])
    publications = []

    for pub in author_filled.get("publications", [])[:limit]:
        filled_pub = scholarly.fill(pub)
        # publication = {
        #     "title": filled_pub.get("bib", {}).get("title"),
        #     "venue": filled_pub.get("bib", {}).get("venue"),
        #     "year": filled_pub.get("bib", {}).get("pub_year"),
        #     "authors": filled_pub.get("bib", {}).get("author", "").split(" and ")
        # }
        publications.append(filled_pub.get("bib", {}))

    return publications

def save_to_json(data, filename="publications.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"Saved {len(data)} publications to {filename}")

# Example usage
if __name__ == "__main__":
    author_name = '1jBAOUoAAAAJ'  # Replace with your author of interest
    publications = fetch_publications_by_scholar(author_name)
    filename = os.path.join('_data','publications.json')
    save_to_json(publications, filename=filename)