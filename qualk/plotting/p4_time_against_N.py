import numpy as np
import pandas as pd
from scipy.signal import find_peaks 
from .p2_marked_state_probability_against_time import p2
from .plots import p4_time_against_N_plot, save_insert, noise_insert
from ..config import parameters
from ..optimise.optimum_gammaNs import read_optimum_gammaNs, lookup_gamma, check_optimum_gammaNs_parameter_type


def p4(start_N, end_N, end_time, time_step, opt_gammaNs, alpha, marked, chain, lat_dim, step_N=1):
    dimensions = list(range(start_N, end_N+1, step_N))
    opt_times = []
    for N in dimensions:
        gamma = lookup_gamma(opt_gammaNs, N)
        times, marked_amplitude = p2(N, gamma, alpha, marked, end_time, time_step, chain, lat_dim)
        marked_probability = np.abs(np.multiply(np.conj(marked_amplitude), marked_amplitude))
        peaks, _ = find_peaks(marked_probability, height=(0.3, 1.05))
        opt_time = times[peaks[0]]
        opt_times.append(opt_time)
        print(f'Computed unitary time of {opt_time} for {N} dimensions (up to {end_N}) '
              f'with gammaN = {gamma*N}')
    return dimensions, opt_times


def run():
    p4_parameters = parameters['p4']

    # Parameters
    chain = parameters['chain']
    lattice_dimension = parameters['lattice_dimension']
    alpha = parameters['alpha']      
    marked_state = parameters['marked_state']

    start_N = p4_parameters['start_dimensions']
    end_N = p4_parameters['end_dimensions']
    step_N = p4_parameters['step_dimensions']
    end_time = p4_parameters['end_time'] 
    time_step = p4_parameters['time_step'] 
    save_plots = p4_parameters['save_plots']

    lat_d_tag = '_lat_dim=2' if lattice_dimension==2 else ''
    chain_tag = '_' + chain
    optimum_gammaNs = f'optimum_gamma/alpha={alpha}{lat_d_tag}{chain_tag}/optimum_gammaNs.csv'
    optimum_gammaNs = check_optimum_gammaNs_parameter_type(optimum_gammaNs)

    # Minimum gaps against dimensions
    dimensions, opt_times = p4(start_N, end_N, end_time, time_step, optimum_gammaNs, alpha, marked_state, chain, lattice_dimension, step_N)

    p4_time_against_N_plot(dimensions, opt_times, alpha, optimum_gammaNs, save_plots, chain, lattice_dimension)

    # CSV
    if save_plots:
        p4_data = {
            'dimensions'                : dimensions,
            'opt_times'                 : opt_times
        }
        p4_df = pd.DataFrame(data=p4_data)

        p4_df.to_csv(f'data/p4_{chain}/alpha={alpha}_lat_dim={lattice_dimension}{save_insert()}{noise_insert()}.csv', index=False)