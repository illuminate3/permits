# Houston coffee-shop conversion: research notes

Scenario: an existing retail storefront (Group M) inside City of Houston limits becomes a coffee shop with about 40 seats (espresso, pastries, maybe sandwiches).
Data file: `houston-requirements.json`. It has 41 requirements, 12 process stages, 25 fee lines and 4 pitch claims, and every entry has a source URL.
Research date: 2026-09-23.

## Key findings

1. **Code basis.** Houston enforces the 2021 IBC, IEBC, IFC and IECC, the 2021 **UPC** and **UMC**, and the 2023 NEC. All carry Houston amendments (Ord. 2023-907, effective Jan 1, 2024). Houston does **not** use the IPC or IMC. No 2024-code adoption was found.
2. **A change of occupancy requires a new CO.** Houston IBC 111.1 and IEBC 110.1/1001.3 require a separate CO for each lease space when the occupancy classification changes. The CO shows the design occupant load and whether a fire alarm or sprinklers are required.
3. **A-2 vs B depends on the calculated occupant load, not the seat count.** Under IBC 303.1.1, an assembly space with fewer than 50 occupants is Group B. Occupant load comes from Table 1004.5: 15 sq ft net per person for tables and chairs, and 200 sq ft gross for a commercial kitchen. A "40-seat" shop with about 750 sq ft or more of seating area is A-2. The demo should compute occupant load from the areas and flag any mismatch with the seat count.
4. **Form CE-1105 (Commercial Prerequisite Checklist, revised Aug 2026) is the best "missing items" checklist.** It covers:
   - the asbestos survey
   - water and sewer availability letters for a change in occupancy
   - the TDLR EAB number when the project exceeds $50,000
   - COMcheck
   - a site plan for a change of use
   - a parking calculation for a change of use classification
   - a code analysis sheet
   - door, glazing and wall schedules
   - sealed sheets
   - MEP plans for a change of occupancy
   - Health plans that include the equipment specs

   Fire alarm, sprinklers and signs must be permitted separately.
5. **One-Stop review is not available.** CE-1042 excludes changes to a more restrictive occupancy, first-time buildouts, anything needing Health or Fire Marshal review, grease traps and cooking equipment, and Type I hoods. Expect full Commercial Plan Review through iPermits and ProjectDox. The plan review fee is 25% of the estimated permit fee.
6. **Houston's food ordinance (Chapter 20) was repealed effective Sept 1, 2025.** Houston now applies the FDA Food Code and the Texas Food Establishment Rules (TFER, 25 TAC 228) by reference. Food-dealer fees changed to $258, $515 or $773 depending on the risk tier. The Health plan-review checklist that HHD still links (Rev. 04/18/2022) cites repealed Chapter 20 sections.
   - Use it for *what reviewers look for*: sink sizes, the 20-ft hand-sink guidance, finishes, lighting.
   - Do not cite it as current law.
7. **Food staff rules.** Under current TFER (§228.31), a certified food protection manager must be on site during all hours of operation, and food handlers must be trained **within 30 days** of hire. Web articles that cite "228.33 / 60 days" are quoting the superseded 2015 rules.
8. **Fire thresholds for a ground-floor coffee shop under 5,000 sq ft are usually not triggered.** Sprinklers for A-2 are required when the fire area exceeds 5,000 sq ft, the occupant load is 100 or more, or the space is not on the level of exit discharge. A fire alarm is required for Group A at 300 or more occupants. For Group B, Houston's amendment sets it at 500 or more. Egress changes at 50 occupants: a second exit is needed, and so are exit signs and emergency lighting.
9. **Fixture counts.** Houston's UPC 422.1 deletes UPC Table 422.1 and points to the **Houston-amended IBC Table 2902.1**. For restaurants that is:
   - 1 water closet per 75 people of each sex
   - 1 lavatory per 200
   - 1 drinking fountain per 500 (waived if water is served free in containers)
   - 1 service sink

   Water closets must be dual-flush or high-efficiency.
10. **Grease.** Sec. 47-513 requires an interceptor with a sample well for restaurants (permits applied for after Aug 31, 2006). Houston's UPC amendments forbid routing a dishwasher or disposer into the grease interceptor. Once operating, the shop needs an annual FOG permit, a pump-out every 90 days, and manifests kept 5 years.
11. **Parking is a likely surprise.** Retail requires 4 spaces per 1,000 sq ft. The food and beverage classes require 4 to 10 spaces per 1,000 sq ft: a take-out restaurant is 4, a dessert shop 6, a small restaurant 8, and a restaurant 10. A grandfathered building cannot become a Restaurant or Dessert Shop without meeting the parking requirement. Exceptions include Market-Based Parking Areas, TOD streets, bike reductions, and variances.
12. **Accessibility.** TDLR registration ($175) is required when construction cost is $50,000 or more. Construction documents go to the RAS within 20 days of issue, and the RAS inspection must happen within 1 year of completion. Key TAS sections:
    - 404.2.3: 32" door clear width
    - 226.1: 5% of dining seats accessible, i.e. 2 of 40
    - 902.3: dining surfaces 28–34" high
    - 904.4: service counter section 36" max high
    - 603/604/606: toilet rooms
    - 202.4: 20% disproportionality cap for path of travel

