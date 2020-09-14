# news class starts here
class news:
    def __init__(self, author, title, description, url, urlToImage, publishedAt):
        self.author = author
        self.title  = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt  = publishedAt

# source class starts here which defines the source of objects
class source:
    def __init__(self, id,name,url):
        self.id = id
        self.name = name
        self.url = url


