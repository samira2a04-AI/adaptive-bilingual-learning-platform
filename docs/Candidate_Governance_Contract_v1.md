# Candidate Governance Contract v1

**Status:** Reconstructed specification.
**Reconstruction basis:** Architectural decision register, existing prototype contracts, previously agreed design intent, and the repository audit baseline.
**Not a recovery claim:** This document is reconstructed from architectural decisions and existing code, not recovered verbatim from a frozen contract file.

---

## 1. Source identity and provenance

### 1.1 SourceVersion

A `SourceVersion` is a timestamped or sequential label associated with one `source_id` that represents one ingested or recognized state of that source at the platform's observed boundary.

A `SourceVersion` record answers:
- which source is involved
- which version of that source is currently claimed
- whether that version is the current, superseded, available, unavailable, or withdrawn view from the KM boundary

A `SourceVersion` is not:
- a content hash alone
- a locator alone
- a guarantee that two identical contents are the same occurrence
- a statement that the educational meaning has changed or remained identical

### 1.2 SourceOccurrence

A `SourceOccurrence` is one perceivable chunk or unit of source content associated with one particular `SourceVersion` and one particular locator.

A `SourceOccurrence` is identified for candidate-governance purposes by a **composite identity**:

```
(source_id, source_version, chunk_id)
```

This composite identity is:
- stable for a given ingested occurrence
- suitable as a candidate-provenance anchor
- subject to the scope and uniqueness constraints in §1.4

It does **not** mean:
- `content_hash` is a globally unique identity
- `locator` is a machine identity
- identical content across two occurrences proves they are the same occurrence
- a new source version implies that the educational concept changed or remained unchanged

### 1.3 Source-version registration and supersession

Source-version registration must support:
- first-version registration
- supersession of a previous version
- distinction between current and superseded versions
- future support for available, unavailable, and withdrawn statuses

Supersession means the previous version is no longer the current view for that source_id. It does **not** mean:
- all educational items derived from that version have changed
- evidence recorded against the previous version is now invalid by default
- any candidate must be automatically reopened, merged, or retired

### 1.4 Scope and uniqueness constraints

- Within a given source registry scope, `(source_id, source_version, chunk_id)` is treated as a candidate composite key for one occurrence.
- Uniqueness of this composite key must be enforced within the scope where occurrences are registered.
- `content_hash` may be used as a **validation** input, not as a globally unique identity.
- `locator` may be used as a human-oriented address or retrieval hint, not as a durable machine identity by itself.

### 1.5 Content hash validation

`content_hash` can support:
- validating that an occurrence's recorded chunk content matches an expected chunk
- detecting accidental duplication or corruption at the chunk-boundary level
- supporting quote validation when the expected content is known exactly

`content_hash` cannot support:
- global identity on its own
- distinguishing two occurrences with identical content but separate provenance
- proving educational equivalence

### 1.6 Locator semantics

A `locator` identifies a position or retrievable area within the source: for example a page, section, lesson, paragraph, or stored chunk boundary.

Locator semantics are:
- useful for human navigation
- useful for retrieval routing
- useful as one input to identity and validation

Locator semantics are not:
- an independent machine identity
- a substitute for `(source_id, source_version, chunk_id)` when durable occurrence identity is required

### 1.7 Source version changes

When a source version changes:
1. KM may record the change.
2. KM may compute affected evidence and knowledge items.
3. KM must not assume:
   - the educational items are now identical to before
   - the educational items are now different
   - the old evidence is still valid or now invalid without review

A source version change is a **provenance event**, not an automatic educational-equivalence judgment.

### 1.8 Duplicate ingestion

If the same source content is ingested more than once, that does **not** by itself establish that two occurrences are the same governance object. Duplicates require explicit governance handling, not silent collapse.

### 1.9 What is currently supported

- Evidence already records `(source_id, source_version)` and `content_hash`.
- `EvidenceRef` already stores `locator`, `content_hash`, and an optional `excerpt`.
- `ContentChunk` already carries `source_id`, `source_version`, `chunk_id`, `locator`, and `content_hash`.

