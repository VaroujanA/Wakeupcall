import os
def give_name_find_path(name):
    subdirs = [x[0] for x in os.walk('.')]
    subdirs.remove('.')
    subdirs.remove('.\\__pycache__')
    for e in subdirs:
        for filename in os.listdir(e):
            if filename.endswith(".mp3"):
                if filename == str(name):
                    path = os.path.join(e, filename)
                    return path