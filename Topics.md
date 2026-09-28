# AI Engineer Plan - Tailored for a .NET Backend Engineer

**Start:** Mon 28 Sep 2026  |  **End:** 18 Jun 2027  |  **264 days / 37 weeks / 1644 items**

**79 days removed** because you already own those skills from C#/.NET/AWS work. Days marked **FAST TRACK** teach only the Python/AI delta versus what you already know.

**Daily 2 hrs:** 45 min theory + 60 min practical + 15 min recall.
---


## Week 1 - Python Fundamentals I
*Phase 1 - Core Software Engineering | Roadmap 0.1*


### Day 1 - Mon 28 Sep 2026 - Variables, data types, strings **[FAST TRACK]**

> Delta only: Python syntax delta vs C#: dynamic typing, str methods, f-strings

**Theory (45 min)**

- [ ] Numbers
- [ ] Str
- [ ] Bool
- [ ] None
- [ ] Immutability
- [ ] F-strings
- [ ] String methods

**Practical (60 min)**

- [ ] Write a text_stats.py that takes a paragraph and prints word count, char count, top 5 words

**Recall (15 min)**

- [ ] Explain variables, data types, strings in your own words: what is numbers, and when does string methods matter in a production LLM system?

### Day 2 - Tue 29 Sep 2026 - Lists & tuples **[FAST TRACK]**

> Delta only: Python delta: list vs C# List<T>, tuples, slicing

**Theory (45 min)**

- [ ] Indexing
- [ ] Slicing
- [ ] Mutation
- [ ] Tuple unpacking
- [ ] When to use which

**Practical (60 min)**

- [ ] Build a flight-leg parser: split 'DEL-BOM-MAA' into legs using slicing + tuples

**Recall (15 min)**

- [ ] Explain lists & tuples in your own words: what is indexing, and when does when to use which matter in a production LLM system?

### Day 3 - Wed 30 Sep 2026 - Sets & dictionaries **[FAST TRACK]**

> Delta only: Python delta: dict/set vs Dictionary/HashSet, comprehension syntax

**Theory (45 min)**

- [ ] Hashing
- [ ] Dict methods
- [ ] Nested dicts
- [ ] Set operations

**Practical (60 min)**

- [ ] De-duplicate 1000 fake flight numbers with a set
- [ ] Build a dict index flight_no -> record

**Recall (15 min)**

- [ ] Explain sets & dictionaries in your own words: what is hashing, and when does set operations matter in a production LLM system?

### Day 4 - Thu 01 Oct 2026 - *args, **kwargs, scope

**Theory (45 min)**

- [ ] Positional vs keyword
- [ ] Packing/unpacking
- [ ] LEGB scope
- [ ] Closures

**Practical (60 min)**

- [ ] Write a retry_call(fn, *args, retries=3, **kwargs) helper function

**Recall (15 min)**

- [ ] Explain *args, **kwargs, scope in your own words: what is positional vs keyword, and when does closures matter in a production LLM system?

### Day 5 - Fri 02 Oct 2026 - Iterators **[FAST TRACK]**

> Delta only: Python delta vs IEnumerable/IEnumerator

**Theory (45 min)**

- [ ] Iterable vs iterator
- [ ] __iter__/__next__
- [ ] StopIteration

**Practical (60 min)**

- [ ] Write a custom ChunkIterator that yields a list in batches of N

**Recall (15 min)**

- [ ] Explain iterators in your own words: what is iterable vs iterator, and when does stopiteration matter in a production LLM system?

### Day 6 - Sat 03 Oct 2026 - Generators **[FAST TRACK]**

> Delta only: Python delta: yield vs C# yield return, lazy pipelines

**Theory (45 min)**

- [ ] Yield
- [ ] Lazy evaluation
- [ ] Memory benefit
- [ ] Generator pipelines

**Practical (60 min)**

- [ ] Stream a 200k-line file with a generator
- [ ] Compare memory vs reading it all with a list

**Recall (15 min)**

- [ ] Explain generators in your own words: what is yield, and when does generator pipelines matter in a production LLM system?

### Day 7 - Sun 04 Oct 2026 - Standard library tour **[FAST TRACK]**

> Delta only: Python delta: collections, itertools, pathlib, re

**Theory (45 min)**

- [ ] Collections
- [ ] Itertools
- [ ] Pathlib
- [ ] Os
- [ ] Re basics

**Practical (60 min)**

- [ ] Use Counter + defaultdict + itertools.groupby to build a per-carrier flight count report

**Recall (15 min)**

- [ ] Explain standard library tour in your own words: what is collections, and when does re basics matter in a production LLM system?

## Week 2 - Decorators, Errors, Async
*Phase 1 - Core Software Engineering | Roadmap 0.2*


### Day 8 - Mon 05 Oct 2026 - Dataclasses **[FAST TRACK]**

> Delta only: Python delta vs C# records

**Theory (45 min)**

- [ ] @dataclass
- [ ] Field()
- [ ] Frozen
- [ ] Defaults
- [ ] Ordering

**Practical (60 min)**

- [ ] Rewrite FlightRecord as a frozen dataclass with computed properties

**Recall (15 min)**

- [ ] Explain dataclasses in your own words: what is @dataclass, and when does ordering matter in a production LLM system?

### Day 9 - Tue 06 Oct 2026 - Type hints **[FAST TRACK]**

> Delta only: Python delta: gradual typing + mypy vs C# static typing

**Theory (45 min)**

- [ ] Basic types
- [ ] Optional
- [ ] Union/|
- [ ] List[str]
- [ ] Callable
- [ ] Mypy basics

**Practical (60 min)**

- [ ] Add full type hints to your flights package
- [ ] Run mypy and fix every error

**Recall (15 min)**

- [ ] Explain type hints in your own words: what is basic types, and when does mypy basics matter in a production LLM system?

### Day 10 - Wed 07 Oct 2026 - TypedDict, Generics, Protocol **[FAST TRACK]**

> Delta only: Python delta: structural typing vs C# interfaces/generics

**Theory (45 min)**

- [ ] TypedDict for JSON shapes
- [ ] TypeVar
- [ ] Generic[T]
- [ ] Protocol structural typing

**Practical (60 min)**

- [ ] Write a Generic Repository[T] Protocol with an in-memory implementation

**Recall (15 min)**

- [ ] Explain typeddict, generics, protocol in your own words: what is typeddict for json shapes, and when does protocol structural typing matter in a production LLM system?

### Day 11 - Thu 08 Oct 2026 - Decorators **[FAST TRACK]**

> Delta only: Python delta vs C# attributes/middleware

**Theory (45 min)**

- [ ] Functions as objects
- [ ] Wrapper pattern
- [ ] Functools.wraps
- [ ] Decorators with args

**Practical (60 min)**

- [ ] Write @retry(times=3, backoff=2) and @log_calls decorators and stack them

**Recall (15 min)**

- [ ] Explain decorators in your own words: what is functions as objects, and when does decorators with args matter in a production LLM system?

### Day 12 - Fri 09 Oct 2026 - async/await basics **[FAST TRACK]**

> Delta only: Python delta: event loop vs .NET Task/TaskScheduler

**Theory (45 min)**

- [ ] Coroutines
- [ ] Event loop
- [ ] Await points
- [ ] Asyncio.run

**Practical (60 min)**

- [ ] Write an async function that 'calls' 5 fake APIs with asyncio.sleep and gathers results

**Recall (15 min)**

- [ ] Explain async/await basics in your own words: what is coroutines, and when does asyncio.run matter in a production LLM system?

### Day 13 - Sat 10 Oct 2026 - Concurrent API calls **[FAST TRACK]**

> Delta only: Python delta: gather/TaskGroup vs Task.WhenAll

**Theory (45 min)**

- [ ] Asyncio.gather
- [ ] TaskGroup
- [ ] Semaphores
- [ ] Timeouts
- [ ] Cancellation

**Practical (60 min)**

- [ ] Fetch 20 URLs with httpx.AsyncClient limited to 5 concurrent with a Semaphore

**Recall (15 min)**

- [ ] Explain concurrent api calls in your own words: what is asyncio.gather, and when does cancellation matter in a production LLM system?

### Day 14 - Sun 11 Oct 2026 - When async helps / hurts **[FAST TRACK]**

> Delta only: Python delta: GIL, blocking-in-loop pitfalls

**Theory (45 min)**

- [ ] IO-bound vs CPU-bound
- [ ] Blocking calls in event loop
- [ ] Threads vs async

**Practical (60 min)**

- [ ] Benchmark: 20 sequential vs 20 concurrent LLM-style IO calls
- [ ] Record the numbers

**Recall (15 min)**

- [ ] Explain when async helps / hurts in your own words: what is io-bound vs cpu-bound, and when does threads vs async matter in a production LLM system?

## Week 3 - Pydantic, Testing, Logging, Git
*Phase 1 - Core Software Engineering | Roadmap 0.2-0.3*


### Day 15 - Mon 12 Oct 2026 - Week 4 review + mini build

**Theory (45 min)**

- [ ] Consolidate async

**Practical (60 min)**

- [ ] Build an async batch processor: 100 items, 10 concurrent workers, retries, timing report

**Recall (15 min)**

- [ ] Explain week 4 review + mini build in your own words: what is consolidate async, and when does week 4 review + mini build matter in a production LLM system?

### Day 16 - Tue 13 Oct 2026 - Pydantic models

**Theory (45 min)**

- [ ] BaseModel
- [ ] Field types
- [ ] Defaults
- [ ] Model_dump/model_validate

**Practical (60 min)**

- [ ] Model a flight API payload in Pydantic v2 and parse 5 good + 5 bad JSON samples

**Recall (15 min)**

- [ ] Explain pydantic models in your own words: what is basemodel, and when does model_dump/model_validate matter in a production LLM system?

### Day 17 - Wed 14 Oct 2026 - Pydantic validation

**Theory (45 min)**

- [ ] Field constraints
- [ ] Field_validator
- [ ] Model_validator
- [ ] Nested models

**Practical (60 min)**

- [ ] Add cross-field validation: arrival must be after departure
- [ ] Custom error messages

**Recall (15 min)**

- [ ] Explain pydantic validation in your own words: what is field constraints, and when does nested models matter in a production LLM system?

### Day 18 - Thu 15 Oct 2026 - Pydantic settings & strictness

**Theory (45 min)**

- [ ] BaseSettings
- [ ] Env vars
- [ ] Strict mode
- [ ] Aliases
- [ ] Serialization

**Practical (60 min)**

- [ ] Create Settings class reading API keys/env from .env
- [ ] Never hardcode secrets

**Recall (15 min)**

- [ ] Explain pydantic settings & strictness in your own words: what is basesettings, and when does serialization matter in a production LLM system?

### Day 19 - Fri 16 Oct 2026 - pytest fundamentals **[FAST TRACK]**

> Delta only: Python delta vs xUnit/NUnit

**Theory (45 min)**

- [ ] Test discovery
- [ ] Assertions
- [ ] Parametrize
- [ ] Fixtures
- [ ] Conftest.py

**Practical (60 min)**

- [ ] Write 15 tests for your validator including parametrized edge cases

**Recall (15 min)**

- [ ] Explain pytest fundamentals in your own words: what is test discovery, and when does conftest.py matter in a production LLM system?

### Day 20 - Sat 17 Oct 2026 - Mocking & integration tests **[FAST TRACK]**

> Delta only: Python delta vs Moq

**Theory (45 min)**

- [ ] Monkeypatch
- [ ] Unittest.mock
- [ ] Faking HTTP
- [ ] Testing failure paths

**Practical (60 min)**

- [ ] Mock an HTTP client and test retry + timeout + non-retryable error paths

**Recall (15 min)**

- [ ] Explain mocking & integration tests in your own words: what is monkeypatch, and when does testing failure paths matter in a production LLM system?

### Day 21 - Sun 18 Oct 2026 - Logging **[FAST TRACK]**

> Delta only: Python delta: structlog/JSON vs Serilog

**Theory (45 min)**

- [ ] Levels
- [ ] Handlers
- [ ] Structured JSON logs
- [ ] Request IDs
- [ ] PII/secret hygiene

**Practical (60 min)**

- [ ] Add JSON structured logging with a correlation_id to your async batch processor

**Recall (15 min)**

- [ ] Explain logging in your own words: what is levels, and when does pii/secret hygiene matter in a production LLM system?

## Week 4 - FastAPI
*Phase 2 - Backend & Data | Roadmap 1.4*


### Day 22 - Mon 19 Oct 2026 - FastAPI setup & routes

**Theory (45 min)**

- [ ] App object
- [ ] Path operations
- [ ] Uvicorn
- [ ] Project layout

**Practical (60 min)**

- [ ] Create a FastAPI app with /health and /v1/documents GET returning static data

**Recall (15 min)**

- [ ] Explain fastapi setup & routes in your own words: what is app object, and when does project layout matter in a production LLM system?

### Day 23 - Tue 20 Oct 2026 - Request & response models

**Theory (45 min)**

- [ ] Pydantic request bodies
- [ ] Response_model
- [ ] Status codes

**Practical (60 min)**

- [ ] Add POST /v1/documents with a validated request model and a typed response

**Recall (15 min)**

- [ ] Explain request & response models in your own words: what is pydantic request bodies, and when does status codes matter in a production LLM system?

### Day 24 - Wed 21 Oct 2026 - Dependency injection

**Theory (45 min)**

- [ ] Depends
- [ ] Shared resources
- [ ] Per-request deps
- [ ] Auth dependency

**Practical (60 min)**

- [ ] Add an api_key dependency that rejects requests with 401 + tests

**Recall (15 min)**

- [ ] Explain dependency injection in your own words: what is depends, and when does auth dependency matter in a production LLM system?

### Day 25 - Thu 22 Oct 2026 - Async endpoints

**Theory (45 min)**

- [ ] Async def routes
- [ ] Blocking pitfalls
- [ ] Background work

**Practical (60 min)**

- [ ] Add an endpoint that calls 3 external APIs concurrently and merges the result

**Recall (15 min)**

- [ ] Explain async endpoints in your own words: what is async def routes, and when does background work matter in a production LLM system?

### Day 26 - Fri 23 Oct 2026 - Exception handlers & middleware

**Theory (45 min)**

- [ ] Custom exception handlers
- [ ] Error envelopes
- [ ] Middleware
- [ ] CORS

**Practical (60 min)**

- [ ] Add a global handler mapping your custom exceptions to clean JSON errors

**Recall (15 min)**

- [ ] Explain exception handlers & middleware in your own words: what is custom exception handlers, and when does cors matter in a production LLM system?

### Day 27 - Sat 24 Oct 2026 - OpenAPI & docs

**Theory (45 min)**

- [ ] Auto docs
- [ ] Tags
- [ ] Examples
- [ ] Descriptions
- [ ] Schema customisation

**Practical (60 min)**

- [ ] Polish /docs: tags, summaries, request/response examples for every endpoint

**Recall (15 min)**

- [ ] Explain openapi & docs in your own words: what is auto docs, and when does schema customisation matter in a production LLM system?

### Day 28 - Sun 25 Oct 2026 - Testing endpoints

**Theory (45 min)**

- [ ] TestClient
- [ ] Fixtures
- [ ] Dependency overrides

**Practical (60 min)**

- [ ] Write 12 endpoint tests including auth failure and validation failure paths

**Recall (15 min)**

- [ ] Explain testing endpoints in your own words: what is testclient, and when does dependency overrides matter in a production LLM system?

## Week 5 - How LLMs Work
*Phase 3 - LLM Fundamentals | Roadmap 3.1-3.5*


### Day 29 - Mon 26 Oct 2026 - What is an LLM

**Theory (45 min)**

- [ ] Language modelling
- [ ] Pretraining
- [ ] Parameters
- [ ] Inference
- [ ] Limitations

**Practical (60 min)**

- [ ] Write a 1-page note in your own words: what an LLM can and cannot do

**Recall (15 min)**

- [ ] Explain what is an llm in your own words: what is language modelling, and when does limitations matter in a production LLM system?

### Day 30 - Tue 27 Oct 2026 - Tokens

**Theory (45 min)**

- [ ] Token definition
- [ ] Input vs output tokens
- [ ] Limits
- [ ] Cost drivers

**Practical (60 min)**

- [ ] Use tiktoken/anthropic tokenizer to count tokens of 10 prompts of varying size

**Recall (15 min)**

- [ ] Explain tokens in your own words: what is token definition, and when does cost drivers matter in a production LLM system?

### Day 31 - Wed 28 Oct 2026 - Tokenization

**Theory (45 min)**

- [ ] BPE/subword
- [ ] Why 1 word != 1 token
- [ ] Non-English cost

**Practical (60 min)**

- [ ] Tokenize English vs Hindi vs JSON vs code
- [ ] Tabulate tokens-per-character

