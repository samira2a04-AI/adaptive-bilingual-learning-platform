# Evaluation Metrics Framework (Week 6 Draft)

Evaluation framework and metrics for the Adaptive Bilingual Learning Platform, aligned with MLCC evaluation practices (AUC, Accuracy, Log Loss) and knowledge tracing performance.

## Primary Metrics (MLCC-Aligned)

| Metric | Definition | Formula | Interpretation |
|---|---|---|---|
| **AUC (Area Under ROC)** | Area under Receiver Operating Characteristic curve | `∫ TPR(FPR) dFPR` | Measures model's ability to distinguish correct vs incorrect responses across all thresholds. 0.5 = random, 1.0 = perfect. |
| **Accuracy** | proportion of correct predictions | `(TP + TN) / (TP + TN + FP + FN)` | Overall correctness rate. Context-dependent; less informative for imbalanced datasets. |
| **Log Loss** | Logarithmic loss of predicted probabilities | `-1/N * Σ [y_i * log(p_i) + (1-y_i) * log(1-p_i)]` | Penalizes confident wrong predictions heavily. Lower is better. 0.0 = perfect. |

## Knowledge Tracing Model Performance

| Model Type | Primary Metrics | Description |
|---|---|---|
| **BKT** | Likelihood of parameter estimates, hold-out accuracy | Bayesian Knowledge Tracing: 2-state hidden Markov model. Parameters: l0 (prior), l1 (learn), l2 (forget), l3 (guess), l4 (slip). |
| **DKT** | AUC-ROC, accuracy, log loss over train/test split | Deep Knowledge Tracing: LSTM-based. Captures sequential dependency beyond BKT's fixed states. |
| **SAKT** | Same as DKT + attention visualization | Self-Attention Knowledge Tracing. Includes attention visualizations for interpretability. |
| **simpleKT** | Simplified likelihood, precision/recall | Minimalist KT model with fewer parameters. Faster training, good baseline. |
| **logistic_regression** | Coefficient significance, AUC, accuracy | Simple logistic regression on features. Baseline for comparing deep models. |

### Model Evaluation Protocol

#### Train-Test Split
- **80/20 split** by student ID (stratified by language group)
- No data leakage across train/test boundaries
- Same KG version for train and test

#### Cross-Validation
- **5-fold cross-validation** by concept
- Ensures model generalization across concept types
- Report mean ± std of AUC, accuracy, log loss

#### Performance Reporting
```
Model: BKT
Dataset: EdNet-KT1 (subset)
Language: Arabic (ar) & English (en) separated

Metrics:
- AUC-ROC: 0.85 (ar), 0.88 (en)
- Accuracy: 0.71 (ar), 0.74 (en)
- Log Loss: 0.48 (ar), 0.44 (en)
- N: 1,243 interactions (ar), 2,187 interactions (en)

Fold statistics:
- Mean AUC: 0.86 ± 0.03
- Mean Accuracy: 0.72 ± 0.04
- Mean Log Loss: 0.46 ± 0.05
```

## Adaptive Routing Effectiveness

### Routing Metrics

| Metric | Description | Target |
|---|---|---|
| **Hit Rate @ N** | Percentage of times the next correctly answered concept was in top-N recommendations | ≥ 0.70 @ N=3 |
| **Diversity @ N** | Concept diversity of recommendations (different layers/concepts) | ≥ 0.60 |
| **Coverage** | Percentage of time a valid next concept is available | ≥ 0.85 |
| **Time-to-Mastery** | Expected interactions to reach mastery threshold from initial estimate | Minimize |
| **Prerequisite Satisfaction Rate** | % of recommended concepts where all hard prerequisites are already mastered | ≥ 0.95 |

### Routing Evaluation

```
Evaluation on: 50 students, 73 concepts, 4 layers

Results:
- Hit Rate @ 1: 0.52
- Hit Rate @ 3: 0.73
- Hit Rate @ 5: 0.81
- Diversity @ 3: 0.67
- Coverage: 0.88
- Prerequisite Satisfaction Rate: 0.96
- Avg Time-to-Mastery: 14.2 interactions
```

## Bilingual UI Usability

### Metrics

| Metric | Description | Collection Method |
|---|---|---|
| **Language Switching Latency** | Time between language toggle and content re-render | Frontend timing APIs |
| **Comprehension Difference** | Performance gap between AR and EN language conditions | A/B test with counterbalanced design |
| **Preference Retention** | % of users who keep their language preference across sessions | Session restore tracking |
| **Comprehension Rate** | % of concept questions answered correctly in each language | Per-concept tracking |

### Pilot Study Protocol

```
Design: Within-subjects A/B test with 30 pilot participants
Conditions: 
  - Group 1: English first, then Arabic
  - Group 2: Arabic first, then English
Tasks: 
  - 20 concept questions per language
  - Mastery pre-test and post-test
Measures: 
  - Accuracy per language
  - Time per question
  - Language switching frequency
  - Student preference survey
Expected: No significant comprehension difference between AR and EN (within ±0.05)
```

