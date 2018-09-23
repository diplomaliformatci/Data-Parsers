import os
import json
import facebook

if __name__ == '__main__':
    token = ('EAACEdEose0cBAD6XpBrSh2PbppDy224r1kAQX0kXIbLvstWGDrxDnJlLQPVzVIVjIPlhLZCVRvQ2G7mGIeGLKZCSLMB2qwSpNfVDyvGmwazneIFtiZCMdqdYuY6ECDjVVuiLfkID9aXdjBPx7othHoQ6YvY31iUf0rRdZA3ADAZDZD')
    graph = facebook.GraphAPI(token)
    profile = graph.get_object('me' , 'name,location' )

    print(json.dumps(profile,indent=4))