**Recall (15 min)**

- [ ] Explain tokenization in your own words: what is bpe/subword, and when does non-english cost matter in a production LLM system?

### Day 32 - Thu 29 Oct 2026 - Context window

**Theory (45 min)**

- [ ] Input+output budget
- [ ] Overflow
- [ ] Long-context tradeoffs
- [ ] Context overflow behaviour and errors

**Practical (60 min)**

- [ ] Write a function that truncates/packs messages to fit a 100k token budget

**Recall (15 min)**

- [ ] Explain context window in your own words: what is input+output budget, and when does long-context tradeoffs matter in a production LLM system?

### Day 33 - Fri 30 Oct 2026 - Context management

**Theory (45 min)**

- [ ] Sliding window
- [ ] Summarisation
- [ ] Selective inclusion

**Practical (60 min)**

- [ ] Implement conversation trimming: keep system + last N turns + a running summary

**Recall (15 min)**

- [ ] Explain context management in your own words: what is sliding window, and when does selective inclusion matter in a production LLM system?

### Day 34 - Sat 31 Oct 2026 - Embeddings vs tokens

**Theory (45 min)**

- [ ] Token IDs vs embedding vectors
- [ ] Why embeddings enable retrieval

**Practical (60 min)**

- [ ] Print a token ID sequence and an embedding vector for the same sentence
- [ ] Compare

**Recall (15 min)**

- [ ] Explain embeddings vs tokens in your own words: what is token ids vs embedding vectors, and when does why embeddings enable retrieval matter in a production LLM system?

### Day 35 - Sun 01 Nov 2026 - Week 10 review

**Theory (45 min)**

- [ ] Consolidate tokens/context

**Practical (60 min)**

- [ ] Build a token+cost estimator CLI: text in -> tokens, est. cost for 3 models

**Recall (15 min)**

- [ ] Explain week 10 review in your own words: what is consolidate tokens/context, and when does week 10 review matter in a production LLM system?

## Week 6 - Transformers & Inference
*Phase 3 - LLM Fundamentals | Roadmap 3.6-3.9*


### Day 36 - Mon 02 Nov 2026 - Attention intuition

**Theory (45 min)**

- [ ] Query/key/value
- [ ] Why attention
- [ ] Context-dependent meaning

**Practical (60 min)**

- [ ] Hand-compute a tiny attention score matrix for a 4-token sentence in numpy

**Recall (15 min)**

- [ ] Explain attention intuition in your own words: what is query/key/value, and when does context-dependent meaning matter in a production LLM system?

### Day 37 - Tue 03 Nov 2026 - Self-attention & multi-head

**Theory (45 min)**

- [ ] Multiple heads
- [ ] Parallelism
- [ ] Long-range dependencies

**Practical (60 min)**

- [ ] Implement scaled dot-product attention in numpy for random Q/K/V

**Recall (15 min)**

- [ ] Explain self-attention & multi-head in your own words: what is multiple heads, and when does long-range dependencies matter in a production LLM system?

### Day 38 - Wed 04 Nov 2026 - Transformer architecture

**Theory (45 min)**

- [ ] Embeddings
- [ ] Positional info
- [ ] FFN
- [ ] Residuals
- [ ] Layer norm

**Practical (60 min)**

- [ ] Draw the full decoder block from memory
- [ ] Check it against the paper diagram

**Recall (15 min)**

- [ ] Explain transformer architecture in your own words: what is embeddings, and when does layer norm matter in a production LLM system?

### Day 39 - Thu 05 Nov 2026 - Encoder vs decoder

**Theory (45 min)**

- [ ] Encoder-only
- [ ] Decoder-only
- [ ] Encoder-decoder
- [ ] Why decoder-only dominates

**Practical (60 min)**

- [ ] Write comparison notes + pick correct architecture for 5 example tasks

**Recall (15 min)**

- [ ] Explain encoder vs decoder in your own words: what is encoder-only, and when does why decoder-only dominates matter in a production LLM system?

### Day 40 - Fri 06 Nov 2026 - Model inference

**Theory (45 min)**

- [ ] Prompt processing
- [ ] Autoregressive generation
- [ ] Stopping

**Practical (60 min)**

- [ ] Instrument an API call: measure time-to-first-token vs total time

**Recall (15 min)**

- [ ] Explain model inference in your own words: what is prompt processing, and when does stopping matter in a production LLM system?

### Day 41 - Sat 07 Nov 2026 - Sampling controls

**Theory (45 min)**

- [ ] Temperature
- [ ] Top-p
- [ ] Top-k
- [ ] Determinism vs creativity

**Practical (60 min)**

- [ ] Run the same prompt at temp 0/0.5/1.0 x3
- [ ] Tabulate variance in outputs

**Recall (15 min)**

- [ ] Explain sampling controls in your own words: what is temperature, and when does determinism vs creativity matter in a production LLM system?

### Day 42 - Sun 08 Nov 2026 - Parameters vs context

**Theory (45 min)**

- [ ] Weights = capacity
- [ ] Context = runtime info
- [ ] Why more context != retraining

**Practical (60 min)**

- [ ] Write the interview answer: 'Does adding context train the model?' in 6 lines

**Recall (15 min)**

- [ ] Explain parameters vs context in your own words: what is weights = capacity, and when does why more context != retraining matter in a production LLM system?

## Week 7 - Hallucination & Approach Choice
*Phase 3 - LLM Fundamentals | Roadmap 3.10-3.13*


### Day 43 - Mon 09 Nov 2026 - Why hallucinations happen

**Theory (45 min)**

- [ ] Knowledge gaps
- [ ] Ambiguity
- [ ] Retrieval failure
- [ ] Generation error

**Practical (60 min)**

- [ ] Deliberately induce 4 hallucination types
- [ ] Log prompt + wrong output for each

**Recall (15 min)**

- [ ] Explain why hallucinations happen in your own words: what is knowledge gaps, and when does generation error matter in a production LLM system?

### Day 44 - Tue 10 Nov 2026 - Reducing hallucination

**Theory (45 min)**

- [ ] Grounding
- [ ] Citations
- [ ] Abstention
- [ ] Verification
- [ ] Why RAG is not a cure

**Practical (60 min)**

- [ ] Add 'answer only from context, else say I don't know' and retest your 4 cases

**Recall (15 min)**

- [ ] Explain reducing hallucination in your own words: what is grounding, and when does why rag is not a cure matter in a production LLM system?

### Day 45 - Wed 11 Nov 2026 - Reasoning models

**Theory (45 min)**

- [ ] Reasoning budget
- [ ] Latency/cost tradeoffs
- [ ] When useful

**Practical (60 min)**

- [ ] Same hard task on a reasoning vs standard model
- [ ] Compare accuracy, latency, cost

**Recall (15 min)**

- [ ] Explain reasoning models in your own words: what is reasoning budget, and when does when useful matter in a production LLM system?

### Day 46 - Thu 12 Nov 2026 - Mixture-of-Experts

**Theory (45 min)**

- [ ] Expert routing
- [ ] Sparse activation
- [ ] Capacity vs compute

**Practical (60 min)**

- [ ] Write a short explainer note on MoE with a routing diagram

**Recall (15 min)**

- [ ] Explain mixture-of-experts in your own words: what is expert routing, and when does capacity vs compute matter in a production LLM system?

### Day 47 - Fri 13 Nov 2026 - Prompting vs RAG vs fine-tuning

**Theory (45 min)**

- [ ] What each changes
- [ ] Cost
- [ ] Maintenance
- [ ] When to use

**Practical (60 min)**

- [ ] Build a decision table for 8 real scenarios
- [ ] Justify each choice in one line

**Recall (15 min)**

- [ ] Explain prompting vs rag vs fine-tuning in your own words: what is what each changes, and when does when to use matter in a production LLM system?

### Day 48 - Sat 14 Nov 2026 - Cost & model selection basics

**Theory (45 min)**

- [ ] Price per 1M tokens
- [ ] Small vs large models
- [ ] Routing

**Practical (60 min)**

- [ ] Estimate monthly cost of a 10k-requests/day assistant for 3 model choices

**Recall (15 min)**

- [ ] Explain cost & model selection basics in your own words: what is price per 1m tokens, and when does routing matter in a production LLM system?

### Day 49 - Sun 15 Nov 2026 - Week 12 review

**Theory (45 min)**

- [ ] Consolidate all of Phase 3

**Practical (60 min)**

- [ ] Self-quiz: answer 20 LLM interview questions out loud, record weak areas

**Recall (15 min)**

- [ ] Explain week 12 review in your own words: what is consolidate all of phase 3, and when does week 12 review matter in a production LLM system?

## Week 8 - Anthropic API
*Phase 4 - LLM APIs & Prompting | Roadmap 4.1*


### Day 50 - Mon 16 Nov 2026 - Messages API

**Theory (45 min)**

- [ ] Endpoint shape
- [ ] Roles
- [ ] Content blocks
- [ ] Max_tokens
- [ ] Stop reasons

**Practical (60 min)**

- [ ] Make your first Claude call
- [ ] Print the full raw response object and study it

**Recall (15 min)**

- [ ] Explain messages api in your own words: what is endpoint shape, and when does stop reasons matter in a production LLM system?

### Day 51 - Tue 17 Nov 2026 - System instructions

**Theory (45 min)**

- [ ] System prompt role
- [ ] Instruction precedence
- [ ] Persona vs rules

**Practical (60 min)**

- [ ] Build a system prompt for a flight-ops assistant
- [ ] Test 5 tricky user inputs

**Recall (15 min)**

- [ ] Explain system instructions in your own words: what is system prompt role, and when does persona vs rules matter in a production LLM system?

### Day 52 - Wed 18 Nov 2026 - Multi-turn conversations

**Theory (45 min)**

- [ ] Message list construction
- [ ] Assistant prefill
- [ ] State on client

**Practical (60 min)**

- [ ] Build a CLI chat loop with history and token-budget trimming

**Recall (15 min)**

- [ ] Explain multi-turn conversations in your own words: what is message list construction, and when does state on client matter in a production LLM system?

### Day 53 - Thu 19 Nov 2026 - Tool use (first look)

**Theory (45 min)**

- [ ] Tool definitions
- [ ] Tool_use blocks
- [ ] Tool_result
- [ ] Loop mechanics

**Practical (60 min)**

- [ ] Give Claude a get_flight_status tool (fake data) and complete one full tool loop

**Recall (15 min)**

- [ ] Explain tool use (first look) in your own words: what is tool definitions, and when does loop mechanics matter in a production LLM system?

### Day 54 - Fri 20 Nov 2026 - Streaming

**Theory (45 min)**

- [ ] SSE events
- [ ] Deltas
- [ ] Partial output
- [ ] Error mid-stream

**Practical (60 min)**

- [ ] Stream a long answer to the terminal token-by-token with graceful error handling

**Recall (15 min)**

- [ ] Explain streaming in your own words: what is sse events, and when does error mid-stream matter in a production LLM system?

### Day 55 - Sat 21 Nov 2026 - Usage, errors, rate limits

**Theory (45 min)**

- [ ] Usage object
- [ ] 429/500 handling
- [ ] Backoff
- [ ] Idempotency

**Practical (60 min)**

- [ ] Wrap the client with retry + exponential backoff + usage logging per request

**Recall (15 min)**

- [ ] Explain usage, errors, rate limits in your own words: what is usage object, and when does idempotency matter in a production LLM system?

### Day 56 - Sun 22 Nov 2026 - Week 13 review

**Theory (45 min)**

- [ ] Consolidate Anthropic API

**Practical (60 min)**

- [ ] Refactor into an llm_client.py module with typed methods + tests (mocked)

**Recall (15 min)**

- [ ] Explain week 13 review in your own words: what is consolidate anthropic api, and when does week 13 review matter in a production LLM system?

## Week 9 - AWS Bedrock & Cost
*Phase 4 - LLM APIs & Prompting | Roadmap 4.2-4.6*


### Day 57 - Mon 23 Nov 2026 - Bedrock fundamentals

**Theory (45 min)**

- [ ] Architecture
- [ ] Model access
- [ ] Regions
- [ ] Runtime vs control plane

**Practical (60 min)**

- [ ] Enable model access in your AWS account
- [ ] List available foundation models via boto3

**Recall (15 min)**

- [ ] Explain bedrock fundamentals in your own words: what is architecture, and when does runtime vs control plane matter in a production LLM system?

### Day 58 - Tue 24 Nov 2026 - Model invocation & Converse API

**Theory (45 min)**

- [ ] InvokeModel vs Converse
- [ ] Request/response shape

**Practical (60 min)**

- [ ] Call Claude on Bedrock via Converse
- [ ] Compare payload to the Anthropic API

**Recall (15 min)**

- [ ] Explain model invocation & converse api in your own words: what is invokemodel vs converse, and when does request/response shape matter in a production LLM system?

### Day 59 - Wed 25 Nov 2026 - Bedrock streaming & IAM

**Theory (45 min)**

- [ ] ConverseStream
- [ ] IAM policies
- [ ] Least privilege
- [ ] Service roles

**Practical (60 min)**

- [ ] Write a minimal IAM policy for bedrock:InvokeModel and test it works

**Recall (15 min)**

- [ ] Explain bedrock streaming & iam in your own words: what is conversestream, and when does service roles matter in a production LLM system?

### Day 60 - Thu 26 Nov 2026 - Provider abstraction

**Theory (45 min)**

- [ ] Why multi-provider
- [ ] Routing
- [ ] Fallbacks
- [ ] Avoiding tight coupling

**Practical (60 min)**

- [ ] Refactor llm_client into an interface with Anthropic + Bedrock implementations

**Recall (15 min)**

- [ ] Explain provider abstraction in your own words: what is why multi-provider, and when does avoiding tight coupling matter in a production LLM system?

### Day 61 - Fri 27 Nov 2026 - Cost management

**Theory (45 min)**

- [ ] Input/output pricing
- [ ] Prompt size
- [ ] Caching
- [ ] Cost per successful task

**Practical (60 min)**

- [ ] Add per-call cost tracking to your client
- [ ] Produce a daily cost report

**Recall (15 min)**

- [ ] Explain cost management in your own words: what is input/output pricing, and when does cost per successful task matter in a production LLM system?

### Day 62 - Sat 28 Nov 2026 - Multimodal APIs

**Theory (45 min)**

- [ ] Images
- [ ] Documents
- [ ] Vision inputs
- [ ] Token accounting
- [ ] Audio input concepts and limits

**Practical (60 min)**

- [ ] Send a PDF page image and ask for structured extraction of its table

**Recall (15 min)**

- [ ] Explain multimodal apis in your own words: what is images, and when does token accounting matter in a production LLM system?

### Day 63 - Sun 29 Nov 2026 - Batch APIs

**Theory (45 min)**

- [ ] Offline workloads
- [ ] Async submission
- [ ] Cost/throughput tradeoffs

**Practical (60 min)**

- [ ] Submit 50 prompts as a batch job
- [ ] Compare cost/latency vs real-time calls

**Recall (15 min)**

- [ ] Explain batch apis in your own words: what is offline workloads, and when does cost/throughput tradeoffs matter in a production LLM system?

## Week 10 - Prompt Engineering Core
*Phase 4 - LLM APIs & Prompting | Roadmap 5.1-5.7*


### Day 64 - Mon 30 Nov 2026 - Prompt anatomy

**Theory (45 min)**

- [ ] Role
- [ ] Task
- [ ] Context
- [ ] Constraints
- [ ] Output format
- [ ] Examples

**Practical (60 min)**

- [ ] Take a bad prompt and rewrite it with all 6 components
- [ ] Compare outputs

**Recall (15 min)**

- [ ] Explain prompt anatomy in your own words: what is role, and when does examples matter in a production LLM system?

### Day 65 - Tue 01 Dec 2026 - System/user/assistant roles

**Theory (45 min)**

- [ ] Message ordering
- [ ] Precedence
- [ ] Trusted vs untrusted data

**Practical (60 min)**

- [ ] Build a prompt where user data is clearly fenced from instructions
- [ ] Try to break it

**Recall (15 min)**

- [ ] Explain system/user/assistant roles in your own words: what is message ordering, and when does trusted vs untrusted data matter in a production LLM system?

### Day 66 - Wed 02 Dec 2026 - Zero-shot prompting

**Theory (45 min)**

- [ ] Clear instructions
- [ ] Constraints
- [ ] Explicit output spec

**Practical (60 min)**

- [ ] Write 5 zero-shot prompts for classification tasks
- [ ] Measure accuracy on 20 samples

**Recall (15 min)**

- [ ] Explain zero-shot prompting in your own words: what is clear instructions, and when does explicit output spec matter in a production LLM system?

