import pandas as pd
from modeling.bayesian_mmm import run_bayesian_mmm

def test_bayesian_mmm_basic():
    df = pd.DataFrame({
        'facebook_spend': [100, 120, 90, 110],
        'google_spend': [200, 210, 190, 220],
        'sales': [20, 23, 19, 25]
    })
    trace, summary = run_bayesian_mmm(df, ['facebook_spend', 'google_spend'], 'sales')
    assert 'alphas' in trace.varnames
    assert summary.shape[0] > 0
