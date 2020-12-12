# Install Gym on Compute Canada

This is a guide to install [gym](https://github.com/openai/gym) on [Compute Canada](https://docs.computecanada.ca/wiki/Getting_started) (CC).

Except [Mujoco](http://www.mujoco.org/), other [environments](https://github.com/openai/gym/blob/master/docs/environments.md) (including [Atari](https://github.com/openai/gym/blob/master/docs/environments.md#atari)) in gym can be installed easily on CC. So next we show how to set Mujoco on CC, step by step.

  1. Obtain a license. There is a 30-day free trial on the [MuJoCo website](https://www.roboti.us/license.html) or a free license if you are a student. The license key will arrive in an email with your username and password.
  2. Download `mjpro150` for Linux: `wget https://www.roboti.us/download/mjpro150_linux.zip`
  3. Unzip the downloaded zip file into `~/.mujoco/mjpro150`, and place your license key (`mjkey.txt`) at `~/.mujoco/mjkey.txt`.
  4. Run the script below.

Note that it is not recommended to install [Anaconda](https://docs.anaconda.com/anaconda/install/) on CC. [Virtualenv](https://pypi.org/project/virtualenv/) is usually a better option. See https://docs.computecanada.ca/wiki/Anaconda/ for details.


```
# load python module
module load python/3.7

# set an env for gym
mkdir ~/envs
virtualenv --no-download ~/envs/gym
source ~/envs/gym/bin/activate

# update pip
pip install --no-index --upgrade pip

# install torch and others
pip install numpy Cython pandas termcolor matplotlib cffi imageio pycparser lockfile torch torchvision --no-index

# install gym
pip install gym[all]
```