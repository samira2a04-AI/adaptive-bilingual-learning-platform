# Candidate Governance Implementation Gap Matrix

**Purpose:** Audit the existing repository against `Candidate_Governance_Contract_v1.md` without modifying application code or tests.

**Reading guide:**
- `EXISTS` means a data model, method, or value exists in the repository.
- `PARTIAL` means something exists but is incomplete, disabled, prototype-scoped, or not fully asserted by tests.
- `MISSING` means no corresponding model, operation, or invariant is present.
- `BROKEN` means existing code is present but non-executable or incorrect.
- `DEFERRED` means the contract explicitly leaves the matter open, or the repository has only an advisory/proposal artifact, not a governed one.

**Important:** An existing model does not prove its workflow works. An existing test does not prove an invariant unless the test actually asserts it.

---

## 1. Source identity and provenance

| Contract requirement | Current implementation | Evidence in repository | Gap | Required change | Dependencies | Tests required |
|---|---|---|---|---|---|---|
| `SourceVersion` as a governed version record | No governed `SourceVersion` entity; source version appears only as a recorded field on chunk/evidence | `ContentChunk.source_version` (`automation.py:44-50`); `EvidenceRef.source_version` (`contracts.py:473-495`); manifest `docs/km_pilot_ingestion_manifest.json`; source inventory `knowledge-model/sources/source_inventory.csv` | MISSING | New source-version registration and supersession model | Source-scope decision; durable store | Yes |
| `SourceOccurrence` with composite identity `(source_id, source_version, chunk_id)` | Composite identity not modeled as a governance object; chunk has the parts separately | `ContentChunk` fields; `EvidenceRef` provenance fields | PARTIAL | Add explicit occurrence model with scope and uniqueness constraints | Source-version model | Yes |
| Source-version current vs superseded distinction | No current/superseded projection or lifecycle | No current source-version registry in repository | MISSING | Add current/superseded semantics | Source-version model | Yes |
| Available, unavailable, withdrawn status | Source status vocabulary not present in KM code | No source status event type or lifecycle | MISSING | Add source status events and projections | Source-version model | Yes |
| Content hash validation of chunk contents | `content_hash` exists and is stored; validation of actual chunk contents is not implemented as a governed operation | `ContentChunk.content_hash`; `EvidenceRef.content_hash` | PARTIAL | Add chunk-content validation against stored source content | Source occurrence model; stored chunk access | Yes |
| `content_hash` not treated as globally unique identity | `content_hash` exists but is used as a chunk-level field, not as global identity | `automation.py:44-50`; `contracts.py:473-495` | EXISTS (as field), contract rule not enforced by dedicated governance type | Clarify governance treatment; avoid using hash as identity in new code | — | Yes |
| `locator` not treated as machine identity | `locator` exists as a field; locator is not asserted as a machine identity | `ContentChunk.locator`; `EvidenceRef.locator` | EXISTS (as field) | Preserve locator as retrieval/hint field; do not promote it to durable identity | — | — |
| Source version change does not imply educational equivalence or difference | No source-version-change behavior implemented; existing `receive_source_change` computes impact but does not decide equivalence | `prototype.py:receive_source_change` (working method); dead `record_source_change` at `prototype.py:151` is BROKEN | PARTIAL | Implement source-version change handling without assuming educational equivalence | Impact closure; candidate governance | Yes |
| Identical content is not proof of same occurrence | No duplicate-ingestion governance in KM; only chunk-level storage | `ContentChunk`; manifest; snapshots | MISSING | Add duplicate-ingestion handling as a governance concern | Source-occurrence model; duplicate governance | Yes |
| Manifest can be validated against source content | Manifest exists; validation against actual source content is not implemented as a governed KM operation | `docs/km_pilot_ingestion_manifest.json` | PARTIAL | Implement validation path using chunk boundary + content hash as inputs | Stored source snapshot or accessible source | Yes |

---

## 2. Candidate identity and revisions

