<h1 align="center" style="border-bottom: none">
   <a href="https://github.com/don-the-data-guy/EthosProbe">
    <img alt="Ethoculus logo" src="https://raw.githubusercontent.com/on-the-data-guy/EthosProbe/main/EthoculusImage.svg" width="200" />
</a>
</h1>
<h2 align="center" style="border-bottom: none">The Open Source AI Engineering Platform for Agents, LLMs & Models</h2>

# EthosProbe

EthosProbe is a manifest-driven framework for probing AI APIs and finding
behavioral weaknesses under pressure — built on MLflow's tracking and
experiment infrastructure, extended with the Ethoculus Probe methodology.

## What it does
- Define a probe manifest: target API, baseline rule, escalating pressure conditions
- Run the probe against any AI API endpoint
- Track every run, response, and integrity score using MLflow's experiment tracking
- Compare weaknesses across models, versions, or vendors over time

## Origin
EthosProbe is a fork of [MLflow](https://github.com/mlflow/mlflow), extended
with the Ethoculus Probe behavioral evaluation methodology
(https://github.com/don-the-data-guy/ethoculus_one_shot_probe).
