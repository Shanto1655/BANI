# BANI — An Offline-First Personal AI Companion

BANI is a public development project to build a personal AI companion that runs locally on Windows, with privacy, safety, and user control at its core.

The long-term vision is a helpful, conversational assistant that can understand requests, maintain user-controlled memory, assist with everyday computer tasks, and support creative work — without depending on cloud AI services for its core functionality.

**Status:** Early development 🚧

## Vision

- **Offline-first:** Designed to work locally without requiring an internet connection during normal operation.
- **Privacy-focused:** Personal data and memory stay on the user's device.
- **Safety-first:** Consequential actions should require explicit approval.
- **Local AI:** Explore open-source models that can run on everyday hardware.
- **Useful, not just conversational:** Work toward carefully controlled file management, creative utilities, and other practical tasks.
- **Built in the open:** Document the learning process, design decisions, tests, and progress.

## Planned Technology

- Python 3.11
- Local AI inference using llama.cpp and a compatible open model
- SQLite for user-controlled persistent memory
- Automated tests with Python's unittest framework
- A Windows desktop interface, planned for a later stage

Technology choices may change as testing reveals better options for performance, safety, and portability.

## Development Roadmap

- [x] Create the initial project workspace
- [x] Set up a Python virtual environment
- [x] Initialize local Git version control
- [ ] Build the application skeleton and initial tests
- [ ] Implement a basic text-based companion
- [ ] Add a restricted, approval-based tool system
- [ ] Integrate and benchmark a local AI model
- [ ] Add user-controlled local memory
- [ ] Build a desktop interface
- [ ] Test offline behavior and package for Windows

## Safety Principles

BANI is being designed around a simple principle:

**The AI may propose an action, but the application must authorize it before execution.**

The design will prioritize explicit approval for consequential operations, restricted tools, input validation, verification of results, and protection of private data.

No software can guarantee absolute security, so security testing and clear limitations are part of the project.

## Current Limitations

BANI is at the beginning of development. The features described above are goals, not completed capabilities. Offline operation, model performance, security controls, and Windows packaging must be tested before they can be considered reliable.

## Contributing

This project is being developed incrementally, with an emphasis on understanding the fundamentals and documenting decisions. Suggestions, constructive feedback, and contributions will be welcome as the project matures.

## License

A project license has not yet been selected. Until one is added, please do not assume that the code is released under an open-source license.
