import datetime

class DealerReview:
	def __init__(self, review):
		"""
		Args:
			review (A Tag object from BeautifulSoup4): 
				A dealer review as a Tag object from the BeautifulSoup4 package.
				For more info about the type of this object, see
				https://www.crummy.com/software/BeautifulSoup/bs4/doc/
		"""
		self.review = review

	def reportParsingError(self, infoType):
		print('Could not parse overall dealership rating from review: \n{}\n'.format(str(self.review)))

	def createdOn(self):
		try:
			dateStr = self.review.find_all("div", class_='review-date')[0].select("div")[0].text
			return datetime.strptime(dateStr, '%b %d, %Y')
		except Exception as e:
			self.reportParsingError("review creation date")
			raise

	def overallRating(self):
		try:
			overallRatingHtml = self.review.find_all("div", class_="dealership-rating")[0]
			return int(list(overallRatingHtml.children)[3]['class'][2].split('-')[1][0])
		except Exception as e:
			self.reportParsingError("overall dealership rating")
			raise

	def reviewer(self):
		pass

	def review(self):
		pass

	def customerServiceRating(self):
		pass

	def friendlinessRating(self):
		pass

	def pricingRating(self):
		pass 

	def overallExpRating(self):
		pass

	def recommendDealer(self):
		pass

	def rawBs4Tag(self):
		return self.review

	def __repr__(self):
		pass
