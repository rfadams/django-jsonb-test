import random

from django.test import TestCase
from django.db.models import Q, F, DecimalField, FloatField, Sum, Avg, Min, Max, Count

from pprint import pprint
from data.models import DummyData

class DummyDataTestCase(TestCase):
    def setUp(self):
        print 'START', '*'*50

        value_4_count = 0
        value_4_sum = 0
        for i in range(400):
            meta = {
                'value_1': random.randint(0, 1000)
            }

            if i >= 100:
                meta['value_2'] = random.randint(0, 10000)
            if i >= 200:
                meta['value_3'] = random.randint(0, 100000)
            if i >= 300:
                meta['value_4'] = random.randint(0, 1000000)
                value_4_count = value_4_count+1 if meta['value_4'] <= 100000 else value_4_count
                value_4_sum += meta['value_4']

            DummyData.objects.create(
                    num_of_people = i,
                    budget = (random.randrange(10000)/100.0),
                    meta = meta
            )

        print DummyData.objects.count()
        print value_4_count
        print value_4_sum

    def test_dynamic_values(self):
        tot_value_sum = 0
        for o in DummyData.objects.annotate(tot_value=Min(F('num_of_people')/F('budget'), output_field=DecimalField())):
            print o.num_of_people, o.budget, o.tot_value
            tot_value_sum += o.tot_value

        print '='*30
        agg_tot_value = DummyData.objects.aggregate(tot_value_sum=Sum(F('num_of_people')/F('budget'), output_field=DecimalField()))
        print tot_value_sum

        self.assertEqual(tot_value_sum, agg_tot_value['tot_value_sum'])

    def test_jsonb_field(self):
        print 'Has value_1', DummyData.objects.filter(meta__has='value_1').count()
        print 'Has value_2', DummyData.objects.filter(meta__has='value_2').count()
        print 'Has value_3', DummyData.objects.filter(meta__has='value_3').count()
        print 'Has value_4', DummyData.objects.filter(meta__has='value_4').count()


        print 'Has value_3 OR value_4', DummyData.objects.filter(meta__has_any=['value_3', 'value_4']).count()
        print 'Has value_1 AND value_4', DummyData.objects.filter(meta__has_all=['value_1', 'value_4']).count()
        
        print 'Has value_4__lte=100000', DummyData.objects.filter(meta__value_4__lte=100000).count()

    def test_jsonb_agg(self):
        vals = DummyData.objects.filter(meta__has='value_4').select_json(value_4='meta__value_4').values('value_4')
        print vals
        # print vals.annotate(value_4_sum=Count('value_4'))

