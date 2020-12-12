from matplotlib import pyplot as plt
import numpy as np


'''
Author: A. Rupam Mahmood (https://armahmood.github.io/)
Make y-label horizontal
'''
plt.plot(np.random.randn(100))
h = plt.ylabel('Overall\n average\n return', labelpad=20)
h.set_rotation(0)
plt.show()


def avg_return_curve(x, y, stride, total_steps):
  '''
  Author: A. Rupam Mahmood (https://armahmood.github.io/)
  Plot average return curves. Specifically, this function transforms termination 
  steps and episodic returns to average returns over equally-spaced intervals.
    param x: A list of list of termination steps for each episode. len(x) == total number of runs 
    param y: A list of list of episodic return. len(y) == total number of runs
    param stride: The timestep interval between two aggregate datapoints to be calculated
    param total_steps: The total number of time steps to be considered 
    return: time steps for calculated data points, average returns for each data points, std-errs
  '''
  assert len(x) == len(y)
  num_runs = len(x)
  avg_ret = np.zeros(total_steps // stride)
  stderr_ret = np.zeros(total_steps // stride)
  avg_ret2 = np.zeros(total_steps // stride)
  stderr_ret2 = np.zeros(total_steps // stride)
  steps = np.arange(stride, total_steps + stride, stride)
  num_rets = np.zeros( total_steps // stride)
  for i in range(0, total_steps // stride):
      rets = []
      avg_rets_per_run = []
      for run in range(num_runs):
          xa = np.array(x[run])
          ya = np.array(y[run])
          rets.append(ya[np.logical_and(i*stride < xa, xa <= (i+1)*stride)].tolist())
          avg_rets_per_run.append(np.mean(rets[-1]))
      flat_rets = np.array([ret for l in rets for ret in l])
      num_rets[i] = flat_rets.shape[0]
      avg_ret[i] = flat_rets.mean()
      stderr_ret[i] = flat_rets.std()/np.sqrt(num_rets[i])
      avg_ret2[i] = np.mean(avg_rets_per_run)
      stderr_ret2[i] = np.std(avg_rets_per_run) / np.sqrt(num_runs)
  return steps, avg_ret, stderr_ret, num_rets, avg_ret2, stderr_ret2