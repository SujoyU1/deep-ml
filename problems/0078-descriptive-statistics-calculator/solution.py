import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
   
    # Find mode
    values, counts = np.unique(data, return_counts=True)
    mode = values[np.argmax(counts)]

    # Percentiles
    p25 = np.percentile(data, 25)
    p50 = np.percentile(data, 50)
    p75 = np.percentile(data, 75)

    # Create dictionary
    result = {
        'mean': np.mean(data),
        'median': np.median(data),
        'mode': mode,
        'variance': np.var(data),
        'standard_deviation': np.std(data),
        '25th_percentile': p25,
        '50th_percentile': p50,
        '75th_percentile': p75,
        'interquartile_range': p75 - p25
    }

    return result