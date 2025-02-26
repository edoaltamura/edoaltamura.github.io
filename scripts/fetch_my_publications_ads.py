import os
import yaml
import ads
import warnings
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Set your NASA ADS API token
ads.config.token = os.getenv("ADS_TOKEN")

# Define your orcid as it appears in ADS records
my_orcid = "0000-0001-6973-1897"
my_author = ["Altamura, Edoardo", "Altamura, E", "Altamura, E."]

# Fetch publications from NASA ADS
# Here we loop over the desired publication types: "article", "review", "preprint".
# The ADS API accepts a "doctype" parameter to filter by type.
fields = [
    "id",  # Unique identifier (Bibcode)
    "title",  # Title of the publication
    "author",  # List of authors
    "aff",  # Affiliations
    "pub",  # Publication venue
    "pubdate",  # Publication date
    "doi",  # Digital Object Identifier
    "citation_count",  # Number of citations
    "doctype",  # Document type (e.g., article, review, preprint)
    "abstract",  # Abstract of the publication
    "orcid_pub",  # ORCID numbers associated with the publication
    "keyword",  # Keywords
    "identifier"
]
my_pubs = []
# for work_type in ["article", "review", "preprint"]:
query = ads.SearchQuery(
    orcid=my_orcid,
    # doctype=work_type,
    # sort="pubdate desc",
    rows=100,
    fl=fields
)
my_pubs.extend(list(query))

# Add specific publications by ID if needed (e.g., ones not returned by the query)
extra_pub_ids = []  # e.g., ["2021A&A...650A..99D", "2020ApJ...890...12D"]
for pub_id in extra_pub_ids:
    query = ads.SearchQuery(
        bibcode=pub_id,
        rows=1,
        fl=fields
    )
    results = list(query)
    if results:
        my_pubs.append(results[0])

print(f"Found {len(my_pubs)} entries")


def process_pubs(pubs: list, exclude_keywords: list[str] | None = None):
    processed_pubs = []

    for pub in pubs:
        # ADS returns title as a list; use the first entry.
        title = pub.title[0] if pub.title else ""

        # Exclude publications with certain keywords in the title
        if exclude_keywords is not None and any(kw in title for kw in exclude_keywords):
            continue

        # Create a new publication dictionary
        new_pub = {}
        new_pub["title"] = title

        # ADS returns authors as a list of strings.
        authors = list(pub.author) if pub.author else []
        orcids = list(pub.orcid_pub) if pub.orcid_pub else []
        new_pub["num_authors"] = len(authors)

        if len(authors) != len(orcids):
            warnings.warn(f"len(authors) != len(orcids): {len(authors)} != {len(orcids)}", RuntimeWarning)

        # Determine "my" position by searching for your ADS author name (case-insensitive)
        my_position = None
        for idx, orcid in enumerate(orcids):
            if orcid == my_orcid:
                my_position = idx
                break

        # If Orcid is not found, try a search by author name
        if my_position is None:
            for idx, author in enumerate(authors):
                if author in my_author:
                    my_position = idx
                    break

        # Skip this publication if your name is not found
        if my_position is None:
            continue

        new_pub["my_position"] = my_position
        new_pub["me_first_author"] = (my_position == 0)
        # ADS does not usually provide affiliations in the search result; leave empty
        new_pub["my_affiliations"] = []

        # Build an author string depending on your author position:
        if my_position < 3:
            authors[my_position] = f'**{my_author[0]}**'
            authors_str = ", ".join(authors[:my_position + 1])
            if len(authors) > my_position + 1:
                authors_str += " *et al.*"
            new_pub["authors_str"] = authors_str
            new_pub["categories"] = ["Main Author"]
        else:
            authors_str = authors[0]
            if "collaboration" in authors_str.lower():
                authors_str = authors[1]
            if len(authors) > 1:
                authors_str += " *et al.*"
            new_pub["authors_str"] = authors_str
            new_pub["categories"] = ["Contributing Author"]

        # Publication date from ADS
        new_pub["publication_date"] = pub.pubdate

        # Use DOI if available; otherwise, fall back on the ADS bibcode (stored in "id")
        if hasattr(pub, 'doi') and pub.doi:
            # pub.doi is usually a list; take the first entry.
            new_pub["doi"] = pub.doi[0] if isinstance(pub.doi, list) else pub.doi
        else:
            new_pub["doi"] = getattr(pub, 'id', '')

        # Try reconstructing the URL
        new_pub["url"] = get_publication_url(pub)

        # Use the ADS "pub" field as the publication venue
        new_pub["source_name"] = pub.pub if (hasattr(pub, 'pub') and pub.pub) else ""
        # Set source_type based on the doctype (use "journal" for articles)
        if hasattr(pub, 'doctype') and pub.doctype:
            new_pub["source_type"] = "journal" if pub.doctype == "article" else pub.doctype
        else:
            new_pub["source_type"] = ""

        # Citation count from ADS
        new_pub["cited_by_count"] = pub.citation_count if hasattr(pub, 'citation_count') else 0

        processed_pubs.append(new_pub)

    # Remove duplicates based on title (see below)
    processed_pubs = remove_duplicate_pubs(processed_pubs)

    return processed_pubs


def remove_duplicate_pubs(pubs: list) -> list:
    """
    Remove duplicate publications (by title) from the list.
    If duplicates are found, prefer the one from a journal source.
    """
    cleaned_pubs = []
    for pub in pubs:
        indices = [i for i, p in enumerate(cleaned_pubs) if p["title"] == pub["title"]]
        if not indices:
            cleaned_pubs.append(pub)
        elif len(indices) > 1:
            raise ValueError("Publication titles in cleaned_pubs are not unique")
        else:
            idx = indices[0]
            if pub["source_type"] == "journal":
                cleaned_pubs[idx] = pub
    return cleaned_pubs


def get_publication_url(pub):
    """
    Given an ADS publication record, return a URL to the publication.
    - If a DOI is available, return the DOI link.
    - Otherwise, if an arXiv identifier is found in the 'identifier' field, return the arXiv URL.
    - As a fallback, return the ADS abstract page URL using the Bibcode.
    """
    if hasattr(pub, 'doi') and pub.doi:
        doi_val = pub.doi[0] if isinstance(pub.doi, list) else pub.doi
        return f"https://doi.org/{doi_val}"
    if hasattr(pub, 'identifier') and pub.identifier:
        for ident in pub.identifier:
            if ident.startswith("arXiv:"):
                arxiv_id = ident.split("arXiv:")[1]
                return f"https://arxiv.org/abs/{arxiv_id}"
    return f"https://ui.adsabs.harvard.edu/abs/{pub.id}/abstract"


if __name__ == "__main__":
    my_processed_pubs = process_pubs(my_pubs)

    # Order publications by your position in the author list (ascending)
    # and then by reverse publication date (recent first)
    my_sorted_pubs = sorted(
        my_processed_pubs,
        key=lambda pub: (
            pub["my_position"],
            -int(pub["publication_date"].replace("-", ""))
        )
    )

    # Build a YAML-friendly list
    pubs_yaml_content = []
    for pub in my_sorted_pubs:
        pub_dict = {
            "path": pub["url"],
            "title": pub["title"],
            "subtitle": pub["source_name"],
            "date": pub["publication_date"],
            "author": pub["authors_str"],
            "description": str(pub["cited_by_count"]),
        }
        pubs_yaml_content.append(pub_dict)

    # Save the processed publications to a YAML file
    with open("../publications/publications.yml", "w") as f:
        yaml.dump(pubs_yaml_content, f, sort_keys=False)
