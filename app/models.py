class Article:
    '''
    news articles class starts here
    '''
    def __init__(self, author, title, description, url, urlToImage, publishedAt):
        self.author = author
        self.title  = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt  = publishedAt

# source class starts here which defines the source of objects
class Source:
    def __init__(self, id,name,description,url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url

# category class
class Category:
    def __init__(self, title, description, url, urlToImage, publishedAt):
        self.title  = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt  = publishedAt

# headlines class
class Headlines:
    def __init__(self, title, description, url, urlToImage, publishedAt):
        self.title  = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt  = publishedAt