| Contract requirement | Current implementation | Evidence in repository | Gap | Required change | Dependencies | Tests required |
|---|---|---|---|---|---|---|
| App-owned candidate identity independent of name/canonical/category/description/granularity/provider ids | Candidate grouping in current pipeline is by canonical-name casefold key; candidate identity is derived from labels | `automation.py:extract_concepts` groups by `candidate.canonical_name.casefold()`; `ExtractedConcept` lacks candidate identity fields | MISSING | Introduce app-owned candidate identity separate from labels | New candidate models; reconciliation | Yes |
| `CandidateOccurrence` | No such type | No occurrence model | MISSING | New type | Candidate revision; evidence association | Yes |
| `CandidateRevision` | No such type; `ConceptDraft.revision` exists but is not a governed candidate-revision lifecycle object | `ConceptDraft.revision` (`contracts.py:503-530`) | MISSING | New type and lifecycle | Candidate occurrence; approval gating | Yes |
| `CandidateRunLink` | No such type | No run-linking model | MISSING | New type | Extraction/ingestion run context | Yes |
| `CandidateRevisionEvidence` | No such type; evidence is associated at chunk/concept level only | `ConceptDraft.evidence_ids`; `EvidenceRef` | MISSING | New association type | Candidate revision; evidence validation | Yes |
| Content change creates new immutable revision | Revision increment exists on `ConceptDraft`, but no governed immutable candidate-revision history | `ConceptDraft.revise_metadata` (`contracts.py:532-541`) | PARTIAL | Distinguish candidate revision from draft metadata revision; enforce immutability | Candidate revision model | Yes |
| New source version does not automatically establish candidate continuity | Not implemented as a governed rule; no candidate continuity decision path | No such workflow | MISSING | Add continuity decision logic; avoid automatic continuity | Source-version change; reconciliation | Yes |

---

## 3. Reconciliation

| Contract requirement | Current implementation | Evidence in repository | Gap | Required change | Dependencies | Tests required |
|---|---|---|---|---|---|---|
| Four permitted outcomes: `match_existing`, `create_new`, `ambiguous`, `insufficient_evidence` | No reconciliation model with those outcomes | No reconciliation operation | MISSING | New reconciliation operation | Candidate occurrence; evidence; duplicate governance | Yes |
| Name similarity alone never authorizes a match | Existing grouping uses name similarity; no safeguard preventing match-by-name | `automation.py:extract_concepts` grouping by casefold canonical name | BROKEN for candidate governance | Add name-similarity-as-signal-only rule | Reconciliation; candidate identity | Yes |
| Evidence overlap alone never authorizes a merge | No merge governance at all | No duplicate/merge governance beyond advisory embedding similarity | MISSING | Add merge guard; evidence overlap is not authority | Duplicate governance; evidence association | Yes |
| One sentence may support multiple distinct educational items | Current pipeline stores only chunk-level evidence for the whole chunk; no per-item evidence span support | `automation.py:extract_concepts` maps candidates to chunk-level evidence; `EvidenceRef.excerpt = chunk.text` | MISSING | Add candidate-specific evidence association or extraction-interface decision | Extraction-interface decision; evidence model | Yes |
| Ambiguous candidates must not be silently merged or promoted | No ambiguous outcome state | No diagnostic record for failed reconciliation | MISSING | Add ambiguous outcome and diagnostic preservation | Reconciliation | Yes |
| Insufficient evidence must not create eligible candidate | No insufficient-evidence outcome | No admission guard tied to evidence sufficiency | MISSING | Add insufficient-evidence outcome and admission gate | Reconciliation; evidence sufficiency | Yes |
| Preserve diagnostic records for unsuccessful reconciliation | No such preservation | No reconciliation diagnostic storage | MISSING | Add diagnostic record storage | Reconciliation; audit | Yes |

---

## 4. Evidence governance

