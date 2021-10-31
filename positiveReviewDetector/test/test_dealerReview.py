import sys 
sys.path.append('..')

from bs4 import BeautifulSoup
from dealerReview import DealerReview
from datetime import datetime
import unittest

class TestDealerReviewParsing(unittest.TestCase):
    maxDiff = None
    def setUp(self):
        reviewsBinary = open("test_reviews_page.txt", "rb")
        binary = reviewsBinary.read()
        reviewsBinary.close()
        soup = BeautifulSoup(binary, 'html.parser')
        self.review = DealerReview(soup.find_all("div", class_="review-entry")[0])
        self.reviewText = "This is the best dealership I have ever walked into and dealt with. The employees are the friendliest and professional at the same time. There was no pressure and all questions answered. Kristina by far was the best saleswoman I’ve worked with as well. She made sure everything was taken care of from our happiness to also our particular vehicular needs."

    def test_createdOn(self):
        self.assertEqual(self.review.createdOn(), datetime.strptime("October 30, 2021", '%B %d, %Y'))

    def test_overallRating(self):
        self.assertEqual(self.review.overallRating(), 5)

    def test_reviewer(self):
        self.assertEqual(self.review.reviewer(), "hill212000")

    def test_reviewText(self):
        self.assertEqual(self.review.reviewText(), self.reviewText)

    def test_repr(self):
        self.assertEqual(
            str(self.review),
            "Created on: October 30, 2021\n" +  
            "Overall Rating: 5/5\n" +
            "Reviewer: hill212000\n" +
            "Review: {}\n".format(self.reviewText)
        )

if __name__ == '__main__':
    unittest.main()