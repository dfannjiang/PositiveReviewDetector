from dealerReview import DealerReview 
import requests
import re

def getTopReviews(url, limit=None):
	"""
	Args:
		url (string): 
			Url of first page of reviews of a dealer at 
		    DealerRater.com. Must start with "https://dealerrater.com".
		limit  (int): 
			Number of reviews to return

	Returns (list):
	    Top "limit" positive reviews for dealer at "url". If "limit" not
	    provided, all reviews will be returned. In either case, result
	    is returned sorted by most positive first.

	    Only reviews on the first 5 pages of reviews are considered.
	"""
	baseUrl =  '/'.join(url.split('/')[:3])
	reviewObjs = []

	reviewPagesToVisit = 5
	while reviewPagesToVisit > 0:

		# Get reviews from current page
		currPage = requets.get(url)
		soup = BeautifulSoup(page)
		reviews = soup.find_all("div", class_="review-entry")
		reviewObjs += [DealerReview(r) for r in reviews]

		# Decrement because we have just visited a reviews page
		reviewPagesToVisit -= 1

		# Get next reviews page to visit
		nextPageButton = soup.select('div.next.page')
		if nextPageButton[0] and nextPageButton[0].has_attr('on_click'):
			url = baseUrl + nextPageButton[0].findChildren("a")[0]['href']


	# Sort reviews by rank: smaller rank value means review is more positive
	sortedReviews = sorted(reviewObjs, key=rank)

	if limit:
		return sortedReviews[:limit]
	else:
		return sortedReviews


"""
Ranker
"""
def rank(review):
	"""
	Args:
		review (A Tag object from BeautifulSoup4): 
			A dealer review as a Tag object from the BeautifulSoup4 package.
			For more info about the type of this object, see
			https://www.crummy.com/software/BeautifulSoup/bs4/doc/

	Returns (int): 
		An integer. The lower it is, the more positive a review it is.
	"""
	return -1

"""
Features
"""