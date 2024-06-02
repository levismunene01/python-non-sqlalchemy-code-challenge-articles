class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.__class__.all.append(self)

    @classmethod
    def all(cls):
        return cls.all

class Author:
    all = []

    def __init__(self, name):
        self.name = name
        self.__class__.all.append(self)

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list(set([magazine.category for magazine in self.magazines()]))

    @classmethod
    def all(cls):
        return cls.all

class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.__class__.all.append(self)

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = [author for author in self.contributors() if len(author.articles()) > 2]
        return authors if authors else None

    @classmethod
    def all(cls):
        return cls.all