### 1.10 What requires future implementation

- A durable source-version registration and supersession model.
- Explicit current-versus-superseded projections.
- Available, unavailable, and withdrawn status lifecycle.
- Durable uniqueness constraints for `(source_id, source_version, chunk_id)` in the production store.
- Validation paths that compare an occurrence against the actual stored source content using the chunk boundary and content hash as inputs.

---

## 2. Candidate identity and revisions

### 2.1 Principles

Candidate identity is **app-owned** and must be **independent** of:
- candidate name
- canonical name
- category or educational role
- description
- granularity disposition
- provider-generated identifiers

A candidate is not the same thing as a label or a provider idea. It is the platform's own governance object for a reconciled educational item.

### 2.2 CandidateOccurrence

A `CandidateOccurrence` represents the platform's first governed record of a reconciled educational item, anchored to one or more source occurrences and evidence references.

A `CandidateOccurrence` does **not** imply:
- approval
- conversion to a final model draft
- that the item is definite or final

It is the beginning of candidate history, not the end.

### 2.3 CandidateRevision

A `CandidateRevision` is an immutable record attached to a candidate occurrence that represents one specific version of that candidate's reconciled educational content.

Rules:
- A content change to the same reconciled educational item creates a new immutable revision.
- A new revision does **not** automatically inherit approval, evidence validity, duplicate-governance decisions, or conversion eligibility from earlier revisions.
- Approval of one revision must not automatically approve later revisions.

### 2.4 CandidateRunLink

A `CandidateRunLink` associates a candidate occurrence or revision with a specific extraction, ingestion, or reconciliation run context so that the provenance of the candidate record can be traced back to the process that produced it.

A `CandidateRunLink` is descriptive, not authoritative for identity.

### 2.5 CandidateRevisionEvidence

A `CandidateRevisionEvidence` record associates one exact candidate revision with one exact evidence reference.

This is not the same as chunk-level provenance. It is the candidate-level evidence association that conversion, review, and duplicate governance may depend on.

### 2.6 New source version versus candidate continuity

A new source version does **not** automatically establish continuity of candidate identity.

If a source changes, the platform may need to:
- create a new candidate occurrence,
- create a new candidate revision,
- reopen or revalidate an existing candidate,
- or record that the item is currently unresolved

depending on the governance decision actually made. Identity continuity is a decision, not a side effect of versioning.

---

## 3. Reconciliation

### 3.1 Purpose

Reconciliation is the decision point where the platform compares an incoming or newly extracted educational item against existing candidate occurrences and decides what to do.

### 3.2 Permitted outcomes

1. **match_existing**
   The item is reconciled with an existing candidate occurrence, subject to explicit evidence and identity safeguards.

2. **create_new**
   A new candidate occurrence is created.

3. **ambiguous**
   The system cannot confidently determine whether the item matches an existing candidate or should be new.

4. **insufficient_evidence**
   There is not enough supporting evidence to create an eligible candidate.

### 3.3 Signals and safeguards

Signals may include:
- name similarity
- description overlap
- evidence overlap
- source overlap
- locator overlap
- human judgment

Safeguards include:
- name similarity alone never authorizes a match
- evidence overlap alone never authorizes a merge
- one sentence may support multiple distinct educational items
- ambiguous candidates must not be silently merged or promoted
- insufficient evidence must not create an eligible candidate

### 3.4 Preservation of unsuccessful attempts

Reconciliation attempts that do not result in a clean outcome must preserve diagnostic records so that:
- why a decision was made is traceable
- why something was left ambiguous is explainable
- retry or human review can proceed on the same evidence

---

## 4. Evidence governance

### 4.1 Evidence record versus candidate-revision evidence association

An **evidence record** is a provenance artifact tied to a source occurrence, chunk, locator, content hash, and evidence kind.

A **candidate-revision evidence association** is the explicit link saying that a particular candidate revision is supported by a particular evidence reference.

