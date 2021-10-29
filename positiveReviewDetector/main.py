if __name__ == "__main__":
	try:
		DEALER_URL = "https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-review-23685"
		for count, r in enumerate(getTopReviews(DEALER_URL, 3)):
			print("{}:".format(count+1))
			print(r)
			print()
	except Exception as e:
		print(repr(e))
