# Candidate Governance Implementation Roadmap

**Purpose:** Recommend the smallest safe implementation milestones that bring the repository toward `Candidate_Governance_Contract_v1.md` without ever allowing extraction to create a `ConceptDraft` directly.

**Scope rule for the whole roadmap:**
`ConceptDraft` may only be created through the controlled conversion path. Extraction, chunking, and provider parsing remain upstream of candidate governance; they do not close the governance loop.

**Constraint reminders from the task:**
- No application code or test modifications in this roadmap document.
- No provider calls, no extraction runs, no chunk processing, no candidate approval or conversion.
- Deferred decisions are not invented here.

---

## Recommended first implementation milestone

**Milestone 0 — Create the smallest candidate-governance seam that breaks the direct extraction-to-draft path.**

### Scope
- Introduce the smallest new models needed to represent an app-owned candidate object distinct from extracted labels:
  - candidate occurrence identity
  - candidate revision identity
  - candidate-revision evidence association
- Introduce the controlled conversion operation skeleton:
  - revision-scoped conversion intent
  - conversion record and idempotency key shape
  - failure behavior contract: no partial writes
- Disconnect the existing direct extraction-to-`ConceptDraft` path from the governed path at the architectural boundary, even if the new conversion path is not yet fully wired.

### Preconditions
- Accept that candidate identity is app-owned and independent of canonical name, description, granularity, and provider identifiers.
- Accept that candidate-specific evidence association is required before conversion can be fully governed.
- Accept that the current provider schema does not yet provide candidate-specific quotations or educational roles, and treat that as an explicit extraction-interface gap.
- Accept that approval, source-version registration, duplicate review, and authorization are not all available yet, so the first milestone is a seam and skeleton, not full governance.

### Files likely affected
- New or modified candidate-governance models package
- New or modified conversion service or operation module
- The existing extraction automation boundary that currently constructs `ConceptDraft` directly
- Repository interface surface that must eventually support candidate operations

### Dependencies
- Candidate identity model
- Candidate-revision evidence association model
- Conversion idempotency design
- Explicit decision that extraction does not directly produce `ConceptDraft`

### Acceptance criteria
- There is a defined candidate object separate from extracted labels.
- There is a defined candidate revision model where a content change can create a new immutable revision.
- There is a defined candidate-revision evidence association distinct from chunk-level provenance.
- There is a defined conversion operation shape with revision scoping and idempotency.
- There is a documented boundary saying extraction no longer directly creates `ConceptDraft` in the governed architecture.
- The repository can be surveyed to show where the old direct path still exists and what must be disabled or replaced.### Required tests

- New candidate identity is independent of label similarity.
- New revision creation preserves immutability semantics.
- Candidate-revision evidence association is explicit rather than inherited from chunk proximity.
- Conversion skeleton validates required inputs and fails without partial writes.
- Extraction path no longer closes the loop to a governed `ConceptDraft` in the new design.

### Conversion skeleton vs. full conversion (Required clarification)

Milestone 0's conversion skeleton must **never** be implemented in a way that can successfully create a `ConceptDraft` while mandatory governance gates are still unimplemented.

Specifically, Milestone 0 must not add a `convert_candidate_to_concept_draft()` operation whose runtime happy path produces a `ConceptDraft`. The approved behavior is:

- Add the **contracts/shapes** of conversion: conversion intent input model, conversion record shape, idempotency key shape, and the documented failure-semantics contract (no partial writes).
- Add the **fail-closed rejection stub** for conversion until the full gate set is wired. If a conversion attempt is made, it must be rejected with a clear contract boundary error, not silently succeed.
- Do not implement a conversion path that would produce a `ConceptDraft` before these gates exist:
  - effective human approval
  - exact candidate-specific evidence association
  - valid evidence association status heads
  - valid source status heads
  - resolved relevant duplicate reviews
  - current and available source version
  - authorization
  - concurrency token

