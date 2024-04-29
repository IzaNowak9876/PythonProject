from faker import Faker

class NewsletterData:
    def __init__(self):
        fake = Faker("pl_PL")
        self.newsletter_email = fake.email()
