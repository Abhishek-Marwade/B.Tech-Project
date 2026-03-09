from api_client import search_semanticscholar

# Replace with your real API key if you have one
papers = search_semanticscholar("Neural Network", max_results=2, api_key='599305d1868ada4180d052e5ca90fba0')

for p in papers:
    print(p)