### Day 67 - Thu 03 Dec 2026 - Few-shot prompting

**Theory (45 min)**

- [ ] Example selection
- [ ] Diversity
- [ ] Format consistency
- [ ] When it helps

**Practical (60 min)**

- [ ] Add 4 examples to the same task
- [ ] Re-measure accuracy and record the delta

**Recall (15 min)**

- [ ] Explain few-shot prompting in your own words: what is example selection, and when does when it helps matter in a production LLM system?

### Day 68 - Fri 04 Dec 2026 - Delimiters & structure

**Theory (45 min)**

- [ ] XML tags
- [ ] Triple quotes
- [ ] Preventing instruction/data ambiguity

**Practical (60 min)**

- [ ] Convert your prompts to XML-tagged sections
- [ ] Retest robustness

**Recall (15 min)**

- [ ] Explain delimiters & structure in your own words: what is xml tags, and when does preventing instruction/data ambiguity matter in a production LLM system?

### Day 69 - Sat 05 Dec 2026 - Context engineering

**Theory (45 min)**

- [ ] Selecting
- [ ] Ordering
- [ ] Compressing context
- [ ] Context budgets

**Practical (60 min)**

- [ ] Build a context packer: rank snippets, fit to budget, drop irrelevant ones

**Recall (15 min)**

- [ ] Explain context engineering in your own words: what is selecting, and when does context budgets matter in a production LLM system?

### Day 70 - Sun 06 Dec 2026 - Prompt templates

**Theory (45 min)**

- [ ] Reusable templates
- [ ] Variables
- [ ] Testing
- [ ] Version fields

**Practical (60 min)**

- [ ] Create a prompts/ folder with versioned template files + a render() function

**Recall (15 min)**

- [ ] Explain prompt templates in your own words: what is reusable templates, and when does version fields matter in a production LLM system?

## Week 11 - Advanced Prompting
*Phase 4 - LLM APIs & Prompting | Roadmap 5.8-5.12*


### Day 71 - Mon 07 Dec 2026 - Prompt versioning

**Theory (45 min)**

- [ ] Version control
- [ ] Rollback
- [ ] Change management
- [ ] Experiments

**Practical (60 min)**

- [ ] Add v1/v2 of a prompt and an A/B runner scoring both on 20 cases

**Recall (15 min)**

- [ ] Explain prompt versioning in your own words: what is version control, and when does experiments matter in a production LLM system?

### Day 72 - Tue 08 Dec 2026 - Prompt caching

**Theory (45 min)**

- [ ] Cacheable prefixes
- [ ] TTL
- [ ] Cost/latency effects
- [ ] Ordering rules

**Practical (60 min)**

- [ ] Enable prompt caching on a long system prompt
- [ ] Measure cost + latency savings

**Recall (15 min)**

- [ ] Explain prompt caching in your own words: what is cacheable prefixes, and when does ordering rules matter in a production LLM system?

### Day 73 - Wed 09 Dec 2026 - XML prompting

**Theory (45 min)**

- [ ] Structured boundaries
- [ ] Nested sections
- [ ] When XML wins

**Practical (60 min)**

- [ ] Rebuild your most complex prompt fully in XML
- [ ] Document readability gains

**Recall (15 min)**

- [ ] Explain xml prompting in your own words: what is structured boundaries, and when does when xml wins matter in a production LLM system?

### Day 74 - Thu 10 Dec 2026 - Prompt chaining

**Theory (45 min)**

- [ ] Multi-step prompts
- [ ] Intermediate validation
- [ ] Error propagation

**Practical (60 min)**

- [ ] Build a 3-step chain: extract -> verify -> summarise, validating between steps

**Recall (15 min)**

- [ ] Explain prompt chaining in your own words: what is multi-step prompts, and when does error propagation matter in a production LLM system?

### Day 75 - Fri 11 Dec 2026 - Advanced reasoning patterns

**Theory (45 min)**

- [ ] Step-by-step
- [ ] Decomposition
- [ ] Self-consistency
- [ ] When NOT to use

**Practical (60 min)**

- [ ] Compare direct vs step-by-step prompting on 10 reasoning problems
- [ ] Tabulate

**Recall (15 min)**

- [ ] Explain advanced reasoning patterns in your own words: what is step-by-step, and when does when not to use matter in a production LLM system?

### Day 76 - Sat 12 Dec 2026 - Prompt failure analysis

**Theory (45 min)**

- [ ] Common failure modes
- [ ] Ambiguity
- [ ] Over-constraining

**Practical (60 min)**

- [ ] Collect 10 failures from the week and write a root-cause table with fixes

**Recall (15 min)**

- [ ] Explain prompt failure analysis in your own words: what is common failure modes, and when does over-constraining matter in a production LLM system?

### Day 77 - Sun 13 Dec 2026 - Week 16 review

**Theory (45 min)**

- [ ] Consolidate prompting

**Practical (60 min)**

- [ ] Write a PROMPTING.md playbook for your future projects

**Recall (15 min)**

- [ ] Explain week 16 review in your own words: what is consolidate prompting, and when does week 16 review matter in a production LLM system?

## Week 12 - Structured Output & Validation
*Phase 5 - Structured Output & Vectors | Roadmap 6*


### Day 78 - Mon 14 Dec 2026 - JSON output

**Theory (45 min)**

- [ ] Valid JSON
- [ ] Required vs optional fields
- [ ] Nested structures

**Practical (60 min)**

- [ ] Force JSON-only output for an extraction task
- [ ] Test 20 messy inputs

**Recall (15 min)**

- [ ] Explain json output in your own words: what is valid json, and when does nested structures matter in a production LLM system?

### Day 79 - Tue 15 Dec 2026 - JSON Schema

**Theory (45 min)**

- [ ] Types
- [ ] Required
- [ ] Enums
- [ ] Arrays
- [ ] Nested objects
- [ ] Constraints

**Practical (60 min)**

- [ ] Write a JSON Schema for a flight-disruption event
- [ ] Validate 10 payloads

**Recall (15 min)**

- [ ] Explain json schema in your own words: what is types, and when does constraints matter in a production LLM system?

### Day 80 - Wed 16 Dec 2026 - Pydantic structured output

**Theory (45 min)**

- [ ] Model definitions
- [ ] Parsing
- [ ] Serialization
- [ ] Schema generation

**Practical (60 min)**

- [ ] Generate the tool/schema from a Pydantic model and parse responses into it

**Recall (15 min)**

- [ ] Explain pydantic structured output in your own words: what is model definitions, and when does schema generation matter in a production LLM system?

### Day 81 - Thu 17 Dec 2026 - Validation failures

**Theory (45 min)**

- [ ] Detecting invalid output
- [ ] Partial output
- [ ] Type coercion risks

**Practical (60 min)**

- [ ] Log every validation failure with the raw model output for analysis

**Recall (15 min)**

- [ ] Explain validation failures in your own words: what is detecting invalid output, and when does type coercion risks matter in a production LLM system?

### Day 82 - Fri 18 Dec 2026 - Retry & repair

**Theory (45 min)**

- [ ] Re-ask with errors
- [ ] Repair prompts
- [ ] Max attempts
- [ ] Budget

**Practical (60 min)**

- [ ] Implement validate -> repair -> retry (max 2) and measure success-rate lift

**Recall (15 min)**

- [ ] Explain retry & repair in your own words: what is re-ask with errors, and when does budget matter in a production LLM system?

### Day 83 - Sat 19 Dec 2026 - Fallback behaviour

**Theory (45 min)**

- [ ] Degraded responses
- [ ] Human escalation
- [ ] Never trusting output

**Practical (60 min)**

- [ ] Add a safe fallback path + alerting when all repair attempts fail

**Recall (15 min)**

- [ ] Explain fallback behaviour in your own words: what is degraded responses, and when does never trusting output matter in a production LLM system?

### Day 84 - Sun 20 Dec 2026 - Week 17 review

**Theory (45 min)**

- [ ] Consolidate structured output

**Practical (60 min)**

- [ ] Ship an /v1/extract FastAPI endpoint with guaranteed schema-valid responses

**Recall (15 min)**

- [ ] Explain week 17 review in your own words: what is consolidate structured output, and when does week 17 review matter in a production LLM system?

## Week 13 - Embeddings & Vector Search
*Phase 5 - Structured Output & Vectors | Roadmap 7.1-7.4*


### Day 85 - Mon 21 Dec 2026 - Embeddings

**Theory (45 min)**

- [ ] What they represent
- [ ] Embedding models
- [ ] Dimensions
- [ ] Vector space

**Practical (60 min)**

- [ ] Embed 50 sentences
- [ ] Find nearest neighbours for 5 queries manually

**Recall (15 min)**

- [ ] Explain embeddings in your own words: what is what they represent, and when does vector space matter in a production LLM system?

### Day 86 - Tue 22 Dec 2026 - Similarity metrics

**Theory (45 min)**

- [ ] Cosine
- [ ] Dot product
- [ ] Euclidean
- [ ] Normalisation
- [ ] Similarity vs distance

**Practical (60 min)**

- [ ] Implement all 3 metrics in numpy
- [ ] Compare rankings on the same dataset

**Recall (15 min)**

- [ ] Explain similarity metrics in your own words: what is cosine, and when does similarity vs distance matter in a production LLM system?

### Day 87 - Wed 23 Dec 2026 - Embedding model choice

**Theory (45 min)**

- [ ] Size
- [ ] Dimension
- [ ] Domain fit
- [ ] Cost
- [ ] Multilingual

**Practical (60 min)**

- [ ] Benchmark 2 embedding models on 20 query/doc pairs
- [ ] Record recall@3

**Recall (15 min)**

- [ ] Explain embedding model choice in your own words: what is size, and when does multilingual matter in a production LLM system?

### Day 88 - Thu 24 Dec 2026 - Exact vs approximate search

**Theory (45 min)**

- [ ] Brute force
- [ ] ANN
- [ ] Recall vs speed tradeoff

**Practical (60 min)**

- [ ] Brute-force search 50k vectors
- [ ] Measure latency,
- [ ] Compare with an ANN index

**Recall (15 min)**

- [ ] Explain exact vs approximate search in your own words: what is brute force, and when does recall vs speed tradeoff matter in a production LLM system?

### Day 89 - Fri 25 Dec 2026 - HNSW & index params

**Theory (45 min)**

- [ ] Graph structure
- [ ] M
- [ ] Ef_construction
- [ ] Ef_search tuning

**Practical (60 min)**

- [ ] Tune ef_search across 5 values
- [ ] Plot recall vs latency

**Recall (15 min)**

- [ ] Explain hnsw & index params in your own words: what is graph structure, and when does ef_search tuning matter in a production LLM system?

### Day 90 - Sat 26 Dec 2026 - Sparse vs dense retrieval

**Theory (45 min)**

- [ ] BM25/keyword vs semantic
- [ ] Strengths
- [ ] Failure cases

**Practical (60 min)**

- [ ] Run BM25 and dense search on the same 20 queries
- [ ] Find where each fails

**Recall (15 min)**

- [ ] Explain sparse vs dense retrieval in your own words: what is bm25/keyword vs semantic, and when does failure cases matter in a production LLM system?

### Day 91 - Sun 27 Dec 2026 - Hybrid retrieval intro

**Theory (45 min)**

- [ ] Score fusion
- [ ] Reciprocal rank fusion
- [ ] Weighting

**Practical (60 min)**

- [ ] Implement RRF combining BM25 + dense
- [ ] Measure improvement

**Recall (15 min)**

- [ ] Explain hybrid retrieval intro in your own words: what is score fusion, and when does weighting matter in a production LLM system?

## Week 14 - Vector Databases
*Phase 5 - Structured Output & Vectors | Roadmap 7.5-7.8*


### Day 92 - Mon 28 Dec 2026 - Vector DB concepts

**Theory (45 min)**

- [ ] Collections
- [ ] Vectors
- [ ] Metadata
- [ ] Top-K
- [ ] Upsert
- [ ] Delete

**Practical (60 min)**

- [ ] Diagram the data model you will use for a document assistant

**Recall (15 min)**

- [ ] Explain vector db concepts in your own words: what is collections, and when does delete matter in a production LLM system?

### Day 93 - Tue 29 Dec 2026 - pgvector setup

**Theory (45 min)**

- [ ] Extension
- [ ] Vector column
- [ ] Dimensions
- [ ] Insert

**Practical (60 min)**

- [ ] Add pgvector to your Postgres
- [ ] Store 1k chunk embeddings

**Recall (15 min)**

- [ ] Explain pgvector setup in your own words: what is extension, and when does insert matter in a production LLM system?

### Day 94 - Wed 30 Dec 2026 - pgvector search & indexes

**Theory (45 min)**

- [ ] <-> operators
- [ ] Ivfflat vs hnsw
- [ ] Tuning

**Practical (60 min)**

- [ ] Create an HNSW index
- [ ] Compare query latency before/after

**Recall (15 min)**

- [ ] Explain pgvector search & indexes in your own words: what is <-> operators, and when does tuning matter in a production LLM system?

### Day 95 - Thu 31 Dec 2026 - Metadata filtering

**Theory (45 min)**

- [ ] Filter + vector search
- [ ] Pre vs post filtering
- [ ] Selectivity

**Practical (60 min)**

- [ ] Search with filters: source, department, date range
- [ ] Verify correctness

**Recall (15 min)**

- [ ] Explain metadata filtering in your own words: what is filter + vector search, and when does selectivity matter in a production LLM system?

### Day 96 - Fri 01 Jan 2027 - Managed vector DB

**Theory (45 min)**

- [ ] Pinecone/Qdrant concepts
- [ ] Namespaces
- [ ] Pods/serverless
- [ ] Upsert API

**Practical (60 min)**

- [ ] Load the same 1k chunks into a managed vector DB and query it

**Recall (15 min)**

- [ ] Explain managed vector db in your own words: what is pinecone/qdrant concepts, and when does upsert api matter in a production LLM system?

### Day 97 - Sat 02 Jan 2027 - Comparing vector stores

**Theory (45 min)**

- [ ] Tradeoffs: ops
- [ ] Cost
- [ ] Filtering
- [ ] Scale
- [ ] Hybrid support

**Practical (60 min)**

- [ ] Write a comparison table: pgvector vs managed
- [ ] Pick one and justify

**Recall (15 min)**

- [ ] Explain comparing vector stores in your own words: what is tradeoffs: ops, and when does hybrid support matter in a production LLM system?

### Day 98 - Sun 03 Jan 2027 - Week 19 review

**Theory (45 min)**

- [ ] Consolidate vectors

**Practical (60 min)**

- [ ] Build a reusable VectorStore interface with pgvector + managed implementations

**Recall (15 min)**

- [ ] Explain week 19 review in your own words: what is consolidate vectors, and when does week 19 review matter in a production LLM system?

## Week 15 - RAG Fundamentals
*Phase 6 - RAG | Roadmap 8*


### Day 99 - Mon 04 Jan 2027 - Why RAG exists

**Theory (45 min)**

- [ ] Knowledge limits
- [ ] Private data
- [ ] Freshness
- [ ] Grounding
- [ ] Citations

**Practical (60 min)**

- [ ] Write the 'why RAG' interview answer and 3 cases where RAG is the wrong tool

**Recall (15 min)**

- [ ] Explain why rag exists in your own words: what is knowledge limits, and when does citations matter in a production LLM system?

### Day 100 - Tue 05 Jan 2027 - RAG architecture

**Theory (45 min)**

- [ ] Ingest -> chunk -> embed -> store -> retrieve -> generate

**Practical (60 min)**

- [ ] Draw the full pipeline diagram
- [ ] Label where each failure mode occurs

**Recall (15 min)**

- [ ] Explain rag architecture in your own words: what is ingest -> chunk -> embed -> store -> retrieve -> generate, and when does rag architecture matter in a production LLM system?

### Day 101 - Wed 06 Jan 2027 - Naive RAG build

**Theory (45 min)**

- [ ] Top-K retrieval
- [ ] Prompt construction
- [ ] Answer generation

**Practical (60 min)**

- [ ] Build end-to-end naive RAG over 20 PDFs in one script

**Recall (15 min)**

- [ ] Explain naive rag build in your own words: what is top-k retrieval, and when does answer generation matter in a production LLM system?

### Day 102 - Thu 07 Jan 2027 - Prompt construction for RAG

**Theory (45 min)**

- [ ] Context formatting
- [ ] Citation instructions
- [ ] Abstention

**Practical (60 min)**

- [ ] Add numbered sources + require inline citations
- [ ] Test 10 questions

**Recall (15 min)**

- [ ] Explain prompt construction for rag in your own words: what is context formatting, and when does abstention matter in a production LLM system?

### Day 103 - Fri 08 Jan 2027 - Answer grounding

**Theory (45 min)**

