import numpy as np
import pandas as pd
from scipy.signal import find_peaks 
from main import p4_parameters
from plots import p4_time_against_N_plot
from p2_marked_state_probability_against_time import p2
from optimum_gammaNs import read_optimum_gammaNs, lookup_gamma


def p4(start_N, end_N, end_time, time_step, opt_gammaNs, alpha, marked, step_N=1):
    dimensions = list(range(start_N, end_N+1, step_N))
    opt_times = []
    for N in dimensions:
        gamma = lookup_gamma(opt_gammaNs, N)
        times, marked_amplitude = p2(N, gamma, alpha, marked, end_time, time_step)
        marked_probability = np.multiply(np.conj(marked_amplitude), marked_amplitude)
        #opt_time = times[np.argmax(marked_probability)]
        peaks, _ = find_peaks(marked_probability, height=(0.7, 1.05))
        opt_time = times[peaks[0]]
        opt_times.append(opt_time)
        print(f'Computed unitary time of {opt_time} for {N} dimensions (up to {end_N}) '
              f'with gammaN = {gamma*N}')
    return dimensions, opt_times


if __name__ == "__main__":
    start_N = p4_parameters['start_dimensions']
    end_N = p4_parameters['end_dimensions']
    step_N = p4_parameters['step_dimensions']
    end_time = p4_parameters['end_time'] 
    time_step = p4_parameters['time_step'] 
    marked_state = p4_parameters['marked_state']
    alpha = p4_parameters['alpha']                             
    optimum_gammaNs = p4_parameters['optimum_gammaNs']
    save_plots = p4_parameters['save_plots']

    if isinstance(optimum_gammaNs, str):
        optimum_gammaNs = read_optimum_gammaNs(optimum_gammaNs, 'dimensions')

    # Minimum gaps against dimensions
    dimensions, opt_times = p4(start_N, end_N, end_time, time_step, optimum_gammaNs, alpha, marked_state, step_N)

    p4_time_against_N_plot(dimensions, opt_times, alpha, optimum_gammaNs, save_plots)