These are different. Chunk-level provenance does not by itself establish candidate-specific support.

### 4.2 Exact candidate-revision-to-evidence association

Conversion, review, and duplicate governance may depend on exact associations, not loose proximity. The contract therefore requires that a candidate revision carry explicit evidence associations rather than relying solely on the chunk it was extracted from.

### 4.3 Quote or passage validation

Quote or passage validation is the process of checking that the candidate-specific evidence actually supports the exact educational item claimed.

This contract does **not** assume the current provider schema can return candidate-specific quotations or educational roles. That is an implementation gap requiring a deliberate extraction-interface decision.

### 4.4 Source integrity validation

Evidence validity depends on source integrity. If a source occurrence is later found to be unavailable, withdrawn, or otherwise changed, the platform must:
- identify affected evidence
- identify affected candidate revisions
- assess whether the candidate remains supported
- not silently assume continuity

### 4.5 Evidence association status events

Each candidate-revision evidence association may carry a status from:
- `valid`
- `invalid`
- `superseded`

These events make evidence changes auditable and allow conversion eligibility to respond to evidence changes.

### 4.6 How evidence changes affect conversion eligibility

If candidate-specific evidence is missing, invalid, or superseded without replacement, conversion eligibility must be affected. The exact policy is a decision point; the contract only requires that the effect be explicit, auditable, and not bypassed by chunk-level defaults.

### 4.7 Chunk-level provenance is not candidate evidence

Current behavior stores evidence at chunk level and ties a whole chunk to a concept. That is insufficient for candidate governance, because one chunk can support multiple distinct educational items and because candidate reconciliation needs item-level support, not only chunk-level existence.

---

## 5. Candidate review governance

### 5.1 Review event model

Review is recorded as append-only `CandidateReviewEvent` records.

Each event must include:
- exact candidate revision
- actor
- action
- rationale where required
- monotonic sequence
- expected previous event or sequence
- stale-write rejection

### 5.2 Supported actions

- `submit_for_review`
- `approve_concept`
- `attach_detail`
- `reject_candidate`
- `request_more_evidence`
- `reopen_for_review`

### 5.3 Reopening

Reopening requires:
- explicit authority
- rationale
- concurrency validation

### 5.4 Approval scope

Approval of one revision must not automatically approve later revisions.

---

## 6. Source version status events

### 6.1 Event model

Source-version status is governed by append-only `SourceVersionStatusEvent` records.

The event history is authoritative. Projections are rebuildable.

### 6.2 Atomic registration

```
register_source_version(
    source_id,
    new_source_version,
    expected_current_source_version_id,
    authorization_context
)
```

This operation supports:
- first-version registration
- supersession
- concurrency safeguards
- a clear prototype-versus-production distinction

### 6.3 Prototype versus production

A single-process prototype may simulate this with in-memory checks. Production requires durable transactions, unique constraints, locking or compare-and-swap, and durable idempotency.

---

## 7. Duplicate governance

### 7.1 Core types

- `DuplicatePair`
- `DuplicateObservation`
- `DuplicateReviewEvent`

### 7.2 Pair semantics

A `DuplicatePair` is a typed unordered pair.

Its canonical pair key is based on **sorted entity type and id**.

Uniqueness is defined by the pair and the duplicate-governance version.

### 7.3 Detector limits

Detector observations are advisory only.

Detector output never:
- merges candidates
- transfers evidence

### 7.4 Human decisions

Human decisions apply to exact revisions.

Supported human decisions:
- `distinct`
- `merge_with_existing`
- `replace_candidate`

### 7.5 Evidence transfer prohibition

New revisions and new detector versions require fresh governance consideration. Automatic evidence transfer is prohibited.

### 7.6 Unresolved duplicates block conversion

Unresolved relevant duplicate pairs block conversion.

---

## 8. Candidate detail attachments

### 8.1 Attachment model

`CandidateDetailAttachment` is immutable.

Lifecycle events are append-only.

### 8.2 Attachment types

