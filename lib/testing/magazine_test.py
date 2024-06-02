import pytest
from classes.many_to_many import Article, Magazine, Author

class TestMagazine:
    """Tests for the Magazine class"""

    def test_has_name(self):
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        assert magazine_1.name == "Vogue"
        assert magazine_2.name == "AD"

    def test_name_is_mutable_string(self):
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_1.name = "New Yorker"
        assert magazine_1.name == "New Yorker"

        # To test type constraint uncomment below:
        # with pytest.raises(Exception):
        #     magazine_1.name = 2

    def test_name_len(self):
        magazine_1 = Magazine("Vogue", "Fashion")
        assert 2 <= len(magazine_1.name) <= 16

        # To test length constraint uncomment below:
        # with pytest.raises(Exception):
        #     magazine_1.name = "New Yorker Plus X"

    def test_has_category(self):
        magazine_1 = Magazine("Vogue", "Fashion")
        assert magazine_1.category == "Fashion"

    def test_category_is_mutable_string(self):
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_1.category = "Life Style"
        assert magazine_1.category == "Life Style"

        # To test type constraint uncomment below:
        # with pytest.raises(Exception):
        #     magazine_1.category = 2

    def test_category_len(self):
        magazine_1 = Magazine("Vogue", "Fashion")
        assert magazine_1.category != ""

        # To test empty category constraint uncomment below:
        # with pytest.raises(Exception):
        #     magazine_1.category = ""

    def test_has_many_articles(self):
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        article_1 = Article(author_1, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author_1, magazine_1, "Dating life in NYC")

        assert len(magazine_1.articles()) == 2
        assert article_1 in magazine_1.articles()
        assert article_2 in magazine_1.articles()

    def test_articles_of_type_articles(self):
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        Article(author_1, magazine_1, "How to wear a tutu with style")

        assert isinstance(magazine_1.articles()[0], Article)

    def test_has_many_contributors(self):
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine_1 = Magazine("Vogue", "Fashion")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_2, magazine_1, "Dating life in NYC")

        assert len(magazine_1.contributors()) == 2
        assert author_1 in magazine_1.contributors()
        assert author_2 in magazine_1.contributors()

    def test_contributors_of_type_author(self):
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine_1 = Magazine("Vogue", "Fashion")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_2, magazine_1, "Dating life in NYC")

        assert all(isinstance(contributor, Author) for contributor in magazine_1.contributors())

    def test_contributors_are_unique(self):
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine_1 = Magazine("Vogue", "Fashion")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_1, magazine_1, "How to be single and happy")
        Article(author_2, magazine_1, "Dating life in NYC")

        assert len(set(magazine_1.contributors())) == len(magazine_1.contributors())

    def test_article_titles(self):
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        Article(author_1, magazine_1, "How to wear a tutu with style")

        assert magazine_1.article_titles() == ["How to wear a tutu with style"]

    def test_contributing_authors(self):
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine_1 = Magazine("Vogue", "Fashion")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_1, magazine_1, "How to be single and happy")
        Article(author_1, magazine_1, "Dating life in NYC")
        Article(author_2, magazine_1, "2023 Eccentric Design Trends")

        assert author_1 in magazine_1.contributing_authors()
        assert author_2 not in magazine_1.contributing_authors()
        assert all(isinstance(author, Author) for author in magazine_1.contributing_authors())
