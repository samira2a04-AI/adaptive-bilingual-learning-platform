# Evaluation Directory

Evaluation framework and metrics for the adaptive bilingual learning platform.

**Primary Metrics:** AUC (Area Under ROC), Accuracy, Log Loss - aligned with MLCC evaluation practices.

**Evaluation Components:**

| Component | Description | Metrics |
|---|---|---|
| Knowledge Tracing Model Performance | BKT, DKT, SAKT, simpleKT, logistic_regression model evaluation | AUC-ROC, Accuracy, Log Loss, F1-score |
| Adaptive Routing Effectiveness | Routing recommendation hit rate, coverage, prerequisite satisfaction | Hit Rate @ N, Coverage, Prerequisite Satisfaction Rate |
| Bilingual UI Usability Pilot Studies | Language switching latency, comprehension difference, preference retention | Switching latency, accuracy difference, retention rate |
| Bias and Fairness Assessments | Demographic parity, equalized odds across language groups | Disparity metrics, bias audit results |

**Primary Metrics Detail:**

| Metric | Formula | Target | Interpretation |
|---|---|---|---|
| AUC-ROC | ∫ TPR(FPR) dFPR | ≥ 0.80 | Model distinguishes correct/incorrect responses |
| Accuracy | (TP+TN)/(TP+TN+FP+FN) | Context-dependent | Overall correctness rate |
| Log Loss | -1/N Σ [y_i log(p_i) + (1-y_i) log(1-p_i)] | Minimize | Penalizes confident wrong predictions |

**Evaluation Data Sources (per NFR-04, ML-01, ML-02):**

| Dataset | Domain | Size | Use Case |
|---|---|---|---|
| ASSISTments 2009-2010 | Education (Math) | ~1M interactions | BKT model training |
| EdNet-KT1 | Education (All subjects) | ~4M interactions | Large-scale KT training |
| Junyi-KT | Education (China) | ~500K interactions | Cross-cultural validation |

**Workstream:** Partners with backend data pipeline and ethics workstream for responsible evaluation. Bias audits performed quarterly per ethics framework protocol.