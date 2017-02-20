db = DAL("sqlite://storage.sqlite")

db.define_table('cover',
   Field('name', unique=True, label='Nombre la portada'),
   Field('quality', label='Calidad de la imagen'),
   Field('contrast', label='Variación del color'),
   Field('layout', label='Diseño'),
   Field('type', label='Tipo de documento'),
   Field('language', label='Idioma'),
   Field('image', 'upload', label='Imagen'),
   format = '%(name)s')

db.define_table('author',
   Field('cover_id', 'reference cover'),
   Field('word', label='Palabra'),
   Field('pos', label='Etiqueta POS'),
   Field('iob', label='Marca de inicio '),
   Field('layout', label='Posición en la portada'),
   Field('font_type', label='Tipo'),
   Field('font_style', label='Estilo'),
   Field('font_size', label='Tamaño'),
   Field('is_same_color', label='Cambio de color'))

db.define_table('title',
   Field('cover_id', 'reference cover'),
   Field('word', label='Palabra'),
   Field('pos', label='Etiqueta POS'),
   Field('iob', label='Marca de inicio '),
   Field('layout', label='Posición en la portada'),
   Field('font_type', label='Tipo'),
   Field('font_style', label='Estilo'),
   Field('font_size', label='Tamaño'),
   Field('is_same_color', label='Cambio de color'))

db.define_table('date',
   Field('cover_id', 'reference cover'),
   Field('word', label='Palabra'),
   Field('pos', label='Etiqueta POS'),
   Field('iob', label='Marca de inicio '),
   Field('layout', label='Posición en la portada'),
   Field('font_type', label='Tipo'),
   Field('font_style', label='Estilo'),
   Field('font_size', label='Tamaño'),
   Field('is_same_color', label='Cambio de color'))

db.define_table('publisher',
   Field('cover_id', 'reference cover'),
   Field('word', label='Palabra'),
   Field('pos', label='Etiqueta POS'),
   Field('iob', label='Marca de inicio '),
   Field('layout', label='Posición en la portada'),
   Field('font_type', label='Tipo'),
   Field('font_style', label='Estilo'),
   Field('font_size', label='Tamaño'),
   Field('is_same_color', label='Cambio de color'))

db.define_table('description',
   Field('cover_id', 'reference cover'),
   Field('word', label='Palabra'),
   Field('pos', label='Etiqueta POS'),
   Field('iob', label='Marca de inicio '),
   Field('layout', label='Posición en la portada'),
   Field('font_type', label='Tipo'),
   Field('font_style', label='Estilo'),
   Field('font_size', label='Tamaño'),
   Field('is_same_color', label='Cambio de color'))


db.cover.name.requires = IS_NOT_IN_DB(db, db.cover.name)
db.cover.quality.requires = IS_IN_SET({'GOOD':'Buena','REGULAR':'Regular','POOR':'Mala'},zero=T('Elige uno'))
db.cover.contrast.requires = IS_IN_SET({'HIGH':'Alto','MEDIUM':'Medio','LOW':'Bajo'},zero=T('Elige uno'))
db.cover.layout.requires = IS_IN_SET({'COMPLEX':'Complejo','NORMAL':'Normal','SIMPLE':'Simple'},zero=T('Elige uno'))
db.cover.type.requires = IS_IN_SET({'BOOK':'Libro','MAGAZINE':'Revista','THESIS':'Tesis'},zero=T('Elige uno'))
db.cover.language.requires = IS_IN_SET({'SPANISH':'Español','ENGLISH':'Inglés','OTHER':'Otro'},zero=T('Elige uno'))
db.cover.image.requires = IS_IMAGE()

db.author.cover_id.requires = IS_IN_DB(db, db.cover.id, '%(name)s')
db.author.word.requires = IS_NOT_EMPTY()
db.author.pos.requires = IS_IN_SET({'NOUN':'Sustantivo','VERB':'Verbo','ADJ':'Adjetivo','ADV':'Adverbio','PRON':'Pronombre','DET':'Determinante o Artículo','ADP':'Preposición o Postposición','NUM':'Número','CONJ':'Conjunción','PRT':'Partícula','.':'Puntuación','X':'Otro'},zero=T('Elige uno'))
db.author.iob.requires = IS_IN_SET({'INSIDE':'Dentro','OUTSIDE':'Otro','BEGINNING':'Inicio'},zero=T('Elige uno'))
db.author.layout.requires = IS_IN_SET({'FIRST_LINE_START':'FLS - Inicio de primera línea','PAGE_START':'PS - Inicio de página','FIRST_LINE_END':'FLE - Fin de primera línea','LINE_START':'LS - Inicio de línea','CENTER':'C - Centro','LINE_END':'LE - Fin de línea','LAST_LINE_START':'LLS - Inicio de última línea','PAGE_END':'PE - Fin de página','LAST_LINE_END':'LLE - Fin de última línea'},zero=T('Elige uno'))
db.author.font_type.requires = IS_IN_SET({'ARTIST':'Artistica','HANDWRITE':'Manuscrita','PRINT':'Molde'},zero=T('Elige uno'))
db.author.font_style.requires = IS_IN_SET({'NORMAL':'Normal','BOLD':'Negrita','ITALIC':'Cursiva'},zero=T('Elige uno'))
db.author.font_size.requires = IS_IN_SET({'SMALL':'Pequeña','MEDIUM':'Mediana','BIG':'Grande','HUGE':'Enorme'},zero=T('Elige uno'))
db.author.is_same_color.requires = IS_IN_SET({'TRUE':'Sí','FALSE':'No'},zero=T('Elige uno'))
db.author.cover_id.writable = db.author.cover_id.readable = False

          
          
          

