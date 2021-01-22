import math

# Online moment estimators
# https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Welford's_online_algorithm


def var_init()->dict:
    return {'count':0,'mean':0,'M2':0}


def var_update(m:dict,x:float)->dict:
    m['count']+= 1
    delta = x - m['mean']
    m['mean'] += delta / m['count']
    delta2 = x - m['mean']
    m['M2'] += delta * delta2
    m['var'] = m['M2'] / (m['count'] - 1) if m['count'] > 1 else 0
    m['pvar'] = m['M2'] / (m['count']) if m['count'] > 0 else 0
    m['std'] = math.sqrt(m['var']) if m['var'] > 0 else 0
    return m


def kurtosis_init()->dict:
    m = var_init()
    m.update({'M3':0,'M4':0})
    return m


def kurtosis_update(m:dict,x:float)->dict:
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