- [ ] Faithfulness
- [ ] Refusing when context is weak
- [ ] Thresholds

**Practical (60 min)**

- [ ] Add a similarity threshold
- [ ] Return 'not found' below it and measure

**Recall (15 min)**

- [ ] Explain answer grounding in your own words: what is faithfulness, and when does thresholds matter in a production LLM system?

### Day 104 - Sat 09 Jan 2027 - RAG vs fine-tuning

**Theory (45 min)**

- [ ] Knowledge updates
- [ ] Behaviour change
- [ ] Cost
- [ ] Maintenance
- [ ] Security

**Practical (60 min)**

- [ ] Write a 1-page decision doc for your own enterprise use case

**Recall (15 min)**

- [ ] Explain rag vs fine-tuning in your own words: what is knowledge updates, and when does security matter in a production LLM system?

### Day 105 - Sun 10 Jan 2027 - Week 20 review

**Theory (45 min)**

- [ ] Consolidate naive RAG

**Practical (60 min)**

- [ ] Refactor the script into modules: ingest.py, retrieve.py, generate.py + tests

**Recall (15 min)**

- [ ] Explain week 20 review in your own words: what is consolidate naive rag, and when does week 20 review matter in a production LLM system?

## Week 16 - Document Ingestion
*Phase 6 - RAG | Roadmap 9*


### Day 106 - Mon 11 Jan 2027 - Document loading

**Theory (45 min)**

- [ ] PDF
- [ ] DOCX
- [ ] HTML
- [ ] Markdown
- [ ] Text
- [ ] Loader libraries

**Practical (60 min)**

- [ ] Write loaders for 5 file types returning a common Document dataclass

**Recall (15 min)**

- [ ] Explain document loading in your own words: what is pdf, and when does loader libraries matter in a production LLM system?

### Day 107 - Tue 12 Jan 2027 - Text extraction quality

**Theory (45 min)**

- [ ] Encoding
- [ ] Layout
- [ ] Columns
- [ ] Headers/footers
- [ ] Tables

**Practical (60 min)**

- [ ] Extract from a messy PDF
- [ ] List 6 extraction defects you observe

**Recall (15 min)**

- [ ] Explain text extraction quality in your own words: what is encoding, and when does tables matter in a production LLM system?

### Day 108 - Wed 13 Jan 2027 - OCR

**Theory (45 min)**

- [ ] Scanned PDFs
- [ ] Image text
- [ ] OCR limitations and error patterns

**Practical (60 min)**

- [ ] Run OCR on a scanned page
- [ ] Measure error rate vs the true text

**Recall (15 min)**

- [ ] Explain ocr in your own words: what is scanned pdfs, and when does ocr limitations and error patterns matter in a production LLM system?

### Day 109 - Thu 14 Jan 2027 - Chunking strategies

**Theory (45 min)**

- [ ] Fixed
- [ ] Recursive
- [ ] Semantic
- [ ] Size and overlap

**Practical (60 min)**

- [ ] Implement all 3 chunkers
- [ ] Chunk the same doc and eyeball boundary quality

**Recall (15 min)**

- [ ] Explain chunking strategies in your own words: what is fixed, and when does size and overlap matter in a production LLM system?

### Day 110 - Fri 15 Jan 2027 - Chunk tuning

**Theory (45 min)**

- [ ] Size vs recall
- [ ] Overlap cost
- [ ] Boundary preservation

**Practical (60 min)**

- [ ] Evaluate 3 chunk sizes on 20 questions
- [ ] Pick a winner with data

**Recall (15 min)**

- [ ] Explain chunk tuning in your own words: what is size vs recall, and when does boundary preservation matter in a production LLM system?

### Day 111 - Sat 16 Jan 2027 - Metadata design

**Theory (45 min)**

- [ ] Doc_id
- [ ] Source
- [ ] Page
- [ ] Department
- [ ] Tenant
- [ ] ACL
- [ ] Timestamp
- [ ] Version

**Practical (60 min)**

- [ ] Attach full metadata to every chunk and store it in the vector DB

**Recall (15 min)**

- [ ] Explain metadata design in your own words: what is doc_id, and when does version matter in a production LLM system?

### Day 112 - Sun 17 Jan 2027 - Incremental indexing

**Theory (45 min)**

- [ ] New/updated/deleted docs
- [ ] Dedupe
- [ ] Re-index
- [ ] Versioning

**Practical (60 min)**

- [ ] Implement upsert-by-hash + delete-on-removal
- [ ] Prove idempotency by re-running

**Recall (15 min)**

- [ ] Explain incremental indexing in your own words: what is new/updated/deleted docs, and when does versioning matter in a production LLM system?

## Week 17 - Retrieval Engineering
*Phase 6 - RAG | Roadmap 10*


### Day 113 - Mon 18 Jan 2027 - Similarity retrieval tuning

**Theory (45 min)**

- [ ] Query embedding
- [ ] Top-K choice
- [ ] Thresholds

**Practical (60 min)**

- [ ] Sweep K = 3/5/10/20 on your eval questions
- [ ] Plot quality vs context cost

**Recall (15 min)**

- [ ] Explain similarity retrieval tuning in your own words: what is query embedding, and when does thresholds matter in a production LLM system?

### Day 114 - Tue 19 Jan 2027 - Metadata filtering in practice

**Theory (45 min)**

- [ ] Permissions
- [ ] Tenant
- [ ] Doc type
- [ ] Date filters

**Practical (60 min)**

- [ ] Add user-scoped filters and prove a user cannot retrieve other departments' docs

**Recall (15 min)**

- [ ] Explain metadata filtering in practice in your own words: what is permissions, and when does date filters matter in a production LLM system?

### Day 115 - Wed 20 Jan 2027 - Hybrid retrieval

**Theory (45 min)**

- [ ] Dense + sparse
- [ ] Fusion
- [ ] Weight tuning

**Practical (60 min)**

- [ ] Ship hybrid retrieval in your pipeline
- [ ] Measure recall improvement

**Recall (15 min)**

- [ ] Explain hybrid retrieval in your own words: what is dense + sparse, and when does weight tuning matter in a production LLM system?

### Day 116 - Thu 21 Jan 2027 - Reranking

**Theory (45 min)**

- [ ] Why stage-1 is imperfect
- [ ] Cross-encoders
- [ ] Candidate sets

**Practical (60 min)**

- [ ] Add a reranker over top-50 -> top-5
- [ ] Measure precision gain and latency cost

**Recall (15 min)**

- [ ] Explain reranking in your own words: what is why stage-1 is imperfect, and when does candidate sets matter in a production LLM system?

### Day 117 - Fri 22 Jan 2027 - Parent-child retrieval

**Theory (45 min)**

- [ ] Small retrieval units
- [ ] Larger generation context

**Practical (60 min)**

- [ ] Implement child-chunk retrieval that returns parent sections to the LLM

**Recall (15 min)**

- [ ] Explain parent-child retrieval in your own words: what is small retrieval units, and when does larger generation context matter in a production LLM system?

### Day 118 - Sat 23 Jan 2027 - Context expansion

**Theory (45 min)**

- [ ] Neighbouring chunks
- [ ] Section expansion
- [ ] Doc-level context

**Practical (60 min)**

- [ ] Add +/-1 neighbour chunk expansion
- [ ] Compare answer completeness

**Recall (15 min)**

- [ ] Explain context expansion in your own words: what is neighbouring chunks, and when does doc-level context matter in a production LLM system?

### Day 119 - Sun 24 Jan 2027 - Query transformation

**Theory (45 min)**

- [ ] Rewriting
- [ ] Decomposition
- [ ] Multi-query
- [ ] HyDE idea

**Practical (60 min)**

- [ ] Implement multi-query rewriting and fuse results
- [ ] Measure on hard questions

**Recall (15 min)**

- [ ] Explain query transformation in your own words: what is rewriting, and when does hyde idea matter in a production LLM system?

## Week 18 - Advanced RAG
*Phase 6 - RAG | Roadmap 11*


### Day 120 - Mon 25 Jan 2027 - Corrective RAG

**Theory (45 min)**

- [ ] Grading retrieved docs
- [ ] Re-retrieval
- [ ] Web fallback

**Practical (60 min)**

- [ ] Add a relevance grader that triggers re-retrieval when docs score low

**Recall (15 min)**

- [ ] Explain corrective rag in your own words: what is grading retrieved docs, and when does web fallback matter in a production LLM system?

### Day 121 - Tue 26 Jan 2027 - Adaptive RAG

**Theory (45 min)**

- [ ] Routing by query type: no-retrieval / single / multi-hop

**Practical (60 min)**

- [ ] Build a query router with 3 paths and test on mixed queries

**Recall (15 min)**

- [ ] Explain adaptive rag in your own words: what is routing by query type: no-retrieval / single / multi-hop, and when does adaptive rag matter in a production LLM system?

### Day 122 - Wed 27 Jan 2027 - Agentic RAG

**Theory (45 min)**

- [ ] Retrieval as a tool
- [ ] Iterative search
- [ ] Stopping criteria

**Practical (60 min)**

- [ ] Turn retrieval into a tool the model calls iteratively with a step cap

**Recall (15 min)**

- [ ] Explain agentic rag in your own words: what is retrieval as a tool, and when does stopping criteria matter in a production LLM system?

### Day 123 - Thu 28 Jan 2027 - Multi-hop retrieval

**Theory (45 min)**

- [ ] Chained questions
- [ ] Intermediate answers
- [ ] Evidence chains

**Practical (60 min)**

- [ ] Answer 5 multi-hop questions requiring 2+ retrievals
- [ ] Log the evidence chain

**Recall (15 min)**

- [ ] Explain multi-hop retrieval in your own words: what is chained questions, and when does evidence chains matter in a production LLM system?

### Day 124 - Fri 29 Jan 2027 - Query decomposition

**Theory (45 min)**

- [ ] Splitting compound questions
- [ ] Sub-answer merging

**Practical (60 min)**

- [ ] Decompose compound questions into sub-queries and merge answers

**Recall (15 min)**

- [ ] Explain query decomposition in your own words: what is splitting compound questions, and when does sub-answer merging matter in a production LLM system?

### Day 125 - Sat 30 Jan 2027 - Context compression

**Theory (45 min)**

- [ ] Extractive filtering
- [ ] Summarisation
- [ ] Redundancy removal

**Practical (60 min)**

- [ ] Compress retrieved context by 50%
- [ ] Check answer quality is preserved

**Recall (15 min)**

- [ ] Explain context compression in your own words: what is extractive filtering, and when does redundancy removal matter in a production LLM system?

### Day 126 - Sun 31 Jan 2027 - Graph RAG (awareness)

**Theory (45 min)**

- [ ] Entity/relationship graphs
- [ ] When graph RAG is worth it

**Practical (60 min)**

- [ ] Write notes + one small entity-graph example
- [ ] Decide if you need it

**Recall (15 min)**

- [ ] Explain graph rag (awareness) in your own words: what is entity/relationship graphs, and when does when graph rag is worth it matter in a production LLM system?

## Week 19 - RAG Evaluation
*Phase 6 - RAG | Roadmap 12*


### Day 127 - Mon 01 Feb 2027 - Evaluation fundamentals

**Theory (45 min)**

- [ ] What to measure
- [ ] Offline vs online
- [ ] Human vs automated

**Practical (60 min)**

- [ ] Define 6 metrics you will track for your RAG system and how each is computed

**Recall (15 min)**

- [ ] Explain evaluation fundamentals in your own words: what is what to measure, and when does human vs automated matter in a production LLM system?

### Day 128 - Tue 02 Feb 2027 - Golden dataset

**Theory (45 min)**

- [ ] Questions
- [ ] Expected answers
- [ ] Relevant docs
- [ ] Citations
- [ ] Edge cases

**Practical (60 min)**

- [ ] Build a 50-question golden set from your corpus with expected sources

**Recall (15 min)**

- [ ] Explain golden dataset in your own words: what is questions, and when does edge cases matter in a production LLM system?

### Day 129 - Wed 03 Feb 2027 - Retrieval metrics

**Theory (45 min)**

- [ ] Precision
- [ ] Recall
- [ ] Recall@K
- [ ] MRR
- [ ] NDCG intuition

**Practical (60 min)**

- [ ] Compute recall@5 and MRR for your retriever on the golden set

**Recall (15 min)**

- [ ] Explain retrieval metrics in your own words: what is precision, and when does ndcg intuition matter in a production LLM system?

### Day 130 - Thu 04 Feb 2027 - Generation metrics

**Theory (45 min)**

- [ ] Correctness
- [ ] Relevance
- [ ] Faithfulness
- [ ] Groundedness
- [ ] Citation accuracy

**Practical (60 min)**

- [ ] Score 50 answers for faithfulness + citation correctness manually

**Recall (15 min)**

- [ ] Explain generation metrics in your own words: what is correctness, and when does citation accuracy matter in a production LLM system?

### Day 131 - Fri 05 Feb 2027 - LLM-as-a-judge

**Theory (45 min)**

- [ ] Judge prompts
- [ ] Rubrics
- [ ] Bias
- [ ] Calibration against humans

**Practical (60 min)**

- [ ] Write a judge prompt
- [ ] Compare its scores to your manual scores
- [ ] Measure agreement

**Recall (15 min)**

- [ ] Explain llm-as-a-judge in your own words: what is judge prompts, and when does calibration against humans matter in a production LLM system?

### Day 132 - Sat 06 Feb 2027 - Ragas

**Theory (45 min)**

- [ ] RAG metrics library
- [ ] Dataset format
- [ ] Experiment comparison

**Practical (60 min)**

- [ ] Run Ragas on your golden set and reconcile with your own metrics

**Recall (15 min)**

- [ ] Explain ragas in your own words: what is rag metrics library, and when does experiment comparison matter in a production LLM system?

### Day 133 - Sun 07 Feb 2027 - Regression testing

**Theory (45 min)**

- [ ] Baselines
- [ ] Thresholds
- [ ] CI gates
- [ ] Comparing versions

**Practical (60 min)**

- [ ] Add an eval script to CI that fails the build if faithfulness drops >5%

**Recall (15 min)**

- [ ] Explain regression testing in your own words: what is baselines, and when does comparing versions matter in a production LLM system?

## Week 20 - Enterprise RAG
*Phase 7 - Enterprise RAG | Roadmap 13*


### Day 134 - Mon 08 Feb 2027 - Enterprise architecture

**Theory (45 min)**

- [ ] Ingestion
- [ ] Retrieval
- [ ] Model
- [ ] API
- [ ] Auth
- [ ] Observability services

**Practical (60 min)**

- [ ] Draw the full service architecture for an enterprise assistant

**Recall (15 min)**

- [ ] Explain enterprise architecture in your own words: what is ingestion, and when does observability services matter in a production LLM system?

### Day 135 - Tue 09 Feb 2027 - Permission-aware retrieval

**Theory (45 min)**

- [ ] Identity
- [ ] ACL metadata
- [ ] Filtering before generation

**Practical (60 min)**

- [ ] Implement ACL filters at query time
- [ ] Write tests proving no leakage

**Recall (15 min)**

- [ ] Explain permission-aware retrieval in your own words: what is identity, and when does filtering before generation matter in a production LLM system?

### Day 136 - Wed 10 Feb 2027 - Multi-tenant RAG

**Theory (45 min)**

- [ ] Tenant isolation
- [ ] Per-tenant indexes vs metadata isolation

**Practical (60 min)**

- [ ] Add tenant_id isolation
- [ ] Write a test attempting cross-tenant access

**Recall (15 min)**

- [ ] Explain multi-tenant rag in your own words: what is tenant isolation, and when does per-tenant indexes vs metadata isolation matter in a production LLM system?

### Day 137 - Thu 11 Feb 2027 - RAG at scale

**Theory (45 min)**

- [ ] Large corpora
- [ ] Indexing throughput
- [ ] Query throughput
- [ ] Sharding

**Practical (60 min)**

- [ ] Load-test retrieval with 100k chunks
- [ ] Record p50/p95 latency

**Recall (15 min)**

- [ ] Explain rag at scale in your own words: what is large corpora, and when does sharding matter in a production LLM system?

### Day 138 - Fri 12 Feb 2027 - Caching & semantic caching

**Theory (45 min)**

- [ ] Response cache
- [ ] Embedding cache
- [ ] Similar-query cache
- [ ] Freshness risk

**Practical (60 min)**

- [ ] Add a semantic cache with a similarity threshold
- [ ] Measure hit rate and risk

**Recall (15 min)**

- [ ] Explain caching & semantic caching in your own words: what is response cache, and when does freshness risk matter in a production LLM system?

### Day 139 - Sat 13 Feb 2027 - Document intelligence

**Theory (45 min)**

