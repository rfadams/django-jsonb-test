import random
import django

from django.db.models import Q, F, DecimalField
from pprint import pprint
from data.models import DummyData


def run():
    print DummyData.objects.count()

    # for i in range(400):
    #     meta = {
    #         'value_1': random.randint(0, 1000)
    #     }
    #
    #     if i >= 100:
    #         meta['value_2'] = random.randint(0, 10000)
    #     if i >= 200:
    #         meta['value_3'] = random.randint(0, 100000)
    #     if i >= 300:
    #         meta['value_4'] = random.randint(0, 1000000)
    #
    #     DummyData.objects.create(
    #             num_of_people = i,
    #             budget = (random.randrange(10000)/100.0),
    #             meta = meta
    #     )


    print DummyData.objects.annotate(tot_value=(F('num_of_people')*F('budget')), output_field=DecimalField())
        # print o.__dict__

    print 'done'


