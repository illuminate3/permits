# GitHub repos and design systems to borrow from

*Research date: 2026-09-23. Stars, last push dates, and licenses come from the GitHub API (`gh api repos/...`) today. Every repo listed below was confirmed to exist. Anything I could not confirm is called out in the last section.*

## TL;DR

- **Design system: use USWDS**, through `@trussworks/react-uswds` v12 (React 19, Apache-2.0). Use `@uswds-tailwind/theme` if you want USWDS tokens available in Tailwind v4. This is the only mature, maintained, US-government-looking React kit that has the components we need: file input, step indicator, process list, summary box, icon list, alert, and validation.
- **Take patterns from GOV.UK and MOJ; don't install them.** Their **task list**, **summary list / check your answers**, **error summary**, and **multi-file upload** are the best civic patterns for a readiness checklist. Rebuild them with USWDS styling.
- **Closest product analogs:** CrossBeam (a Claude-hackathon ADU permit assistant, Next.js), PlanX (UK planning applications: upload each file and label which requirement it meets), BC Building Permit Hub (requirement templates with automated compliance checks), and BOPS (officer-side "validation requests").

## Ranked top repos

| # | Repo | Stars | Last push | License | What we'd take |
|---|------|------:|-----------|---------|----------------|
| 1 | [trussworks/react-uswds](https://github.com/trussworks/react-uswds) | 230 | 2026-09-20 | Apache-2.0 | **Drop-in React components.** v12.0.0 (Aug 2026), peer `react ^19`, `@uswds/uswds 3.13`. Includes `FileInput`, `StepIndicator`, `ProcessList`, `SummaryBox`, `IconList`, `Alert`, `Validation` (a live checklist), `Accordion`, `Tag`, `Table`, `Fieldset`, `Form`. An App Router / server-component issue (#2540) is closed. |
| 2 | [uswds/uswds](https://github.com/uswds/uswds) | 7,199 | 2026-09-23 | Public domain (CC0), plus Apache/OFL fonts and icons | The source of truth for tokens, Public Sans, the `usa-` markup, and the component guidance ("step indicator", "process list", "summary box"). Its docs are the spec to copy from. |
| 3 | [IHIutch/uswds-tailwind](https://github.com/IHIutch/uswds-tailwind) | 33 | 2026-09-15 | MIT | `@uswds-tailwind/theme` is a **Tailwind v4 theme with USWDS tokens** (peer `tailwindcss ^4`). With it, our own Tailwind components match USWDS colors, spacing, and type. The React package is alpha (0.3.0-alpha.7), so use only the theme. |
| 4 | [navapbc/template-application-nextjs](https://github.com/navapbc/template-application-nextjs) | 21 | 2026-09-23 | Apache-2.0 | Nava's production template: Next.js 15 + `@trussworks/react-uswds` + `@uswds/uswds` + next-intl + Storybook. Copy its USWDS Sass/asset wiring and its layout shell. |
| 5 | [alphagov/govuk-frontend](https://github.com/alphagov/govuk-frontend) | 1,457 | 2026-09-23 | MIT | **Pattern source.** Its `task-list`, `summary-list`, `error-summary`, `notification-banner`, and `file-upload` are the best-researched designs for "here's what's done, what's missing, and why". Port the markup and behavior to USWDS styles. Don't use the GOV.UK brand (crown, GDS Transport). |
| 6 | [mikeOnBreeze/cc-crossbeam](https://github.com/mikeOnBreeze/cc-crossbeam) | 292 | 2026-03-02 | MIT | **Nearest competitor.** It won the Anthropic Claude Code hackathon in Feb 2026. A California ADU permit assistant in Next.js (Supabase, Cloud Run, Agent SDK). One flow reads plans with vision; its "Permit Checklist Generator" flow is almost our exact use case. Study how it structures citations to Gov Code sections and city-specific "gotchas". |
| 7 | [theopensystemslab/planx-new](https://github.com/theopensystemslab/planx-new) | 18 | 2026-09-23 | MPL-2.0 | UK digital planning applications (React/TS). Look at the components `FileUploadAndLabel` (the applicant tags each upload with the required document it satisfies), `TaskList`, `PlanningConstraints`, `ResponsiveChecklist`, `Review`, and `NextSteps`. `FileUploadAndLabel` is the model for mapping our PDFs to requirements. |
| 8 | [bcgov/HOUS-permit-portal](https://github.com/bcgov/HOUS-permit-portal) | 8 | 2026-09-23 | Apache-2.0 | BC's "Building Permit Hub" (Rails + React/Chakra/MobX, Uppy uploads). It standardizes applications across 400+ local governments using **requirement templates** and automated compliance checks. Good data model for "jurisdiction → permit type → required docs". |
| 9 | [unboxed/bops](https://github.com/unboxed/bops) | 13 | 2026-09-22 | MIT | Back-office planning system (the officer's view). Its `AdditionalDocumentValidationRequest` and other validation-request models show how a reviewer phrases "missing or insufficient" items. Use that language for our "likely to be rejected because…" rows. |
| 10 | [CMSgov/design-system](https://github.com/CMSgov/design-system) | 365 | 2026-09-23 | CC0 (GitHub shows NOASSERTION) | A USWDS-derived system with React 19 components (`@cmsgov/design-system` 18.1.0). Its `StepList`, `Review`, `ChoiceList`, `Alert`, and `HelpDrawer` are useful references, especially **HelpDrawer** for "why is this required?" citation panels. Heavier and Healthcare.gov-branded, so reference it rather than adopt it. |
| 11 | [ministryofjustice/moj-frontend](https://github.com/ministryofjustice/moj-frontend) | 58 | 2026-09-23 | MIT | Extends GOV.UK with `multi-file-upload`, `task-list`, `timeline`, `progress-bar`, `badge`, and `ticket-panel`. Its multi-file-upload (per-file status rows) and timeline are good patterns for our upload tray and "what happens next". |
| 12 | [buildingSMART/IDS](https://github.com/buildingSMART/IDS) + [IfcOpenShell/IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell) | 321 / 2,805 | 2026-09-08 / 2026-09-23 | NOASSERTION / LGPL-3.0 | The real "plan check" stack: IDS is machine-readable requirements, and IfcOpenShell's `ifctester` validates IFC models against it. Café applicants upload PDFs, not IFC, so this doesn't apply to the MVP. It does give a credible roadmap line and a good requirement-schema model (facet + applicability + requirement). |

Honorable mentions: [inosca/ebau](https://github.com/inosca/ebau) (26★, EUPL-1.2), a live Swiss cantonal e-building-permit system built with Ember and Python. It's a good reference for permit workflow states but hard to lift code from. [NYCPlanning/labs-zola](https://github.com/NYCPlanning/labs-zola) (96★) is a zoning-lookup map, useful only if we add a "what's allowed at this address" step. [buildingSMART/validate](https://github.com/buildingSMART/validate) (67★, MIT) is an IFC validation service UI.

## Component coverage matrix

| Need | USWDS / react-uswds | GOV.UK | CMS | PlanX / MOJ |
|---|---|---|---|---|
| File upload | `FileInput` (drag and drop, multiple files) | `file-upload` | none | `FileUploadAndLabel`, MOJ `multi-file-upload` |
| Step indicator | `StepIndicator` | none (task list instead) | `StepList` | none |
| Process list ("what happens next") | `ProcessList` | none | none | MOJ `timeline` |
| Summary box | `SummaryBox` | `panel` / `inset-text` | `Alert` | none |
| Checklist / status | `IconList`, `Validation`, `Tag` | `task-list` + `tag` | `Review` | `TaskList`, `ResponsiveChecklist` |
| Error / missing summary | `Alert` (list) | `error-summary` | `Alert` | none |
| Next.js readiness | Nava template, App Router issue closed | none (vanilla JS/Nunjucks) | React 19 peer | PlanX uses React/Vite + MUI |

USWDS has no dedicated "task list". Build ours with USWDS tokens: a row for each requirement with a status `Tag` (Ready / Missing / Needs review), a citation link, and an expandable "why" section, following GOV.UK's task-list layout.

## Recommendation: adopt USWDS

We're on Next.js 16, React 19, and Tailwind v4, and we have one hackathon to ship in. **Use USWDS 3.13 with `@trussworks/react-uswds` 12 for the complex pieces, and `@uswds-tailwind/theme` for everything we already built in Tailwind.**

1. **Compatibility.** react-uswds supports React 19 and USWDS 3.13, and it's the library Nava's production Next.js template uses. The App Router issue is closed. Interactive components (FileInput, ComboBox) need `"use client"` wrappers. Don't also load `uswds.js` (react-uswds warns about double initialization).
2. **Effort (about half a day).** Import `@uswds/uswds/css/uswds.min.css` and `@trussworks/react-uswds/lib/index.css` inside `@layer base`/`components`, before Tailwind utilities, so Tailwind preflight doesn't fight USWDS's normalize. Add the `@uswds-tailwind/theme` tokens under `@theme` and swap our custom buttons, alerts, and uploader for the USWDS ones. Replace the generic gradient/card look with Public Sans, USWDS spacing, `usa-alert`, `usa-summary-box`, `usa-step-indicator`, and `usa-process-list`.
3. **Look.** It reads as "American civic software" right away, which fixes the "AI slop" complaint better than any custom theme. Houston's own permitting sites are plain municipal pages, and USWDS is the vocabulary US city and county services borrow. GOV.UK looks better for task lists, but it reads as British, and its branding is restricted to UK government. CMS is heavier and Healthcare.gov-flavored.
4. **Guardrail.** Don't use `usa-banner` ("An official website of the United States government") or the federal identifier. We're a private tool, not a .gov site. Keep our own name and a clear "not affiliated with the City of Houston" footer.

## Looked relevant but abandoned, moved, or unsuitable

- **VA.gov (`department-of-veterans-affairs/component-library`, `vets-website`, `vets-design-system-documentation`)** return **404 on github.com** today. The npm package's repository URL now points to `va.ghe.com` (VA's GitHub Enterprise), so the source is no longer public. `@department-of-veterans-affairs/web-components` (24.15.0) is still published on npm, but it's Stencil web components tied to VA branding. Use design.va.gov for pattern ideas only.
- **govuk-react/govuk-react** (458★, MIT): last push was 2025-05-29. It uses styled-components CSS-in-JS, which clashes with Tailwind and RSC, and it has no task-list component. Skip it.
- **California:** `cagov/ca-ds-beta` (90★) is **archived** (maintenance ended 2026-07-01). Its successor, `Office-of-Digital-Services/California-Design-System` (5★, GPL-2.0), is pre-alpha. Don't adopt either.
- **San Francisco:** `SFDigitalServices/sf-design-system` was archived in 2021, and `formio-sfds` is archived and deprecated.
- **Philadelphia:** `CityOfPhiladelphia/phila-ui` (Vue, last push 2024). **Boston:** `CityOfBoston/permit-finder` (0★, 2022). Both are stale or the wrong framework.
- **NYC:** `CityOfNewYork/ACCESS-NYC-PATTERNS` (16★) is maintained but GPL-3.0, which is risky to copy code from. Visual reference only.
- **Forms platforms:** `GSA-TTS/forms` (10x Forms Platform) has been **paused since May 2025** and has no license. `formio/formio` (2.3k★) is OSL-3.0 and a heavy JSON-form server, which is overkill for us. Code for America's `form-flow` (Java/Spring) and `honeycrisp-gem` (Rails) are the wrong stacks.
- **BLDS** (Building & Land Development Specification): `blds/blds.github.io` has 0★ and hasn't been touched since 2019. The field names (permit type, work class, status) are still a reasonable vocabulary for our data model, but there's no code to reuse.
- **opensourceBIM/BIMserver** (1.7k★) is AGPL-3.0, Java, and IFC-only. It doesn't fit PDF intake.
- **LLM zoning / municipal-code RAG repos** (`WAT-ai/ZoningLLM`, `jmepperson/cville-rag`, `mariozig/angry-inspector`, `vsheigani/building_code_rag`, and others) all have **5 stars or fewer**. They're toy pipelines with nothing better than our current rules + LLM approach. CrossBeam is the only credible AI permit OSS.
- `adhocteam/uswds_nextjs_starter` (10★) was last pushed in July 2024. It's superseded by the Nava template.
- `usds/justice40-tool` is archived.
