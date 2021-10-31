import sys 
sys.path.append('..')

from bs4 import BeautifulSoup
from dealerReview import DealerReview
from datetime import datetime
from dealerReviewRanker import *
import unittest

class TestDealerReviewRanker(unittest.TestCase):
    def setUp(self):
        reviewsBinary = open("test_reviews_page.txt", "rb")
        binary = reviewsBinary.read()
        reviewsBinary.close()
        soup = BeautifulSoup(binary, 'html.parser')
        self.review = DealerReview(soup.find_all("div", class_="review-entry")[0])
        self.review2 = DealerReview(soup.find_all("div", class_="review-entry")[1])
        self.allReviews = [DealerReview(r) for r in soup.find_all("div", class_="review-entry")]

    def test_numExclamations(self):
        self.assertEqual(numExclamations(self.review), 0)
        self.assertEqual(numExclamations(self.review2), 2)

    def test_totalRankOfSubRatings(self):
        self.assertEqual(totalRankOfSubRatings(self.review), 8)

    def test_ratingToRank(self):
        self.assertEqual(ratingToRank(5), 2)
        self.assertEqual(ratingToRank(4), 1)
        self.assertEqual(ratingToRank(3), 0)
        self.assertEqual(ratingToRank(2), -1)
        self.assertEqual(ratingToRank(1), -2)
        self.assertEqual(ratingToRank(0), -3)

    def test_rank(self):
        self.assertEqual(
            [rank(r) for r in self.allReviews],
            [10, 18, 11, 30, 12, 10, 10, 10, 10, 40]
        )

    def test_getTopReviews(self):
        top3 = getTopReviews(self.allReviews, 3)
        self.assertEqual(top3[0], self.allReviews[9])
        self.assertEqual(top3[1], self.allReviews[3])
        self.assertEqual(top3[2], self.allReviews[1])

if __name__ == '__main__':
    unittest.main()