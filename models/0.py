from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'My New App'
settings.subtitle = 'powered by web2py'
settings.author = 'you'
settings.author_email = 'you@example.com'
settings.keywords = ''
settings.description = 'Catalog of Christian musicians and their songs'
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = 'f2b41437-75a0-458a-b207-447955816e9d'
settings.email_server = 'localhost'
settings.email_sender = 'you@example.com'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = ['']
