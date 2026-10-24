from pathlib import Path

import typer
import yaml

from topo_qubit_toolkit.config import TopoQubitConfig

app = typer.Typer(
    name="topo-toolkit",
    help="Exact-diagonalisation and tensor-network tools for topological qubits.",
    add_completion=False,
)


@app.command()
def run(
    config: Path = typer.Option(
        ...,
        "--config",
        "-c",
        exists=True,
        dir_okay=False,
        readable=True,
        help="Path to the YAML configuration file.",
    ),
) -> None:
    """Run a simulation pipeline from a YAML configuration file."""
    typer.echo(f"Loading configuration from: {config}")
    
    with open(config, "r", encoding="utf-8") as f:
        raw_cfg = yaml.safe_load(f)
        
    if raw_cfg is None:
        typer.echo("Error: Configuration file is empty.", err=True)
        raise typer.Exit(code=1)

    # Validate and parse configuration
    cfg = TopoQubitConfig.model_validate(raw_cfg)
    
    typer.echo("Configuration validated successfully.")
    typer.echo(f"Resolved configuration:\n{cfg.model_dump_json(indent=2)}")
    
    # Ensure output directory exists
    cfg.run.output_dir.mkdir(parents=True, exist_ok=True)
    
    # Dispatch logic will be implemented in Phase 7
    if cfg.kitaev:
        typer.echo("\n-> Kitaev chain simulation requested.")
    if cfg.toric:
        typer.echo("\n-> Toric code simulation requested.")
    if cfg.noise:
        typer.echo("\n-> Noise/decoherence simulation requested.")
        
    typer.echo("\nSimulation setup complete. (Execution logic to be wired in Phase 7)")


if __name__ == "__main__":
    app()