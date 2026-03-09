from app.database.papers_store import get_all_papers
from app.utils.embeddings import embed_texts
from app.database.vector_store import vector_store
import numpy as np

papers = get_all_papers()
print(f'Found {len(papers)} papers')

for paper in papers:
    text = paper['title'] + ' ' + paper.get('abstract', '')
    print(f'Generating embedding for paper {paper["id"]}: {paper["title"][:50]}...')

    try:
        embedding = embed_texts([text])[0]
        vector_store.add_embedding(paper['id'], np.array(embedding))
        print(f'Successfully stored embedding for paper {paper["id"]}')
    except Exception as e:
        print(f'Error generating embedding: {e}')

# Force save
vector_store.save()
print('Vector store stats after:', vector_store.get_stats())