from dealerReviewRanker import getTopReviewsFromUrl

DEALER_URL = "https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/#mobileLink"

if __name__ == "__main__":
	try:
		reviews = getTopReviewsFromUrl(DEALER_URL, 3)
		print()
		print("Top 3 overly positive reviews (most positive listed first):")
		for count, r in enumerate(reviews):
			print("{}:".format(count+1))
			print(r)
	except Exception as e:
		print(repr(e))
