from momentum.functions import forgettingvar_init, forgettingvar_update
from pprint import pprint


def test_forget():
    import numpy as np
    xs = list(np.random.randn(5000))+list(2*np.random.randn(5000))
    m = forgettingvar_init(alpha=0.01)
    for x in xs:
        m = forgettingvar_update(m,x)
    assert 1.6<m['std']<2.4
    assert -0.5<m['mean']<0.5


if __name__=='__main__':
    test_forget()