- [ ] Tables
- [ ] Charts
- [ ] Images
- [ ] Layout
- [ ] Multimodal extraction

**Practical (60 min)**

- [ ] Extract a complex table from a PDF into structured JSON and validate it

**Recall (15 min)**

- [ ] Explain document intelligence in your own words: what is tables, and when does multimodal extraction matter in a production LLM system?

### Day 140 - Sun 14 Feb 2027 - Production failure modes

**Theory (45 min)**

- [ ] Bad chunks
- [ ] Missing docs
- [ ] Wrong retrieval
- [ ] Permission leaks
- [ ] Stale data

**Practical (60 min)**

- [ ] Write a RAG runbook: 8 failure modes, detection signal, and fix for each

**Recall (15 min)**

- [ ] Explain production failure modes in your own words: what is bad chunks, and when does stale data matter in a production LLM system?

## Week 21 - Tool Calling
*Phase 8 - Agents | Roadmap 14*


### Day 141 - Mon 15 Feb 2027 - Why tools

**Theory (45 min)**

- [ ] Fresh data
- [ ] Actions
- [ ] Deterministic compute
- [ ] DB/API access

**Practical (60 min)**

- [ ] List 8 tools your enterprise assistant would need and why

**Recall (15 min)**

- [ ] Explain why tools in your own words: what is fresh data, and when does db/api access matter in a production LLM system?

### Day 142 - Tue 16 Feb 2027 - Tool anatomy

**Theory (45 min)**

- [ ] Name
- [ ] Description
- [ ] Input schema
- [ ] Execution
- [ ] Output
- [ ] Errors

**Practical (60 min)**

- [ ] Define 3 tools with Pydantic schemas + clean descriptions

**Recall (15 min)**

- [ ] Explain tool anatomy in your own words: what is name, and when does errors matter in a production LLM system?

### Day 143 - Wed 17 Feb 2027 - Tool schemas

**Theory (45 min)**

- [ ] JSON Schema
- [ ] Required/optional
- [ ] Enums
- [ ] Validation

**Practical (60 min)**

- [ ] Generate JSON Schema from Pydantic
- [ ] Validate LLM-provided args before execution

**Recall (15 min)**

- [ ] Explain tool schemas in your own words: what is json schema, and when does validation matter in a production LLM system?

### Day 144 - Thu 18 Feb 2027 - Tool selection

**Theory (45 min)**

- [ ] How models choose
- [ ] Description quality
- [ ] Ambiguity
- [ ] Routing
- [ ] Dynamic tool selection for large toolsets (Roadmap 14.10)
- [ ] Tool discovery and reducing tool-selection errors

**Practical (60 min)**

- [ ] Create 2 deliberately ambiguous tools
- [ ] Fix descriptions until selection is reliable
- [ ] Register 20 tools and measure selection accuracy before/after adding a routing layer

**Recall (15 min)**

- [ ] Explain tool selection in your own words: what is how models choose, and when does routing matter in a production LLM system?

### Day 145 - Fri 19 Feb 2027 - Sequential tool calling

**Theory (45 min)**

- [ ] Multi-step loops
- [ ] Passing results back
- [ ] Step limits

**Practical (60 min)**

- [ ] Implement a full tool loop: model -> tool -> model -> final answer, capped at 6 steps

**Recall (15 min)**

- [ ] Explain sequential tool calling in your own words: what is multi-step loops, and when does step limits matter in a production LLM system?

### Day 146 - Sat 20 Feb 2027 - Parallel tool calling

**Theory (45 min)**

- [ ] Independent calls
- [ ] Concurrency
- [ ] Aggregation

**Practical (60 min)**

- [ ] Execute independent tool calls concurrently with asyncio.gather

**Recall (15 min)**

- [ ] Explain parallel tool calling in your own words: what is independent calls, and when does aggregation matter in a production LLM system?

### Day 147 - Sun 21 Feb 2027 - Tool errors & security

**Theory (45 min)**

- [ ] Retryable vs not
- [ ] Timeouts
- [ ] Authz
- [ ] Input/output validation
- [ ] Least privilege

**Practical (60 min)**

- [ ] Add per-tool timeouts, error envelopes, and an approval gate for write actions

**Recall (15 min)**

- [ ] Explain tool errors & security in your own words: what is retryable vs not, and when does least privilege matter in a production LLM system?

## Week 22 - AI Agents
*Phase 8 - Agents | Roadmap 15*


### Day 148 - Mon 22 Feb 2027 - What is an agent

**Theory (45 min)**

- [ ] Agent vs LLM call vs workflow
- [ ] Autonomy spectrum

**Practical (60 min)**

- [ ] Classify 8 systems as workflow vs agent
- [ ] Justify each

**Recall (15 min)**

- [ ] Explain what is an agent in your own words: what is agent vs llm call vs workflow, and when does autonomy spectrum matter in a production LLM system?

### Day 149 - Tue 23 Feb 2027 - The agent loop

**Theory (45 min)**

- [ ] Query -> decide -> act -> observe -> repeat -> answer

**Practical (60 min)**

- [ ] Hand-build an agent loop in plain Python (no framework) with 3 tools

**Recall (15 min)**

- [ ] Explain the agent loop in your own words: what is query -> decide -> act -> observe -> repeat -> answer, and when does the agent loop matter in a production LLM system?

### Day 150 - Wed 24 Feb 2027 - Agent state

**Theory (45 min)**

- [ ] Conversation
- [ ] Tool results
- [ ] Scratchpad
- [ ] Persistent state

**Practical (60 min)**

- [ ] Add a typed AgentState object and log every state transition

**Recall (15 min)**

- [ ] Explain agent state in your own words: what is conversation, and when does persistent state matter in a production LLM system?

### Day 151 - Thu 25 Feb 2027 - Termination

**Theory (45 min)**

- [ ] Final answer
- [ ] Success/failure
- [ ] Max steps
- [ ] Timeout
- [ ] Escalation

**Practical (60 min)**

- [ ] Add 4 termination conditions and test each one fires correctly

**Recall (15 min)**

- [ ] Explain termination in your own words: what is final answer, and when does escalation matter in a production LLM system?

### Day 152 - Fri 26 Feb 2027 - ReAct

**Theory (45 min)**

- [ ] Reason-act-observe pattern
- [ ] Traces
- [ ] Iteration

**Practical (60 min)**

- [ ] Implement ReAct-style prompting and print readable reasoning/action traces

**Recall (15 min)**

- [ ] Explain react in your own words: what is reason-act-observe pattern, and when does iteration matter in a production LLM system?

### Day 153 - Sat 27 Feb 2027 - Router agents

**Theory (45 min)**

- [ ] Classification
- [ ] Specialist selection
- [ ] Route execution

**Practical (60 min)**

- [ ] Build a router that sends queries to RAG / calculator / API specialist paths

**Recall (15 min)**

- [ ] Explain router agents in your own words: what is classification, and when does route execution matter in a production LLM system?

### Day 154 - Sun 28 Feb 2027 - Human-in-the-loop & interrupts

**Theory (45 min)**

- [ ] Approval
- [ ] Review
- [ ] Escalation
- [ ] Pause/resume
- [ ] Persisted state

**Practical (60 min)**

- [ ] Add an approval interrupt before any write tool
- [ ] Resume from persisted state

**Recall (15 min)**

- [ ] Explain human-in-the-loop & interrupts in your own words: what is approval, and when does persisted state matter in a production LLM system?

## Week 23 - Agent Memory
*Phase 8 - Agents | Roadmap 16*


### Day 155 - Mon 01 Mar 2027 - Conversation memory

**Theory (45 min)**

- [ ] Message history
- [ ] Windowing
- [ ] Summarisation

**Practical (60 min)**

- [ ] Add rolling-summary memory to your agent
- [ ] Verify long chats stay in budget

**Recall (15 min)**

- [ ] Explain conversation memory in your own words: what is message history, and when does summarisation matter in a production LLM system?

### Day 156 - Tue 02 Mar 2027 - Short-term memory

**Theory (45 min)**

- [ ] Working state within a task
- [ ] Scratchpad
- [ ] Tool outputs

**Practical (60 min)**

- [ ] Persist intermediate tool results and reuse them instead of recalling tools

**Recall (15 min)**

- [ ] Explain short-term memory in your own words: what is working state within a task, and when does tool outputs matter in a production LLM system?

### Day 157 - Wed 03 Mar 2027 - Long-term memory

**Theory (45 min)**

- [ ] Across sessions
- [ ] User profiles
- [ ] Storage design

**Practical (60 min)**

- [ ] Store per-user facts in Postgres and load them at session start

**Recall (15 min)**

- [ ] Explain long-term memory in your own words: what is across sessions, and when does storage design matter in a production LLM system?

### Day 158 - Thu 04 Mar 2027 - Semantic & episodic memory

**Theory (45 min)**

- [ ] Facts vs events
- [ ] What to store
- [ ] Decay

**Practical (60 min)**

- [ ] Implement two memory types and a write-policy deciding which gets used

**Recall (15 min)**

- [ ] Explain semantic & episodic memory in your own words: what is facts vs events, and when does decay matter in a production LLM system?

### Day 159 - Fri 05 Mar 2027 - Memory retrieval & ranking

**Theory (45 min)**

- [ ] Embedding memory
- [ ] Recency + relevance scoring

**Practical (60 min)**

- [ ] Retrieve memories by hybrid recency+similarity score
- [ ] Test on 10 sessions

**Recall (15 min)**

- [ ] Explain memory retrieval & ranking in your own words: what is embedding memory, and when does recency + relevance scoring matter in a production LLM system?

### Day 160 - Sat 06 Mar 2027 - Memory compression

**Theory (45 min)**

- [ ] Summarising old memories
- [ ] Dedupe
- [ ] Size caps

**Practical (60 min)**

- [ ] Add compaction that caps memory at N items without losing key facts

**Recall (15 min)**

- [ ] Explain memory compression in your own words: what is summarising old memories, and when does size caps matter in a production LLM system?

### Day 161 - Sun 07 Mar 2027 - Memory security

**Theory (45 min)**

- [ ] PII
- [ ] Consent
- [ ] Deletion
- [ ] Leakage across users/tenants

**Practical (60 min)**

- [ ] Implement a delete-my-data path and test cross-user isolation

**Recall (15 min)**

- [ ] Explain memory security in your own words: what is pii, and when does leakage across users/tenants matter in a production LLM system?

## Week 24 - LangChain
*Phase 9 - Frameworks | Roadmap 17*


### Day 162 - Mon 08 Mar 2027 - LangChain architecture

**Theory (45 min)**

- [ ] Models
- [ ] Prompts
- [ ] Retrievers
- [ ] Tools
- [ ] Runnables

**Practical (60 min)**

- [ ] Rebuild your naive RAG in LangChain and compare LOC vs your own code

**Recall (15 min)**

- [ ] Explain langchain architecture in your own words: what is models, and when does runnables matter in a production LLM system?

### Day 163 - Tue 09 Mar 2027 - Runnables & LCEL

**Theory (45 min)**

- [ ] Composition
- [ ] Invoke/batch/stream
- [ ] RunnablePassthrough

**Practical (60 min)**

- [ ] Build a 4-step LCEL chain with streaming and batching

**Recall (15 min)**

- [ ] Explain runnables & lcel in your own words: what is composition, and when does runnablepassthrough matter in a production LLM system?

### Day 164 - Wed 10 Mar 2027 - Chains

**Theory (45 min)**

- [ ] Simple chains
- [ ] Multi-step pipelines
- [ ] When a chain is enough

**Practical (60 min)**

- [ ] Convert your extract->verify->summarise chain to LCEL with validation

**Recall (15 min)**

- [ ] Explain chains in your own words: what is simple chains, and when does when a chain is enough matter in a production LLM system?

### Day 165 - Thu 11 Mar 2027 - Retrievers

**Theory (45 min)**

- [ ] Retriever abstraction
- [ ] Vector/hybrid retrievers
- [ ] Compression retriever

**Practical (60 min)**

- [ ] Wrap pgvector as a custom LangChain retriever with metadata filters

**Recall (15 min)**

- [ ] Explain retrievers in your own words: what is retriever abstraction, and when does compression retriever matter in a production LLM system?

### Day 166 - Fri 12 Mar 2027 - Tools in LangChain

**Theory (45 min)**

- [ ] @tool
- [ ] Schemas
- [ ] Tool execution
- [ ] Bind_tools

**Practical (60 min)**

- [ ] Port your 3 tools into LangChain and run an agent with them

**Recall (15 min)**

- [ ] Explain tools in langchain in your own words: what is @tool, and when does bind_tools matter in a production LLM system?

### Day 167 - Sat 13 Mar 2027 - Output parsers

**Theory (45 min)**

- [ ] Structured output
- [ ] Pydantic parsers
- [ ] Retry parsers

**Practical (60 min)**

- [ ] Use with_structured_output and test failure/repair behaviour

**Recall (15 min)**

- [ ] Explain output parsers in your own words: what is structured output, and when does retry parsers matter in a production LLM system?

### Day 168 - Sun 14 Mar 2027 - LangSmith basics

**Theory (45 min)**

- [ ] Tracing
- [ ] Projects
- [ ] Datasets
- [ ] Debugging runs
- [ ] LangServe awareness: when serving chains as an API is worth it (Roadmap 17.8)

**Practical (60 min)**

- [ ] Enable tracing
- [ ] Inspect a failed run end-to-end in LangSmith

**Recall (15 min)**

- [ ] Explain langsmith basics in your own words: what is tracing, and when does debugging runs matter in a production LLM system?

## Week 25 - LangGraph I
*Phase 9 - Frameworks | Roadmap 18.1-18.7*


### Day 169 - Mon 15 Mar 2027 - Why graphs

**Theory (45 min)**

- [ ] Explicit state
- [ ] Branching
- [ ] Loops
- [ ] Persistence
- [ ] Intervention

**Practical (60 min)**

- [ ] Rewrite your hand-built agent loop as a graph diagram before coding

**Recall (15 min)**

- [ ] Explain why graphs in your own words: what is explicit state, and when does intervention matter in a production LLM system?

### Day 170 - Tue 16 Mar 2027 - StateGraph & State

**Theory (45 min)**

- [ ] State schema
- [ ] Reducers
- [ ] Typed state
- [ ] Annotations

**Practical (60 min)**

- [ ] Define a TypedDict state with an add-messages reducer

**Recall (15 min)**

- [ ] Explain stategraph & state in your own words: what is state schema, and when does annotations matter in a production LLM system?

### Day 171 - Wed 17 Mar 2027 - Nodes

**Theory (45 min)**

- [ ] Node functions
- [ ] Pure updates
- [ ] Side effects
- [ ] Naming

**Practical (60 min)**

- [ ] Build a 4-node graph: classify -> retrieve -> generate -> format

**Recall (15 min)**

- [ ] Explain nodes in your own words: what is node functions, and when does naming matter in a production LLM system?

### Day 172 - Thu 18 Mar 2027 - Edges

**Theory (45 min)**

- [ ] Normal edges
- [ ] Entry/finish points
- [ ] Graph compilation

**Practical (60 min)**

- [ ] Wire edges and compile
- [ ] Visualise the graph

**Recall (15 min)**

- [ ] Explain edges in your own words: what is normal edges, and when does graph compilation matter in a production LLM system?

### Day 173 - Fri 19 Mar 2027 - Conditional routing

**Theory (45 min)**

- [ ] Conditional edges
- [ ] Routing functions
- [ ] Multiple branches

**Practical (60 min)**

- [ ] Add routing: simple query -> direct answer, complex -> retrieval path

**Recall (15 min)**

- [ ] Explain conditional routing in your own words: what is conditional edges, and when does multiple branches matter in a production LLM system?

### Day 174 - Sat 20 Mar 2027 - Tool nodes

**Theory (45 min)**

- [ ] ToolNode
- [ ] Tool condition
- [ ] Agent-tool cycles

**Practical (60 min)**

- [ ] Build the classic agent<->tools cycle with a step limit

**Recall (15 min)**

- [ ] Explain tool nodes in your own words: what is toolnode, and when does agent-tool cycles matter in a production LLM system?

### Day 175 - Sun 21 Mar 2027 - Week 30 review

**Theory (45 min)**

- [ ] Consolidate graph basics

**Practical (60 min)**

- [ ] Refactor your RAG+agent into one compiled LangGraph app with tests

**Recall (15 min)**

- [ ] Explain week 30 review in your own words: what is consolidate graph basics, and when does week 30 review matter in a production LLM system?

## Week 26 - LangGraph II
*Phase 9 - Frameworks | Roadmap 18.8-18.14*


### Day 176 - Mon 22 Mar 2027 - Checkpointing

**Theory (45 min)**

- [ ] Checkpointers
- [ ] Thread_id
- [ ] State snapshots