| Contract requirement | Current implementation | Evidence in repository | Gap | Required change | Dependencies | Tests required |
|---|---|---|---|---|---|---|
| Distinction between evidence record and candidate-revision evidence association | Evidence record exists; candidate-revision evidence association does not | `EvidenceRef`; `ConceptDraft.evidence_ids` | PARTIAL | Add explicit candidate-revision evidence association | Candidate revision model; evidence validation | Yes |
| Exact candidate-revision-to-evidence association | Evidence is associated to concept by chunk, not to a specific candidate revision’s exact passage | `automation.py:extract_concepts` creates one `EvidenceRef` per chunk and groups by casefold name | MISSING | Add exact association model | Candidate revision; extraction-interface decision | Yes |
| Quote or passage validation | No candidate-specific quote validation; `EvidenceRef.excerpt` stores whole chunk text | `contracts.py:473-495`; `automation.py:228` excerpt handling | MISSING | Add quote/passage validation mechanism or deferred decision marker | Extraction-interface decision; source content access | Yes |
| Source integrity validation | Source integrity change is partially handled by `receive_source_change` impact closure; candidate-specific re-support is assessed only at concept/relationship level, not at candidate-revision evidence level | `prototype.py:_compute_impact_closure`; `prototype.py:_assess_re_support`; `ReSupportState` | PARTIAL | Extend impact and re-support logic to candidate revisions and exact evidence | Source-version change; candidate governance | Yes |
| Evidence association status events: `valid`, `invalid`, `superseded` | No such status events on candidate-revision evidence | No candidate-revision evidence status model | MISSING | Add status event model | Candidate revision evidence | Yes |
| Evidence changes affect conversion eligibility | Not implemented; no conversion path exists yet | No conversion operation | MISSING | Add conversion eligibility rules tied to evidence status | Conversion; evidence status | Yes |
| Current provider schema cannot be assumed to return candidate-specific quotations or educational roles | True of current schema; not yet documented as a deliberate extraction-interface gap in the governed contract | `automation.py:_parse_concepts`; provider schemas in `gemini_provider.py` and `openai_provider.py` | PARTIAL | Document extraction-interface decision; do not weaken evidence requirement | Extraction-interface decision | Yes |

---

## 5. Candidate review governance

| Contract requirement | Current implementation | Evidence in repository | Gap | Required change | Dependencies | Tests required |
|---|---|---|---|---|---|---|
| Append-only `CandidateReviewEvent` records | No candidate review event type; concept review uses `ReviewState` transitions and generic `AuditEvent` | `ReviewState`; `AuditEvent`; `review_submit_concept`; `review_reject_concept` | MISSING | Add candidate-specific review event type with exact revision, actor, action, rationale, sequence, expected previous event, stale-write rejection | Candidate revision; approval gating | Yes |
| Supported actions: `submit_for_review`, `approve_concept`, `attach_detail`, `reject_candidate`, `request_more_evidence`, `reopen_for_review` | Submission and rejection exist for concepts, but approval is disabled; no candidate review action vocabulary or reopening governance | `review_submit_concept`; `review_reject_concept`; `approve_for_prototype` raises `PrototypeBoundaryError` | PARTIAL | Add full candidate review action set and reopening authority/validation | Approval authority decision; candidate revision | Yes |
| Reopening requires authority, rationale, concurrency validation | Not implemented; reopening not modeled | No reopening operation | MISSING | Add reopening operation with authority and concurrency validation | Review event model; authorization | Yes |
| Approval of one revision must not automatically approve later revisions | Not enforced anywhere because approval is disabled | `approve_for_prototype` disabled | MISSING | Enforce revision-scoped approval | Approval gating; candidate revision | Yes |

---

## 6. Source version status events

| Contract requirement | Current implementation | Evidence in repository | Gap | Required change | Dependencies | Tests required |
|---|---|---|---|---|---|---|
| Append-only `SourceVersionStatusEvent` records | No such event type | No source-status event model | MISSING | New event type and event history projection | Source-version model | Yes |
| Event history authoritative; projections rebuildable | Not implemented | No source status history | MISSING | Implement event-driven source status | Source-version model | Yes |
| Atomic `register_source_version` with expected current version id and authorization context | No such operation; prototype has no source registration | `PrototypeSnapshotRegistry` exists but is for model snapshots, not source versions | MISSING | Add source-version registration operation | Source-version model; authorization; concurrent writes | Yes |
| First-version registration and supersession | Not implemented | No source-version lifecycle | MISSING | Implement first-version and supersession paths | Source-version model | Yes |
| Prototype-vs-production distinction | Prototype in-memory support only; no production claim | `PrototypeRepository`; `PrototypeSnapshotRegistry` | EXISTS (prototype boundary documented) | Keep distinction; do not claim production durability from in-memory repo | Durable store; concurrency | Yes |

---

## 7. Duplicate governance

