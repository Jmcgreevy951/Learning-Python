def make_album(artist, album, release=None):
    music = {'name': artist, 'record': album}
    if release.lower() != 'n/a':
        music['release'] = release
    return music