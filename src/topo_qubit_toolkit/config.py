
from pathlib import Path
from typing import Literal, Optional

from pydantic import BaseModel, Field


class KitaevChainConfig(BaseModel):

    L: int = Field(10, ge=2, description="Number of lattice sites.")
    t: float = Field(1.0, description="Hopping amplitude.")
    mu: float = Field(0.0, description="Chemical potential.")
    delta: float = Field(1.0, description="Superconducting pairing gap.")
    boundary: Literal["open", "periodic"] = Field(
        "open", description="Boundary conditions."
    )
    disorder_strength: float = Field(
        0.0, ge=0.0, description="Standard deviation of random chemical potential."
    )
    compute_majorana_modes: bool = Field(
        True, description="Whether to compute and save Majorana zero-mode wavefunctions."
    )
    compute_gap: bool = Field(
        True, description="Whether to compute the many-body energy gap."
    )


class ToricCodeConfig(BaseModel):


    L: int = Field(3, ge=2, description="Linear size of the torus or open patch.")
    topology: Literal["torus", "open"] = Field(
        "torus", description="Lattice topology."
    )
    hx: float = Field(0.0, description="Transverse magnetic field strength.")
    hz: float = Field(0.0, description="Longitudinal magnetic field strength.")
    compute_topological_entropy: bool = Field(
        True, description="Whether to compute topological entanglement entropy."
    )


class NoiseConfig(BaseModel):
  

    temperature: float = Field(
        0.0, ge=0.0, description="Temperature in units of the superconducting gap."
    )
    gamma_poisson: float = Field(
        0.01, ge=0.0, description="Quasiparticle poisoning (parity flip) rate."
    )
    gamma_dephase: float = Field(
        0.001, ge=0.0, description="Pure dephasing rate."
    )
    t_max: float = Field(100.0, description="Maximum simulation time.")
    dt: float = Field(0.1, description="Time step for integration.")
    num_trajectories: int = Field(
        100, ge=1, description="Number of Monte Carlo trajectories to average."
    )


class RunConfig(BaseModel):
  

    seed: int = Field(42, description="Global random seed for reproducibility.")
    output_dir: Path = Field(
        Path("results"), description="Directory to save output data and plots."
    )
    save_plots: bool = Field(True, description="Whether to generate and save plots.")
    backend: Literal["numpy", "scipy", "tenpy", "qiskit", "qutip"] = Field(
        "scipy", description="Primary numerical backend to use."
    )


class TopoQubitConfig(BaseModel):
   
    kitaev: Optional[KitaevChainConfig] = None
    toric: Optional[ToricCodeConfig] = None
    noise: Optional[NoiseConfig] = None