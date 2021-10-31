from datetime import datetime
import re

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
		print('Could not parse {} from review:\n'.format(infoType))

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
			dateStr = self.review \
				.find_all("div", class_='review-date')[0].select("div")[0].text
			return datetime.strptime(dateStr, '%B %d, %Y')
		except Exception as e:
			self.reportParsingError("review creation date")
			raise

	def overallRating(self):
		"""
		Returns (int):
			The overall rating of the review
		"""
		try:
			overallRatingHtml = self.review \
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

	def reviewText(self):
		"""
		Returns (str):
			The body text of the review
		"""
		try:
			review = self.review.find_all("div", class_="review-wrapper")[0]
			reviewBody = list(review.children)[7]
			return reviewBody.select("p")[0].text.strip()
		except Exception as e:
			self.reportParsingError("review")
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

		Object: bs4.element.tag
		Created on: May 20th, 2020
		Overall Rating: 4/5
		Reviewer: test reviewer
		Review: This is my review!
		Recommend Dealer: Yes
		"""
		return "Object: bs4.element.tag\n" + str(self)

	def __str__(self):
		"""
		Returns a string of the form:

		Created on: May 20th, 2020
		Overall Rating: 4/5
		Reviewer: test reviewer
		Review: This is my review!
		Recommend Dealer: Yes
		"""
		return "Created on: {}\n".format(self.createdOn().strftime("%B %d, %Y")) + \
			"Overall Rating: {}/5\n".format(self.overallRating()) + \
			"Reviewer: {}\n".format(self.reviewer()) + \
			"Review: {}\n".format(self.reviewText())

	def __eq__(self, other):
		return str(self) == str(other)
		
			
