import math


# Online moment estimators
# https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Welford's_online_algorithm


def var_init() -> dict:
    return {'count': 0, 'mean': 0, 'M2': 0}


def var_update(m: dict, x: float) -> dict:
    m['count'] += 1
    delta = x - m['mean']
    m['mean'] += delta / m['count']
    delta2 = x - m['mean']
    m['M2'] += delta * delta2
    m['var'] = m['M2'] / (m['count'] - 1) if m['count'] > 1 else 0
    m['pvar'] = m['M2'] / (m['count']) if m['count'] > 0 else 0
    m['std'] = math.sqrt(m['var']) if m['var'] > 0 else 0
    return m


def kurtosis_init() -> dict:
    m = var_init()
    m.update({'M3': 0, 'M4': 0})
    return m


def kurtosis_update(m: dict, x: float) -> dict:
    n1 = m['count']
    m['count'] = m['count'] + 1
    delta = x - m['mean']
    delta_n = delta / m['count']
    delta_n2 = delta_n * delta_n
    term1 = delta * delta_n * n1
    m['mean'] = m['mean'] + delta_n
    m['M4'] = m['M4'] + term1 * delta_n2 * (
            m['count'] * m['count'] - 3 * m['count'] + 3) + 6 * delta_n2 * m['M2'] - 4 * delta_n * m['M3']
    m['M3'] = m['M3'] + term1 * delta_n * (m['count'] - 2) - 3 * delta_n * m['M2']
    m['M2'] = m['M2'] + term1
    m['kurtosis'] = (m['count'] * m['M4']) / (m['M2'] * m['M2']) - 3
    m['skewness'] = m['M3'] / m['M2']
    return m


def rvar(m: dict, x: float = None, rho=0.01, n=10):
    """ One function that performs either initialization or an update.
        Pass m={} to initialize
    """
    if m:
        return rvar_update(m=m, x=x)
    else:
        return rvar_init(rho=rho, n=n)


def rvar_init(rho: float, n=10) -> dict:
    """ Recency weighted running variance
    :param rho:  How much to use the most recent observation
    :param n: How many obs to use standard variance calc for, before switching
    """
    assert 0 <= rho <= 1
    state = var_init()
    state.update({'rho': rho, 'n': n})
    return state


def rvar_update(m: dict, x: float) -> dict:
    if m['count'] < m['n']:
        rho = m['rho']
        m = var_update(m, x)
        m['rho'] = rho
        return m
    else:
        m['count'] += 1
        rho = m['rho']
        m['var'] = (1 - rho) * (m['var'] + rho * ((x - m['mean']) ** 2))
        m['mean'] = (1 - rho) * m['mean'] + rho * x
        m['pvar'] = ((m['count'] - 1) / m['count']) * m['var']  # Not sure this really makes sense :)
        if m.get('M2'):
            del m['M2']
        m['std'] = math.sqrt(m['var']) if m['var'] > 0 else 0
        return m
