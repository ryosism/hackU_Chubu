class InsertReviewApiRequest:
    def __init__(self, kougiID, star, title, text):
        self.kougiID = kougiID
        self.star = star
        self.title = title
        self.text = text
