# Overview
The following tool outputs the top 3 positive reviews for "McKaig Chevrolet Buick" from [DealerRater](https://www.DealerRater.com). 

## "Positiveness" calculation
A review has an overall rating, as well as ratings for different sub-categories such as "Customer Service" and "Pricing". Each of these ratings are out of 5 stars.

Thus, the "positiveness" of a review is calculated as follows:
1. For each rating, subtract by 3, and then add all ratings up.
2. Multiply the sum by the number of exclamation marks in the review (or multiply by 1 if there are no exclamation marks).

In other words, the calculation is as follows
```
sum(rating - 3 for rating in allRatings) * max(1, num exclamation marks in review)
```
where `allRatings` is a list containing the overall rating and the ratings for each of the sub-categories.

For example, if a review has an overall rating of 4/5, with sub-category ratings of 4/5 for "Customer Service" and 5/5 for "Pricing", and the review has 2 exclamation marks in it, then its overall "positiveness" rating is:
```
(1+1+2)*2 = 8
```

## Running the tool
From the current directory (where this README is), run
```
python positiveReviewDetector/main.py 
```

## Additional packages installed
The BeautifulSoup library was used for webscraping, and was installed with:
```
conda install -c anaconda beautifulsoup4
```
See [bs4 documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## How to run all tests
Navigate to the `positiveReviewDetector/test` directory and run
```
python -m unittest discover .
```