## Bias and Fairness Assessments

### Demographic Parity

```
P(model recommends concept | student_group = ar) 
  ≈ P(model recommends concept | student_group = en)
```
- Target: within ±0.10 disparity
- Measured per concept across language groups

### Equalized Odds

```
P(recommendation | mastery=yes, group=ar) 
  ≈ P(recommendation | mastery=yes, group=en)
P(recommendation | mastery=no, group=ar) 
  ≈ P(recommendation | mastery=no, group=en)
```
- Target: within ±0.15 disparity
- Measured across mastery states

### Bias Audit Frequency
- **Weekly**: Automated bias check via `/api/v1/ethics/bias-check`
- **Quarterly**: Full manual audit per protocol in docs/ethics-and-consent/
- **Per-release**: Bias checkpoint before any production deployment

## Evaluation Data Sources (per NFR-04, ML-01, ML-02)

### Public Datasets

| Dataset | Domain | Size | Use Case |
|---|---|---|---|
| **ASSISTments 2009-2010** | Education (Math) | ~1M interactions | BKT model training, evaluation |
| **EdNet-KT1** | Education (All subjects) | ~4M interactions | Large-scale KT model training |
| **Junyi-KT** | Education (China) | ~500K interactions | Cross-cultural validation, bilingual research |

### Attribution & Licensing

- ASSISTments: open educational dataset; verify terms of use before exporting models or metrics
- EdNet: open educational dataset; citation requirements per provider
- Junyi-KT: open educational dataset; Chinese curriculum alignment
- **No raw dataset files committed to repository** (per .gitignore)
- Model manifests include: source hash, kg_version, and git commit for roll-backability

### Synthetic Data Generation
- When public dataset access is restricted, generate synthetic data with known properties
- Preserve prerequisite graph structure and realistic interaction patterns
- Document generation parameters and seed for reproducibility

## Evaluation Pipeline

```
1. Data Ingestion → 2. Preprocessing → 3. Model Training → 4. Evaluation → 5. Reporting → 6. Model Registry
                                                                    ↓                                    │
                          ------------------------------------------------------------┘
```

### Pipeline Steps

1. **Data Ingestion**: Load interaction events from database; filter by KG version; separate by language group
2. **Preprocessing**: Sequence alignment by user_id; handle missing interactions; create train/test splits
3. **Model Training**: Train BKT/DKT/SAKT per language group; optimize parameters via maximum likelihood
4. **Evaluation**: Compute AUC-ROC, accuracy, log loss on test set; compute routing metrics via simulation
5. **Reporting**: Generate evaluation report with metrics, bias analysis, and recommendations
6. **Model Registry**: Register model version with full manifest (per ethics framework); mark active/inactive

### Continuous Evaluation

- **Daily**: Automated metric checks on shadow mode (model recommendations without live impact)
- **Weekly**: Full evaluation pipeline rerun with newest data
- **Per-release**: Evaluation checkpoint before deploying model or routing changes
- **On-consent-change**: Re-evaluate if consent patterns shift population demographics

## Evaluation Report Template

```
# Evaluation Report v{version}
# Model: {model_type}
# KG Version: {kg_version}
# Language: {ar/en/both}
# Date: {date}

## Executive Summary
- Overall AUC: {value}
- Key finding: {summary}

## Primary Metrics
| Metric | Value | Interpretation |
|---|---|---|
| AUC-ROC | {value} | {interpretation} |
| Accuracy | {value} | {interpretation} |
| Log Loss | {value} | {interpretation} |

## Per-Language Breakdown
| Metric | Arabic (ar) | English (en) | Disparity |
|---|---|---|---|
| AUC-ROC | {value} | {value} | {value} |
| Accuracy | {value} | {value} | {value} |
| Log Loss | {value} | {value} | {value} |

## Routing Effectiveness
| Metric | Value | Target | Status |
|---|---|---|---|
| Hit Rate @ 3 | {value} | ≥ 0.70 | {'✓' if met else '✗'} |
| Coverage | {value} | ≥ 0.85 | {'✓' if met else '✗'} |
| Prereq Satisfaction | {value} | ≥ 0.95 | {'✓' if met else '✗'} |

## Bias Assessment
| Check | Disparity | threshold | Status |
|---|---|---|---|
| Demographic Parity | {value} | ≤ 0.10 | {'✓' if met else '✗'} |
| Equalized Odds | {value} | ≤ 0.15 | {'✓' if met else '✗'} |

## Recommendations
1. {action item}
2. {action item}
3. {action item}

## Model Registry Entry
- model_version_id: {id}
- model_type: {type}
- artifact_uri: {uri}
- config_json: {config}
- training_data_hash: {hash}
- kg_version: {version}
- git_commit: {commit}
- metrics_json: {metrics}
- is_active: {true/false}
- created_at: {timestamp}
```