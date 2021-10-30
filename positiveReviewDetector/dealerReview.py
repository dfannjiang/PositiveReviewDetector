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
		"""
		Prints an error message that information of infoType could not be
		parsed from the review
		"""
		print(
			'Could not parse overall dealership rating from review: \n{}\n'
				.format(str(self.review))
		)

	def extractRatingFromClass(self, classes):
		"""
		Returns (int):
			Given an array of CSS classes, where one of the classes is
			of the form "rating-(1-5)0", return the rating as an integer.
			For example, if "rating-50" is in classes, return 5 
		"""
		rgx = re.compile('rating-(\d)\d')
		return int(rgx.search(' '.join(classes)).group(1))

	def createdOn(self):
		"""
		Returns (datetime):
			A datetime object of when the review was created
		"""
		try:
			dateStr = self.review
				.find_all("div", class_='review-date')[0].select("div")[0].text
			return datetime.strptime(dateStr, '%b %d, %Y')
		except Exception as e:
			self.reportParsingError("review creation date")
			raise

	def overallRating(self):
		"""
		Returns (int):
			The overall rating of the review
		"""
		try:
			overallRatingHtml = self.review
				.find_all("div", class_="dealership-rating")[0]
			return self.extractRatingFromClass(
				list(overallRatingHtml.children)[3]['class']
			)
		except Exception as e:
			self.reportParsingError("overall dealership rating")
			raise

	def reviewer(self):
		"""
		Returns (str):
			The name of the reviewer
		"""
		try:
			review = self.review.find_all("div", class_="review-wrapper")[0]
			reviewTitle = list(review.children)[3]

			# Text is of the form "- <reviewer name>"
			reviewer = reviewTitle.select("span")[0].text
			return reviewer[2:]
		except Exception as e:
			self.reportParsingError("reviewer name")
			raise

	def review(self):
		"""
		Returns (str):
			The body text of the review
		"""
		try:
			review = self.review.find_all("div", class_="review-wrapper")[0]
			reviewBody = list(review.children)[7]
			return reviewBody.select("p")[0].text
		except Exception as e:
			self.reportParsingError("review")
			raise

	def customerServiceRating(self):
		"""
		Returns (int):
			The customer service rating
		"""
		try:
			allRatings = self.review
				.find_all("div", class_="review-ratings-all")[0]
			
			customerServiceHtml = list(allRatings.children)[0].children.filter(
				lambda tag: list(tag.children)[0].text == "Customer Service"
			)[0]

			return self.extractRatingFromClass(
				list(customerServiceHtml.children)[1]['class']
			)
		except Exception as e:
			self.reportParsingError("Customer Service rating")
			raise

	def qualityOfWorkRating(self):
		"""
		Returns (int):
			The quality of work rating
		"""
		try:
			allRatings = self.review
				.find_all("div", class_="review-ratings-all")[0]
			
			customerServiceHtml = list(allRatings.children)[0].children.filter(
				lambda tag: list(tag.children)[0].text == "Quality of Work"
			)[0]

			return self.extractRatingFromClass(
				list(customerServiceHtml.children)[1]['class']
			)
		except Exception as e:
			self.reportParsingError("Quality of Work rating")
			raise

	def friendlinessRating(self):
		"""
		Returns (int):
			The friendliness rating
		"""
		try:
			allRatings = self.review
				.find_all("div", class_="review-ratings-all")[0]
			
			customerServiceHtml = list(allRatings.children)[0].children.filter(
				lambda tag: list(tag.children)[0].text == "Friendliness"
			)[0]

			return self.extractRatingFromClass(
				list(customerServiceHtml.children)[1]['class']
			)
		except Exception as e:
			self.reportParsingError("Friendliness rating")
			raise

	def pricingRating(self):
		"""
		Returns (int):
			The pricing rating
		"""
		try:
			allRatings = self.review
				.find_all("div", class_="review-ratings-all")[0]
			
			customerServiceHtml = list(allRatings.children)[0].children.filter(
				lambda tag: list(tag.children)[0].text == "Pricing"
			)[0]

			return self.extractRatingFromClass(
				list(customerServiceHtml.children)[1]['class']
			)
		except Exception as e:
			self.reportParsingError("Pricing rating")
			raise 

	def overallExpRating(self):
		"""
		Returns (int):
			The overall experience rating
		"""
		try:
			allRatings = self.review
				.find_all("div", class_="review-ratings-all")[0]
			
			customerServiceHtml = list(allRatings.children)[0].children.filter(
				lambda tag: list(tag.children)[0].text == "Overall Experience"
			)[0]

			return self.extractRatingFromClass(
				list(customerServiceHtml.children)[1]['class']
			)
		except Exception as e:
			self.reportParsingError("Overall Experience rating")
			raise

	def recommendDealer(self):
		"""
		Returns (bool):
			True if the reviewer recommends the dealer, and False if not
		"""
		try:
			allRatings = self.review
				.find_all("div", class_="review-ratings-all")[0]
			
			customerServiceHtml = list(allRatings.children)[0].children.filter(
				lambda tag: list(tag.children)[0].text == "Recommend Dealer"
			)[0]

			return 'YES' in list(customerServiceHtml.children)[1].text.upper()
		except Exception as e:
			self.reportParsingError("Recommend Dealer indicator")
			raise

	def rawBs4Tag(self):
		"""
		Returns (Tag object from BeautifulSoup4):
			The raw review data
		"""
		return self.review

	def __repr__(self):
		"""
		Returns a string of the form:

		Object: BeautifulSoup4.Tag
		Created on: May 20th, 2020
		Overall Rating: 4/5
		Reviewer: test reviewer
		Review: This is my review!
		Customer Service Rating: 5/5
		Quality of Work Rating: 5/5
		Friendliness Rating: 4/5
		Pricing Rating: 4/5
		Overall Experience Rating: 4/5
		Recommend Dealer: Yes
		"""
		return "Object: BeautifulSoup4.Tag\n" + str(self)

	def __str__(self):
		"""
		Returns a string of the form:

		Created on: May 20th, 2020
		Overall Rating: 4/5
		Reviewer: test reviewer
		Review: This is my review!
		Customer Service Rating: 5/5
		Quality of Work Rating: 5/5
		Friendliness Rating: 4/5
		Pricing Rating: 4/5
		Overall Experience Rating: 4/5
		Recommend Dealer: Yes
		"""
		return
			"Created on: {}\n"
				.format(datetime.strptime(self.createdOn(), '%b %d, %Y'))
			+ "Overall Rating: {}/5\n"
				.format(self.overallRating())
			+ "Reviewer: {}\n"
				.format(self.reviewer())
			+ "Review: {}\n"
				.format(self.review())
			+ "Customer Sevice Rating: {}/5\n"
				.format(self.customerServiceRating())
			+ "Quality of Work Rating: {}/5\n"
				.format(self.qualityOfWorkRating())
			+ "Friendliness Rating: {}/5\n"
				.format(self.friendlinessRating())
			+ "Pricing Rating: {}/5\n"
				.format(self.pricingRating())
			+ "Overall Experience Rating: {}/5\n"
				.format(self.overallExpRating())
			+ "Recommend Dealer: {}\n"
				.format('Yes' if self.recommendDealer() else 'No')
		
			