db.title.cover_id.requires = IS_IN_DB(db, db.cover.id, '%(name)s')
db.title.word.requires = IS_NOT_EMPTY()
db.title.pos.requires = IS_IN_SET({'NOUN':'Sustantivo','VERB':'Verbo','ADJ':'Adjetivo','ADV':'Adverbio','PRON':'Pronombre','DET':'Determinante o Artículo','ADP':'Preposición o Postposición','NUM':'Número','CONJ':'Conjunción','PRT':'Partícula','.':'Puntuación','X':'Otro'},zero=T('Elige uno'))
db.title.iob.requires = IS_IN_SET({'INSIDE':'Dentro','OUTSIDE':'Fuera','BEGINNING':'Inicio'},zero=T('Elige uno'))
db.title.layout.requires = IS_IN_SET({'FIRST_LINE_START':'FLS - Inicio de primera línea','PAGE_START':'PS - Inicio de página','FIRST_LINE_END':'FLE - Fin de primera línea','LINE_START':'LS - Inicio de línea','CENTER':'C - Centro','LINE_END':'LE - Fin de línea','LAST_LINE_START':'LLS - Inicio de última línea','PAGE_END':'PE - Fin de página','LAST_LINE_END':'LLE - Fin de última línea'},zero=T('Elige uno'))
db.title.font_type.requires = IS_IN_SET({'ARTIST':'Artistica','HANDWRITE':'Manuscrita','PRINT':'Molde'},zero=T('Elige uno'))
db.title.font_style.requires = IS_IN_SET({'NORMAL':'Normal','BOLD':'Negrita','ITALIC':'Cursiva'},zero=T('Elige uno'))
db.title.font_size.requires = IS_IN_SET({'SMALL':'Pequeña','MEDIUM':'Mediana','BIG':'Grande','HUGE':'Enorme'},zero=T('Elige uno'))
db.title.is_same_color.requires = IS_IN_SET({'TRUE':'Sí','FALSE':'No'},zero=T('Elige uno'))
db.title.cover_id.writable = db.title.cover_id.readable = False

db.date.cover_id.requires = IS_IN_DB(db, db.cover.id, '%(name)s')
db.date.word.requires = IS_NOT_EMPTY()
db.date.pos.requires = IS_IN_SET({'NOUN':'Sustantivo','VERB':'Verbo','ADJ':'Adjetivo','ADV':'Adverbio','PRON':'Pronombre','DET':'Determinante o Artículo','ADP':'Preposición o Postposición','NUM':'Número','CONJ':'Conjunción','PRT':'Partícula','.':'Puntuación','X':'Otro'},zero=T('Elige uno'))
db.date.iob.requires = IS_IN_SET({'INSIDE':'Dentro','OUTSIDE':'Fuera','BEGINNING':'Inicio'},zero=T('Elige uno'))
db.date.layout.requires = IS_IN_SET({'FIRST_LINE_START':'Inicio de primera línea','PAGE_START':'Inicio de página','FIRST_LINE_END':'Fin de primera línea','LINE_START':'Inicio de línea','CENTER':'Centro','LINE_END':'Fin de línea','LAST_LINE_START':'Inicio de última línea','PAGE_END':'Fin de página','LAST_LINE_END':'Fin de última línea'},zero=T('Elige uno'))
db.date.font_type.requires = IS_IN_SET({'ARTIST':'Artistica','HANDWRITE':'Manuscrita','PRINT':'Molde'},zero=T('Elige uno'))
db.date.font_style.requires = IS_IN_SET({'NORMAL':'Normal','BOLD':'Negrita','ITALIC':'Cursiva'},zero=T('Elige uno'))
db.date.font_size.requires = IS_IN_SET({'SMALL':'Pequeña','MEDIUM':'Mediana','BIG':'Grande','HUGE':'Enorme'},zero=T('Elige uno'))
db.date.is_same_color.requires = IS_IN_SET({'TRUE':'Sí','FALSE':'No'},zero=T('Elige uno'))
db.date.cover_id.writable = db.date.cover_id.readable = False