**Practical (60 min)**

- [ ] Add a Postgres checkpointer
- [ ] Resume a conversation after process restart

**Recall (15 min)**

- [ ] Explain checkpointing in your own words: what is checkpointers, and when does state snapshots matter in a production LLM system?

### Day 177 - Tue 23 Mar 2027 - Persistence

**Theory (45 min)**

- [ ] Durable state
- [ ] History
- [ ] Time-travel
- [ ] State inspection

**Practical (60 min)**

- [ ] Inspect state history and replay from an earlier checkpoint

**Recall (15 min)**

- [ ] Explain persistence in your own words: what is durable state, and when does state inspection matter in a production LLM system?

### Day 178 - Wed 24 Mar 2027 - Interrupts

**Theory (45 min)**

- [ ] Interrupt()
- [ ] Pause/resume
- [ ] Human decision injection

**Practical (60 min)**

- [ ] Pause before a destructive tool, get CLI approval, resume the graph

**Recall (15 min)**

- [ ] Explain interrupts in your own words: what is interrupt(), and when does human decision injection matter in a production LLM system?

### Day 179 - Thu 25 Mar 2027 - Human-in-the-loop patterns

**Theory (45 min)**

- [ ] Approve
- [ ] Edit state
- [ ] Reject with feedback

**Practical (60 min)**

- [ ] Implement all three HITL actions and test each path

**Recall (15 min)**

- [ ] Explain human-in-the-loop patterns in your own words: what is approve, and when does reject with feedback matter in a production LLM system?

### Day 180 - Fri 26 Mar 2027 - Parallel nodes

**Theory (45 min)**

- [ ] Fan-out/fan-in
- [ ] Concurrent branches
- [ ] Merging state

**Practical (60 min)**

- [ ] Run 3 retrievers in parallel branches and merge results

**Recall (15 min)**

- [ ] Explain parallel nodes in your own words: what is fan-out/fan-in, and when does merging state matter in a production LLM system?

### Day 181 - Sat 27 Mar 2027 - Durable execution & recovery

**Theory (45 min)**

- [ ] Idempotent nodes
- [ ] Retries
- [ ] Failure recovery
- [ ] Partial progress

**Practical (60 min)**

- [ ] Kill the process mid-run
- [ ] Prove it resumes without redoing completed work

**Recall (15 min)**

- [ ] Explain durable execution & recovery in your own words: what is idempotent nodes, and when does partial progress matter in a production LLM system?

### Day 182 - Sun 28 Mar 2027 - Week 31 review

**Theory (45 min)**

- [ ] Consolidate LangGraph

**Practical (60 min)**

- [ ] Write LANGGRAPH-NOTES.md covering every concept with your own examples

**Recall (15 min)**

- [ ] Explain week 31 review in your own words: what is consolidate langgraph, and when does week 31 review matter in a production LLM system?

## Week 27 - MCP
*Phase 10 - MCP & Security | Roadmap 19*


### Day 183 - Mon 29 Mar 2027 - MCP fundamentals

**Theory (45 min)**

- [ ] Problem it solves
- [ ] Host
- [ ] Client
- [ ] Server roles

**Practical (60 min)**

- [ ] Diagram MCP architecture
- [ ] Connect an existing MCP server to a client and test

**Recall (15 min)**

- [ ] Explain mcp fundamentals in your own words: what is problem it solves, and when does server roles matter in a production LLM system?

### Day 184 - Tue 30 Mar 2027 - MCP primitives

**Theory (45 min)**

- [ ] Tools
- [ ] Resources
- [ ] Prompts
- [ ] Their differences

**Practical (60 min)**

- [ ] Write notes mapping each primitive to a use case in your work

**Recall (15 min)**

- [ ] Explain mcp primitives in your own words: what is tools, and when does their differences matter in a production LLM system?

### Day 185 - Wed 31 Mar 2027 - MCP communication

**Theory (45 min)**

- [ ] JSON-RPC
- [ ] Transports (stdio/http)
- [ ] Requests
- [ ] Errors

**Practical (60 min)**

- [ ] Trace raw JSON-RPC messages for one tool call end-to-end

**Recall (15 min)**

- [ ] Explain mcp communication in your own words: what is json-rpc, and when does errors matter in a production LLM system?

### Day 186 - Thu 01 Apr 2027 - Build an MCP server I

**Theory (45 min)**

- [ ] Server setup
- [ ] Tool definitions
- [ ] Input validation

**Practical (60 min)**

- [ ] Build an MCP server with 3 tools over your Postgres data

**Recall (15 min)**

- [ ] Explain build an mcp server i in your own words: what is server setup, and when does input validation matter in a production LLM system?

### Day 187 - Fri 02 Apr 2027 - Build an MCP server II

**Theory (45 min)**

- [ ] Execution
- [ ] Structured results
- [ ] Error handling
- [ ] Logging

**Practical (60 min)**

- [ ] Add validation, structured errors and logging
- [ ] Test failure paths

**Recall (15 min)**

- [ ] Explain build an mcp server ii in your own words: what is execution, and when does logging matter in a production LLM system?

### Day 188 - Sat 03 Apr 2027 - MCP discovery & remote MCP

**Theory (45 min)**

- [ ] Tool/capability discovery
- [ ] Progressive disclosure
- [ ] Remote transport + auth

**Practical (60 min)**

- [ ] Expose your server over HTTP with bearer auth and connect remotely

**Recall (15 min)**

- [ ] Explain mcp discovery & remote mcp in your own words: what is tool/capability discovery, and when does remote transport + auth matter in a production LLM system?

### Day 189 - Sun 04 Apr 2027 - MCP security

**Theory (45 min)**

- [ ] Trust boundaries
- [ ] Malicious tools
- [ ] Tool poisoning
- [ ] Exfiltration

**Practical (60 min)**

- [ ] Write a threat model for your MCP server with 6 risks and mitigations

**Recall (15 min)**

- [ ] Explain mcp security in your own words: what is trust boundaries, and when does exfiltration matter in a production LLM system?

## Week 28 - AI Security
*Phase 10 - MCP & Security | Roadmap 20*


### Day 190 - Mon 05 Apr 2027 - Prompt injection

**Theory (45 min)**

- [ ] Direct vs indirect
- [ ] Untrusted content
- [ ] Instruction hierarchy

**Practical (60 min)**

- [ ] Poison a document in your RAG corpus
- [ ] Prove the attack,
- [ ] Block it

**Recall (15 min)**

- [ ] Explain prompt injection in your own words: what is direct vs indirect, and when does instruction hierarchy matter in a production LLM system?

### Day 191 - Tue 06 Apr 2027 - Sensitive information disclosure

**Theory (45 min)**

- [ ] PII
- [ ] Secrets
- [ ] Internal docs
- [ ] Prompt leakage

**Practical (60 min)**

- [ ] Add PII detection/redaction on inputs and outputs
- [ ] Test with fake PII

**Recall (15 min)**

- [ ] Explain sensitive information disclosure in your own words: what is pii, and when does prompt leakage matter in a production LLM system?

### Day 192 - Wed 07 Apr 2027 - Tool injection & excessive agency

**Theory (45 min)**

- [ ] Malicious tool inputs
- [ ] Output manipulation
- [ ] Least privilege

**Practical (60 min)**

- [ ] Restrict each tool's scope
- [ ] Add transaction limits and an approval policy

**Recall (15 min)**

- [ ] Explain tool injection & excessive agency in your own words: what is malicious tool inputs, and when does least privilege matter in a production LLM system?

### Day 193 - Thu 08 Apr 2027 - RAG poisoning

**Theory (45 min)**

- [ ] Malicious docs
- [ ] Poisoned embeddings
- [ ] Retrieval manipulation

**Practical (60 min)**

- [ ] Add source trust levels + ingestion validation
- [ ] Re-run the poisoning test

**Recall (15 min)**

- [ ] Explain rag poisoning in your own words: what is malicious docs, and when does retrieval manipulation matter in a production LLM system?

### Day 194 - Fri 09 Apr 2027 - Jailbreaks & improper output handling

**Theory (45 min)**

- [ ] Safety bypasses
- [ ] Never executing raw output
- [ ] Sanitisation

**Practical (60 min)**

- [ ] Test 10 jailbreak prompts
- [ ] Add output sanitisation before any execution

**Recall (15 min)**

- [ ] Explain jailbreaks & improper output handling in your own words: what is safety bypasses, and when does sanitisation matter in a production LLM system?

### Day 195 - Sat 10 Apr 2027 - Guardrails

**Theory (45 min)**

- [ ] Input/output filters
- [ ] Topic controls
- [ ] Policy enforcement
- [ ] Bedrock Guardrails
- [ ] Sandboxing: isolated execution, restricted filesystem/network, resource limits (Roadmap 20.9)

**Practical (60 min)**

- [ ] Attach a guardrail layer to your API
- [ ] Verify blocked vs allowed cases
- [ ] Run one tool inside a restricted sandbox (no network, temp FS) and verify limits hold

**Recall (15 min)**

- [ ] Explain guardrails in your own words: what is input/output filters, and when does bedrock guardrails matter in a production LLM system?

### Day 196 - Sun 11 Apr 2027 - OWASP GenAI Top 10 & red teaming

**Theory (45 min)**

- [ ] Current risks
- [ ] Mitigations
- [ ] Attack datasets
- [ ] Regression tests

**Practical (60 min)**

- [ ] Build a 30-case security regression suite and run it in CI

**Recall (15 min)**

- [ ] Explain owasp genai top 10 & red teaming in your own words: what is current risks, and when does regression tests matter in a production LLM system?

## Week 29 - Evaluation & Observability
*Phase 11 - Production | Roadmap 21*


### Day 197 - Mon 12 Apr 2027 - Evaluation fundamentals redux

**Theory (45 min)**

- [ ] Offline
- [ ] Online
- [ ] Human
- [ ] Automated
- [ ] Eval-driven development

**Practical (60 min)**

- [ ] Define your eval strategy doc for the enterprise assistant

**Recall (15 min)**

- [ ] Explain evaluation fundamentals redux in your own words: what is offline, and when does eval-driven development matter in a production LLM system?

### Day 198 - Tue 13 Apr 2027 - LLM evaluation

**Theory (45 min)**

- [ ] Correctness
- [ ] Relevance
- [ ] Faithfulness
- [ ] Safety
- [ ] Format compliance

**Practical (60 min)**

- [ ] Add automated scoring for all 5 dimensions on a nightly run

**Recall (15 min)**

- [ ] Explain llm evaluation in your own words: what is correctness, and when does format compliance matter in a production LLM system?

### Day 199 - Wed 14 Apr 2027 - Agent evaluation

**Theory (45 min)**

- [ ] Task success
- [ ] Tool selection accuracy
- [ ] Steps
- [ ] Cost
- [ ] Latency

**Practical (60 min)**

- [ ] Build an agent eval set of 30 tasks and score tool-selection accuracy

**Recall (15 min)**

- [ ] Explain agent evaluation in your own words: what is task success, and when does latency matter in a production LLM system?

### Day 200 - Thu 15 Apr 2027 - Tracing

**Theory (45 min)**

- [ ] Request traces
- [ ] LLM/retrieval/tool/DB spans
- [ ] Correlation IDs

**Practical (60 min)**

- [ ] Instrument the full request path so one trace shows every span

**Recall (15 min)**

- [ ] Explain tracing in your own words: what is request traces, and when does correlation ids matter in a production LLM system?

### Day 201 - Fri 16 Apr 2027 - Metrics

**Theory (45 min)**

- [ ] Latency
- [ ] Error rate
- [ ] Tokens
- [ ] Cost
- [ ] Retrieval quality
- [ ] Success rate

**Practical (60 min)**

- [ ] Emit these 6 metrics and build a simple dashboard

**Recall (15 min)**

- [ ] Explain metrics in your own words: what is latency, and when does success rate matter in a production LLM system?

### Day 202 - Sat 17 Apr 2027 - Langfuse / LangSmith

**Theory (45 min)**

- [ ] Traces
- [ ] Sessions
- [ ] Scores
- [ ] Prompt tracking
- [ ] Dataset experiments

**Practical (60 min)**

- [ ] Run a dataset experiment comparing two prompt versions and pick a winner

**Recall (15 min)**

- [ ] Explain langfuse / langsmith in your own words: what is traces, and when does dataset experiments matter in a production LLM system?

### Day 203 - Sun 18 Apr 2027 - OpenTelemetry

**Theory (45 min)**

- [ ] Traces
- [ ] Metrics
- [ ] Logs
- [ ] Instrumentation
- [ ] Exporters

**Practical (60 min)**

- [ ] Export OTel traces from FastAPI + LLM calls to a collector

**Recall (15 min)**

- [ ] Explain opentelemetry in your own words: what is traces, and when does exporters matter in a production LLM system?

## Week 30 - Production Engineering + AWS Bedrock Deep Dive
*Phase 11 - Production | Roadmap 22, Roadmap 25*


### Day 204 - Mon 19 Apr 2027 - Caching

**Theory (45 min)**

- [ ] Response
- [ ] Prompt/context
- [ ] Retrieval caching
- [ ] Invalidation

**Practical (60 min)**

- [ ] Layer all three caches
- [ ] Report hit rates and cost savings

**Recall (15 min)**

- [ ] Explain caching in your own words: what is response, and when does invalidation matter in a production LLM system?

### Day 205 - Tue 20 Apr 2027 - Streaming

**Theory (45 min)**

- [ ] Token streaming
- [ ] SSE
- [ ] Partial responses
- [ ] Mid-stream errors

**Practical (60 min)**

- [ ] Add a streaming endpoint with proper error frames and client handling

**Recall (15 min)**

- [ ] Explain streaming in your own words: what is token streaming, and when does mid-stream errors matter in a production LLM system?

### Day 206 - Wed 21 Apr 2027 - Cost engineering

**Theory (45 min)**

- [ ] Model selection
- [ ] Prompt reduction
- [ ] Caching
- [ ] Batching
- [ ] Routing
- [ ] Provider rate limits, 429 handling and burst strategy for LLM APIs
- [ ] Circuit breaker + fallback to a cheaper model on provider failure

**Practical (60 min)**

- [ ] Cut the cost of one workflow by 40% and document how
- [ ] Force a 429 from the provider and verify backoff + cheaper-model fallback both fire

**Recall (15 min)**

- [ ] Explain cost engineering in your own words: what is model selection, and when does routing matter in a production LLM system?

### Day 207 - Thu 22 Apr 2027 - Latency & A/B testing

**Theory (45 min)**

- [ ] TTFT
- [ ] Parallelism
- [ ] Model latency
- [ ] Canary
- [ ] Traffic splitting

**Practical (60 min)**

- [ ] Measure and reduce p95 latency
- [ ] Set up a 90/10 prompt-version split

**Recall (15 min)**

- [ ] Explain latency & a/b testing in your own words: what is ttft, and when does traffic splitting matter in a production LLM system?

### Day 208 - Fri 23 Apr 2027 - Bedrock fundamentals redux

**Theory (45 min)**

- [ ] Model access
- [ ] Runtime
- [ ] Regions
- [ ] Quotas
- [ ] Cross-region inference

**Practical (60 min)**

- [ ] Audit which models you can call in which region
- [ ] Document constraints

**Recall (15 min)**

- [ ] Explain bedrock fundamentals redux in your own words: what is model access, and when does cross-region inference matter in a production LLM system?

### Day 209 - Sat 24 Apr 2027 - Model invocation patterns

**Theory (45 min)**

- [ ] Converse
- [ ] Streaming
- [ ] Errors
- [ ] Usage accounting

**Practical (60 min)**

- [ ] Wrap Bedrock with the same interface as your Anthropic client
- [ ] Swap at runtime

**Recall (15 min)**

- [ ] Explain model invocation patterns in your own words: what is converse, and when does usage accounting matter in a production LLM system?

### Day 210 - Sun 25 Apr 2027 - Claude on Bedrock

**Theory (45 min)**

- [ ] Model selection
- [ ] Prompting
- [ ] Tool use
- [ ] Streaming differences

**Practical (60 min)**

- [ ] Run your full agent on Bedrock Claude
- [ ] Note every behavioural difference

**Recall (15 min)**

- [ ] Explain claude on bedrock in your own words: what is model selection, and when does streaming differences matter in a production LLM system?

## Week 31 - AWS Bedrock Deep Dive + Multi-Agent & Communication
*Phase 12 - AWS | Roadmap 25, Roadmap 26*


### Day 211 - Mon 26 Apr 2027 - Bedrock Knowledge Bases

**Theory (45 min)**

- [ ] Data sources
- [ ] Sync
- [ ] Retrieve
- [ ] Retrieve-and-generate

**Practical (60 min)**

