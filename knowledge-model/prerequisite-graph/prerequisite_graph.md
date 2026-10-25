# Prerequisite Graph (Week 6 Draft)

A Directed Acyclic Graph (DAG) representing concept dependencies across 73 concepts in 4 layers. Edges represent hard prerequisites used for adaptive routing.

## Layer 1: Mathematics Prerequisites

| Edge ID | Concept ID (dependent) | Prerequisite Concept ID | Strength | Description |
|---|---|---|---|---|
| E01 | M02 | M01 | 1.0 | Fractions requires Arithmetic Operations |
| E02 | M03 | M01 | 1.0 | Decimals requires Arithmetic Operations |
| E03 | M04 | M03 | 1.0 | Variables & Substitution requires Decimals |
| E04 | M05 | M03 | 1.0 | Algebraic Expressions requires Decimals |
| E05 | M06 | M04 | 1.0 | Linear Inequalities requires Variables & Substitution |
| E06 | M07 | M04 | 1.0 | Linear Equations requires Variables & Substitution |
| E07 | M08 | M04 | 1.0 | Equations with One Unknown requires Variables & Substitution |
| E08 | M09 | M08 | 1.0 | Algebraic Word Problems requires Equations with One Unknown |
| E09 | M10 | M05 | 1.0 | Polynomials requires Algebraic Expressions |
| E10 | M11 | M09 | 1.0 | Factoring requires Algebraic Word Problems |
| E11 | M12 | M10 | 1.0 | Quadratic Equations requires Polynomials |
| E12 | M13 | M11 | 1.0 | Systems of Equations requires Factoring |
| E13 | M14 | M07 | 1.0 | Functions requires Linear Equations |
| E14 | M15 | M14 | 1.0 | Function Composition requires Functions |
| E15 | M16 | M14 | 1.0 | Inverse Functions requires Functions |
| E16 | M17 | M14 | 1.0 | Inequality Systems requires Linear Equations |
| E17 | M18 | M14 | 1.0 | Absolute Value requires Linear Equations |
| E18 | M19 | M17 | 1.0 | Exponents and Powers requires Inequality Systems |
| E19 | M20 | M18 | 1.0 | Logarithms requires Exponents and Powers |
| E20 | M21 | M19 | 1.0 | Sequences and Series requires Exponents and Powers |
| E21 | M22 | M20 | 1.0 | Basic Probability requires Logarithms |

## Layer 2: Programming Prerequisites

| Edge ID | Concept ID (dependent) | Prerequisite Concept ID | Strength | Description |
|---|---|---|---|---|
| E22 | P03 | P02 | 1.0 | Input/Output requires Data Types |
| E23 | P04 | P02 | 1.0 | Conditional Statements requires Data Types |
| E24 | P05 | P03 | 1.0 | Comparison Operators requires Input/Output |
| E25 | P06 | P03 | 1.0 | Boolean Logic requires Input/Output |
| E26 | P07 | P04 | 1.0 | Loops (for) requires Conditional Statements |
| E27 | P08 | P04 | 1.0 | Loops (while) requires Conditional Statements |
| E28 | P09 | P07 | 1.0 | Loop Control (break/continue) requires Loops (for) |
| E29 | P10 | P06 | 1.0 | Functions requires Boolean Logic |
| E30 | P11 | P10 | 1.0 | Function Parameters requires Functions |
| E31 | P12 | P10 | 1.0 | Return Values requires Functions |
| E32 | P13 | P11 | 1.0 | Recursion requires Function Parameters |
| E33 | P14 | P11 | 1.0 | Arrays requires Function Parameters |
| E34 | P15 | P13 | 1.0 | Array Indexing requires Arrays |
| E35 | P16 | P14 | 1.0 | Array Methods (map, filter, reduce) requires Array Indexing |
| E36 | P17 | P14 | 1.0 | Strings requires Array Methods |
| E37 | P18 | P16 | 1.0 | String Methods requires String Methods |
| E38 | P19 | P17 | 1.0 | File Input/Output requires Strings |
| E39 | P20 | P18 | 1.0 | Error Handling requires File Input/Output |

## Layer 3: Data Prerequisites

