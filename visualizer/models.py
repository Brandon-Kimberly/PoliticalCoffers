from django.db import models

# Create your models here.

class Donation(models.Model):
    amount = models.DecimalField(default=0, decimal_places=2, max_digits=11)

    def __str__(self):
        return str(self.amount)

class Candidate(models.Model):
    name = models.CharField(max_length=200)
    party = models.CharField(max_length=50)
    total_donation_amount = models.DecimalField(default=0, decimal_places=2, max_digits=15)
    total_spent_amount = models.DecimalField(default=0, decimal_places=2, max_digits=15)
    beginning_cash = models.DecimalField(default=0, decimal_places=2, max_digits=15)
    ending_cash = models.DecimalField(default=0, decimal_places=2, max_digits=15)
    total_ind_contrib = models.DecimalField(default=0, decimal_places=2, max_digits=15)
    year = models.CharField(default="0000", max_length=4)

    def __str__(self):
        return self.name + "\n" + self.party + "\n" + str(self.total_donation_amount) + "\n" + str(self.total_spent_amount) + str(self.beginning_cash) + "\n" + str(self.ending_cash) + "\n" + str(self.total_ind_contrib) + "\n" + self.year