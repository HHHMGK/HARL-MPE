from absl import flags
from harl.envs.pettingzoo_mpe.pettingzoo_mpe_logger import PettingZooMPELogger

FLAGS = flags.FLAGS
FLAGS(["train_sc.py"])

LOGGER_REGISTRY = {
    "pettingzoo_mpe": PettingZooMPELogger,
}