| Contract requirement | Current implementation | Evidence in repository | Gap | Required change | Dependencies | Tests required |
|---|---|---|---|---|---|---|
| `DuplicatePair` with typed unordered pair and canonical pair key from sorted entity type and id | No such type; similarity is computed as an unordered pair but not governed | `duplicate_candidates` returns sorted pairs; `recommend_duplicate_merge` is advisory | MISSING | Add governed `DuplicatePair` model with canonical key | Candidate revision; duplicate review | Yes |
| `DuplicateObservation` | No such type; embedding similarity and merge recommendation exist as advisory output only | `duplicate_candidates`; `recommend_duplicate_merge` | MISSING | Add observation type; mark detector output advisory | Detector output separation; duplicate review | Yes |
| `DuplicateReviewEvent` | No such event type | No duplicate review governance | MISSING | Add duplicate review event model | Candidate revision; duplicate decision | Yes |
| Uniqueness by pair and duplicate-governance version | Not enforced | No duplicate governance version or unique constraint | MISSING | Add uniqueness rule | Duplicate pair model; durable store | Yes |
| Detector observations are advisory only | Code produces advisory recommendations; tests assert recommendation content, not governance rule that detector cannot merge | `recommend_duplicate_merge`; `test_km_t8_candidate_diff.py`-style expectations not examined here | PARTIAL | Make advisory-only rule explicit in governance | Duplicate review | Yes |
| Detector output never merges candidates or transfers evidence | No merge/transfer path in detector code, but no governed prohibition either | `duplicate_candidates`; `recommend_duplicate_merge` | PARTIAL | Add explicit prohibition | Duplicate governance | Yes |
| Human decisions apply to exact revisions | Not implemented | No duplicate decision on revisions | MISSING | Add revision-scoped duplicate decisions | Candidate revision; duplicate review | Yes |
| Supported human decisions: `distinct`, `merge_with_existing`, `replace_candidate` | No such governed decisions | No duplicate decision vocabulary | MISSING | Add decision vocabulary and consequences | Duplicate review; evidence governance | Yes |
| Automatic evidence transfer prohibited | Not implemented as a rule | No evidence transfer path, but no prohibition either | MISSING | Add explicit prohibition | Evidence governance; duplicate governance | Yes |
| Unresolved relevant duplicate pairs block conversion | No conversion path; no block rule | No conversion operation | MISSING | Add block rule to conversion | Conversion; duplicate review | Yes |
| New revisions and new detector versions require fresh governance consideration | Not implemented | No versioning of duplicate governance | MISSING | Add versioned duplicate governance consideration | Duplicate pair model; detector versioning | Yes |

---

## 8. Candidate detail attachments

| Contract requirement | Current implementation | Evidence in repository | Gap | Required change | Dependencies | Tests required |
|---|---|---|---|---|---|---|
| Immutable `CandidateDetailAttachment` | No such type | No attachment model | MISSING | New type | Candidate revision; lifecycle | Yes |
| Append-only lifecycle events | No attachment lifecycle | No attachment events | MISSING | Add lifecycle events | Attachment model | Yes |
| Attachment types: `property_or_characteristic`, `component`, `example`, `procedure_or_step` | Not modeled | No attachment type vocabulary | MISSING | Add type vocabulary | Attachment model | Yes |
| Initial target type: `concept_draft` | Not modeled | No target type | MISSING | Define initial target type | Attachment model | Yes |
| Attachment must not create independent concept or prerequisite node | Not enforced; no attachment concept exists | No attachment model | MISSING | Add constraint | Attachment model; graph model | Yes |
| Lifecycle: creation, activation, supersession, withdrawal, target rejection | Not implemented | No attachment lifecycle | MISSING | Add lifecycle states/events | Attachment model; approval gating | Yes |
| Attachment active only when exact target revision passes required approval gate | Not implemented; approval itself is disabled | `approve_for_prototype` disabled | MISSING | Add activation rule tied to approval gate | Attachment model; approval | Yes |

---

## 9. Controlled conversion to ConceptDraft

