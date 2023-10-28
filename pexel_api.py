import requests


class PexelApi:

    def fetch_images(self, retry=0, **kwargs):
        
        if retry >= 5:
            return
        headers = {"Authorization": "****"}
        url = "https://api.pexels.com/v1/search"
        query = kwargs.get('query')
        per_page = kwargs.get('per_page')
        page = kwargs.get('page')
        url += f"?query={query}&per_page={per_page}&page={page}"
        try:
            response = requests.get(url, headers=headers)
            if not response.ok:
                return self.fetch_images(retry + 1, **kwargs)
        except:
            return 
        return response.json()