- `property_or_characteristic`
- `component`
- `example`
- `procedure_or_step`

Initial target type is `concept_draft`.

### 8.3 Attachment constraints

An attachment must not create an independent concept or prerequisite node.

### 8.4 Lifecycle states

Lifecycle events cover:
- creation
- activation
- supersession
- withdrawal
- target rejection

### 8.5 Activation rule

An attachment is active only when its exact target revision passes the required approval gate.

---

## 9. Controlled conversion to ConceptDraft

### 9.1 Requirement

`ConceptDraft` may only be created through the controlled conversion path in the new architecture.

### 9.2 Conversion requirements

Conversion must require:
- exact candidate revision
- effective human approval
- valid evidence association heads
- valid source status heads
- validated candidate-specific evidence
- resolved relevant duplicate reviews
- current and available source version
- authorization
- concurrency token

### 9.3 Atomicity

Conversion must be atomic.

### 9.4 Conversion record

Conversion must produce:
- a conversion record
- a snapshot of relevant event heads
- an idempotency key

### 9.5 Existing-conversion behavior

If a conversion already exists for the same logical operation, the system must handle it explicitly rather than silently creating a second draft.

### 9.6 Failure behavior

Failure must produce no partial writes.

### 9.7 Prototype limitations

A prototype may demonstrate the invariant that extraction cannot directly create `ConceptDraft`, but it cannot claim production-grade durability, locking, or authorization guarantees.

---

## 10. Compatibility and migration

### 10.1 Preserved values

Preserve existing source-role values:
- `instructor`
- `reference`

Do not silently rename or reinterpret production contracts.

### 10.2 Compatible existing models

Compatibility must be assessed for:
- `ContentChunk`
- `EvidenceRef`
- `ConceptDraft`
- `ReviewState`
- `RelationshipDraft`
- `PrototypeRepository`

### 10.3 Paths that must be disabled, replaced, or adapted

Existing paths that allow direct extraction-to-`ConceptDraft` bypass must be disabled, replaced, or adapted so that `ConceptDraft` can only be created through the controlled conversion path.

---

## 11. Prototype versus production boundaries

### 11.1 Single-process prototype guarantees

A single-process prototype can demonstrate:
- data-model structure
- deterministic in-memory logic
- fail-closed rejection of invalid input
- prototype-level event identity
- workflow sequencing and audit recording in one process

### 11.2 Requires durable transactions

- conversion atomicity
- source-version registration with supersession
- append-only review and duplicate history
- Idempotency that survives process restart

### 11.3 Requires unique database constraints

- candidate identity
- occurrence identity
- duplicate pair uniqueness
- event ordering and duplicate suppression

### 11.4 Requires locking or compare-and-swap

- concurrent source-version registration
- concurrent conversion attempts
- concurrent review and duplicate decisions on the same revision

### 11.5 Requires durable idempotency

- source-change event processing
- conversion idempotency keys
- duplicate-governance operation replay safety

### 11.6 Requires authorization infrastructure

- authority model for approval, reopening, severity assessment, restriction clearance
- capability assignment
- attribution and non-repudiation for production use

### 11.7 No false production claims

A prototype must not be represented as providing production-grade guarantees.

---

## 12. Deferred decisions

The following are explicitly unresolved and must not be invented by this contract:

- Authority and capability model
- Retention policies
- Superseded evidence publication policy
- Production persistence design
- Re-conversion policy
- Cross-source and cross-version candidate continuity
- Exact quote extraction strategy
- Bilingual normalization rules

Any requirement that depends on these matters is marked **OPEN DECISION** where relevant.

---

## 13. Open decisions in this contract

- Exact conversion eligibility policy for evidence that is `superseded` but not yet replaced: **OPEN DECISION**.
- Exact rule for when a new source version forces reopening versus allowing the existing candidate to remain current: **OPEN DECISION**.
- Exact relationship between candidate-specific evidence extraction and the provider schema: **OPEN DECISION**.
- Exact production authorization model: **OPEN DECISION**.
