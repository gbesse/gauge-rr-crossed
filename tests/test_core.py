import unittest,math
from gauge_rr_crossed.core import run
class DomainTests(unittest.TestCase):
 def fixture(self):return {'measurements':[dict(part=p,operator=o,value=base+offset+e)for p,base in [('A',0),('B',10)]for o,offset in [('X',0),('Y',2)]for e in [-1,1]]}
 def test_anova_sum(self):
  d=self.fixture();x=run(d);vs=[r['value']for r in d['measurements']];mean=sum(vs)/len(vs);self.assertAlmostEqual(sum(v['ss']for v in x['anova'].values()),sum((v-mean)**2 for v in vs));self.assertEqual(x['raw_variance_components']['repeatability'],2)
 def test_raw_negative_visible(self):self.assertLess(run(self.fixture())['raw_variance_components']['interaction'],0)
 def test_unbalanced(self):
  d=self.fixture();d['measurements'].pop()
  with self.assertRaises(ValueError):run(d)
