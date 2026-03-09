from app.agents.search_agent import search_agent_logic

print("Testing search with embeddings...")
results = search_agent_logic('typhoon model', max_results=5, top_k=5)
print(f'Found {len(results)} results')

for i, paper in enumerate(results[:3]):
    similarity = paper.get('similarity_score', 'N/A')
    print(f'{i+1}. {paper["title"][:60]}... (similarity: {similarity})')