| Contract requirement | Current implementation | Evidence in repository | Gap | Required change | Dependencies | Tests required |
|---|---|---|---|---|---|---|
| `ConceptDraft` only through controlled conversion | Direct creation exists in current pipeline; extraction creates `ConceptDraft` directly | `automation.py:extract_concepts` creates `ConceptDraft` and calls `propose_concept` | BROKEN for new contract | Remove direct extraction-to-draft path; add conversion gate | Candidate governance; approval; evidence | Yes |
| Conversion requires exact candidate revision | No conversion operation | No conversion operation | MISSING | Add conversion operation with revision scoping | Candidate revision; approval | Yes |
| Conversion requires effective human approval | Approval disabled; no conversion path | `approve_for_prototype` disabled | MISSING | Add approval-gated conversion | Approval authority; candidate revision | Yes |
| Conversion requires valid evidence association heads | No evidence association heads model | No conversion operation | MISSING | Add evidence-head validation in conversion | Candidate revision evidence; source status | Yes |
| Conversion requires valid source status heads | No source status heads model | No conversion operation | MISSING | Add source-status validation in conversion | Source-version model; source status events | Yes |
| Conversion requires validated candidate-specific evidence | Not implemented | No candidate-specific evidence validation | MISSING | Add candidate-specific evidence validation | Quote/passage validation; source integrity | Yes |
| Conversion requires resolved relevant duplicate reviews | No duplicate review model | No conversion operation | MISSING | Add duplicate-review resolution requirement | Duplicate review | Yes |
| Conversion requires current and available source version | No source availability model | No source status model | MISSING | Add current/available version requirement | Source-version model; source status | Yes |
| Conversion requires authorization and concurrency token | Not implemented | No authorization model for conversion | MISSING | Add authorization and concurrency token | Authorization model; durable store | Yes |
| Conversion must be atomic | No conversion operation | No conversion operation | MISSING | Implement atomic conversion | Durable store; transaction support | Yes |
| Conversion record, event head snapshot, idempotency key | Not implemented | No conversion record model | MISSING | Add conversion record and snapshot model | Conversion; audit | Yes |
| Existing-conversion behavior defined | Not implemented | No conversion operation | MISSING | Define existing-conversion handling | Conversion idempotency | Yes |
| Failure behavior with no partial writes | No conversion operation; partial-write guarantees not applicable yet | No conversion operation | MISSING | Define failure semantics and implement without partial writes | Atomic conversion | Yes |
| Prototype limitations vs production requirements | Prototype can enforce the invariant that extraction does not directly create `ConceptDraft`; production needs durable constraints | `PrototypeRepository`; `automation.py` path | PARTIAL | Implement prototype invariant; document production requirements separately | Durable store; authorization; locking/CAS | Yes |

---

## 10. Compatibility and migration

| Contract requirement | Current implementation | Evidence in repository | Gap | Required change | Dependencies | Tests required |
|---|---|---|---|---|---|---|
| Preserve existing source-role values `instructor` and `reference` | Code already restricts `source_role` to those two values | `EvidenceRef.source_role`; `ContentChunk.source_role`; `contracts.py` validation | EXISTS | Preserve; do not rename or reinterpret silently | — | — |
| Compatibility with `ContentChunk` | Model exists; not yet governed under candidate provenance rules | `ContentChunk` | EXISTS (model), compatibility rule not governed | Adapt use under candidate governance | Source occurrence model | Yes |
| Compatibility with `EvidenceRef` | Model exists; excerpt is whole chunk; no candidate-specific evidence field | `EvidenceRef` | EXISTS (model), candidate-specific gap remains | Adapt or extend for candidate-specific evidence | Extraction-interface decision | Yes |
| Compatibility with `ConceptDraft` | Model exists; created directly by extraction today | `ConceptDraft`; `automation.py:extract_concepts` | EXISTS (model), creation path conflicts with contract | Restrict creation to conversion path | Conversion; extraction bypass disable | Yes |
| Compatibility with `ReviewState` | Enum exists; no candidate review event layer on top | `ReviewState` | EXISTS (model), insufficient for candidate review governance | Add review event layer; preserve enum compatibility | Candidate review governance | Yes |
| Compatibility with `RelationshipDraft` | Model exists; not in scope of candidate governance directly but affected by evidence and source changes | `RelationshipDraft` | EXISTS (model) | Keep compatibility; assess impact of candidate governance on relationship evidence | Evidence governance; source-change impact | Yes |
| Compatibility with `PrototypeRepository` | Exists; prototype can host candidate governance demo but cannot claim production guarantees | `PrototypeRepository` | EXISTS (model), prototype-only | Keep prototype behavior; explicit boundary documentation | Production persistence decision | Yes |
| Existing paths that must be disabled/replaced/adapted to prevent direct extraction-to-draft bypass | Direct creation path exists | `automation.py:extract_concepts` creates `ConceptDraft` | BROKEN for contract | Disable/replace/adapt extraction-to-draft path | Conversion; candidate governance | Yes |

---

