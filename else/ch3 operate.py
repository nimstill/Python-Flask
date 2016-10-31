u = models.User(nickname='john', email='john@email.com')
db.session.add(u)
db.session.commit()

import datetime
u = models.User.query.get(1)
p = models.Post(body='my first post!', timestamp=datetime.utcnow(), author=u)
db.session.add(p)
db.session.commit()

users = models.User.query.all()
for u in users:
    db.session.delete(u)

posts = models.Post.query.all()
for p in posts:
    db.session.delete(p)

db.session.commit()
