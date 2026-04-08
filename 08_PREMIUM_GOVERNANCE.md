# Premium Governance

This repository is the strict master template for building AI agents in a repeatable, production-oriented way.

## Core rules
- keep prompts in real files
- document tools clearly
- document API bindings clearly
- use approval rules for risky actions
- avoid undocumented assumptions
- require tests before release

## Required before development
- completed input brief
- clear scope
- allowed actions
- forbidden actions
- tool list
- API list
- approval boundaries
- target environment
- success criteria
- realistic test cases

## Risk levels
- LOW: analysis only
- MEDIUM: internal lookups and structured processing
- HIGH: external communication or write actions
- CRITICAL: destructive or irreversible actions