- [ ] Build a Knowledge Base over your S3 docs and query it

**Recall (15 min)**

- [ ] Explain bedrock knowledge bases in your own words: what is data sources, and when does retrieve-and-generate matter in a production LLM system?

### Day 212 - Tue 27 Apr 2027 - Managed vs custom RAG

**Theory (45 min)**

- [ ] Control
- [ ] Cost
- [ ] Features
- [ ] Portability tradeoffs

**Practical (60 min)**

- [ ] Compare KB answers vs your custom RAG on the golden set
- [ ] Tabulate

**Recall (15 min)**

- [ ] Explain managed vs custom rag in your own words: what is control, and when does portability tradeoffs matter in a production LLM system?

### Day 213 - Wed 28 Apr 2027 - Bedrock Guardrails

**Theory (45 min)**

- [ ] Input/output safeguards
- [ ] PII
- [ ] Harmful content
- [ ] Prompt attacks

**Practical (60 min)**

- [ ] Attach a guardrail and test denied topics, PII masking and injection filtering

**Recall (15 min)**

- [ ] Explain bedrock guardrails in your own words: what is input/output safeguards, and when does prompt attacks matter in a production LLM system?

### Day 214 - Thu 29 Apr 2027 - Bedrock Agents / AgentCore

**Theory (45 min)**

- [ ] Agent architecture
- [ ] Action groups
- [ ] KBs
- [ ] Current service direction

**Practical (60 min)**

- [ ] Build one simple managed agent
- [ ] Write when you'd use it vs LangGraph

**Recall (15 min)**

- [ ] Explain bedrock agents / agentcore in your own words: what is agent architecture, and when does current service direction matter in a production LLM system?

### Day 215 - Fri 30 Apr 2027 - Why multi-agent

**Theory (45 min)**

- [ ] Separation of concerns
- [ ] Specialisation
- [ ] Parallelism
- [ ] Costs

**Practical (60 min)**

- [ ] List when multi-agent is justified vs a single agent with more tools

**Recall (15 min)**

- [ ] Explain why multi-agent in your own words: what is separation of concerns, and when does costs matter in a production LLM system?

### Day 216 - Sat 01 May 2027 - Supervisor pattern

**Theory (45 min)**

- [ ] Supervisor
- [ ] Workers
- [ ] Routing
- [ ] Aggregation

**Practical (60 min)**

- [ ] Build a supervisor + 3 worker agents in LangGraph

**Recall (15 min)**

- [ ] Explain supervisor pattern in your own words: what is supervisor, and when does aggregation matter in a production LLM system?

### Day 217 - Sun 02 May 2027 - Planner/worker & reviewer

**Theory (45 min)**

- [ ] Planning
- [ ] Execution
- [ ] Replanning
- [ ] Critique loops

**Practical (60 min)**

- [ ] Add a planner node and a reviewer node that can send work back

**Recall (15 min)**

- [ ] Explain planner/worker & reviewer in your own words: what is planning, and when does critique loops matter in a production LLM system?

## Week 32 - Multi-Agent & Communication + ML Fundamentals & Evaluation
*Phase 15 - Specialisation | Roadmap 26, Roadmap 27-28, Roadmap 31*


### Day 218 - Mon 03 May 2027 - Router & swarm patterns

**Theory (45 min)**

- [ ] Routing strategies
- [ ] Handoffs
- [ ] Shared state

**Practical (60 min)**

- [ ] Implement agent handoff where any agent can transfer to another

**Recall (15 min)**

- [ ] Explain router & swarm patterns in your own words: what is routing strategies, and when does shared state matter in a production LLM system?

### Day 219 - Tue 04 May 2027 - Reflection

**Theory (45 min)**

- [ ] Self-critique
- [ ] Revision loops
- [ ] Diminishing returns

**Practical (60 min)**

- [ ] Add one reflection pass
- [ ] Measure quality gain vs extra cost and latency

**Recall (15 min)**

- [ ] Explain reflection in your own words: what is self-critique, and when does diminishing returns matter in a production LLM system?

### Day 220 - Wed 05 May 2027 - A2A & event-driven agents

**Theory (45 min)**

- [ ] Agent identity
- [ ] Discovery
- [ ] Task handoff
- [ ] Messaging
- [ ] ACP and AG-UI: awareness-level only (Roadmap 28.4-28.5)

**Practical (60 min)**

- [ ] Sketch an A2A design for two independent services
- [ ] Note the protocol pieces

**Recall (15 min)**

- [ ] Explain a2a & event-driven agents in your own words: what is agent identity, and when does messaging matter in a production LLM system?

### Day 221 - Thu 06 May 2027 - Transformers & Hugging Face

**Theory (45 min)**

- [ ] Architecture recap
- [ ] Tokenizers
- [ ] Pipelines
- [ ] Model hub

**Practical (60 min)**

- [ ] Run a HF pipeline for embeddings + classification locally

**Recall (15 min)**

- [ ] Explain transformers & hugging face in your own words: what is architecture recap, and when does model hub matter in a production LLM system?

### Day 222 - Fri 07 May 2027 - Why fine-tuning & vs RAG

**Theory (45 min)**

- [ ] Behaviour vs knowledge
- [ ] Cost
- [ ] Maintenance
- [ ] Evaluation

**Practical (60 min)**

- [ ] Write the decision framework with 6 real scenarios and verdicts

**Recall (15 min)**

- [ ] Explain why fine-tuning & vs rag in your own words: what is behaviour vs knowledge, and when does evaluation matter in a production LLM system?

### Day 223 - Sat 08 May 2027 - Training data

**Theory (45 min)**

- [ ] Dataset design
- [ ] Quality
- [ ] Size
- [ ] Formatting
- [ ] Splits

**Practical (60 min)**

- [ ] Build a 200-example instruction dataset from your own domain

**Recall (15 min)**

- [ ] Explain training data in your own words: what is dataset design, and when does splits matter in a production LLM system?

### Day 224 - Sun 09 May 2027 - Supervised fine-tuning & LoRA

**Theory (45 min)**

- [ ] SFT loop
- [ ] LoRA adapters
- [ ] Rank
- [ ] Target modules

**Practical (60 min)**

- [ ] Fine-tune a small model with LoRA on your dataset

**Recall (15 min)**

- [ ] Explain supervised fine-tuning & lora in your own words: what is sft loop, and when does target modules matter in a production LLM system?

## Week 33 - Fine-Tuning & Inference + Coding Agents & Dev Workflow
*Phase 15 - Specialisation | Roadmap 31, Roadmap 32-33*


### Day 225 - Mon 10 May 2027 - QLoRA & PEFT

**Theory (45 min)**

- [ ] Quantised training
- [ ] Memory savings
- [ ] PEFT library

**Practical (60 min)**

- [ ] Re-run the fine-tune with QLoRA
- [ ] Compare memory and quality

**Recall (15 min)**

- [ ] Explain qlora & peft in your own words: what is quantised training, and when does peft library matter in a production LLM system?

### Day 226 - Tue 11 May 2027 - RLHF & alignment (awareness)

**Theory (45 min)**

- [ ] Preference data
- [ ] Reward models
- [ ] DPO idea

**Practical (60 min)**

- [ ] Write concise notes suitable for an interview answer

**Recall (15 min)**

- [ ] Explain rlhf & alignment (awareness) in your own words: what is preference data, and when does dpo idea matter in a production LLM system?

### Day 227 - Wed 12 May 2027 - GPUs, batching, throughput vs latency

**Theory (45 min)**

- [ ] Why GPUs
- [ ] Memory
- [ ] Batch size
- [ ] KV cache
- [ ] Quantisation

**Practical (60 min)**

- [ ] Benchmark batch sizes 1/4/16 on local inference
- [ ] Plot throughput vs latency

**Recall (15 min)**

- [ ] Explain gpus, batching, throughput vs latency in your own words: what is why gpus, and when does quantisation matter in a production LLM system?

### Day 228 - Thu 13 May 2027 - Model serving & vLLM

**Theory (45 min)**

- [ ] Serving stacks
- [ ] Continuous batching
- [ ] Speculative decoding idea

**Practical (60 min)**

- [ ] Serve a small model with vLLM and load-test it

**Recall (15 min)**

- [ ] Explain model serving & vllm in your own words: what is serving stacks, and when does speculative decoding idea matter in a production LLM system?

### Day 229 - Fri 14 May 2027 - Coding agent concepts

**Theory (45 min)**

- [ ] Agent loop
- [ ] Repo understanding
- [ ] Planning
- [ ] Validation

**Practical (60 min)**

- [ ] Use a coding agent to add a feature to your repo
- [ ] Review every diff critically

**Recall (15 min)**

- [ ] Explain coding agent concepts in your own words: what is agent loop, and when does validation matter in a production LLM system?

### Day 230 - Sat 15 May 2027 - Claude Code / Cursor workflows

**Theory (45 min)**

- [ ] Context control
- [ ] Iteration
- [ ] Verification
- [ ] Guardrails

**Practical (60 min)**

- [ ] Run the same task in two tools
- [ ] Document quality and control differences

**Recall (15 min)**

- [ ] Explain claude code / cursor workflows in your own words: what is context control, and when does guardrails matter in a production LLM system?

### Day 231 - Sun 16 May 2027 - CLAUDE.md

**Theory (45 min)**

- [ ] Project instructions
- [ ] Conventions
- [ ] Commands
- [ ] Do-nots

**Practical (60 min)**

- [ ] Write a strong CLAUDE.md for your RAG repo

**Recall (15 min)**

- [ ] Explain claude.md in your own words: what is project instructions, and when does do-nots matter in a production LLM system?

## Week 34 - Coding Agents & Dev Workflow + Project 1: Production RAG Assistant
*Phase 16 - Projects | Roadmap 32-33, Roadmap 34*


### Day 232 - Mon 17 May 2027 - Skills

**Theory (45 min)**

- [ ] Reusable skill files
- [ ] Structure
- [ ] When to use

**Practical (60 min)**

- [ ] Create a SKILL.md for your standard 'add a FastAPI endpoint' workflow

**Recall (15 min)**

- [ ] Explain skills in your own words: what is reusable skill files, and when does when to use matter in a production LLM system?

### Day 233 - Tue 18 May 2027 - Subagents

**Theory (45 min)**

- [ ] Delegation
- [ ] Scoped context
- [ ] Parallel work

**Practical (60 min)**

- [ ] Configure a review subagent that audits diffs before you merge

**Recall (15 min)**

- [ ] Explain subagents in your own words: what is delegation, and when does parallel work matter in a production LLM system?

### Day 234 - Wed 19 May 2027 - Hooks & MCP integration

**Theory (45 min)**

- [ ] Lifecycle hooks
- [ ] Automation
- [ ] Connecting MCP servers

**Practical (60 min)**

- [ ] Add a pre-commit hook + connect your own MCP server to the coding agent

**Recall (15 min)**

- [ ] Explain hooks & mcp integration in your own words: what is lifecycle hooks, and when does connecting mcp servers matter in a production LLM system?

### Day 235 - Thu 20 May 2027 - Choosing coding-agent tools

**Theory (45 min)**

- [ ] Cost
- [ ] Control
- [ ] Security
- [ ] Enterprise constraints

**Practical (60 min)**

- [ ] Write your recommendation doc as if presenting to your DXC team

**Recall (15 min)**

- [ ] Explain choosing coding-agent tools in your own words: what is cost, and when does enterprise constraints matter in a production LLM system?

### Day 236 - Fri 21 May 2027 - Requirements & architecture

**Theory (45 min)**

- [ ] Scope
- [ ] NFRs
- [ ] Architecture decisions
- [ ] ADRs

**Practical (60 min)**

- [ ] Write requirements + architecture doc with 6 recorded decisions

**Recall (15 min)**

- [ ] Explain requirements & architecture in your own words: what is scope, and when does adrs matter in a production LLM system?

### Day 237 - Sat 22 May 2027 - Ingestion & chunking

**Theory (45 min)**

- [ ] Loaders
- [ ] Extraction
- [ ] Chunk strategy
- [ ] Metadata

**Practical (60 min)**

- [ ] Build the production ingestion service over a real 200+ doc corpus

**Recall (15 min)**

- [ ] Explain ingestion & chunking in your own words: what is loaders, and when does metadata matter in a production LLM system?

### Day 238 - Sun 23 May 2027 - Embeddings & vector store

**Theory (45 min)**

- [ ] Model choice
- [ ] Batching
- [ ] Upsert
- [ ] Incremental indexing

**Practical (60 min)**

- [ ] Index the corpus with idempotent incremental updates

**Recall (15 min)**

- [ ] Explain embeddings & vector store in your own words: what is model choice, and when does incremental indexing matter in a production LLM system?

## Week 35 - Project 1: Production RAG Assistant + Project 2: Tool-Using Agent
*Phase 16 - Projects | Roadmap 34, Roadmap 35.1*


### Day 239 - Mon 24 May 2027 - Hybrid search & reranking

**Theory (45 min)**

- [ ] Dense+sparse fusion
- [ ] Reranker
- [ ] Tuning

**Practical (60 min)**

- [ ] Ship hybrid + rerank
- [ ] Measure recall@5 and precision improvements

**Recall (15 min)**

- [ ] Explain hybrid search & reranking in your own words: what is dense+sparse fusion, and when does tuning matter in a production LLM system?

### Day 240 - Tue 25 May 2027 - Generation with citations

**Theory (45 min)**

- [ ] Prompting
- [ ] Grounding
- [ ] Abstention
- [ ] Citation formatting

**Practical (60 min)**

- [ ] Return answers with verifiable inline citations
- [ ] Test 30 questions

**Recall (15 min)**

- [ ] Explain generation with citations in your own words: what is prompting, and when does citation formatting matter in a production LLM system?

### Day 241 - Wed 26 May 2027 - FastAPI + Docker

**Theory (45 min)**

- [ ] Endpoints
- [ ] Auth
- [ ] Streaming
- [ ] Containerisation

**Practical (60 min)**

- [ ] Expose /query and /ingest, containerise, run via compose

**Recall (15 min)**

- [ ] Explain fastapi + docker in your own words: what is endpoints, and when does containerisation matter in a production LLM system?

### Day 242 - Thu 27 May 2027 - Evaluation, observability, AWS deploy

**Theory (45 min)**

- [ ] Golden set
- [ ] Metrics
- [ ] Tracing
- [ ] Deployment

**Practical (60 min)**

- [ ] Deploy to AWS with tracing + nightly eval
- [ ] Record final metrics

**Recall (15 min)**

- [ ] Explain evaluation, observability, aws deploy in your own words: what is golden set, and when does deployment matter in a production LLM system?

### Day 243 - Fri 28 May 2027 - Design & tool inventory

**Theory (45 min)**

- [ ] Use case
- [ ] Tools
- [ ] State
- [ ] Termination
- [ ] Risks

**Practical (60 min)**

- [ ] Write the agent design doc: 5 tools, state schema, failure policy

**Recall (15 min)**

- [ ] Explain design & tool inventory in your own words: what is use case, and when does risks matter in a production LLM system?

### Day 244 - Sat 29 May 2027 - Tools & external APIs

**Theory (45 min)**

- [ ] Schemas
- [ ] Auth
- [ ] Rate limits
- [ ] Error mapping

**Practical (60 min)**

- [ ] Implement 5 real tools including 2 external APIs with auth

**Recall (15 min)**

- [ ] Explain tools & external apis in your own words: what is schemas, and when does error mapping matter in a production LLM system?

### Day 245 - Sun 30 May 2027 - LangGraph agent loop

**Theory (45 min)**

- [ ] Nodes
- [ ] Edges
- [ ] Routing
- [ ] Tool node
- [ ] Step caps

**Practical (60 min)**

- [ ] Build the graph and get an end-to-end successful run

**Recall (15 min)**

- [ ] Explain langgraph agent loop in your own words: what is nodes, and when does step caps matter in a production LLM system?

## Week 36 - Project 2: Tool-Using Agent + Project 3: Enterprise AI Assistant
*Phase 16 - Projects | Roadmap 35.1, Roadmap 35.2*


### Day 246 - Mon 31 May 2027 - State & persistence

**Theory (45 min)**

- [ ] Checkpointing
- [ ] Threads
- [ ] Resume

**Practical (60 min)**

- [ ] Add a persistent checkpointer
- [ ] Resume mid-task after a restart

**Recall (15 min)**

- [ ] Explain state & persistence in your own words: what is checkpointing, and when does resume matter in a production LLM system?

### Day 247 - Tue 01 Jun 2027 - Human approval

**Theory (45 min)**

- [ ] Interrupts
- [ ] Approve/edit/reject
- [ ] Audit of decisions

**Practical (60 min)**

- [ ] Add approval for sensitive actions with a full audit trail

**Recall (15 min)**

