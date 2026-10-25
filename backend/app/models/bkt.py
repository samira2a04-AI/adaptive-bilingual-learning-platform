# Bayesian Knowledge Tracing Model (Week 6 Draft)

Implementation of BKT for concept mastery prediction. Supports the adaptive routing workstream.

## Model Parameters

| Parameter | Description | Typical Value |
|---|---|---|
| `l0` | Initial prior probability of knowing | 0.1–0.3 |
| `l1` | Learning probability (P(know_t=1 | know_{t-1}=0)) | 0.1–0.5 |
| `l2` | Forgetting probability (P(know_t=0 | know_{t-1}=1)) | 0.01–0.2 |
| `l3` | guessing probability (P(correct | know=0)) | 0.1–0.3 |
| `l4` | slipping probability (P(incorrect | know=1)) | 0.1–0.3 |

## BKT State Update

Given a student's response (correct/incorrect) to an item testing the concept:

```
P(know_t | correct) = [(1 - l2) * (1 - l3)] / P(correct)
P(know_t | incorrect) = [l4 * l2] / P(incorrect)

Where:
P(correct) = (1 - l2) * (1 - l3) + l2 * l4
P(incorrect) = 1 - P(correct)

Mastery estimate after interaction: P(know_t = 1)
```

## Learning Curve

Tracking mastery over time with the three-state derivation:

```
status = unknown (initial)
status = learning (0.0 < estimate < 1.0)
status = mastered (estimate >= threshold, e.g., 0.85)
```

## API Integration

```python
from app.models.bkt import BKTModel

bkt = BKTModel(l0=0.2, l1=0.3, l2=0.1, l3=0.2, l4=0.1)

# Update after correct response
estimate = bkt.update(response=True)

# Update after incorrect response
estimate = bkt.update(response=False)

# Get current state
state = bkt.status(estimate)  # returns "unknown", "learning", or "mastered"
```