import h5py
import numpy as np

def main():
    # create an h5 file which contains two groups, each with two folders one called behavior and one called neural
    # each of these folders contains a dataset called data
    neural = np.random.rand(100, 96, 1000)
    data=vel = np.random.rand(1,1000)

    with h5py.File('test.h5', 'w') as f:

        f.create_dataset('stray_dataset', data=vel)

        f.create_dataset('mouse1/behavior/scalars/data=velocity', data=vel)
        f.create_dataset('mouse1/behavior/scalars/angle', data=vel)
        f.create_dataset('mouse1/behavior/scalars/height', data=vel)
        f.create_dataset('mouse1/behavior/scalars/syllable', data=vel)

        f.create_dataset('mouse1/neural/imaging/data', data=vel)
        f.create_dataset('mouse1/neural/imaging/hash', data=vel)
        f.create_dataset('mouse1/neural/imaging/date', data=vel)
        f.create_dataset('mouse1/neural/ephys/data', data=neural)

        f.create_dataset('mouse2/behavior/scalars/data=velocity', data=vel)
        f.create_dataset('mouse2/behavior/scalars/angle', data=vel)
        f.create_dataset('mouse2/behavior/scalars/height', data=vel)
        f.create_dataset('mouse2/behavior/scalars/syllable', data=vel)

        f.create_dataset('mouse2/neural/imaging/data', data=vel)
        f.create_dataset('mouse2/neural/imaging/hash', data=vel)
        f.create_dataset('mouse2/neural/imaging/date', data=vel)
        f.create_dataset('mouse2/neural/ephys/data', data=neural)



    f.close()


if __name__ == "__main__":
    main()