from mongoengine import QuerySet
from django.conf import settings

def sum_template(form):
    pipeline = [
            {
                "$group": {
                    "_id" : { "$dateToString": { 
                        "date": "$createdAt", 
                        "format": form, }},
                    "value": { "$sum" : "$amount"}
                }
            },
            {
                "$sort": { "_id": -1}
            },
            {
                "$project": {
                    "key": "$_id",
                    "_id": 0,
                    "value": 1
                }
            }
        ]
    return pipeline

def count_template(form):
    pipeline = [
            {
                "$group": {
                    "_id" : { "$dateToString": { 
                        "date": "$createdAt", 
                        "format": form, }},
                    "value": { "$count" : {}}
                }
            },
            {
                "$sort": { "_id": -1}
            },
            {
                "$project": {
                    "key": "$_id",
                    "_id": 0,
                    "value": 1
                }
            }
        ]
    return pipeline


class TransactionQuerySet(QuerySet):

    def is_overload(self):
        return self.count() > settings.MAX_TRANSACTION_COUNT

    def get_daily_sum(self):
        return self.aggregate(sum_template("%Y-%m-%d"))

    def get_weekly_sum(self):
        return self.aggregate(sum_template("%Y/%U"))

    def get_monthly_sum(self):
        return self.aggregate(sum_template("%Y-%m"))

    def get_daily_count(self):
        return self.aggregate(count_template("%Y-%m-%d"))

    def get_weekly_count(self):
        return self.aggregate(count_template("%Y/%U"))

    def get_monthly_count(self):
        return self.aggregate(count_template("%Y-%m"))