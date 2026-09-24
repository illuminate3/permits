# How cities help applicants get a permit submission right before they submit

Research date: 2026-09-23. This brief supports the UI work on Permit Preflight Houston.

About the sources:
- "(loaded)" means the page was fetched and read.
- "(search result only)" means the claim comes from a search-engine snippet. The page itself was not loaded.
- Claims marked **UNVERIFIED** should not appear in the product or the pitch.

---

## 1. City "which permits do I need" flows

| City | Tool | Pattern |
|---|---|---|
| **Houston** | Buildout Permit page, [hpwcode1148](https://www.houstonpermittingcenter.org/hpwcode1148) (loaded) | One page per permit type with collapsible sections for fees, more information and contact. It lists 4 documents: the application, plans, CE-1105 and CE-1380/1381. Processing is 15 business days. The [Business Portal](https://houstontx.gov/business/plan/permits-inspections.html) (loaded) is a page of links. It has no wizard. |
| **Houston** | [CE-1105 Commercial Prerequisite Checklist](https://www.houstonpermittingcenter.org/media/1811/download) (loaded, rev. Aug 2026) | A 4-page PDF table. Every row has an **RQ / N/A** checkbox and a **"Sheet No./Location"** column: the applicant says *where in the plan set* each item can be found. The form says "Omitted items applicable to the scope of work will extend the permit process." |
| **Houston** | [Commercial Permitting 101](https://www.houstonpermittingcenter.org/media/1926/download) (loaded) | A slide deck. It shows the phases as a horizontal timeline: Planning & Research → Site Development → Plan Review/Corrections → Construction → CO. It has a **"Frequently Missed Plan Review Prerequisites"** box listing water/wastewater letters, sealed structural plans, code analysis, the Hazmat/High-piled form, the traffic access form, and "submitting final design plans and not preliminary plans". Its flowchart shows a Permit Technician gate that asks "Does the project meet prerequisites?" If not, the plans are returned to the applicant. |
| **NYC** | [Step-by-Step wizard](https://nyc-business.nyc.gov/nycbusiness/wizard) (loaded) | A questionnaire with the promise "It takes 10 minutes". The button reads "Start a New Scenario". You can log in to save progress. The output is a "customized list of requirements" covering City, State and Federal permits. A third-party guide says the output is a printable checklist ([helpnewyork](https://helpnewyork.com/opening-a-storefront-in-nyc-how-to-use-nyc-best-and-the-step-by-step-wizard-to-cut-through-permits-licenses-and-red-tape-in-2026/), loaded). Each permit's detail page, for example the [Food Service Establishment Permit](https://nyc-business.nyc.gov/nycbusiness/description/food-service-establishment-permit) (loaded), has fixed tabs: **About / How to Apply / After You Apply / Operating and Renewing / Additional Resources**. The fee ($280) and time ("start operating 22 days after you submit") are stated up front. |
| **San Francisco** | [Guide to opening a restaurant](https://www.sf.gov/guide-opening-restaurant) (loaded) | A long guide page with 7 sections: Get started / Find a location / Set up your business / Prepare your space / Food and alcohol / After opening / More considerations. It advises consulting DPH and SFFD *before signing a lease* about hoods, sprinklers and exits. The [food facility plan check guide](https://www.sf.gov/plan-check-guide-building-and-remodeling-food-facility) (loaded) gives 3 numbered steps: Prepare your plans → Go to the Permit Center → Have Public Health review your plans. The old Business Portal "Permit Locator" was retired and replaced by human permit specialists ([sf.gov](https://www.sf.gov/news--san-francisco-business-portal-moving-sfgov), search result only). |
| **Boston** | [How to Open a Restaurant](https://www.boston.gov/boston-permitting/start-or-grow-business/how-open-restaurant-boston) (loaded) | 6 numbered steps, each on its own page: Get Ready / Choose a Location / Construction and Renovation / Prepare to Serve Food and Drink / Entertainment and Guest Experience / Renewals. There is a flowchart and a sidebar of the 9 departments involved. The [Construction step](https://www.boston.gov/boston-permitting/start-or-grow-business/how-open-restaurant-boston/construction-and-renovation) (loaded) gives **a time range for every permit**, for example Health plan review 2–6 weeks, CO 1–4+ weeks, and Place of Assembly (50+ seats) 1 week to 3+ months. |
| **Los Angeles** | [Restaurant & Small Business Express Program](https://dbs.lacity.gov/services/core-services/inspection/inspection-special-assistance/restaurant-small-business-express-program) (loaded) | Human case management. After an online request, a Case Manager is assigned and follows 4 stages (Design → Permitting → Construction → Completion). According to a [LA Business Portal snippet](https://business.lacity.gov/resource/city-los-angeles-restaurant-hospitality-express-program) (search result only), you can also book a "Preliminary Plan Check" meeting with an engineer before submitting through ePlanLA. |
| **Seattle** | [SDCI New Businesses](https://www.seattle.gov/sdci/permits/common-projects/new-businesses) (loaded) | Question headings: "What Permits Do You Need?", "Should You Hire a Professional?", "What Do You Want To Do?". It offers **Commercial Space Permit Coaching**. It explains that permits depend on "the last legally permitted business in SDCI records". Pre-submittal conferences are optional and paid ([SDCI](https://www.seattle.gov/construction-and-inspections/permits/permits-we-issue-(a-z)/construction-permit---addition-or-alteration), search result only). |
| **Austin** | [Small Business Permitting](https://www.austintexas.gov/development-services/small-business-permitting) (loaded) | 3 phases: Create Your Project / Review and Revise / Build and Inspect. It offers 20-minute Development Process Team appointments. It says: "As of Oct. 1, 2025, reviews have been reduced from 11 disciplines to three" for a small-business change of use, taking about two weeks instead of two months. It has no interactive tool. |
| **Denver** | [StartSmart: Restaurants](https://www.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Community-Planning-and-Development/Plan-Review-Permits-and-Inspections/Commercial-and-Multifamily-Projects/Restaurants-and-Commercial-Kitchen-Permits/StartSmart-Restaurant-Guide) (loaded) | An external form plus PDF applications. The [Restaurants page](https://denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Community-Planning-and-Development/Plan-Review-Permits-and-Inspections/Commercial-and-Multifamily-Projects/Restaurants-and-Commercial-Kitchen-Permits) (search result only) sets expectations: 1–2 months of design, then 2–3 months of review. Restaurants "cannot be reviewed at the counter" because they need health review. |
| **Chicago** | [Restaurant Start-Up Guide](https://www.chicago.gov/content/dam/city/depts/bacp/Small%20Business%20Center/restaurantstartupguide.pdf) (search result only; the fetch returned 403) | Before a BACP consultation you fill in a **Restaurant Start-up Worksheet**. CDPH publishes a "[Retail Food License Readiness Checklist](https://www.chicago.gov/content/dam/city/depts/cdph/FoodProtection/2026/retail-food-license-readiness-checklist.ax.jm.em.pdf)" (title seen only; the fetch returned 403). |
| **San Diego** | [AB 671 restaurant review](https://www.sandiego.gov/development-services/news-programs/ab671) (loaded) | A licensed professional certifies the plans, and review takes 20 business days, with 10 for a resubmittal. The pre-submittal step is a meeting with the Small Business & Restaurant Express Program. The online system "helps to pre-screen that the minimum required files are uploaded" ([Project Submittal Manual](https://www.sandiego.gov/development-services/codes-regulations/project-submittal-manual); that quote is from a search result only). |
| **Phoenix** | ["Where Do I Start?"](https://www.phoenix.gov/administration/departments/pdd/tools-resources/where-do-i-start.html) (loaded) | Four cards for choosing a path. It has no branching questions. It points to the Ombudsman/Customer Advocacy team. |

### The best 5 in detail

1. **NYC Step-by-Step.** Questions first, with a time estimate, save and resume, and a personalised list as the output. Every permit page then follows the same 5-tab template.
2. **Boston.** 6 steps, one page each, with a range of weeks for every permit and a sidebar of departments.
3. **Houston CE-1105.** The best model for a "completeness" row: Required / N/A / *which sheet*.
4. **SF.** Numbered steps (3) inside a long guide. Its strongest content is "check this before you sign a lease".
5. **LA RSBEP.** Not a UI, but it shows how a staged case works: Design → Permitting → Construction → Completion.

## 2. AI and automated pre-check tools cities actually use (2023–2026)

- **CivCheck (acquired by Clariti in Oct 2025) in Honolulu.** Honolulu launched voluntary "Priority Review" on July 2, 2026 ([GovTech](https://www.govtech.com/artificial-intelligence/honolulu-launches-ai-assisted-fast-track-permit-review), loaded).
  - The applicant passes an AI pre-screen and gets a **CivCheck ID**, then enters that ID in HNL Build.
  - Average review time fell from 73 to 32.5 days, and review cycles from 3.4 to 1.4. The sample was **19 vs 17 residential permits**, which is small.
  - An earlier 2024 pilot reported more than 70% less reviewer time ([CivCheck case study](https://www.civcheck.ai/blog/honolulu-pilot-case-study-2024), loaded).
  - The product page describes a "Permit Application Readiness score", completeness flags before submission, and explanations of "what reviewers are looking for and why" ([Clariti](https://www.claritisoftware.com/products/civcheck-ai-plan-review-software), loaded).
- **CivCheck in Seattle.** A proof-of-value study ran March–October 2025 and was published June 17, 2026 ([Seattle Innovation Hub](https://innovation-hub.seattle.gov/2026/06/17/ai-construction-permitting-seattle-civcheck-study/), loaded).
  - Completeness checks were **87% accurate**; compliance checks were 92%.
  - Search results also report about 50% fewer intake days and 35% fewer correction cycles (search result only).
  - Key finding: partial detection **does not remove a review cycle**. Coverage matters more than cleverness.
  - The recommendation was a production pilot for **completeness pre-screening only**.
- **Archistar eCheck / AI PreCheck in LA County.** The beta launched July 15, 2025 ([LA County](https://lacounty.gov/2025/07/15/la-county-launches-echeck-ai-pilot-as-part-of-express-lane-for-faster-rebuilding/), loaded; [LA County Recovers](https://recovery.lacounty.gov/la-county-echeck/), loaded).
  - It covers fire-rebuild single-family homes (R-1) only.
  - The flow: look up the address → upload the PDF → choose "Like-for-Like" or not → receive a **downloadable compliance report within up to 10 business days**, which you attach to the permit application.
  - It is voluntary, and there is a public dashboard of usage counts.
  - LA's CIO described the output as "Here are nine areas you should resolve before you submit your plans" ([Archistar](https://www.archistar.ai/blog/approved-building-permits/), loaded).
  - "81% fewer resubmissions" is **UNVERIFIED**: it appeared only in a search snippet and is not on the pages that were loaded.
- **Austin.** A Development Services memo dated Feb 13, 2026 ([memo](https://services.austintexas.gov/edims/document.cfm?id=467702), loaded) says "approximately **85 percent** of initial applications submitted were not complete" (site plans, Dec 2024–Dec 2025), and that "AI solutions ... [for] a completeness check" are being evaluated.
  - Archistar PreCheck is in beta for residential zoning, with "roughly 50% time-savings" (search result only).
  - A Noetic site-plan pilot started April 2026 (search result only).
- **Govstream.ai in Bellevue, WA** ([Bellevue](https://bellevuewa.gov/city-government/departments/ITD/innovation-programs/innovation-partnerships/innovation-partnership-govstreamai), loaded, dated Aug 4, 2026).
  - It has three phases: Permit Guide (a Q&A assistant), Application Assistant, and First Review.
  - Results after one month: "3 times more applications arrive complete on the first submission", "96% required documents correctly identified at intake", and 152 staff hours saved.
  - The Application Assistant shows a **live completeness score toward 100%** with "actionable feedback with examples and citations" ([Govstream](https://www.govstream.ai/product/application-assistant), loaded).
- **Harris County (unincorporated areas; not the City of Houston).** The county approved a 2-year AI pilot in Nov 2025 and budgeted more than $750K in FY2027 for Archistar ([Spring Reporter](https://springreporter.com/articles/harris-county-puts-750k-toward-ai-to-speed-building-permits-mspq906n), loaded).
  - Scope: pre-screening, technical review and an applicant chatbot.
  - "A human reviewer conducts a final sign-off." The goal is 50% faster processing.
  - This matters locally: our pitch can say the region is already buying this capability.
- **CodeComply.ai (partnered with CivicPlus in Mar 2026)** ([CodeComply](https://www.codecomply.ai/ai-plan-review/), loaded).
  - The tool is aimed at reviewers.
  - Each finding is pinned to **the exact sheet**, cites a code section, and suggests a fix.
  - It offers applicant "Readiness Checks" and states that "final approval always stays with your team."
- **Other tools, all unverified or from search results only:**
  - UpCodes Plan Review, launched Jun 2026, is aimed at architects. It returns issues "organized by severity and category, each linked to the relevant drawing page and governing code section" (search result only).
  - Symbium handles instant solar permitting across more than 271 California jurisdictions under SB379 (search result only).
  - PermitFlow raised a $54M Series B in Dec 2025 and serves builders, not cities (search result only).
  - San Jose: "about 75% of ADU applications incomplete" (search result only, **UNVERIFIED**).

## 3. Completeness check and intake as a formal step

- **Houston** treats it as a hard gate. CE-1105 says submittals are not "considered complete" without the checklist. A Permit Technician checks prerequisites, and plans that fail are returned (CE-1105 and Permitting 101, both loaded). Incomplete plans also cannot use the After-Hours Review service.
- **Austin** accepts a project for review before sending an invoice and upload link. Incomplete applications get a **Master Comment Report** ([Commercial Plan Review](https://www.austintexas.gov/development-services/commercial-plan-review), loaded). Small projects are reviewed in 5 business days. That includes tenant finish-out under 10,000 sq ft, even with a change of use.
- **San Francisco** publishes metrics for time to the "completeness check letter". It notes "there may be multiple rounds of completeness check review per project" ([SF metrics](https://www.sf.gov/additional-information-on-permit-performance-metrics), loaded).
- **Pre-application meetings** are offered in several places:
  - LA: Preliminary Plan Check (search result only)
  - Seattle: paid pre-submittal conference (search result only)
  - Chicago: BACP consult plus worksheet (search result only)
  - San Diego: Restaurant Express meeting (loaded)
- **Incompleteness statistics:**
  - Austin: 85% of initial site plans were incomplete (loaded).
  - UK: "about 50% of planning applications that councils receive are invalid" ([Local Digital RIPA](https://www.localdigital.gov.uk/funded-project/reducing-invalid-planning-applications/), loaded).
  - PlanX, the UK tool that grew out of RIPA, claims "typically reduced invalid applications by 60%, and overall processing time by 45%". It is used by 18+ councils ([PlanX](https://www.planx.uk/), loaded). This is the closest international analogue to what we are building.

## 4. Design norms

- **USWDS.** Its [showcase](https://designsystem.digital.gov/documentation/showcase/) (loaded) lists only federal sites, with no city permitting portals. **No US city permitting portal built on USWDS was found.**
- **California Design System.** The beta is frozen, with maintenance through Jul 1, 2026 ([CA Design System](https://designsystem.webstandards.ca.gov/), search result only). No permitting use was found.
- **GOV.UK patterns** are the most relevant. All of the following were loaded:
  - [Question pages](https://design-system.service.gov.uk/patterns/question-pages/): one question per page, the question as the `<h1>`/legend, a Back link, and a left-aligned "Continue" button (never "Next").
  - [Complete multiple tasks (task list)](https://design-system.service.gov.uk/patterns/complete-multiple-tasks/): tasks named with verbs and grouped into sections. The statuses are *Completed, Incomplete, In progress, Not yet started, Cannot start yet, There is a problem*. The guidance says to keep the set small.
  - [Check answers](https://design-system.service.gov.uk/patterns/check-answers/): a summary list with "Change" links, "Not provided" for skipped answers, and a return to this page after editing.
  - [Step by step navigation](https://design-system.service.gov.uk/patterns/step-by-step-navigation/): numbered steps with "and"/"or" substeps, for journeys across departments. Do **not** use it inside a transaction.
  - [File upload](https://design-system.service.gov.uk/components/file-upload/): a drop zone that is always visible (Mar 2025). Error messages follow set wording, e.g. "The selected file must be a PDF", "The selected file is empty", "The selected file is password protected".
  - [Error summary](https://design-system.service.gov.uk/components/error-summary/): headed "There is a problem", placed at the top, linking to each field, with focus moved to it. The page title gets an "Error: " prefix.
  - [Confirmation page](https://design-system.service.gov.uk/patterns/confirmation-pages/): a panel with a reference number, "What happens next", and a way to save a PDF.

---

## Patterns worth copying

1. **Required / N/A / "Found on sheet ___" for every requirement row.** From Houston CE-1105. For each checklist item, show the sheet where we detected it (e.g. "A-101") or why it is N/A. This is exactly the form the city asks for.
2. **A "Frequently missed" callout.** From Houston Permitting 101. Pin the 5–6 items Houston itself says people miss, and check those first.
3. **Short scoping questions first, with a time estimate.** From the NYC wizard ("It takes 10 minutes"). For example: change of use? food prep? seats? alcohol? cost over $50k? The answers decide which rows apply, the way the NYC wizard personalises its list.
4. **A fixed template on every requirement's detail page.** From NYC: *About / How to apply / After you apply*, with the fee and timeline in the first lines.
5. **A time range next to each permit or step.** From Boston ("2–6 weeks") and Denver (1–2 months of design, 2–3 months of review). Use the official source ranges only.
6. **A task-list results page using GOV.UK statuses.** Use "Ready / Missing / Needs attention / Not applicable" (keep it to about 4). Sections: "Before you submit", "Plans", "Supporting documents", "Separate permits".
7. **A downloadable pre-check report the applicant can carry forward.** From LA County eCheck, which gets attached to the permit application, and Honolulu's CivCheck ID. Give ours a report ID and date and make it printable.
8. **Numbered, actionable findings.** From LA's "Here are nine areas you should resolve before you submit." Show a count of what to fix, not a score.
9. **Every finding cites its source and location.** From CodeComply, UpCodes and Govstream: the sheet, the code section or form item (e.g. "CE-1105, p.3: Health Plans"), and a suggested fix.
10. **Human sign-off stated plainly.** From Harris County, CodeComply and Honolulu. Say: "This is a pre-check. The City's Permit Technician makes the completeness decision."
11. **A "Before you sign a lease" check.** From SF. Put CO history, parking for the change of use, and the grease interceptor up front.
12. **One-question-per-page intake, a check answers page, an error summary, and GOV.UK file-upload error wording.** From GOV.UK. Use it for the questions and upload steps. The results page can be denser.

## What NOT to do

- **Don't show a single "AI readiness score" or percentage as the headline.** Seattle found that partial coverage does not save a review cycle, so a 92% score misleads. Show the list of blocking items.
- **Don't claim the tool makes the city's decision, or that the plans are "approved" or "compliant".** Every real deployment keeps a human reviewer, and Houston's gate is a Permit Technician.
- **Don't use chat as the main interface.** Cities use chat for *questions* (Govstream Permit Guide, Harris County chatbot). The pre-check output is always a structured list or report.
- **Don't use decorative UI: gradients, sparkle icons, "magic" wording, or big hero cards.** Every government pattern above is plain text, numbered steps, tables and status tags.
- **Don't hide the source.** Every finding needs the form, page or section and a link. An uncited finding is less useful than Houston's own PDF.
- **Don't invent timelines or accuracy numbers.** Houston does not publish commercial review times, and "81% fewer resubmissions" is unverified.
- **Don't say "Next" or put the primary button on the right.** Use "Continue", left-aligned, per GOV.UK.
- **Don't treat Harris County's AI pilot as the City of Houston's.** They are separate jurisdictions.