| Edge ID | Concept ID (dependent) | Prerequisite Concept ID | Strength | Description |
|---|---|---|---|---|
| E40 | D03 | D02 | 1.0 | Tables and Relations requires Records and Tuples |
| E41 | D04 | D03 | 1.0 | Primary Key requires Tables and Relations |
| E42 | D05 | D03 | 1.0 | Foreign Key requires Tables and Relations |
| E43 | D06 | D04 | 1.0 | Joins (INNER, LEFT, RIGHT) requires Primary Key |
| E44 | D07 | D05 | 1.0 | Aggregation (COUNT, SUM, AVG) requires Foreign Key |
| E45 | D08 | D05 | 1.0 | Group By requires Foreign Key |
| E46 | D09 | D04 | 1.0 | Filtering (WHERE, HAVING) requires Primary Key |
| E47 | D10 | D04 | 1.0 | Sorting (ORDER BY) requires Primary Key |
| E48 | D11 | D07 | 1.0 | Set Operations (UNION, INTERSECT) requires Aggregation |
| E49 | D12 | D11 | 1.0 | Joins with Subqueries requires Set Operations |
| E50 | D13 | D12 | 1.0 | Normalization (1NF, 2NF, 3NF) requires Joins with Subqueries |
| E51 | D14 | D13 | 1.0 | Indexing and Performance requires Normalization |
| E52 | D15 | D14 | 1.0 | Cursors and Iteration requires Indexing and Performance |

## Layer 4: ML Core Prerequisites

| Edge ID | Concept ID (dependent) | Prerequisite Concept ID | Strength | Description |
|---|---|---|---|---|
| E53 | ML04 | ML03 | 1.0 | Train-Test Split requires Model Evaluation |
| E54 | ML05 | ML03 | 1.0 | Cross-Validation requires Model Evaluation |
| E55 | ML06 | ML05 | 1.0 | Accuracy requires Cross-Validation |
| E56 | ML07 | ML05 | 1.0 | Precision and Recall requires Cross-Validation |
| E57 | ML08 | ML06 | 1.0 | AUC-ROC requires Accuracy |
| E58 | ML09 | ML06 | 1.0 | Log Loss requires Accuracy |
| E59 | ML10 | ML07 | 1.0 | Overfitting and Underfitting requires Precision and Recall |
| E60 | ML11 | ML09 | 1.0 | Bias-Variance Tradeoff requires Log Loss |
| E61 | ML12 | ML04 | 1.0 | Knowledge Tracing (BKT) requires Train-Test Split |
| E62 | ML13 | ML05 | 1.0 | Knowledge Tracing (DKT) requires Cross-Validation |
| E63 | ML14 | ML11 | 1.0 | Prerequisite Graph requires Bias-Variance Tradeoff |
| E64 | ML15 | ML13 | 1.0 | Graph-Aware Routing requires Knowledge Tracing (DKT) |
| E65 | ML16 | ML12 | 1.0 | Spaced Repetition requires Knowledge Tracing (BKT) |

## Cross-Layer Prerequisites

| Edge ID | Concept ID (dependent) | Prerequisite Concept ID | Strength | Description |
|---|---|---|---|---|
| E66 | P09 | M18 | 0.8 | Loop Control conceptualizes Absolute Value logic |
| E67 | D09 | M06 | 0.7 | Filtering (WHERE) conceptualizes Linear Inequalities |
| E68 | ML14 | P13 | 0.9 | Prerequisite Graph requires understanding Recursion (recursive concept mapping) |
| E69 | ML15 | D06 | 0.8 | Graph-Aware Routing requires Foreign Key concept (relational thinking) |
| E70 | ML16 | M22 | 0.7 | Spaced Repetition builds on Basic Probability (retention decay models) |

## Graph Properties

- **Total concepts**: 73 (22 Mathematics + 20 Programming + 15 Data + 16 Machine Learning)
- **Total edges**: 72 directed prerequisite relationships
- **Graph structure**: Layered DAG with intra-layer and cross-layer edges
- **Root concepts** (no prerequisites): M01, P02, P03, D02, ML01, ML02
- **Leaf concepts** (no dependents): M22, P20, D15, ML16
- **Usage**: Adaptive routing determines next concept based on mastered prerequisites and student mastery estimates