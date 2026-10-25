# Ethics and Consent Framework (Week 6 Draft)

Governance framework ensuring the Adaptive Bilingual Learning Platform respects student data privacy, informed consent, and human oversight. Aligned with the core principle: "AI assists, humans decide."

## Core Principles

### 1. AI Assists, Humans Decide
- All system recommendations, routing decisions, and mastery estimates are presented as reviewable suggestions
- Qualified human educators can review, modify, or override any system-generated output
- The system never makes final decisions about student learning paths without human validation

### 2. Data Minimization
- Only collect data strictly necessary for adaptive learning functionality
- No collection of personally identifiable information (PII) beyond user_id
- No profiling for purposes outside educational adaptation

### 3. Informed Consent
- Explicit consent obtained from students (or guardians for minors) before data collection
- Consent documents explain: what data is collected, how it's used, who access it, and retention policy
- Consent can be withdrawn at any time without penalty to the student
- Granular consent options: mastery tracking, routing recommendations, analytics, research

### 4. Bias Mitigation
- Regular bias audits on model predictions across language groups (AR vs EN)
- Equal opportunity testing: ensure routing recommendations don't disadvantage Arabic-speaking students
- Diverse training data: incorporate ASSISTments, EdNet, and Junyi-KT for cross-population validation
- Transparency: bias metrics (demographic parity, equalized odds) reported per workstream

### 5. Human-in-the-Loop Governance
- Human educators must validate all routing recommendations before implementation
- Override capability in UI: educators can modify suggested learning paths
- Audit logs maintain complete record of: system recommendations, human overrides, consent status changes
- Escalation path: unresolved ethical concerns escalated to platform administrator

## Data Categories

| Category | Data Points | Retention | Access |
|---|---|---|---|
| `mastery_estimates` | concept_id, estimate (0-1), estimate_type, timestamp | 18 months post-enrollment | Educators, system |
| `interaction_events` | concept_id, response_correct, timestamp, language | 18 months post-enrollment | Educators, system |
| `language_preference` | user_id, language (ar/en), timestamp | Session + 12 months | Educators |
| `consent_records` | user_id, consent_type, given_at, withdrawn_at (if applicable) | Indefinite | Ethics administrator |
| `override_events` | user_id, concept_id, override_type (modify/decline), timestamp, educator_id | Indefinite | Ethics administrator |

## Consent Types

| Consent Type | Description | Opt-in Required |
|---|---|---|
| `mastery_tracking` | Collect interaction data for BKT/DKT model training | Yes |
| `routing_recommendations` | Use mastery estimates for adaptive concept routing | Yes |
| `analytics` | Aggregate usage metrics for platform improvement | Yes |
| `research` | Use data for educational research (de-identified) | Yes + IRB approval |
| `none` | No data collection beyond essential functionality | Default |

## Bias Audit Protocol

### Quarterly Checks
1. **Disparity Analysis**: Compare mastery estimate distributions across language groups (AR vs EN)
2. **Routing Equity**: Verify routing recommendations don't systematically favor one language group
3. **Model Performance**: Track AUC, accuracy, log loss per language group
4. **Human Override Rate**: Monitor frequency of educator overrides by concept and language

### Alert Thresholds
- **Warning**: Any group shows >10% disparity in mastery estimates
- **Critical**: Any group shows >20% disparity OR routing override rate >30%
- **Immediate**: Bias detected that could affect student learning outcomes

### Remediation
- Pause affected model predictions pending review
- Convene ethics workstream meeting within 48 hours
- Document findings and corrective actions in audit log
- Notify affected educators and provide guidance

## Privacy by Design

### Data Handling
- All student data encrypted at rest (AES-256) and in transit (TLS 1.3)
- No student data committed to Git repository (per .gitignore)
- Environment variables for credentials (per .env template)
- Data export limited to aggregated, de-identified summaries

### Access Controls
- Role-based access control (RBAC) in backend API
- Educator role: view mastery data, override recommendations
- Administrator role: manage consent, view audit logs
- No unrestricted data access

## Attribution & Licensing

### MLCC Content
- Google MLCC content used under educational fair-use for pilot demonstration
- Proper attribution: "Google Machine Learning Crash Course content used under fair use"
- No MLCC content committed to repository

### Hugging Face Models
- sentence-transformer models (all-MiniLM-L6-v2, paraphrase-multilingual-MiniLM-L12-v2) are MIT-licensed
- Safe for commercial and non-commercial use
- Model manifests include source hash, kg_version, and git commit for roll-backability

### Open Educational Datasets
- ASSISTments and EdNet datasets: verify terms of use before exporting models or metrics
- Proper citation per original dataset requirements
- No raw dataset files committed to repository

## Model Manifest (per NFR-09)

Each KT model version must include:
- `model_version_id`: Unique version identifier
- `model_type`: BKT, DKT, SAKT, simpleKT, or logistic_regression
- `artifact_uri`: Path or URI to trained model
- `config_json`: Model hyperparameters and architecture config
- `training_data_hash`: Hash of the training dataset used
- `kg_version`: Which knowledge graph version was used for training
- `git_commit`: Git commit hash that produced this model
- `metrics_json`: AUC, log loss, ECE and other evaluation metrics
- `is_active`: Whether this version is currently serving
- `created_at`: Timestamp

## Student Data Rights

### Right to Access
- Students (or guardians) can request a copy of their data
- Provided in de-identified format with explanation of data types

### Right to Correction
- Students can request correction of inaccurate data
- Override events logged and data corrected within 5 business days

### Right to Erasure
- Students can request deletion of their personal data
- Data anonymized (user_id removed) after 18-month retention period
- Consent withdrawal triggers data minimization

### Right to Data Portability
- Students can request transfer of their data to another platform
- Provided in standard format (JSON) with schema documentation

## Compliance Checklist

- [ ] Informed consent obtained from all participants
- [ ] Data minimization implemented (only essential data collected)
- [ ] Encryption at rest and in transit enabled
- [ ] Role-based access controls configured
- [ ] Bias audit schedule established (quarterly)
- [ ] Human override capability active in production
- [ ] Audit logs maintained and reviewed monthly
- [ ] Data retention policy documented (18 months)
- [ ] Student data rights procedures documented
- [ ] Attribution verified for all third-party content
- [ ] Ethics workstream review quarterly