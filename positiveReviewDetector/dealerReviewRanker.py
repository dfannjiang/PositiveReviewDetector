from dealerReview import DealerReview 
from bs4 import BeautifulSoup
import requests
import re

def getTopReviewsFromUrl(url, limit=None):
	"""
	Args:
		url (string): 
			Url of first page of reviews of a dealer at 
		    DealerRater.com. Must start with "https://dealerrater.com".
		limit  (int): 
			Number of reviews to return.
			If not provided, all reviews are returned

	Returns (list):
	    Top "limit" positive reviews for dealer at "url". If "limit" not
	    provided, all reviews will be returned. In either case, result
	    is returned sorted by most positive first.

	    Only reviews on the first 5 pages of reviews are considered.
	"""
	baseUrl =  '/'.join(url.split('/')[:3])
	reviewObjs = []

	# Only consider the first 5 pages of reviews.
	reviewPagesToVisit = 5
	while reviewPagesToVisit > 0:
		print('Getting reviews from {}...'.format(url))
		# Get reviews from current page
		currPage = requests.get(url)
		soup = BeautifulSoup(currPage.content, 'html.parser')
		reviews = soup.find_all("div", class_="review-entry")
		reviewObjs += [DealerReview(r) for r in reviews]

		# Decrement because we have just visited a reviews page
		reviewPagesToVisit -= 1

		# Get next reviews page to visit
		nextPageButton = soup.select('div.next.page')
		if nextPageButton[0] and nextPageButton[0].has_attr('onclick'):
			url = baseUrl + nextPageButton[0].findChildren("a")[0]['href']

	print()
	return getTopReviews(reviewObjs, limit)

	

def getTopReviews(dealerReviews, limit=None):
	"""
	Args:
		dealerReviews (list):
			A list of DealerReview objects
		limit (int):
			Integer of number of reviews to return. If None, all are returned.

	Returns (list):
	    Top "limit" positive reviews among dealerReviews. If "limit" not
	    provided, all reviews will be returned. In either case, result
	    is returned sorted by most positive first.
	"""

	# Sort reviews by rank: higher rank value means review is more positive
	sortedReviews = sorted(dealerReviews, key=rank, reverse=True)

	if limit:
		return sortedReviews[:limit]
	else:
		return sortedReviews

"""
Ranker
"""
def rank(dealerReview):
	"""
	Args:
		review (A Tag object from BeautifulSoup4): 
			A dealer review as a Tag object from the BeautifulSoup4 package.
			For more info about the type of this object, see
			https://www.crummy.com/software/BeautifulSoup/bs4/doc/

	Returns (int): 
		An integer. The higher it is, the more positive a review it is.
	"""
	rank = ratingToRank(dealerReview.overallRating())
	rank += totalRankOfSubRatings(dealerReview)
	return rank * max(1, numExclamations(dealerReview))

"""
Features/Helpers
"""
def ratingToRank(rating):
	"""
	Returns (int):
		Review rank corresponding to a rating.
		5 (very good) transforms to 2
		3 (neutral) transforms to 0
		0 (terrible) transforms to -3
		etc.
	"""
	return rating - 3

def numExclamations(dealerReview):
	"""
	Returns (int):
		The number of exclamations in the review
	"""
	return dealerReview.reviewText().count('!')

def totalRankOfSubRatings(dealerReview):
	allRatings = dealerReview.rawBs4Tag() \
		.find_all("div", class_="review-ratings-all")[0]
    
	totalRank = 0
	for tag in list(allRatings.children)[3].find_all(class_="rating-static-indv"):
		totalRank += ratingToRank(
			dealerReview.extractRatingFromClass(tag['class'])
		)

	return totalRank




