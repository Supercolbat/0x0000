from flask import jsonify

def urlexists(url):
    with open("urls.json") as f:
        urls = json.load(f)
        
        if url in urls.values():
            return True
        return False