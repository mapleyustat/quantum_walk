import numpy as np
import random 


class Ket:

    def __init__(self, dimensions, type='s', marked=1, alpha=1, jth=2, j_list=[2]):
        """Creates different types of kets given by a letter."""
        self.dimensions = dimensions
        self.type = type.lower()
        if self.type == 'm':
            self.ket = Ket.marked_state(dimensions, marked)
            self.marked = marked
        elif self.type == 's':
            self.ket = Ket.superposition_state(dimensions)
        elif self.type == 'anti_s':
            self.ket = Ket.anti_superposition_state(dimensions)
        elif self.type == 'f':
            self.ket = Ket.fourier_state(dimensions, jth)
        elif self.type == 'fs':
            self.ket = Ket.fourier_superposition_state(dimensions, j_list)
        elif self.type == 'cos':
            self.ket = Ket.cosine_state(dimensions, jth)
        elif self.type == 'coss':
            self.ket = Ket.cosine_superposition_state(dimensions, j_list)
        elif self.type == 'a':
            self.ket = Ket.a_state(dimensions, alpha)
        elif self.type == 'b':
            self.ket = Ket.b_state(dimensions)
        elif self.type == 'sq':
            self.ket = Ket.squared_state(dimensions)
        else:
            raise ValueError(f'No ket has type: {self.type}')

    def __str__(self):
        return self.type

    @staticmethod
    def marked_state(N, marked):
        return np.array([0 if i != (marked-1) else 1 for i in range(N)])

    @staticmethod
    def superposition_state(N):
        return (1/np.sqrt(N))*np.array([1 for _ in range(N)])

    @staticmethod
    def anti_superposition_state(N):
        return (1/np.sqrt((N-1)*N))*np.array([np.sum([np.exp(1j*2*np.pi*(jth-1)*i/N) for jth in range(1,N,1)]) for i in range(N)])

    @staticmethod
    def fourier_state(N, jth):
        return (1/np.sqrt(N))*np.array([np.exp(1j*2*np.pi*(jth-1)*i/N) for i in range(N)])

    @staticmethod
    def fourier_superposition_state(N, j_list):
        return (1/np.sqrt(len(j_list)*N))*np.array([np.sum([np.exp(1j*2*np.pi*(jth-1)*i/N) for jth in j_list]) for i in range(N)])

    @staticmethod
    def cosine_state(N, jth):
        return (1/np.sqrt(N))*np.array([np.cos((np.pi/(2*N))*(jth-1)*(2*i-1)) for i in range(N)])

    @staticmethod
    def cosine_superposition_state(N, j_list):
        return (1/np.sqrt(len(j_list)*N))*np.array([np.sum([np.cos((np.pi/(2*N))*(jth-1)*(2*i-1)) for jth in j_list]) for i in range(N)])

    @staticmethod
    def a_state(N, alpha):
        unnormalised = np.array([np.float_power(i+1,-alpha) + np.float_power((N-i),-alpha) for i in range(N)])
        norm = np.sqrt(np.inner(unnormalised, unnormalised))
        return (1/norm)*unnormalised

    @staticmethod
    def b_state(N):
        unnormalised = np.array([random.randrange(9000, 11000)/10000 for i in range(N)])
        norm = np.sqrt(np.inner(unnormalised, unnormalised))
        return (1/norm)*unnormalised

    @staticmethod
    def squared_state(N):
        a, b = 0.0001, 0.5
        unnormalised = np.array([a*(i-1/2-N/2)**2 + b for i in range(N)])
        norm = np.sqrt(np.inner(unnormalised, unnormalised))
        return (1/norm)*unnormalised