@auth.requires_login()
def index():
    grid = SQLFORM.smartgrid(db.cover,linked_tables=['title','author', 'date', 'publisher', 'description'])
    if any (k in request.args for k in ('title.cover_id','author.cover_id', 'date.cover_id', 'publisher.cover_id', 'description.cover_id')):
        cover = db.cover(request.args(2,cast=int)) or redirect(URL('index'))
        return dict(grid=grid,cover=cover)
    return dict(grid=grid)


def download():
    return response.download(request, db)

def user():
    return dict(form=auth())