## 11. Prototype versus production boundaries

| Contract requirement | Current implementation | Evidence in repository | Gap | Required change | Dependencies | Tests required |
|---|---|---|---|---|---|---|
| Single-process prototype guarantees | Prototype can demonstrate in-memory deterministic logic and fail-closed rejection | `PrototypeRepository`; `receive_source_change`; `validation.py` | EXISTS for in-memory demo | Keep prototype scope explicit | — | Yes |
| Durable transactions | Not available | No persistence layer in KM | MISSING | Add or bind durable store for production | Production persistence design | Yes |
| Unique database constraints | Not available | No DB constraints | MISSING | Add unique constraints for candidate identity, occurrence identity, duplicate pair, etc. | Production persistence design | Yes |
| Locking or compare-and-swap | Not available | No concurrent write control in prototype | MISSING | Add CAS/locking for concurrent operations | Production persistence design | Yes |
| Durable idempotency | Only in-memory idempotent results | `PrototypeRepository._idempotent_results` | PARTIAL | Make idempotency durable for production | Production persistence design | Yes |
| Authorization infrastructure | Only capability seams; no real authority model | Capability names in `PrototypeRepository`; `AuthorizationContext` | MISSING | Add authority/capability model | Authorization decision | Yes |
| No false production claims | Prototype boundary is documented in code and audit | `prototype.py` scope docstring; `KM_T0_Independent_Repository_Audit.md` | EXISTS | Preserve honest boundary language | — | — |

---

## 12. Deferred decisions

| Contract requirement | Current implementation | Evidence in repository | Gap | Required change | Dependencies | Tests required |
|---|---|---|---|---|---|---|
| Authority and capability model | Not decided | Only capability seams | DEFERRED | Decide before production authorization work | ADR-11 style decision | Yes |
| Retention policies | Not decided | No retention model | DEFERRED | Decide later; do not invent | — | — |
| Superseded evidence publication policy | Not decided | No superseded-evidence policy | DEFERRED | Decide later | Evidence status events | Yes |
| Production persistence design | Not decided | No production persistence | DEFERRED | Decide later | — | — |
| Re-conversion policy | Not decided | No conversion operation yet | DEFERRED | Decide later; mark OPEN DECISION in contract | Conversion model | Yes |
| Cross-source and cross-version candidate continuity | Not decided | No continuity rules | DEFERRED | Decide later; mark OPEN DECISION | Source-version model; candidate continuity | Yes |
| Exact quote extraction strategy | Not decided; current schema does not return candidate-specific quotes | `automation.py:_parse_concepts`; provider schemas | DEFERRED | Decide extraction-interface change or gap | Extraction-interface decision | Yes |
| Bilingual normalization rules | Not decided | Bilingual content exists in artifacts; no normalization rules in KM | DEFERRED | Decide later | Bilingual content model | Yes |

---

## Summary counts

- EXISTS: source-role values; several existing data models; prototype boundary documentation; in-memory idempotent logic; audit event recording.
- PARTIAL: source/version/chunk fields already exist but not governed as occurrence/source-version/candidate objects; advisory duplicate detection exists but not governed duplicate review; concept review submission/rejection exists but not candidate review governance; impact closure exists but not candidate-specific evidence re-support.
- MISSING: candidate occurrence, candidate revision, candidate review event, candidate-revision evidence association, source-version registration, source status events, duplicate pair/observation/review event, attachment model, controlled conversion operation, quote/passage validation, exact candidate-specific evidence, blocking rule for unresolved duplicates, activation rule for attachments.
- BROKEN: extraction currently creates `ConceptDraft` directly; that path must not remain the conversion path; some existing review/approval seams are disabled; no candidate-specific evidence extraction exists in current schema.
- DEFERRED: all deferred matters listed in contract §12.

---

## Items most important to the first implementation boundary

1. Extraction must not directly create `ConceptDraft`.
2. Candidate identity must be app-owned and independent of labels.
3. Candidate-specific evidence association must exist before conversion can be governed.
4. Conversion must be gated by approval, evidence heads, source status, duplicate resolution, authorization, and concurrency.
5. Source-version registration and source status events are prerequisite governance for source-change-driven candidate effects.

These items are why the first milestone cannot be full candidate governance; it must be the smallest boundary that breaks the direct extraction-to-draft path while introducing app-owned candidate identity and candidate-specific evidence association.