## Uncertainties and conflicts

- **Reinspection fee.** The 2026 BCE fee schedule says $94.00. The HPC CO service page says $112.64.
- **Food dealer fee.** HPC page hhd1003 still shows the pre-Sept 2025 amounts ($224.44–$739.44 plus admin and inspection fees). The HHD fee-change document shows $258, $515 or $773. Treat the HHD document as current.
- **Food risk tier.** Not confirmed for an espresso/pastry/sandwich operation.
- **Fees not found:** Health plan review fee, pre-opening inspection fee (other than a general inspection fee of $150), FOG permit fee, and impact/WCR fees.
- **Commercial review times** are not published. The HPC dashboard shows the live "Oldest Plan (in business days)".
- **Parking ratios** come from a 2014 Municode print hosted on houstontx.gov. Which food and beverage class a coffee shop falls into depends on the Sec. 26-471 definitions, which were not verified.
- **Fire alarm threshold.** The "300" figure in IBC 907.2.1 is the model-code value. Houston's IFC amendment skips 907.2.1, so it is unamended, but the full text was not loaded.
- **Table 1006.2.1 common-path limits for Group B** vary with occupant load and sprinklers, and exact values were not verified. Show "49 occupants max for a single exit". Do not quote precise common-path distances without checking.
- **Sealing thresholds.** Architect: Occ. Code 1051.606 (commercial building of 2 stories or less and 20,000 sq ft or less; alterations exempt unless there is a substantial structural or exit change). Engineer: 1001.056 (5,000 sq ft or less and no clear span over 24 ft). Both were read on texas.public.law, not capitol.texas.gov. Houston may also require seals "where specifically required by the Building Official".
- **Type I hood.** Whether espresso/pastry equipment needs a Type I hood depends on the equipment listing and the mechanical reviewer.
- **Direct fetches failed** for Municode (Ch. 47, Ch. 26), codes.iccsafe.org (403) and the TAC texreg pages. The same text was confirmed through HHD, up.codes, Cornell LII, and the TDLR TAS PDF instead.
- **Jurisdiction.** There is no verified official "is this address in Houston city limits" lookup URL. Unincorporated Harris County and the ETJ fall under Harris County Public Health for food permits.

## What the demo must NOT claim

- Do not say Houston "has zoning". It is unzoned and relies on deed restrictions (the CE-1380/1381 declaration) and on Chapter 26 parking and Chapter 42 development rules.
- Do not cite "Houston Code Sec. 20-xx" as current food law (repealed Sept 1, 2025), and do not cite 25 TAC 228.33 or a 60-day food-handler window.
- Do not treat 40 seats as automatically "under 50 occupants, so Group B". Occupant load is calculated from floor area.
- Do not say Houston uses the IPC or IMC. It uses the UPC and UMC; fixture counts come from its amended IBC Table 2902.1.
- Do not promise review durations for commercial permits. The 30-day pilot is **residential only**, single-family, and counted in **business days**.
- Do not say TDLR enforces the ADA. TDLR enforces TAS; the ADA is federal and applies separately.
- Do not present the illustrative fee math ($100k valuation → about $545 permit plus about $136 plan review) as an official quote. Point users to the HPC Fee Estimator.
- Do not state fees marked "not found" or confidence "low" as facts.
- Do not claim One-Stop or same-day review is available for this project.

## Pitch claim verdicts (details in JSON)

- (a) The 30-day residential pilot in 2025 is **TRUE**. It was announced July 3, 2025 (HPC dates the launch July 7), is single-family only, and is measured in business days.
- (b) HPC daily metrics for plans in review and the oldest plan are **TRUE**. The dashboard labels are "Total Plans in System for Review" and "Oldest Plan (in business days)".
- (c) The business-guide "difficult" statement is **TRUE with a wording fix**. The OBO New Business Guide says: "it can be difficult to understand which permits or licenses you need". It does not say "agencies/docs".
- (d) The Innovation & Performance mission claim is **TRUE as a paraphrase**. The mission is "create lasting and substantial improvements in the way the City operates". Data and efficiency appear in its core values, not in the mission sentence.