db.publisher.cover_id.requires = IS_IN_DB(db, db.cover.id, '%(name)s')
db.publisher.word.requires = IS_NOT_EMPTY()
db.publisher.pos.requires = IS_IN_SET({'NOUN':'Sustantivo','VERB':'Verbo','ADJ':'Adjetivo','ADV':'Adverbio','PRON':'Pronombre','DET':'Determinante o Artículo','ADP':'Preposición o Postposición','NUM':'Número','CONJ':'Conjunción','PRT':'Partícula','.':'Puntuación','X':'Otro'},zero=T('Elige uno'))
db.publisher.iob.requires = IS_IN_SET({'INSIDE':'Dentro','OUTSIDE':'Fuera','BEGINNING':'Inicio'},zero=T('Elige uno'))
db.publisher.layout.requires = IS_IN_SET({'FIRST_LINE_START':'FLS - Inicio de primera línea','PAGE_START':'PS - Inicio de página','FIRST_LINE_END':'FLE - Fin de primera línea','LINE_START':'LS - Inicio de línea','CENTER':'C - Centro','LINE_END':'LE - Fin de línea','LAST_LINE_START':'LLS - Inicio de última línea','PAGE_END':'PE - Fin de página','LAST_LINE_END':'LLE - Fin de última línea'},zero=T('Elige uno'))
db.publisher.font_type.requires = IS_IN_SET({'ARTIST':'Artistica','HANDWRITE':'Manuscrita','PRINT':'Molde'},zero=T('Elige uno'))
db.publisher.font_style.requires = IS_IN_SET({'NORMAL':'Normal','BOLD':'Negrita','ITALIC':'Cursiva'},zero=T('Elige uno'))
db.publisher.font_size.requires = IS_IN_SET({'SMALL':'Pequeña','MEDIUM':'Mediana','BIG':'Grande','HUGE':'Enorme'},zero=T('Elige uno'))
db.publisher.is_same_color.requires = IS_IN_SET({'TRUE':'Sí','FALSE':'No'},zero=T('Elige uno'))
db.publisher.cover_id.writable = db.publisher.cover_id.readable = False

db.description.cover_id.requires = IS_IN_DB(db, db.cover.id, '%(name)s')
db.description.word.requires = IS_NOT_EMPTY()
db.description.pos.requires = IS_IN_SET({'NOUN':'Sustantivo','VERB':'Verbo','ADJ':'Adjetivo','ADV':'Adverbio','PRON':'Pronombre','DET':'Determinante o Artículo','ADP':'Preposición o Postposición','NUM':'Número','CONJ':'Conjunción','PRT':'Partícula','.':'Puntuación','X':'Otro'},zero=T('Elige uno'))
db.description.iob.requires = IS_IN_SET({'INSIDE':'Dentro','OUTSIDE':'Fuera','BEGINNING':'Inicio'},zero=T('Elige uno'))
db.description.layout.requires = IS_IN_SET({'FIRST_LINE_START':'FLS - Inicio de primera línea','PAGE_START':'PS - Inicio de página','FIRST_LINE_END':'FLE - Fin de primera línea','LINE_START':'LS - Inicio de línea','CENTER':'C - Centro','LINE_END':'LE - Fin de línea','LAST_LINE_START':'LLS - Inicio de última línea','PAGE_END':'PE - Fin de página','LAST_LINE_END':'LLE - Fin de última línea'},zero=T('Elige uno'))
db.description.font_type.requires = IS_IN_SET({'ARTIST':'Artistica','HANDWRITE':'Manuscrita','PRINT':'Molde'},zero=T('Elige uno'))
db.description.font_style.requires = IS_IN_SET({'NORMAL':'Normal','BOLD':'Negrita','ITALIC':'Cursiva'},zero=T('Elige uno'))
db.description.font_size.requires = IS_IN_SET({'SMALL':'Pequeña','MEDIUM':'Mediana','BIG':'Grande','HUGE':'Enorme'},zero=T('Elige uno'))
db.description.is_same_color.requires = IS_IN_SET({'TRUE':'Sí','FALSE':'No'},zero=T('Elige uno'))
db.description.cover_id.writable = db.description.cover_id.readable = False


from gluon.tools import Auth
auth = Auth(db)
auth.define_tables(username=True)
