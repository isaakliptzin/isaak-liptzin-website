from flask_frozen import Freezer
from app import app, PROJECTS, DOCUMENTARIES, NEWS_EVENTS

freezer = Freezer(app)

@freezer.register_generator
def project():
    for p in PROJECTS:
        yield {'project_id': p['id']}

@freezer.register_generator
def documentary_detail():
    for p in DOCUMENTARIES:
        yield {'project_id': p['id']}

@freezer.register_generator
def news_event_detail():
    for p in NEWS_EVENTS:
        yield {'project_id': p['id']}

if __name__ == '__main__':
    freezer.freeze()
