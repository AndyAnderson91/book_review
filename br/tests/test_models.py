import datetime

from django.test import TestCase
from django.contrib.auth.models import User
from br.models import Book, Author, Genre, Review


class AuthorTestCase(TestCase):
    """
    Class for testing Author model
    """
    @classmethod
    def setUpTestData(cls):
        # Author with full name
        cls.full_name_author = Author.objects.create(
            id=1,
            first_name='Anton',
            patronymic='Pavlovich',
            last_name='Chekhov',
            born=datetime.date(1860, 1, 17)
        )
        # Author with short name
        cls.short_name_author = Author.objects.create(
            id=2,
            first_name='Jack',
            last_name='London',
            born=datetime.date(1876, 1, 12)
        )

    def test_unique_together_full_name(self):
        """
        Expects Exception raising since Author model has unique_together constraint on [first_name, patronymic, last_name, born]
        """
        with self.assertRaises(Exception):
            Author.objects.create(
                first_name='Anton',
                patronymic='Pavlovich',
                last_name='Chekhov',
                born=datetime.date(1860, 1, 17)
            )

    def test_unique_together_short_name(self):
        """
        Expects Exception raising since Author model has unique_together constraint on [first_name, patronymic, last_name, born]
        """
        with self.assertRaises(Exception):
            Author.objects.create(
                first_name='Jack',
                last_name='London',
                born=datetime.date(1876, 1, 12)
            )

    def test_str_representation_full_name(self):
        """
        Expects 'first_name patronymic last_name' str representation for authors with patronymic field filled
        """
        expected_full_name = "{0} {1} {2}".format(
            self.full_name_author.first_name,
            self.full_name_author.patronymic,
            self.full_name_author.last_name
        )
        self.assertEqual(expected_full_name, str(self.full_name_author))

    def test_str_representation_short_name(self):
        """
        Expects 'first_name last_name' str representation for authors with patronymic field empty
        """
        expected_short_name = "{0} {1}".format(
            self.short_name_author.first_name,
            self.short_name_author.last_name
        )
        self.assertEqual(expected_short_name, str(self.short_name_author))


class BookTestCase(TestCase):
    """
    Class for testing Book model
    """
    @classmethod
    def setUpTestData(cls):
        # Book published some time ago
        cls.past_book = Book.objects.create(
            title='past_book',
            pub_date=datetime.date.today() - datetime.timedelta(days=10)
        )
        # Book published today
        cls.today_book = Book.objects.create(
            title='present_book',
            pub_date=datetime.date.today()
        )
        # Book to be released in the future
        cls.future_book = Book.objects.create(
            title='future_book',
            pub_date=datetime.date.today() + datetime.timedelta(days=10)
        )

    def test_book_is_published_method(self):
        """
        is_published() method should return True if pub_date <= today
        """
        self.assertTrue(self.past_book.is_published())
        self.assertTrue(self.today_book.is_published())
        self.assertFalse(self.future_book.is_published())

    def test_unique_together(self):
        """
        Expects Exception raising since Book model has unique_together constraint on [title, pub_date]
        """
        with self.assertRaises(Exception):
            Book.objects.create(
                title='present_book',
                pub_date=datetime.date.today()
            )


class ReviewTestCase(TestCase):
    """
    Class for testing Review model
    """
    @classmethod
    def setUpTestData(cls):
        # book is required as foreign_key field in Review
        book = Book.objects.create(
            title='book',
            pub_date=datetime.date.today(),
        )
        # same with user
        owner = User.objects.create_user(
            username='andy',
            password='1'
        )
        # review on 'book' by 'andy' user
        Review.objects.create(
            book=book,
            owner=owner,
            rating=5
        )

    def test_unique_together(self):
        """
        Expects Exception raising since book may have only 1 review per user
        """
        with self.assertRaises(Exception):
            Review.objects.create(
                book=Book.objects.get(title='book'),
                owner=User.objects.get(username='andy')
            )