- [ ] Explain human approval in your own words: what is interrupts, and when does audit of decisions matter in a production LLM system?

### Day 248 - Wed 02 Jun 2027 - Evaluation & tracing

**Theory (45 min)**

- [ ] Task success
- [ ] Tool accuracy
- [ ] Steps
- [ ] Cost
- [ ] Traces

**Practical (60 min)**

- [ ] Run a 30-task eval
- [ ] Publish a results table in the README

**Recall (15 min)**

- [ ] Explain evaluation & tracing in your own words: what is task success, and when does traces matter in a production LLM system?

### Day 249 - Thu 03 Jun 2027 - Requirements & threat model

**Theory (45 min)**

- [ ] Users
- [ ] Roles
- [ ] Data classes
- [ ] Risks
- [ ] Compliance

**Practical (60 min)**

- [ ] Write requirements + a full threat model

**Recall (15 min)**

- [ ] Explain requirements & threat model in your own words: what is users, and when does compliance matter in a production LLM system?

### Day 250 - Fri 04 Jun 2027 - Permission-aware RAG

**Theory (45 min)**

- [ ] ACL metadata
- [ ] Filtered retrieval
- [ ] Leak tests

**Practical (60 min)**

- [ ] Ship ACL-filtered retrieval
- [ ] Write 10 leakage tests that must fail to retrieve

**Recall (15 min)**

- [ ] Explain permission-aware rag in your own words: what is acl metadata, and when does leak tests matter in a production LLM system?

### Day 251 - Sat 05 Jun 2027 - Agent tools + MCP

**Theory (45 min)**

- [ ] Enterprise tools
- [ ] MCP server
- [ ] Least privilege

**Practical (60 min)**

- [ ] Connect your MCP server as the tool layer with scoped permissions

**Recall (15 min)**

- [ ] Explain agent tools + mcp in your own words: what is enterprise tools, and when does least privilege matter in a production LLM system?

### Day 252 - Sun 06 Jun 2027 - Bedrock + guardrails

**Theory (45 min)**

- [ ] Model routing
- [ ] Guardrails
- [ ] Region strategy

**Practical (60 min)**

- [ ] Run the assistant on Bedrock with guardrails enabled end-to-end

**Recall (15 min)**

- [ ] Explain bedrock + guardrails in your own words: what is model routing, and when does region strategy matter in a production LLM system?

## Week 37 - System Design for AI + Interview Preparation & Final Polish
*Phase 17 - Interview | Roadmap 35.3, Roadmap 37-40*


### Day 253 - Mon 07 Jun 2027 - RAG system design

**Theory (45 min)**

- [ ] Ingestion
- [ ] Chunking
- [ ] Store
- [ ] Retrieval
- [ ] Rerank
- [ ] Generate
- [ ] Eval

**Practical (60 min)**

- [ ] Timed design: enterprise knowledge assistant for 1M documents

**Recall (15 min)**

- [ ] Explain rag system design in your own words: what is ingestion, and when does eval matter in a production LLM system?

### Day 254 - Tue 08 Jun 2027 - Agent system design

**Theory (45 min)**

- [ ] State
- [ ] Tools
- [ ] Loop
- [ ] Routing
- [ ] Persistence
- [ ] Approval
- [ ] Recovery

**Practical (60 min)**

- [ ] Timed design: autonomous ticket-resolution agent

**Recall (15 min)**

- [ ] Explain agent system design in your own words: what is state, and when does recovery matter in a production LLM system?

### Day 255 - Wed 09 Jun 2027 - Document intelligence design

**Theory (45 min)**

- [ ] OCR
- [ ] Layout
- [ ] Tables
- [ ] Extraction
- [ ] Validation
- [ ] Human review

**Practical (60 min)**

- [ ] Timed design: invoice processing at 100k docs/day

**Recall (15 min)**

- [ ] Explain document intelligence design in your own words: what is ocr, and when does human review matter in a production LLM system?

### Day 256 - Thu 10 Jun 2027 - Scale, latency & cost design

**Theory (45 min)**

- [ ] Caching
- [ ] Routing
- [ ] Batching
- [ ] Autoscaling
- [ ] Budgets

**Practical (60 min)**

- [ ] Redesign one earlier system for 10x traffic at half the cost

**Recall (15 min)**

- [ ] Explain scale, latency & cost design in your own words: what is caching, and when does budgets matter in a production LLM system?

### Day 257 - Fri 11 Jun 2027 - Security & multi-tenancy design

**Theory (45 min)**

- [ ] Isolation
- [ ] ACLs
- [ ] Guardrails
- [ ] Audit

**Practical (60 min)**

- [ ] Timed design: multi-tenant SaaS AI assistant

**Recall (15 min)**

- [ ] Explain security & multi-tenancy design in your own words: what is isolation, and when does audit matter in a production LLM system?

### Day 258 - Sat 12 Jun 2027 - Tradeoff drilling

**Theory (45 min)**

- [ ] Latency
- [ ] Cost
- [ ] Reliability
- [ ] Security
- [ ] Accuracy
- [ ] Maintainability

**Practical (60 min)**

- [ ] Defend 10 design decisions out loud against counter-arguments

**Recall (15 min)**

- [ ] Explain tradeoff drilling in your own words: what is latency, and when does maintainability matter in a production LLM system?

### Day 259 - Sun 13 Jun 2027 - Python interview questions

**Theory (45 min)**

- [ ] Data structures
- [ ] OOP
- [ ] Async
- [ ] Generators
- [ ] Exceptions
- [ ] Testing

**Practical (60 min)**

- [ ] Answer 30 Python questions out loud
- [ ] Code 5 of them from scratch

**Recall (15 min)**

- [ ] Explain python interview questions in your own words: what is data structures, and when does testing matter in a production LLM system?

## Week 38 - Interview Preparation & Final Polish
*Phase 17 - Interview | Roadmap 37-40*


### Day 260 - Mon 14 Jun 2027 - LLM interview questions

**Theory (45 min)**

- [ ] Tokens
- [ ] Context
- [ ] Attention
- [ ] Transformers
- [ ] Hallucination
- [ ] Temperature

**Practical (60 min)**

- [ ] Answer 25 LLM questions in under 2 minutes each

**Recall (15 min)**

- [ ] Explain llm interview questions in your own words: what is tokens, and when does temperature matter in a production LLM system?

### Day 261 - Tue 15 Jun 2027 - RAG interview questions

**Theory (45 min)**

- [ ] Chunking
- [ ] Retrieval
- [ ] Hybrid
- [ ] Rerank
- [ ] Eval
- [ ] Failure modes
- [ ] Security

**Practical (60 min)**

- [ ] Answer 25 RAG questions using your own project as evidence

**Recall (15 min)**

- [ ] Explain rag interview questions in your own words: what is chunking, and when does security matter in a production LLM system?

### Day 262 - Wed 16 Jun 2027 - Agent & MCP questions

**Theory (45 min)**

- [ ] Agent vs workflow
- [ ] Loop
- [ ] State
- [ ] Memory
- [ ] HITL
- [ ] LangGraph
- [ ] MCP

**Practical (60 min)**

- [ ] Answer 25 agent questions
- [ ] Whiteboard the agent loop from memory

**Recall (15 min)**

- [ ] Explain agent & mcp questions in your own words: what is agent vs workflow, and when does mcp matter in a production LLM system?

### Day 263 - Thu 17 Jun 2027 - Production & security questions

**Theory (45 min)**

- [ ] Latency
- [ ] Cost
- [ ] Failures
- [ ] Monitoring
- [ ] Securing agents
- [ ] Evaluating RAG

**Practical (60 min)**

- [ ] Answer the 6 core production questions with real numbers from your projects

**Recall (15 min)**

- [ ] Explain production & security questions in your own words: what is latency, and when does evaluating rag matter in a production LLM system?

### Day 264 - Fri 18 Jun 2027 - Resume, portfolio & mock interview

**Theory (45 min)**

- [ ] Project framing
- [ ] Impact metrics
- [ ] STAR stories
- [ ] Salary talk

**Practical (60 min)**

- [ ] Update resume + GitHub READMEs
- [ ] Do a full 60-min mock interview

**Recall (15 min)**

- [ ] Explain resume, portfolio & mock interview in your own words: what is project framing, and when does salary talk matter in a production LLM system?


---

## Removed topics (already covered by your .NET/AWS experience)

| Original week | Topic | Why removed |
|---|---|---|
| 1 - Python Fundamentals I | Loops & comprehensions | for/foreach/LINQ already known - syntax only, merged into Python Fast Track |
| 1 - Python Fundamentals I | Functions | Method design already known |
| 1 - Python Fundamentals I | Week 1 review + mini build | Merged |
| 2 - Python Fundamentals II | Modules & packages | Assemblies/namespaces equivalent |
| 2 - Python Fundamentals II | File I/O & JSON | System.IO + System.Text.Json equivalent |
| 2 - Python Fundamentals II | datetime & timezones | You already do IST/UTC/DST work on FLIFO daily |
| 2 - Python Fundamentals II | Week 2 review + mini build | Merged |
| 3 - Python for Production | Classes & objects | C# OOP mastered |
| 3 - Python for Production | Composition vs inheritance | Design principle already mastered |
| 3 - Python for Production | Enums & context managers | Enums known; only 'with' syntax needed - merged |
| 3 - Python for Production | Week 3 review + mini build | Merged |
| 4 - Decorators, Errors, Async | Exception handling | try/catch/finally mastered |
| 4 - Decorators, Errors, Async | Custom exceptions | Exception hierarchies mastered |
| 5 - Pydantic, Testing, Logging, Git | Git, GitHub & packaging | Branches/PRs/rebase mastered - only pyproject/venv needed, merged |
| 6 - HTTP, REST, Auth | HTTP fundamentals | Core backend skill already mastered |
| 6 - HTTP, REST, Auth | Query, path params & bodies | Already mastered |
| 6 - HTTP, REST, Auth | REST principles | Already mastered |
| 6 - HTTP, REST, Auth | Pagination, errors, versioning | Already mastered |
| 6 - HTTP, REST, Auth | API keys & bearer tokens | Already mastered |
| 6 - HTTP, REST, Auth | JWT & OAuth concepts | Already mastered |
| 6 - HTTP, REST, Auth | Week 6 review + mini build | Merged |
| 8 - Background Work, SQL | Background tasks | Hosted services / SQS workers already mastered |
| 8 - Background Work, SQL | Queues & long jobs | SQS/Solace worker patterns already mastered |
| 8 - Background Work, SQL | Webhooks | Already mastered |
| 8 - Background Work, SQL | SQL basics | Already mastered |
| 8 - Background Work, SQL | Aggregations & GROUP BY | Already mastered |
| 8 - Background Work, SQL | JOINs & subqueries | Already mastered |
| 8 - Background Work, SQL | CTEs, transactions, indexes | Already mastered |
| 9 - PostgreSQL, Redis, Pipelines | PostgreSQL setup & tables | RDBMS concepts mastered - only pgvector matters (Week 19) |
| 9 - PostgreSQL, Redis, Pipelines | Keys, indexes, optimisation | Already mastered |
| 9 - PostgreSQL, Redis, Pipelines | Connections & pooling | Already mastered |
| 9 - PostgreSQL, Redis, Pipelines | Redis basics | Caching concepts already mastered |
| 9 - PostgreSQL, Redis, Pipelines | Redis for rate limiting & locks | Covered again in Production week |
| 9 - PostgreSQL, Redis, Pipelines | Data pipelines | You build ETL/FLIFO pipelines daily |
| 9 - PostgreSQL, Redis, Pipelines | Idempotency & recovery | Core to your FLIFO/DynamoDB work already |
| 35 - Production Engineering | Reliability | Retries/backoff/timeouts already mastered |
| 35 - Production Engineering | Circuit breakers & degradation | Already known (Polly equivalent) |
| 35 - Production Engineering | Rate limiting | Already known |
| 36 - Docker & Deployment | Docker fundamentals | Already used in your delivery pipeline |
| 36 - Docker & Deployment | Env, volumes, networks | Already known |
| 36 - Docker & Deployment | CI: build & test | Already known |
| 36 - Docker & Deployment | CI: security & image publish | Veracode/scan pipelines already known |
| 36 - Docker & Deployment | CD & rollback | Already known - you run DEV/QA/STG/PRD deployments |
| 37 - AWS for AI Engineers | IAM | You already write Lambda/AWS IAM policies |
| 37 - AWS for AI Engineers | S3 | Already mastered |
| 37 - AWS for AI Engineers | CloudWatch | Already mastered |
| 37 - AWS for AI Engineers | Lambda | You build Lambdas daily |
| 37 - AWS for AI Engineers | DynamoDB | You build DynamoDB tables daily |
| 37 - AWS for AI Engineers | API Gateway & ECS | Already mastered |
| 39 - Enterprise AI Architecture | Authentication | Already mastered |
| 39 - Enterprise AI Architecture | Authorization & RBAC | Already mastered |
| 39 - Enterprise AI Architecture | IAM & secrets management | Already mastered |
| 39 - Enterprise AI Architecture | Microservices & event-driven | You work on event-driven Solace/SQS systems daily |
| 39 - Enterprise AI Architecture | Disaster recovery | Already known |
| 46 - Project 2: Tool-Using Agent | Reliability | Retries/backoff/timeouts already mastered |
| 48 - System Design for AI | System design framework | Backend system design already known - AI-specific designs retained |
| 30 - Production Engineering + Docker & Deployment | Containerising AI apps | Docker skills you already have; AI delta is trivial |
| 30 - Production Engineering + Docker & Deployment | Kubernetes basics | Infra ops - not a Python or AI skill; only needed if the role is platform-focused |
| 30 - Production Engineering + Docker & Deployment | OpenSearch | Another managed search service - pgvector + one managed vector DB is enough |
| 32 - Multi-Agent & Communication + Enterprise AI Architecture | Data isolation & multi-tenancy | Backend architecture you already do; AI-specific part stays in Enterprise RAG week |
| 32 - Multi-Agent & Communication + Enterprise AI Architecture | Audit logging | Backend logging you already do |
| 33 - ML Fundamentals & Evaluation + Multi-Agent & Communication | Debate/consensus/blackboard (awareness) | Roadmap itself lists these as 'do not delay interviews for' |
| 33 - ML Fundamentals & Evaluation + Multi-Agent & Communication | Supervised & unsupervised learning | Classical ML - not asked for GenAI application engineer roles |
| 33 - ML Fundamentals & Evaluation + Multi-Agent & Communication | Classification & regression | Classical ML - not required for your target roles |
| 33 - ML Fundamentals & Evaluation + Multi-Agent & Communication | Train/val/test & cross-validation | Classical ML training workflow - not your job as an AI Engineer |
| 33 - ML Fundamentals & Evaluation + Multi-Agent & Communication | Overfitting, underfitting, bias/variance | Model-training concern, not LLM application engineering |
| 33 - ML Fundamentals & Evaluation + Multi-Agent & Communication | Feature engineering | Classical ML - superseded by prompting/retrieval in your target roles |
| 34 - Deep Learning + ML Fundamentals & Evaluation | Core metrics | Classical ML metrics - RAG/agent evaluation metrics are what you actually need |
| 34 - Deep Learning + ML Fundamentals & Evaluation | ROC-AUC, PR-AUC, regression metrics | Classical ML metrics - not used in LLM evaluation |
| 34 - Deep Learning + ML Fundamentals & Evaluation | Neural networks | Transformer/attention understanding is what interviews test - covered in Week 6 |
| 34 - Deep Learning + ML Fundamentals & Evaluation | Forward pass & loss functions | Training internals - skip unless targeting ML research roles |
| 34 - Deep Learning + ML Fundamentals & Evaluation | Backpropagation | Training internals - you will never train a model from scratch in these roles |
| 34 - Deep Learning + ML Fundamentals & Evaluation | Gradient descent & optimizers | Training internals - not required for AI application engineering |
| 34 - Deep Learning + ML Fundamentals & Evaluation | PyTorch basics | Only needed for ML/research roles, not GenAI application roles |
| 35 - Fine-Tuning & Inference + Deep Learning | CNN & RNN/LSTM concepts | Superseded by transformers; awareness-level only |
| 39 - Project 3: Enterprise AI Assistant + Project 2: Tool-Using Agent | Auth & RBAC | Already your daily work - reused directly in Project 3 |
| 39 - Project 3: Enterprise AI Assistant + Project 2: Tool-Using Agent | Audit logging & cost tracking | Audit part already known; cost tracking already covered in Cost management day |
| 40 - System Design for AI + Project 3: Enterprise AI Assistant | Production deployment & demo | Deployment already known - demo prep folded into the final interview week |
| 41 - Interview Preparation & Final Polish | SQL interview questions | You answer these from experience |
