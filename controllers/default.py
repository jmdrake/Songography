# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()

def error():
    return dict()

@auth.requires_login()
def artist_manage():
    form = SQLFORM.smartgrid(db.t_artist,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def album_manage():
    form = SQLFORM.smartgrid(db.t_album,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def song_manage():
    form = SQLFORM.smartgrid(db.t_song,onupdate=auth.archive)
    return locals()

def artist_list():
    artists = db().select(db.t_artist.ALL)
    return locals()

def artist_show():
    artist = db.t_artist(request.args(0))
    albums = db(db.t_album.f_artist_id_reference==artist.id).select()
    return locals()

def artist_add_albums():
    import re
    form = FORM(DIV(TEXTAREA(_id='albumlist', _name='albumlist')), INPUT(_type="submit"))
    albumlist = request.vars.albumlist
    if albumlist != "":
        rx = re.compile("([\w|\s]+),([\w|\s]+)\d+.")
        albums = rx.findall(albumlist)
    return locals()

def album_show():
    album = db.t_album(request.args(0))
    songs = db(db.t_song.f_album_id_reference==album.id).select()
    return locals()

def buildquery(searchstring, varstring):
    keywords = searchstring.split()
    sqlstr = ""
    for kw in keywords:
        sqlstr += " AND (" + varstring + " LIKE '%" + kw + "%')"
    return sqlstr

from gluon.tools import Auth
auth = Auth(db)
auth.define_tables()
    
def song_search():
    form=FORM(DIV("Search Artists : ", INPUT(_name="artistkeywords")), \
        DIV("Search Collections : ", INPUT(_name="albumkeywords")), \
        DIV("Search Songs : ", INPUT(_name="songkeywords")), \
        INPUT(_type="submit"))
    query = request.vars.songkeywords
    sql = "SELECT t_artist.f_name, t_album.f_title, t_song.f_title FROM t_artist, t_album, t_song" + \
        " WHERE t_artist.id=t_album.f_artist_id_reference AND t_song.f_album_id_reference=t_album.id"
    if request.vars.songkeywords != None:
        sql += buildquery(request.vars.songkeywords, "t_song.f_title")
    if request.vars.artistkeywords != None:
        sql += buildquery(request.vars.artistkeywords, "t_artist.f_name")
    if request.vars.albumkeywords != None:        
        sql += buildquery(request.vars.albumkeywords, "t_album.f_title")        

    rows = db.executesql(sql)
    profile = db().select(db.auth_user.first_name)
    return locals()

@auth.requires_login()
def shoppingcart():
    return 'this requires login'
