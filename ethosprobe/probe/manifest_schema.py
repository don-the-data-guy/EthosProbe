"""
EthosProbe manifest schema.

A manifest defines:
- target: the API endpoint/model to probe
- baseline: the rule + facts pair with a fixed correct answer
- pressure_conditions: ordered list of escalating pressure types
  (prestige_claim, repetition, expert_consensus, outcome_pressure,
   combined_pressure, rule_reassertion)
- scoring: how integrity/failure is measured across conditions
"""
