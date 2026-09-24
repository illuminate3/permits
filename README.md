# Houston, TX coffee shop / cafe permits: research plus PASS and FAIL test sets

This folder contains:

- `blank_forms/`: official blank forms, downloaded unmodified from the City of Houston, Harris County and the Texas Comptroller.
- `set_PASS_bayou_bean_coffee/`: a complete, internally consistent package that should be approved.
- `set_FAIL_magnolia_grind_coffee/`: a package with 40 planted defects that should be rejected.
- `EXPECTED_REVIEW.md` in each set folder: the answer key for that set.
- `build_sets.py`: regenerates both sets from the blank forms. Run `.venv/bin/python build_sets.py`.

All applicants, people, addresses, IDs and signatures in the two sets are fictitious, and every page carries a red "SAMPLE / TEST DATA" footer. Documents that only a government office or a third party can issue (the Certificate of Occupancy, the food manager certificate, driver's licenses, file-stamped filings) are **not** fabricated. The PASS set has labeled placeholder pages for them instead.

## Permits a Houston coffee shop needs (inside Houston city limits)

| # | Permit / registration | Agency | Form (in `blank_forms/`) | Fee (published) | When |
|---|---|---|---|---|---|
| 1 | Assumed name (DBA) | Harris County Clerk for sole proprietors and partnerships; TX SOS Form 503 for LLCs and corporations | `HarrisCounty_D0207_Assumed_Name_Certificate.pdf` | $24 notarized (+$0.50 per extra owner); $22 for veterans | First |
| 2 | Texas Sales and Use Tax Permit | Texas Comptroller | `TX_Comptroller_AP-201_Sales_Tax_Permit.pdf` (or apply online) | No fee (a security deposit may be required) | Before opening; needed for the food permit |
| 3 | Building permit (tenant finish-out) plus deed-restriction declaration | Houston Permitting Center (iPermits / ProjectDox) | `HPC_Building_Permit_Application.pdf` (CE-1263); `HPC_CE-1381_...` if the land owner is an entity, `HPC_CE-1380_...` if an individual | Based on valuation (city fee schedule) | Before construction |
| 4 | Health plan review (food establishment) | Houston Health Dept. plan review, 1002 Washington, 3rd floor | `HHD_Food_Plan_Submission_Checklist.pdf` | Plan review fee | New or converted food spaces |
| 5 | TDLR / TABS accessibility registration | Texas Dept. of Licensing and Regulation | online | TDLR fee | Projects of $50,000 or more |
| 6 | Certificate of Occupancy | HPC Occupancy Inspections | `HPC_CE-1045A_Occupancy_Inspection_Application.pdf`, `HPC_CO_How-To.pdf` | $94 CO; $268.56 (under 3,000 sf in a multi-tenant building) or $537.12 compliance fee; $33.56 admin fee; $112.64 re-inspection | After build-out |
| 7 | Food Dealer's (food service) permit | Houston Health Dept., Consumer Health | `HHD_Food_Dealer_Permit_Application.pdf` | $224.44 to $739.44 depending on risk, plus $33.56 admin and a $112.57 or $225.14 inspection fee | Apply 30 days or more before the pre-opening inspection; renew yearly |
| 8 | FOG / grease-trap generator permit | HHD Special Waste (issued at 8000 N Stadium Dr) | no public form; see `HHD_Waste_Generator_FAQ.pdf` | $123.54 + $33.56 admin | With the food permit; interceptor pumped every 90 days |
| 9 | Fire alarm permit (if the space has an alarm system) | Houston Fire Dept. | `HFD_Fire_Alarm_Permit_Application.pdf` + `HFD_Unsworn_Declaration.pdf` | City fee schedule | Before the system goes live |
| 10 | Place of Assembly operational permit | Houston Fire Dept. | `HFD_Fire_Prevention_Permit_Application.doc` | City fee schedule | Only if occupant load is **50 or more** (Houston Fire Code 105.5.39) |
| 11 | Sign permit | HPC Sign Administration (filed by the sign contractor) | `HPC_Sign_Administration_Plan_Review.pdf` (CE-1427) | City fee schedule | If there is exterior signage; needs a valid CO |
| 12 | TABC permit | Texas Alcoholic Beverage Commission | online | varies | Only if alcohol is sold |
| - | Certified Food Manager and food handler cards | Texas-accredited providers | - | varies | At least one CFM required |

If the shop is in unincorporated Harris County (outside Houston city limits), Harris County Public Health issues the food permit instead of the Houston Health Dept.

## How the two sets differ (summary)

| | PASS: Bayou Bean Coffee | FAIL: Magnolia Grind Coffee |
|---|---|---|
| Entity | Sole proprietor; filed the county DBA (correct) | LLC that filed the county DBA (wrong office), for 15 years (maximum is 10), not notarized |
| Menu / risk | Beverages and bakery-made pastries; marked Low risk | Cook-to-order eggs, cooked and cooled chicken, alcohol; wrongly marked Low risk |
| Seats / occupant load | 32 seats, load 42, Group B | 64 seats, load about 73, A-2; no Place of Assembly permit |
| Plan | 3-compartment sink, 2 hand sinks, mop sink, 100-gal interceptor, light finishes, public corridor to restroom | 2-compartment sink, hand sink 28 ft away through a door, no interceptor, griddle with no hood, restroom through the kitchen, black ceiling |
| Consistency | Name, suite and dates match everywhere | Suite 200 vs 210; "Cafe" vs "Coffee"; P.O. Box given as the place of business |
| Signatures | All signed and dated | AP-201, CE-1263, CE-1045A and fire alarm unsigned |
| Timing | Food application 42 days before opening | 14 days (30 required) |

The full list is in `set_FAIL_magnolia_grind_coffee/EXPECTED_REVIEW.md` (F01 to F40).

## Sources

- Houston Health Dept., Opening a Food Establishment: https://www.houstonhealth.org/services/permits/food-permits/opening-food-establishment
- Food Dealer permit (HHD1003): https://www.houstonpermittingcenter.org/hhd1003
- Food Dealer's Permit Application: https://www.houstonhealth.org/media/14901/download
- Food Inspection Plan Review Checklist: https://www.houstonconsumer.org/media/36/download
- Certificate of Occupancy: https://www.houstonpermittingcenter.org/hpwcode1106 (CE-1045A: https://www.houstonpermittingcenter.org/media/941/download)
- Declarations CE-1380 / CE-1381: https://www.houstonpermittingcenter.org/media/2386/download and https://www.houstonpermittingcenter.org/media/2391/download
- Building Permit Application CE-1263: https://www.houstonpermittingcenter.org/media/1226/download
- FOG generator registration (HHD1017): https://www.houstonpermittingcenter.org/hhd1017 ; FAQ: https://www.houstonhealth.org/media/271/download
- HFD forms and permits: https://houstontx.gov/fire/formsandpermits/
- Houston Fire Code 2021, Chapter 1 (105.5.39 Places of assembly): https://up.codes/viewer/houston/ifc-2021/chapter/1/scope-and-administration
- Harris County Clerk D-02-07: https://www.cclerk.hctx.net/Forms/Uploads/D/D0207.pdf
- Texas Comptroller AP-201: https://comptroller.texas.gov/forms/ap-201.pdf
- Sign Administration CE-1427: https://www.houstonpermittingcenter.org/media/5581/download
- Houston Code of Ordinances Ch. 20 (Food) and Ch. 47 Art. XI (interceptors): https://library.municode.com/tx/houston/codes/code_of_ordinances

Fees were current when these pages were retrieved on 2026-09-23. Check the City of Houston fee schedule before relying on them.
