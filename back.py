from threading import Thread

def app():
  !clip-retrieval back --port 1234 --indices-paths indices_paths.json

if __name__ == '__main__':
    t1 = Thread(target = app)
    a = t1.start()
    !lt --port 1234