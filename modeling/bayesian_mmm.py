import pandas as pd
import pymc3 as pm
import arviz as az
import numpy as np

def run_bayesian_mmm(df, media_vars, target_var):
    '''
    Implements Bayesian Marketing Mix Model.
    df: DataFrame with media spend columns and target outcomes.
    media_vars: list of spend column names.
    target_var: string; name of dependent variable.
    Returns: PyMC3 trace and AzDataInferred.
    '''
    data = df.copy()
    y = data[target_var].values
    X = data[media_vars].values

    with pm.Model() as mmm:
        # Priors
        alphas = pm.Normal('alphas', mu=0, sigma=1, shape=len(media_vars))
        intercept = pm.Normal('intercept', mu=0, sigma=1)
        sigma = pm.HalfNormal('sigma', sigma=1)

        # Adstock decay parameters
        theta = pm.Beta('theta', alpha=2, beta=2, shape=len(media_vars))
        adstocked = []
        for i, var in enumerate(media_vars):
            ad = pm.Deterministic(
                f'adstock_{var}',
                np.array([data[var].iloc[t] + theta[i] * (adstocked[i][t-1] if t>0 else 0)
                          for t in range(len(data))])
            )
            adstocked.append(ad)

        mu = intercept
        for i in range(len(media_vars)):
            mu += alphas[i] * adstocked[i]

        y_obs = pm.Normal('y_obs', mu=mu, sigma=sigma, observed=y)
        trace = pm.sample(draws=1000, tune=1000, target_accept=0.9)
        summary = az.summary(trace, round_to=2)

    return trace, summary
