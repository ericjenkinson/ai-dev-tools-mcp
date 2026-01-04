import glob
import os
import zipfile
from typing import List, Dict

from minsearch import Index


def collect_docs_from_zips(directory: str = '.') -> List[Dict]:
    docs = []
    pattern = os.path.join(directory, '*.zip')
    for zpath in glob.glob(pattern):
        try:
            with zipfile.ZipFile(zpath, 'r') as z:
                for name in z.namelist():
                    lname = name.lower()
                    if lname.endswith('.md') or lname.endswith('.mdx'):
                        try:
                            raw = z.read(name)
                            text = raw.decode('utf-8', errors='ignore')
                        except Exception:
                            continue
                        # Remove first path component
                        if '/' in name:
                            filename = name.split('/', 1)[1]
                        else:
                            filename = name
                        docs.append({'filename': filename, 'content': text})
        except zipfile.BadZipFile:
            continue
    return docs


def build_index(docs: List[Dict]) -> Index:
    index = Index(text_fields=['content'], keyword_fields=['filename'])
    index.fit(docs)
    return index


def search_index(index: Index, query: str, top_n: int = 5) -> List[Dict]:
    results = index.search(query, num_results=top_n)
    return results


def main():
    docs = collect_docs_from_zips('.')
    print(f'Collected {len(docs)} markdown/mdx documents from zip archives')
    if not docs:
        print('No documents found. Ensure .zip files are present in the current directory.')
        return
    index = build_index(docs)
    q = 'demo'
    results = search_index(index, q, top_n=5)
    print(f'--- Top {len(results)} results for query: "{q}" ---')
    for r in results:
        print('FILE:', r.get('filename'))
        snippet = (r.get('content') or '')[:300].replace('\n', ' ')
        print('SNIPPET:', snippet)
        print()


if __name__ == '__main__':
    main()