This protects the core invariant: a new conversion skeleton must not become an alternate bypass around candidate governance. Without this clarification, Milestone 0 risks adding a `convert_candidate_to_concept_draft()` path that would satisfy the literal text "conversion skeleton" while contradicting the contract rule that `ConceptDraft` may only be created through the controlled conversion path with all gates satisfied.



### Rollback considerations
- If the seam is introduced but the old path is not clearly retired or contained, the system can silently keep bypassing governance.
- If candidate identity is accidentally tied to labels during implementation, rollback must restore independence from canonical name and aliases.
- If conversion skeleton is introduced without clear failure semantics, a later conversion attempt may appear governed while still permitting partial effects.

---

## Subsequent milestone directions

These are directions, not commitments, and each should be evaluated against deferred decisions before full implementation.

### Milestone A — Candidate review governance skeleton
- Add candidate review event model with revision-scoped events.
- Add reopening with authority, rationale, and concurrency validation.
- Add the rule that approval of one revision does not automatically approve later revisions.
- Exclude: final approval authority model; production durable review history.

### Milestone B — Source version registration and status events
- Add source-version registration operation with expected current version and authorization context.
- Add current/superseded distinction.
- Add source status event history with rebuildable projections.
- Exclude: production durable transactions and unique constraints until the persistence design is decided.

### Milestone C — Candidate-specific evidence and quote validation decision
- Decide the extraction-interface change or documented gap for candidate-specific quotations and educational roles.
- Add quote/passage validation support enough to validate candidate-specific evidence against a chunk or stored source content.
- Add evidence association status events: `valid`, `invalid`, `superseded`.
- Exclude: inventing a final extraction strategy if it is still deferred.

### Milestone D — Duplicate governance
- Add governed duplicate pair model with canonical pair key.
- Add duplicate observation as advisory only.
- Add duplicate review events and human decisions: `distinct`, `merge_with_existing`, `replace_candidate`.
- Add prohibition on automatic evidence transfer.
- Add block rule: unresolved relevant duplicate pairs block conversion.
- Exclude: any path that lets detector output merge candidates.

### Milestone E — Controlled conversion with full gates
- Wire conversion to require:
  - exact candidate revision
  - effective human approval
  - valid evidence association heads
  - valid source status heads
  - validated candidate-specific evidence
  - resolved relevant duplicate reviews
  - current and available source version
  - authorization
  - concurrency token
- Add conversion record, event-head snapshot, and idempotency key.
- Add atomic failure behavior with no partial writes.
- Exclude: claiming production durability unless durable constraints are actually in place.

### Milestone F — Prototype-to-production hardening
- Add unique constraints for candidate identity, occurrence identity, duplicate pair, and event ordering where applicable.
- Add locking or compare-and-swap for concurrent registration and conversion.
- Make idempotency durable.
- Add authorization infrastructure or binding to an external authority model.
- Keep explicit prototype-versus-production boundary.

---

## What the first milestone must preserve

- Extraction cannot directly create `ConceptDraft`.
- Candidate identity remains app-owned.
- Candidate-specific evidence is distinct from chunk-level provenance.
- Deferred decisions stay deferred.
- No false production-grade claims from in-memory behavior.

---

## Recommended immediate next step

Start with Milestone 0 as three small pieces, in this order: 0A, then 0B, then 0C.

It is the smallest technically valid boundary because it introduces the candidate-governance concepts that the contract requires while breaking the existing direct extraction-to-`ConceptDraft` path, without pretending that approval, source registration, duplicate review, or production persistence are already solved.

It is also intentionally **not** a combined milestone. The Gap Matrix and this review both indicate that a single milestone combining candidate identity, candidate-revision evidence association, breaking the extraction bypass, and a conversion skeleton is too large to verify coherently. Even for the first milestone, the conversion piece must stay a fail-closed skeleton: a conversion skeleton must never successfully create a `ConceptDraft` while mandatory governance gates are unimplemented.

This matches the handover note's sequencing: 0A first, 0B next, 0C last.
