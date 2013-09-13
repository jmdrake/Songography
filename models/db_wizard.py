### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_artist',
    Field('f_name', type='string',
          label=T('Name')),
    auth.signature,
    format='%(f_name)s',
    migrate=settings.migrate)

db.define_table('t_artist_archive',db.t_artist,Field('current_record','reference t_artist',readable=False,writable=False))

########################################
db.define_table('t_album',
    Field('f_title', type='string',
          label=T('Title')),
    Field('f_artist_id_reference', type='reference t_artist',
          label=T('Artist Id Reference')),
    auth.signature,
    format='%(f_title)s',
    migrate=settings.migrate)

db.define_table('t_album_archive',db.t_album,Field('current_record','reference t_album',readable=False,writable=False))

########################################
db.define_table('t_song',
    Field('f_title', type='string',
          label=T('Title')),
    Field('f_album_id_reference', type='reference t_album',
          label=T('Album Id Reference')),
    auth.signature,
    format='%(f_title)s',
    migrate=settings.migrate)

db.define_table('t_song_archive',db.t_song,Field('current_record','reference t_song',readable=False,writable=False))
