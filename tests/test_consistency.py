from momentum.objects import RunningVariance, RunningKurtosis
from momentum.functions import var_init, var_update, kurtosis_init, kurtosis_update
import os
import pprint

# Tested locally but not

def test_var_against_each_other():
    if os.environ.get('GITHUB_ACTIONS'):
        print('skipping')
    else:
        import numpy as np
        from statistics import variance, pvariance

    xs = list(np.random.randn(100))
    machine = RunningVariance()
    m = var_init()
    for x in xs:
        machine.update(value=x)
        m = var_update(m,x)
    dv1 = m['var']-machine.var()
    dv2 = m['pvar']-machine.pvar()
    assert(abs(dv1)<1e-8)
    assert(abs(dv2) < 1e-8)

    du1 = m['mean'] - machine.mean
    du2 = m['std'] - machine.std()
    assert(abs(du1)<1e-8)
    assert(abs(du2) < 1e-8)


def test_kurtosis():
    if os.environ.get('GITHUB_ACTIONS'):
        print('skipping')
    else:
        import numpy as np
        xs = list(np.random.randn(200))
        machine = RunningKurtosis()

        m = kurtosis_init()
        for x in xs:
            machine.update(value=x)
            m = kurtosis_update(m, x)

        k1 = machine.kurtosis()
        k2 = m['kurtosis']
        s1 = machine.kurtosis()
        s2 = m['kurtosis']

        assert (abs(k1 - k2) < 0.0001)
        assert (abs(s1 - s2) < 0.0001)