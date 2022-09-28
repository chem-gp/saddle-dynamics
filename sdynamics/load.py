import torch
from tqdm import tqdm
import gpytorch


import numpy as np
from ase import io
import matplotlib.pyplot as plt

import os
import glob



def parse_trajectories(
        traj_folder="../data/dynamics/ene_grad_fitting/data/trj/"
        ):

        trj_files = glob.glob(traj_folder + "*.xyz")
        # print(trj_files)

        energies_trj = {} # energies parsed per trajectory

        trj_concat = [] # concatenated trajectory containing all the configurations
        energies_concat = [] #similarly concatenated energies

        trajectories = {}

        trj_files_basename = []

        print("Reading trajectory files...")
        for f in tqdm(trj_files):
                mol_traj = io.read(f, index=":")
                trj_concat = trj_concat + mol_traj
                e_list = []
                # print(len(mol_traj))

                for m in mol_traj:
                        e = float(list(m.info)[-1])
                        e_list.append(e)

                trj_name = os.path.basename(f)
                energies_trj[trj_name] = e_list
                trajectories[trj_name] = mol_traj

                energies_concat = energies_concat + e_list
                trj_files_basename.append(trj_name)

        print("Trajectory files reading done!")
        return trajectories, energies_trj, trj_files_basename
# Returns:
# energies_trj # dict with energies
# trajectories # dict with trajectories
# trj_files_basename # list with basenames that serve as keys to the above dicts
# all dicts are indexed by the trajectory name, e.g. forces_trj['aimd_dft_t549_r2_002_trj.xyz']




def parse_forces(
        forces_path = '../data/dynamics/ene_grad_fitting/data/grad/',
        trj_files_basenames=None):     
        
        forces_trj = {}

        print("Reading .npy files with forces...")
        for f in trj_files_basenames:
                forces_filename = forces_path + f[:-7] + 'grad.npy'
                forces = np.load(forces_filename)

                forces_trj[f] = forces

        print("Reading .npy files with forces done!")
        return forces_trj
# Returns:
# forces_trj # dict with forces
# all dicts are indexed by the trajectory name, e.g. forces_trj['aimd_dft_t549_r2_002_trj.xyz']



def flatten_trj_dictionaries(
        traj_dict, 
        energies_trj, 
        trj_files_basenames, 
        forces_trj):

        traj = []
        energies = []
        forces = []

        for fname in trj_files_basenames:
                traj = traj + traj_dict[fname]
                energies = energies + energies_trj[fname]
                forces = forces + [ forces_trj[fname] ]

        energies_np = np.array(energies)
        forces_np = np.vstack(forces)

        print("Flattening done!")

        return traj, energies_np, forces_np


# Output: concatenated trajectory, forces, and energies in numpy format