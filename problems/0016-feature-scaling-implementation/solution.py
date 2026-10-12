import numpy as np
def feature_scaling(data: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
	data=data.astype(float)
	a=np.mean(data,axis=0)
	b=np.std(data,axis=0)
	data_min=np.min(data,axis=0)
	data_max=np.max(data,axis=0)
	data_range=data_max-data_min
	stds=np.where(b==0,1,b)

	standardized_data=(data-a)/stds
	normalized_data = (data - data_min) / data_range

	return (np.round(standardized_data, 4),np.round(normalized_data, 4))